"""Load the data files and check them for consistency."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

import yaml

if TYPE_CHECKING:
    from datetime import date
    from pathlib import Path

MARKS = ("✓", "(✓)", "✗")  # a policy left out of a CfP file shows as "?"
NOT_MENTIONED = "not-mentioned"  # shown as "—"
NUMBER = re.compile(r"\d+|\(\d+\)")  # such as a page count; "(10)" is "pretty much 10"
FENCE = "~~~~"
SOURCES = {"website": 0, "dmanet": 1, "types-announce": 1}  # lower is preferred


class DataError(Exception):
    """The data files are inconsistent."""


@dataclass(frozen=True)
class Venue:
    """A conference series, such as STOC."""

    id: str
    short: str
    name: str
    dblp: str
    url: str


@dataclass(frozen=True)
class Policy:
    """A policy, such as a limit on submissions per author: a column of the table."""

    name: str
    title: str
    short: str
    summary: str


@dataclass(frozen=True)
class Round:
    """One submission round: venue, year, and (if needed) track and round."""

    venue: str
    year: int
    id: str  # "" when the edition has a single round; otherwise "A", "B/1", ...
    conference: date | None  # first day of the conference


@dataclass(frozen=True)
class Statement:
    """What one CfP says about one policy."""

    policy: str
    value: str  # a mark, or a number such as a submission limit
    quotes: tuple[str, ...]
    applies_to: tuple[str, ...] | None
    note: str


@dataclass(frozen=True)
class CfP:
    """One call for papers, as published (or retrieved) on a given date."""

    path: Path
    venue: str
    year: int
    slug: str
    date: date
    meta: dict[str, Any]
    covers: tuple[str, ...]
    deadlines: dict[str, date]
    supersedes: str | None
    statements: tuple[Statement, ...]
    text: str

    def spans(self) -> list[tuple[int, int, str]]:
        """Return (start, end, anchor) for every quote, in text order."""
        found = []
        for i, statement in enumerate(self.statements):
            for j, quote in enumerate(statement.quotes):
                match = quote_pattern(quote).search(self.text)
                if match is None:
                    msg = f"{self.path}: quote not in text: {quote!r}"
                    raise DataError(msg)
                found.append((match.start(), match.end(), f"q{i}-{j}"))
        return sorted(found)


@dataclass(frozen=True)
class Database:
    """Everything in the repository."""

    venues: dict[str, Venue]
    policies: dict[str, Policy]
    rounds: list[Round]
    cfps: list[CfP]

    def versions(self, rnd: Round) -> list[CfP]:
        """Return the CfPs covering the given round, the one to show first.

        The conference website comes first, then the announcement lists, then
        anything else; within each, the most recent first.
        """
        covering = [
            c
            for c in self.cfps
            if (c.venue, c.year) == (rnd.venue, rnd.year) and rnd.id in c.covers
        ]
        covering.sort(key=lambda c: c.date, reverse=True)
        return sorted(
            covering, key=lambda c: SOURCES.get(c.meta["source"], len(SOURCES))
        )


def quote_pattern(quote: str) -> re.Pattern[str]:
    """Match the quote verbatim, except that any run of whitespace matches any other."""
    return re.compile(r"\s+".join(map(re.escape, quote.split())))


class _Loader(yaml.SafeLoader):
    """A YAML loader that rejects duplicate keys instead of keeping the last."""

    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> dict:  # noqa: FBT001, FBT002 -- as in SafeLoader
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in seen:
                msg = f"duplicate key {key!r}"
                raise yaml.constructor.ConstructorError(
                    None, None, msg, key_node.start_mark
                )
            seen.add(key)
        return super().construct_mapping(node, deep=deep)


def parse(text: str, path: Path) -> Any:  # noqa: ANN401 -- whatever the YAML holds
    """Parse YAML, naming the file in any error."""
    try:
        return yaml.load(text, Loader=_Loader)  # noqa: S506 -- a SafeLoader
    except yaml.YAMLError as error:
        msg = f"{path}: {error}"
        raise DataError(msg) from error


def read(path: Path) -> tuple[dict[str, Any], str]:
    """Split a Markdown file into its YAML front matter and its body."""
    _, front, body = path.read_text(encoding="utf-8").split("---\n", 2)
    return parse(front, path) or {}, body.strip()


def load(root: Path) -> Database:
    """Load and check all data files below root."""
    venues = {p.stem: Venue(id=p.stem, **read(p)[0]) for p in root.glob("venues/*.md")}
    path = root / "policies.yaml"
    entries = parse(path.read_text(encoding="utf-8"), path)
    policies = {e["name"]: Policy(**e) for e in entries}  # in the order of the file
    names = [e["name"] for e in entries]
    if len(policies) < len(names):
        msg = f"{path}: duplicate name {next(n for n in names if names.count(n) > 1)!r}"
        raise DataError(msg)
    rounds = [
        Round(p.parent.name, int(p.stem), rnd, front.get("conference"))
        for p in sorted(root.glob("editions/*/*.md"))
        for front in [read(p)[0]]
        for rnd in front.get("rounds", [""])
    ]
    cfps = [_load_cfp(p, policies, rounds) for p in sorted(root.glob("cfps/*/*/*.md"))]
    db = Database(venues, policies, rounds, cfps)
    _check(db)
    return db


def _load_cfp(path: Path, policies: dict[str, Policy], rounds: list[Round]) -> CfP:
    front, body = read(path)
    venue, year = path.parent.parent.name, int(path.parent.name)
    edition = [r.id for r in rounds if (r.venue, r.year) == (venue, year)]
    if not edition:
        msg = f"{path}: no edition file for {venue} {year}"
        raise DataError(msg)
    if not (body.startswith(FENCE) and body.endswith(FENCE)):
        msg = f"{path}: body must be the CfP text inside a {FENCE} fence"
        raise DataError(msg)
    covers = tuple(front.get("covers", edition))
    if not set(covers) <= set(edition):
        msg = f"{path}: covers {covers}, but the edition has rounds {edition}"
        raise DataError(msg)
    deadline = front.get("deadline", {})
    deadlines = (
        deadline if isinstance(deadline, dict) else dict.fromkeys(covers, deadline)
    )
    if not set(deadlines) <= set(covers):
        msg = f"{path}: deadline for a round not in covers {covers}"
        raise DataError(msg)
    statements = tuple(
        _statement(path, name, raw, policies, covers)
        for name, raw in (front.get("policies") or {}).items()
    )
    cfp = CfP(
        path=path,
        venue=venue,
        year=year,
        slug=path.stem,
        date=front.get("published") or front["retrieved"],
        meta=front,
        covers=covers,
        deadlines=deadlines,
        supersedes=front.get("supersedes"),
        statements=statements,
        text=body.removeprefix(FENCE).split("\n", 1)[1].removesuffix(FENCE),
    )
    cfp.spans()  # raises unless every quote is in the text
    return cfp


def _statement(
    path: Path,
    policy: str,
    raw: str | dict[str, Any],
    policies: dict[str, Policy],
    covers: tuple[str, ...],
) -> Statement:
    if raw == NOT_MENTIONED:  # shorthand for value: not-mentioned
        raw = {"value": NOT_MENTIONED}
    if not isinstance(raw, dict):
        msg = f"{path}: {policy}: must be {NOT_MENTIONED} or a block with value, quote"
        raise DataError(msg)
    value = str(raw.get("value", ""))
    quotes = raw.get("quote", [])
    statement = Statement(
        policy=policy,
        value="—" if value == NOT_MENTIONED else value,
        quotes=(quotes,) if isinstance(quotes, str) else tuple(quotes),
        applies_to=tuple(raw["applies-to"]) if "applies-to" in raw else None,
        note=raw.get("note", ""),
    )
    problems = []
    if policy not in policies:
        problems.append(f"unknown policy {policy!r}")
    if value not in (*MARKS, NOT_MENTIONED) and not NUMBER.fullmatch(value):
        problems.append(
            f"value {value!r} is not ✓, (✓), ✗, {NOT_MENTIONED}, or a number"
        )
    if value != NOT_MENTIONED and not statement.quotes:
        problems.append(f"needs a quote, unless the value is {NOT_MENTIONED}")
    if not set(statement.applies_to or ()) <= set(covers):
        problems.append("applies-to must be a subset of covers")
    if problems:
        msg = f"{path}: {policy}: {'; '.join(problems)}"
        raise DataError(msg)
    return statement


def _check(db: Database) -> None:
    slugs = {(c.venue, c.year, c.slug) for c in db.cfps}
    for cfp in db.cfps:
        if cfp.venue not in db.venues:
            msg = f"{cfp.path}: unknown venue {cfp.venue!r}"
            raise DataError(msg)
        if cfp.supersedes and (cfp.venue, cfp.year, cfp.supersedes) not in slugs:
            msg = f"{cfp.path}: supersedes unknown CfP {cfp.supersedes!r}"
            raise DataError(msg)

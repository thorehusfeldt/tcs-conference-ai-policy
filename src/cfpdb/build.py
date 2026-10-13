"""Build the static website into _site/."""

from __future__ import annotations

import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from html import escape
from itertools import pairwise
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup

from cfpdb.model import CfP, Database, DataError, Round, load

ROOT = Path.cwd()
OUT = ROOT / "_site"
REPO = "https://github.com/thorehusfeldt/tcs-conference-ai-policy"
SOURCE_NAMES = {
    "website": "conference website",
    "pc-chair-page": "PC chair\u2019s page",
    "dmanet": "DMAnet",
    "types-announce": "TYPES/announce",
}
SILENT = "Not mentioned in the call for papers."


@dataclass(frozen=True)
class Cell:
    """One cell of the overview table."""

    text: str
    href: str
    quotes: tuple[str, ...] = ()
    note: str = ""

    @property
    def title(self) -> str:
        """Return the hover text: the quotes, then the note."""
        return " … ".join(filter(None, [*self.quotes, self.note])) or SILENT


@dataclass(frozen=True)
class Line:
    """One row of the overview table: what one CfP says about one round."""

    cfp: CfP | None
    deadline: date | None
    cells: list[Cell]


@dataclass(frozen=True)
class Row:
    """A submission round, with the CfP in force first and then every version."""

    round: Round
    current: Line
    versions: list[Line]


@dataclass(frozen=True)
class Series:
    """A conference, or one track of it, such as ICALP B: its rounds, newest first."""

    label: str
    rows: list[Row]

    @property
    def current(self) -> Row:
        """Return the round with the latest known deadline, among those with a CfP."""
        known = [r for r in self.rows if r.versions] or self.rows
        return max(known, key=lambda r: (r.current.deadline or date.min, r.round.year))


def main() -> None:
    """Load the data, then write every page."""
    try:
        db = load(ROOT)
    except DataError as error:
        sys.exit(f"error: {error}")
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)
    env.globals.update(
        db=db,
        repo=REPO,
        source=source_links,
        label=label,
        when=when,
        page=page,
        sources=SOURCE_NAMES,
    )
    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(ROOT / "static", OUT / "static")

    rows = [
        row(db, r) for r in sorted(db.rounds, key=lambda r: (-r.year, r.venue, r.id))
    ]
    venues = sorted({db.venues[r.venue] for r in db.rounds}, key=lambda v: v.short)
    write(
        env,
        "index.html",
        "index.html.j2",
        series=series(db, rows),
        venues=venues,
    )
    for i, policy in enumerate(db.policies.values()):
        uses = [(r.round, x) for r in rows if (x := r.current.cells[i]).text != "?"]
        write(
            env,
            f"policies/{policy.name}.html",
            "policy.html.j2",
            policy=policy,
            uses=uses,
        )
    for cfp in db.cfps:
        write(env, page(cfp), "cfp.html.j2", cfp=cfp, text=highlight(cfp))
    print(f"wrote {OUT}")


def write(env: Environment, path: str, template: str, **context: object) -> None:
    """Render a template to a file below _site, with a relative path to the root."""
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    root = "../" * path.count("/")
    target.write_text(env.get_template(template).render(root=root, **context))


def page(cfp: CfP) -> str:
    """Return the site path of a CfP."""
    return f"cfps/{cfp.venue}/{cfp.year}/{cfp.slug}.html"


def when(rnd: Round) -> str:
    """Return, for example, '2027 (round 1)'."""
    _, _, number = rnd.id.partition("/")
    return f"{rnd.year} (round {number})" if number else str(rnd.year)


def label(db: Database, rnd: Round) -> str:
    """Return, for example, 'ICALP B 2027 (round 1)'."""
    track = rnd.id.partition("/")[0]
    return " ".join(filter(None, [db.venues[rnd.venue].short, track, when(rnd)]))


def series(db: Database, rows: list[Row]) -> list[Series]:
    """Group the rounds by conference and track."""
    groups = defaultdict(list)
    for r in rows:
        groups[r.round.venue, r.round.id.partition("/")[0]].append(r)
    return sorted(
        (
            Series(
                f"{db.venues[venue].short} {track}".strip(),
                sorted(rs, key=lambda r: (r.round.year, r.round.id), reverse=True),
            )
            for (venue, track), rs in groups.items()
        ),
        key=lambda s: s.current.round.conference or date.min,
        reverse=True,
    )


def row(db: Database, rnd: Round) -> Row:
    """Collect what every CfP version says about this round."""
    versions = [
        Line(cfp, cfp.deadlines.get(rnd.id), [cell(cfp, rnd, c) for c in db.policies])
        for cfp in db.versions(rnd)
    ]
    unknown = Line(
        None, None, [Cell("?", "", note="Not yet checked.")] * len(db.policies)
    )
    return Row(rnd, versions[0] if versions else unknown, versions)


def cell(cfp: CfP, rnd: Round, policy: str) -> Cell:
    """Say what this CfP says about this policy, for this round."""
    for i, s in enumerate(cfp.statements):
        if s.policy == policy and (s.applies_to is None or rnd.id in s.applies_to):
            anchor = f"#q{i}-0" if s.quotes else ""
            return Cell(s.value, page(cfp) + anchor, s.quotes, s.note)
    return Cell("?", "", note="Not yet checked.")


def highlight(cfp: CfP) -> Markup:
    """Return the CfP text as HTML, with every quote marked and anchored.

    Quotes may overlap, so the text is cut at every quote boundary; each piece
    is marked once, or as `both` if more than one quote covers it.
    """
    spans = cfp.spans()
    cuts = sorted({0, len(cfp.text)} | {i for s, e, _ in spans for i in (s, e)})
    parts = []
    for a, b in pairwise(cuts):
        parts += [
            f'<span class="anchor" id="{x}"></span>' for s, _, x in spans if s == a
        ]
        depth = sum(s <= a and b <= e for s, e, _ in spans)
        piece = escape(cfp.text[a:b])
        if depth == 1:
            piece = f"<mark>{piece}</mark>"
        elif depth > 1:
            piece = f'<mark class="both">{piece}</mark>'
        parts.append(piece)
    return Markup("".join(parts))  # noqa: S704 -- every text part is escaped above


def source_links(path: str | Path) -> dict[str, str]:
    """Return links to a data file and to its history on GitHub."""
    rel = Path(path).resolve().relative_to(ROOT).as_posix()
    return {
        "source": f"{REPO}/blob/main/{rel}",
        "history": f"{REPO}/commits/main/{rel}",
    }


if __name__ == "__main__":
    main()

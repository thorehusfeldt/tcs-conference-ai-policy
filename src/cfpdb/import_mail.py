"""Turn one e-mail from a Mailman archive (such as DMAnet) into a CfP file."""

from __future__ import annotations

import argparse
import re
import sys
from email import message_from_string
from email.utils import parsedate_to_datetime
from pathlib import Path

import yaml

from cfpdb.model import FENCE


def main() -> None:
    """Read the e-mail and write it to cfps/VENUE/YEAR/DATE-SOURCE.md."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mail", type=Path, help="one message, as split from the archive"
    )
    parser.add_argument("venue", help="for example icalp")
    parser.add_argument(
        "year", type=int, help="year of the conference, not of the e-mail"
    )
    parser.add_argument("--source", default="dmanet")
    args = parser.parse_args()

    raw = args.mail.read_text(encoding="utf-8").removeprefix("From ").split("\n", 1)[1]
    message = message_from_string(raw)
    if message.is_multipart():
        sys.exit(f"error: {args.mail} is a multipart message; extract the text by hand")
    text = message.get_payload().strip("\n")
    if FENCE in text:
        sys.exit(f"error: {args.mail} contains {FENCE}")

    published = parsedate_to_datetime(message["Date"]).date()
    sender = re.search(r"\((.*)\)", message["From"])
    front = {
        "source": args.source,
        "published": published,
        "subject": " ".join(message["Subject"].split()),
        "from": sender.group(1) if sender else message["From"],
        "message-id": message["Message-ID"],
        "policies": {},
    }
    target = Path("cfps", args.venue, str(args.year), f"{published}-{args.source}.md")
    if target.exists():
        sys.exit(f"error: {target} exists")
    target.parent.mkdir(parents=True, exist_ok=True)
    header = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
    target.write_text(f"---\n{header}---\n\n{FENCE} text\n{text}\n{FENCE}\n")
    print(f"wrote {target}")

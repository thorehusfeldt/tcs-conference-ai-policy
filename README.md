# TCS conference policies

What the calls for papers of theoretical computer science conferences say about
submission, reviewing, and the use of AI in 2026-.

See Action 6 of
[*AI and TCS: The Next Six Months*](https://simons.berkeley.edu/news-publications-videos/ai-tcs-working-group)
(Simons Institute, 2026).

## Policies

Each call for papers is checked for the following policies, one per column of the table.
They are defined in `policies.yaml`; the name is what CfP files use.

| Name | Policy | What is checked |
|---|---|---|
| `ai-use-permitted` | AI use in authoring is permitted | AI use in ideas or writing is permitted and not penalized, as long as it does not inhibit human understanding. |
| `author-attestation` | Author attestation | Authors attest that they understand and have verified the work, and accept responsibility for its correctness and presentation. |
| `ai-methodology` | AI methodology section | Papers contain a section on how AI was used, addressing an itemized checklist. |
| `key-ideas-upfront` | Key ideas within the first pages | The number of pages within which the submission must present its results, motivation, and key ideas; the rest is read at the committee’s discretion. In parentheses if only recommended. |
| `video-talk` | Video talk with submission | Submissions are accompanied by a recorded talk in which an author explains the work. |
| `submission-limit` | Submission limit per author | Each author may appear on at most a fixed number of submissions. |
| `reviewer-ai` | AI-assisted reviewing, with disclosure | Reviewers may use AI to check technical claims, disclosing its use; judgements of novelty, significance, and interest remain the reviewer's own. |
| `anonymity` | Authors anonymous | Whether the program committee reviews submissions without seeing the authors' names: ✓ double-blind (at most the PC chairs see them), (✓) partly, ✗ not anonymous. |
| `public-posting` | Public posting of submissions | Submissions are posted publicly, for example on arXiv, no later than the submission deadline. |
| `exposition-rejection` | Rejection for poor exposition | Papers may be rejected with a one-sentence review solely because of sufficiently unclear exposition. |
| `idea-lineage` | Lineage of AI-generated ideas | Authors trace the lineage of AI-generated ideas and credit prior work where the ideas are introduced. |

## Data model

| Directory | One file per | Contents |
|---|---|---|
| `venues/` | conference series | name, DBLP key, website |
| `editions/VENUE/` | year | the submission rounds, if more than one (tracks, rounds) |
| `policies.yaml` | (a single file) | the policies, one per column of the table, left to right |
| `cfps/VENUE/YEAR/` | call for papers | the full text, as published, and what it says about each policy |

Most information lives in the CfP files; these consist of a YAML block and verbatim CfP copy:

```
---
<metadata in YAML>
---
~~~~ text
<the CfP in raw text>
~~~~
```

The metadata includes hand-curated information concerning various policies that are given in prose raw text, for instance
```yaml
policies:
  video-talk: not-mentioned
  anonymity:
    value: "(✓)"
    quote: reviewers will not see the authors' names or affiliations as they initially review a paper. The authors' names will then be revealed to the reviewers only once their reviews have been submitted.
```

Each policy in a CfP file has a `value` that should be a best-effort single token summarising the `quote`.
Possible values include `5` and `(✓)` (meaning “pretty much yes”) and `not-mentioned` (meaning “the call does not mention this issue”, shown as — in the table).
This value is shown in the overview table.
Except for `not-mentioned`, the value must have a supporting quote from the CfP.

## Metadata fields

Dates are written YYYY-MM-DD, such as `2026-10-22`. Fields not marked *required* may be left out.

### CfP files: `cfps/VENUE/YEAR/DATE-SOURCE.md`

The venue and year come from the path; the file name is the CfP's identifier.

| Field | Meaning |
|---|---|
| `source` | *required.* Where the text comes from: `website`, `dmanet`, `types-announce`, `pc-chair-page`, or any other name, such as a mailing list. The table shows the conference website first, then DMAnet and TYPES/announce, then the rest. |
| `url` | Where the text was found. |
| `published` | When it was posted, for a mailing list post. |
| `retrieved` | When it was copied, for a web page. One of `published` and `retrieved` is required; it orders the versions of a call. |
| `last-modified` | The date a web page says it was last changed. |
| `subject`, `from`, `message-id` | The headers of a mailing list post (filled in by `cfpdb-import-mail`). |
| `call` | Which call this is, such as `2nd call`; shown next to the version. |
| `note` | Anything a reader should know about this copy, such as where the dates come from. |
| `covers` | The rounds this call applies to, such as `[B/1]`. Default: every round of the edition. |
| `deadline` | The submission deadline: a date, or one per round, such as `{B/1: 2026-09-15}`. |
| `supersedes` | The identifier of an earlier CfP file that this one replaces, such as `2026-08-29-dmanet`. |
| `policies` | *required.* What the call says about each policy; see below. |

### Policies in a CfP file

Under `policies`, each key is the `name` of a policy in `policies.yaml`, such as `submission-limit`.
Its value is either `not-mentioned` (short for `value: not-mentioned`) or a block with these fields:

| Field | Meaning |
|---|---|
| `value` | *required.* `✓` (yes), `(✓)` (pretty much), `✗` (no), `not-mentioned` (shown as —), or a number, such as `5` for a submission limit or `10` for pages; `(10)` means pretty much 10. |
| `quote` | A passage of the call, or a list of them. Required unless the value is `not-mentioned`. Each must occur verbatim in the text; line breaks and spacing don't matter. |
| `note` | Our comment, shown after the quote and in the hover text. Not the call's words. |
| `applies-to` | The rounds this applies to, if not all that the call covers. |

A policy that is left out shows as `?` (not yet checked).

### Editions: `editions/VENUE/YEAR.md`

| Field | Meaning |
|---|---|
| `conference` | The first day of the conference; the table is sorted by it. |
| `rounds` | The submission rounds, if more than one: tracks such as `[A, B]`, or rounds within a track such as `[A, B/1, B/2]`. |

### Venues: `venues/VENUE.md`

| Field | Meaning |
|---|---|
| `short` | *required.* The abbreviation shown in the table, such as `ICALP`. |
| `name` | *required.* The full name. |
| `dblp` | *required.* The DBLP key, such as `conf/icalp`. |
| `url` | *required.* The website of the conference series. |

### Policies: `policies.yaml`

A list, one entry per column of the table, in the order of the columns.

| Field | Meaning |
|---|---|
| `name` | *required.* The name that CfP files use, such as `submission-limit`. |
| `title` | *required.* The full name, as a page heading. |
| `short` | *required.* The column heading in the table. |
| `summary` | *required.* One sentence; the hover text of the column heading. |

## Adding or correcting a call for papers

Add a new CfP (fill out `policies`, and `covers` if needed, by hand) or correct existing entries.
Then send a pull request.

Alternatively, raise an issue.


## Building the site locally

    uv run cfpdb-build
    python -m http.server -d _site

The build fails if any file is inconsistent, for example if a quote does not occur in its call for papers.

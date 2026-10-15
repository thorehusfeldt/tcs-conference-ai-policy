---
kind: reviewing-guidelines
source: pc-chair-page
url: https://people.inf.ethz.ch/hoffmann/Reviewing_Guidelines_SoCG_2026.pdf
published: 2025-11-14
note: >-
  The reviewing guidelines, a PDF linked from the call for papers; dated on
  every page. Text extracted from the PDF: page headers removed, lost spaces
  and line breaks repaired, list markers added; the two rating tables are
  set as lists.
policies:
  idea-lineage: not-mentioned
  ai-methodology: not-mentioned
  ai-use-permitted: not-mentioned
  author-attestation: not-mentioned
  key-ideas-upfront: not-mentioned
  exposition-rejection: not-mentioned
  submission-limit: not-mentioned
  reviewer-ai:
    value: "✗"
    quote: reviewers must not upload or share any details of submissions with third-party generative AI tools and technologies, such as ChatGPT.
  public-posting: not-mentioned
  video-talk: not-mentioned
  anonymity:
    value: "✓"
    quote: Under double blind review, and allowing PC submissions, other hard CoIs can materialize.
---

~~~~ text
Reviewing for SoCG 2026

Guidelines

Hee-Kap Ahn, Michael Hoffmann, Amir Nayyeri

November 14, 2025

Abstract

This document describes guidelines for reviewing submissions to the 42nd
International Symposium on Computational Geometry (SoCG’26). They apply to
everyone who reviews submissions for SoCG’26, may it be as a member of the
program committee (PC) or as an external subreviewer. Collectively, this target
audience is referred to as reviewers here. Reviews serve two main purposes: (1)
they provide information to help the PC decide which submissions are accepted
for presentation at the conference and (2) they provide useful feedback to the
authors about the quality of their submission—independently of whether or not it
is accepted. To serve both of these purposes, high-quality, detailed reviews are
required. So, what does a high-quality, detailed review entail? The goal of this
document is to present our view on this matter, along with a number of issues
related to the review process overall. The guidelines are structured as follows:

- 1. Ethical issues and conflicts of interest
- 2. Typical structure of a review
- 3. Scope
- 4. General criteria
- 5. Criteria specific to each paper type
- 6. Score and confidence ratings
- 7. Appendix and supplemental data

1 Ethical issues and conflicts of interest

Submitted papers are strictly confidential. Reviewers must not distribute them,
nor use them for their research. In particular, reviewers must not upload or
share any details of submissions with third-party generative AI tools and
technologies, such as ChatGPT. Furthermore, the reviews, grades, and confidence
scores must be kept confidential.

There are two types of conflicts of interest (CoIs): hard and soft. PC members
and reviewers can have either, while authors can only have hard CoIs. A reviewer
should declare a CoI if they may be biased in regards to (one of) the authors,
or if there is some other reason that they cannot review a paper objectively.
CoIs are mostly handled automatically by HotCRP and in some cases manually by
the PC chairs. One should have a good reason to declare a CoI, but the reason
need not be specified as part of the declaration.

Hard CoIs. A hard CoI prohibits a person from reviewing a paper and excludes
them from the discussion and decision process for the paper.

Specifically, a hard CoI is indicated if the relationship between author and
reviewer is one of the following:

- Family member, (ex-)significant other, or close friend.
- PhD advisor or advisee (no time limit), or postdoctoral or undergraduate
  mentor or mentee within the past five years.
- Same institutional affiliation.
- Reviewer owes author a favor (e.g., recently requested a reference letter).

Furthermore, if the reviewer and the author were involved in an incident that
violates the code of conduct, then either can declare a hard CoI. It is not
required that the incident has been reported.

A hard CoI can also be declared for a frequent or recent collaborator. In this
case it is up to the reviewer and author to decide if the collaboration and
relationship would make an objective review difficult. If they feel that an
unbiased evaluation is possible, they should declare a soft CoI instead, which
does not a priori exclude the reviewer from the process of handling the paper.
Note that if either side declares a hard CoI, it is marked as a hard CoI.

Under double blind review, and allowing PC submissions, other hard CoIs can
materialize. For instance, submissions that significantly overlap in content
(i.e., main results) with your own submission(s) to SoCG’26 should be treated as
hard COIs.

If after being assigned a review you notice a hard CoI, please contact the PC
chairs immediately.

Soft CoIs. A soft CoI does not prevent someone from reviewing a paper, however,
it indicates that there may be a perceived bias. For example, if the reviewer is
a recent coauthor or collaborator of one of the authors or is otherwise vested
in their success, but the relationship has not risen to the level where the
reviewer/author believes it does not allow them to write an unbiased review.

If you have a soft CoI, use your judgment on whether you want to review the
paper. Do so only if you feel you can be objective in your evaluation, or at
least provide unbiased factual information.

If you choose to review a paper with a soft CoI, you should disclose the soft
CoI in the review form as a “comment to the PC“.

A reviewer may feel they have a soft CoI due to minor overlap with one of their
own submissions to SoCG’26, but not a large enough overlap to constitute a hard
CoI. In this case, they should not declare it in the “comments to the PC” field,
as it may divulge blinded information on another paper. If they are concerned
about the perception of bias, they can contact the PC chairs.

Declaring Hard CoIs for PC members. PC members should declare their hard CoIs
through HotCRP. If they have done this before for another conference, the
information may be present already. The process is as follows:

- 1. Log into HotCRP.
- 2. Click on your id (email address) in the upper right corner.
- 3. Select “Your Profile” from the dropdown menu.
- 4. Under Collaborators and other affiliations list your hard CoIs, one line
  each in the specified format.

2 Typical structure of a review

Typically, a review contains the following:

- A concise summary of the paper, the problems considered and the main
  contributions. If a paper is written well, then it is easy to identify the
  main contributions—the abstract describes them. But some authors might
  overstate their results or might not realize the significance of certain
  aspects of their work, and so a reviewer may give a different summary of the
  main contributions than the authors.
- A list of the strengths and weaknesses, supported by evidence (see criteria
  below).
- An overall evaluation based on the strengths and weaknesses.
- Some constructive and professional feedback to the authors for improving the
  paper.
- Optionally, in a separate section, some confidential feedback to the program
  committee. Please only put information there that should not be disclosed to
  the authors (typically, information that would break anonymity of the
  reviewer).

Please note that short reviews are not very useful. Precise and supported
arguments are crucial to help the PC to arrive at a well-reasoned decision.
Specifically, if you believe that there is an error in a statement or a gap in a
proof, provide a clear description of the problem so that other reviewers can
check and verify. In a similar vein, a review should not simply state “the
solution is trivial” without explicitly giving an argument (should be easy if it
is trivial, indeed), or pointing to previous work or textbook material that
essentially implies the result. Analogously, this applies to positive comments:
Simply stating “great result” or “elegant proof” without any further explanation
is not very helpful and insightful; so such a statement should always be
accompanied with a few more words that detail what exactly is great or elegant
there. At the end of the day an evaluation is always subjective, but it should
be well-founded and well communicated.

Always be polite and constructive. Reviewers should assume that the authors have
put their best efforts into their submissions. Hence any comments that could be
interpreted as hurtful or condescending should be avoided. Be mindful of
cultural differences and try to abstain from the use of negative adjectives and
sarcasm. As a reviewer you should feel comfortable to sign your review with your
name (even if there are good reasons not to do so).

Remember that your assessment is only an expression of your personal opinion (in
particular when it comes to whether the problems or results are interesting).
Try to phrase your assessment as much as possible as an expression of this
opinion and not as facts. In short, write reviews with the care and
professionalism that you would want to be applied to reviews of your own papers.

3 Scope

From the call for papers: We invite submissions of high quality that describe
original research on computational problems in a geometric setting. Topics of
interest include, but are not limited to:

- Design, analysis, and implementation of geometric algorithms and data
  structures;
- Computational complexity of geometric problems;
- Implementation and experimental evaluation of geometric algorithms and
  heuristics, including mathematical, numerical, and algebraic aspects;
- Discrete and combinatorial geometry;
- Computational topology, topological data analysis, and topological
  combinatorics;
- Applications of computational geometry in any field.

4 General criteria

When evaluating a paper, one should address the following (interrelated) issues.
A paper with a high score should in general score high on several of them. These
criteria are general and apply to all papers, theoretical or practical.
Additionally one should address issues specific to the paper type, as discussed
in Section 5.

Relevance. In what respect is the paper relevant to computational geometry? Is
it directly relevant for the design, use, analysis, or implementation of
geometric algorithms? Does it have indirect implications for the development of
geometric algorithms? Does it contribute to the mathematical foundations of
discrete or combinatorial geometry and/or algebraic geometry and/or
computational topology? (See “SoCG scope” above.)

Connection to other fields or application domains. Does the paper establish a
connection to other domains? If so, in which direction? How
surprising/novel/established is this connection? How interesting and relevant is
the connection for either side? Does the paper contribute to the other domain?
If so, how significant is this contribution and what is its impact? Is the
connection described in sufficient detail and clarity?

Foundational/conceptual contribution. Does the paper introduce a new model, new
notion, new definition, new approach, novel implementation, novel application?
Note the significance and reasons for this novelty (and note the absence of such
a novelty, if applicable). Does it have the potential to influence or affect
future work?

Completeness. Are enough details provided to verify correctness and to reproduce
the results? For example, for a theorem, we need enough proof details in the
body or appendix of the paper to verify its correctness. For software, we need
to be able to build and test it to verify the claims. For an experiment, we need
enough material to be able to reproduce it.

Technical development. Does the paper involve

- an introduction of a new technique?
- a novel use of known technique?
- a talented use of known technique?
- a traditional use of known technique?
- a trivial use of previous technical knowledge?

Relation to open problems. Does the paper solve completely/partially an open
question? How important is this question
(central/important/interesting/legitimate/unimportant)? How much effort has been
invested previously in solving it and by whom?

Social interest in paper. Is it potentially interesting to the whole community
of computational geometry, to a major field, to everyone in a restricted area,
or interesting only to the authors?

Type of contribution. Is it a

- first step (opens a new area)?
- last step (closes an important area)?
- giant step (makes essential progress)?
- none of the above?

Clarity of presentation. Is the paper well written, or in a too preliminary
form? Have the authors made an effort to make it accessible, or does the way the
paper is written make the paper unnecessarily hard to read and/or narrow down
its interest to specialists?

5 Criteria specific to each paper type

When evaluating a paper, it is important to keep in mind that there are
different types of papers and that the criteria by which papers of one type are
evaluated may be different from those used for papers of another type. Moreover,
the importance of a common criterion may vary from type to type. The strengths
and weaknesses of a particular paper may be diverse in nature. Among the paper
types that we expect to encounter are papers focusing on:

- mathematical foundations,
- algorithmic complexity,
- implementation & engineering, and
- experimentation.

Hybrid papers, which consist, for example, of both an algorithmic design and
analysis part and an experimental part are of course also common.

Below is an attempt to characterize these paper types and to specify the main
criteria by which they should be evaluated.

Mathematical Foundations: A typical paper contains theorems and proofs
describing new results in discrete or combinatorial geometry, discrete
differential geometry or topology, or in topological combinatorics. The paper
will primarily be evaluated on the connection of the problem studied to
computational geometry and topology, the importance of the results, the
technical depth, the elegance of the solution, and the potential future impact
on algorithm development.

Algorithmic Complexity: A typical paper contains algorithms, data structures,
theorems, proofs, or lower bound constructions describing new results on
computational geometry or topology problems. The paper will primarily be
evaluated on the relevance and importance of the problem studied, its technical
depth, the elegance of the solution, and the potential future impact of the
results or the proposed new methods and techniques.

Implementation & Engineering: A typical paper addresses practical aspects of
solving computational geometry and/or topology problems, such as algorithm
implementation and engineering, constants vs. asymptotics, exact, approximate,
or algebraic computation, robustness, or heuristics. The paper will primarily be
evaluated on the (theoretical and practical) relevance and importance of the
problem, the clarity and completeness of the exposition, the quality and
expected impact of the results, the simplicity and elegance of the solution, and
the completeness and soundness of the validation.

Experimentation: A typical paper contains experimental evaluations of data
related to computational geometry and/or topology problems (potentially arising
from external fields), such as a comparison of competing algorithmic approaches,
the design and generation of benchmark data, or cognitive studies on user
interaction. The paper will primarily be evaluated on the relevance and
importance of the problem, the clarity of the hypotheses, the soundness and
completeness of the experiments and evaluation, and the expected impact of the
results.

6 Score and confidence ratings

Each review comes with a score rating and a confidence rating, neither of which
are sent to the authors. As for the score rating, please keep in mind that SoCG
is a highly selective conference. Typically about 30% of the papers submitted
will be accepted; the ratings given by each PC member should take this
constraint into account. These ratings are used as a reference or guide, but the
contents of the reviews are more important and meaningful than the numerical
scores.

Score                 Interpretation

- Strong accept (5)
  An enthusiastic accept. An excellent paper, advancing the field in an
  important way, and well written. People should definitely attend the talk. I
  think this paper will be in the top third of the accepted papers (so roughly
  in the top 10% of the submissions) and is a possible candidate for the best
  paper award. I would fight strongly for this paper.
- Accept (4)
  A strong contribution. I would definitely like to see this paper at the
  conference. I feel I learned something worthwhile from this paper, and believe
  that people will be interested in the talk. I think it will be in the middle
  third of the accepted papers (so roughly in the top 20% of the submissions,
  though perhaps not top 10%).
- Weak accept (3)
  A good contribution, probably in the bottom third of the accepted papers. Not
  a stellar result, but I think it should be accepted, and hope there is enough
  space for it.
- Weak reject (2)
  A contribution with some merits, but probably below the cutoff (that is, not
  within the top one-third of the submissions): I think the problem is not very
  interesting, the solution is not very innovative, and/or the writing is not so
  stellar. I am willing to be convinced otherwise, but there are probably enough
  better papers.
- Reject (1)
  This paper is clearly below the cut in my opinion: the results are not strong
  enough, the writing is quite poor, and/or there are serious concerns about
  correctness or novelty. I would actively argue against accepting the paper.

The confidence ratings are described below.

Grade                 Interpretation

- Expert (4)
  Consider me an “expert” on this paper. I understand it in detail. I know the
  field, and I am perfectly sure about my judgment; I have checked and
  understood all proofs.
- High (3)
  I am fairly familiar with the area of this paper and have read the paper
  closely enough to be confident of my judgment.
- Medium (2)
  I have read the paper carefully and understood the main ideas. I am moderately
  confident of my judgment.
- Low (1)
  I am not an expert. My evaluation is that of an informed outsider. I have some
  idea of what this paper is about, but I’m not all that confident of my
  judgment.

7 Appendix and supplemental data

From the call for papers: All results must be reproducible, that is, all details
needed to verify the results must be provided. For a theorem, there must be a
complete proof that a reviewer could verify. For an implementation, there must
be a package with the full source code and test data or generators that a
reviewer could build and run to reproduce the results. For an experiment, the
setup, conduct, and evaluation must be described in complete detail, so that a
reviewer could go and replicate it. Even though the limited timeframe for
reviewing may not allow to fully review all details, it is upon the authors to
make time the only limiting factor.

Supporting material, such as proofs of theoretical claims, source code of
implementations, and experimental details, that do not fit in the 500-line limit
should be provided in an appendix or as supplemental data. The authors should
include in the main part specific pointers to the relevant locations in the
appendix or to the supplemental data. Additional material will be published, but
not as part of the proceedings. Thus, the paper without the appendix and
supplemental data should be able to stand on its own.

As a consequence, reviewers should comment on the completeness of the
submission. Is sufficient information provided to allow verification and
reproduction of the results?

History of this document. This version of the document was edited by Hee-Kap
Ahn, Michael Hoffmann, and Amir Nayyeri to be used for SoCG 2026. The section on
CoIs was revised based on the “SoCG 2025 Conflict of Interest Guidelines” by
Oswin Aichholzer and Haitao Wang. The first public version of these guidelines
was written by the 2020–2022 CG Steering Committee, consisting of Mark de Berg,
Sándor Fekete, Michael Hoffmann, Matya Katz, Bettina Speckmann, and Yusu Wang,
and published at cg.org on November 26, 2021. The document is based on the
SoCG’21 reviewing guidelines by Kevin Buchin and Éric Colin de Verdière, which
in turn drew inspiration from unpublished versions of similar guidelines that
were circulated among SoCG PCs in earlier years.
~~~~

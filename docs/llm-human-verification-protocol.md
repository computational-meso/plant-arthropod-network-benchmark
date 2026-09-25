# Human verification of AI-assisted data curation

Status: active protocol, adopted 2026-09-25. Human review is not yet complete.

## Purpose

This project uses an LLM to assist with finding source material, reading data
and methods, proposing evidence classes, drafting provenance notes, and
identifying records that need review. The model does not make the final
scientific inclusion or interpretation decision. Named human researchers
remain responsible for the released data and manuscript claims.

The protocol follows the responsibility, accountability, integrity,
transparency, and human-oversight principles in:

> Flemyng E, Noel-Storr A, Macura B, et al. (2025). Position statement on
> artificial intelligence (AI) use in evidence synthesis across Cochrane, the
> Campbell Collaboration, JBI and the Collaboration for Environmental Evidence
> 2025. *Environmental Evidence* 14:20.
> <https://doi.org/10.1186/s13750-025-00374-5>

This framework was written for evidence synthesis rather than ecological data
integration specifically. We apply its general principles to the consequential
interpretive decisions in this derived dataset.

## Division of responsibility

Automated checks establish mechanical consistency: checksums, table schemas,
row and column reconciliation, matrix orientation, identifier uniqueness,
edge hashes, deterministic rebuilding, and mathematical properties of
`B^T B`. They cannot establish whether the project has interpreted the
ecological meaning of a source correctly.

The AI-assisted curation was performed in OpenAI Codex using a GPT-5-based
model. Exact model and session information should be retained when available.
The model's classifications and prose are proposals subject to human review,
not independent expert determinations.

Human reviewers verify consequential ecological judgments against the cited
original data and methods, including:

1. whether the observations represent a natural or semi-natural field
   ecology;
2. whether each plant--arthropod link is evidence of feeding rather than
   incidental association;
3. whether place, sampling window, habitat, and protocol justify the proposed
   network boundary;
4. whether the evidence class and release layer are conservative and correct;
5. whether nested or repeated networks share the correct dependency lineage;
6. whether exclusions, holds, and caveats are scientifically justified.

Manual parser reconstruction is a separate validation task. Reviewers compare
selected raw source records with the normalized and canonical tables, checking
orientation, taxa, positive links, zeros, blanks, totals, and edge hashes.

## Review procedure

For every queued source decision or reconstruction:

1. Open the linked original data, open methods, and source-specific audit note.
2. Compare the source evidence with the proposed interpretation or parsed
   network.
3. Record `pass` or `changes_required`, the reviewer's name, an ISO 8601 date,
   and a short justification in
   `data/empirical/benchmark/human_review_ledger.draft.json`.
4. If a correction is required, update the source audit or parser, rebuild the
   collection, and review the regenerated record again.
5. Escalate unresolved ecological ambiguity for discussion; classify
   conservatively until resolved.

The current queue contains 19 source decisions and 19 manual reconstruction
checks. Accepted and borderline source decisions require a second human
review. Automated validation by the same system that proposed a classification
does not satisfy that requirement.

## Provenance and reporting

Retain the source citation and URL, controlled raw-object checksum, source
audit note, proposed model interpretation, human decision, reviewer identity,
review date, and any correction. Repository history and versioned releases
provide the change record. Do not include private prompts, credentials, or
unnecessary personal data in the public release.

Before review is complete, manuscripts must describe classifications as
provisional and human verification as planned or in progress. After all gates
pass, suitable wording is:

> An LLM-assisted workflow was used to propose source interpretations and
> identify records for review. Human reviewers checked all consequential
> ecological inclusion and classification decisions against the original data
> and methods, while independent manual reconstructions tested selected parser
> outputs. All corrections were incorporated before release, and the review
> status and provenance were retained in the versioned build records.

This statement should be revised if the completed workflow differs from the
protocol above. The model name, its limited role, and the number and disposition
of reviewed records should be reported in the final manuscript.

# Human review packet

This folder is a transparency copy of the generated review packets. It shows
exactly which ecological interpretations require human confirmation, but the
public preview intentionally does not redistribute controlled raw source files
or the editable private review ledger. Review work is recorded in the source
repository's `data/empirical/benchmark/human_review_ledger.draft.json`, then a
fresh public preview is generated.

## Manual network reconstruction

Open `manual_reconstruction_packet.csv`. In the controlled source workspace,
open `raw_object_path` and locate `source_file_or_member`. Compare that source
object with `source_normalized_matrix` and `binary_matrix` using the supplied
checklist. A ZIP member path is relative to the archive; a workbook source may
instead name a sheet or embedded table. Record `pass` only when orientation,
taxa, values, interaction states, and the stated ecology boundary agree.

## Independent source decisions

Open `source_decision_packet.csv`. For each included study or exclusion/deferral, check
the DOI, methods, license evidence, decision basis, and linked audit note. The reviewer
should be independent of the primary screen to the extent practical for the thesis team.

## Recording decisions

For each `ledger_key`, the assigned reviewer updates only the matching entry in
the controlled authoritative ledger; the paths in these public packets are
provenance references and are not expected to resolve in this repository.
Allowed statuses are `pending`, `pass`, and `changes_required`. Every non-pending entry
requires a reviewer name and ISO date (`YYYY-MM-DD`). Explain discrepancies in `notes`;
do not edit generated release tables. Rebuild the benchmark after any ledger change.
Publication remains blocked until both review groups pass.

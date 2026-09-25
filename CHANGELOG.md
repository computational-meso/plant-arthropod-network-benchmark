# Changelog

## 0.1.0-preview.3 — 2026-09-25

- Adds an executed Python/Jupyter quick-start notebook and public release validator.
- Adds automated GitHub checks for the data, script, notebook, and manifests.
- Renames active taxon counts in `network_metrics` to remove ambiguity with
  source-pool counts in `networks`.
- Corrects Parquet paths in the data-package metadata and replaces the stale
  private-build manifest with a public-package manifest.
- Clarifies that public review packet paths refer to the controlled source
  workspace and removes an accidental Python cache file from release packaging.

## 0.1.0-preview.2 — 2026-09-25

- Adds verified Python and R quick-start examples. The R convenience example
  was retired in preview.3 to keep the supported path focused on Python.
- Adds installation, table, analysis, and contribution guidance.
- Adds a minimal Python dependency specification.
- Keeps the data tables and scientific status unchanged from preview.1.

## 0.1.0-preview.1 — 2026-09-25

- First public technical preview.
- Publishes 17 canonical derived tables and matching Parquet views.
- Records 346 network objects from 10 ingested studies.
- Marks 126 E0/E1 networks as provisionally direct and 220 networks as E2.
- Reports 723 passing automated QA checks.
- Leaves two human-review release gates explicitly pending.
- Excludes all upstream raw archives from redistribution.

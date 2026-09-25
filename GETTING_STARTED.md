# Getting started

The repository is ready for analysis without downloading the larger CSV
archive. The committed Parquet tables contain the same rows as the canonical
CSV tables and load quickly in Python.

## Python

Requirements: Python 3.10 or newer and Git.

```sh
git clone https://github.com/computational-meso/plant-arthropod-network-benchmark.git
cd plant-arthropod-network-benchmark
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 examples/quickstart.py
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

The example is read-only. A successful run reports the total corpus, the
provisional direct layer, the number of dependency clusters, and a verified
`B.T @ B` projection for one qualifying network.

## Guided Jupyter notebook

The notebook shows the same import path and adds a compact study summary, an
incidence matrix, a verified shared-host projection, and the ten strongest
shared-host pairs in one example network. Install the optional notebook tools
and open it from the repository root:

```sh
python3 -m pip install -r requirements-notebook.txt
python3 -m jupyter lab notebooks/quickstart.ipynb
```

The committed notebook includes verified example output, so it is also readable
directly on GitHub without installing anything.

## Verify the complete public package

Run the same integrity and graph-reconstruction checks used by continuous
integration:

```sh
python3 scripts/validate_release.py
```

The validator checks identifiers and joins, interaction states, complete source
grids, taxon and network counts, all 94,631 projected edges, metadata entities,
and available checksums. In a release download it also verifies all canonical
CSV files.

## Which files should I use?

- Begin with `data/parquet/networks.parquet` to select networks.
- Join `data/parquet/interactions.parquet` by `network_id` for ecological
  interactions.
- Join `studies.parquet` for study and source-provided ecosystem labels.
- Join `sampling_events.parquet` for place, time, habitat, and protocol.
- Use `competition_edges.parquet` for the precomputed shared-host projection.
- Use `network_metrics.parquet` for graph sizes and analysis gates.
- Use `sources.parquet` and `derived_products.parquet` for provenance and
  attribution.

The release download additionally supplies all 17 tables as canonical CSVs,
EML metadata, and checksums.

In `networks`, `plant_count` and `herbivore_count` include every source-pool
taxon represented in the bounded grid. In `network_metrics`, the explicitly
named `active_plant_count` and `active_herbivore_count` include only taxa with
at least one observed positive link.

## Recommended first subset

For the paper's direct-data analyses, start with rows of `networks` where
`eligible_direct` is true and `evidence_class` is E0 or E1. These classifications
remain provisional while human review is in progress.

Treat `independence_cluster_id`, rather than `network_id`, as the conservative
field-replication unit. Repeated years, seasons, guilds, protocols, or nested
spatial grains may be distinct networks without being statistically independent.

## Interaction states

The canonical interaction table distinguishes `observed_positive`,
`sampled_zero`, `structural_zero`, `not_sampled`, and `unknown`. Do not replace
unknown or unsampled records with biological zeros. The quick-start projection
uses confirmed positive incidence only; its zero entries mean that no positive
edge is represented in that projection, not necessarily that a pair was
demonstrably sampled and absent.

## Quantitative weights

Use `binary_value` for cross-study analyses. `source_value` retains counts,
damage, biomass, occurrence frequencies, molecular reads, or other source units
and should only be compared within compatible studies or in explicitly labeled
sensitivity analyses.

## Before publishing results

Read `docs/ANALYSIS_NOTES.md`, cite the original source datasets relevant to
your subset, report the exact preview or final version, and state how repeated
networks were handled. Do not call projected shared-host edges observed
competition.

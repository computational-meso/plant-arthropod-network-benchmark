# Harmonized terrestrial plant–arthropod interaction networks

> **Provisional public preview — human review is still in progress.**
>
> This is not the final EDI dataset release and has no DOI. Ecological evidence
> classifications remain provisional until the documented second review and
> manual reconstruction checks are complete. Use the exact preview version if
> referring to these files, and do not describe the collection as globally
> representative or fully audited.

This repository provides an early, analysis-ready preview of a derived
collection of terrestrial plant–arthropod interaction networks. The governing
unit is:

> one network = place × sampling window × habitat × protocol.

The collection preserves source-level provenance, explicit interaction states,
verbatim taxon names, evidence classes, nested sampling relationships, and
dependency-aware identifiers. It also supplies projected shared-host graphs for
studying potential exploitative competition. A projected edge means two
herbivores share a host plant; it is not evidence of realized competition.

## Preview contents

Version `0.1.0-preview.3` contains:

- 346 bounded network objects from 10 ingested field studies;
- 126 provisional direct E0/E1 networks from 8 studies;
- 220 E2 derived or conservatively classified networks;
- 38 dependency-aware direct field lineages;
- 6 source-described direct ecosystem classes;
- 848,907 represented interaction cells;
- 19,855 positive bipartite links;
- 723 passing automated checks and 2 pending human-review gates.

The compact Parquet tables are committed under `data/parquet/`. The GitHub
release contains the complete 17-table canonical CSV archive, EML metadata,
checksums, and the same Parquet tables. Upstream raw archives are intentionally
not redistributed.

## Get started in five minutes

You need Python 3.10 or newer and Git. Clone the repository, create an isolated
environment, install the small analysis dependency set, and run the verified
example:

```sh
git clone https://github.com/computational-meso/plant-arthropod-network-benchmark.git
cd plant-arthropod-network-benchmark
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 examples/quickstart.py
```

The example loads the tables, selects the provisional E0/E1 direct layer,
constructs one plant-by-herbivore incidence matrix, computes `B.T @ B`, and
checks the host-breadth diagonal. It does not alter the data.

For a guided version, open the executed
[Python quick-start notebook](notebooks/quickstart.ipynb). Start with
[GETTING_STARTED.md](GETTING_STARTED.md) for setup instructions,
[docs/TABLE_GUIDE.md](docs/TABLE_GUIDE.md) for table relationships, and
[docs/ANALYSIS_NOTES.md](docs/ANALYSIS_NOTES.md) before conducting cross-network
statistics.

## Start analysis

The canonical relationship is a long interaction table. Join interactions to
networks by `network_id`. For the current direct-data analysis, filter networks
to evidence classes `E0` and `E1`, and account for
`independence_cluster_id` rather than treating all network objects as
independent replicates.

```python
import pandas as pd

networks = pd.read_parquet("data/parquet/networks.parquet")
interactions = pd.read_parquet("data/parquet/interactions.parquet")

direct_ids = networks.loc[
    networks["eligible_direct"]
    & networks["evidence_class"].isin(["E0", "E1"]),
    "network_id",
]
direct = interactions[interactions["network_id"].isin(direct_ids)]
```

Do not turn blank, unknown, or unsampled combinations into biological zeros.
See `metadata/eml-draft.xml` for machine-readable field definitions and
[docs/TABLE_GUIDE.md](docs/TABLE_GUIDE.md) for table relationships.

## Evidence and release layers

- `E0`: direct, bounded field ecology.
- `E1`: repeated or nested direct ecology with parent/dependency identifiers.
- `E2`: locally inferred, filtered, molecular, or conservatively classified
  network.
- `E3`: target layer extracted from a broader bounded food web.
- `M`: regional or global metaweb, kept separate from local ecologies.
- `X`: enrichment or screened source without a complete eligible network.

Only E0/E1 networks are candidates for headline direct-data claims. Evidence
class is separate from an analysis threshold: valid networks can remain in the
dataset even when omitted from a particular statistical test.

## Validation status

The complete source build passes 28 automated tests and 723 automated QA checks.
The public repository also runs a release validator, Python script, and notebook
on every change through GitHub Actions.
Two scientific validation gates remain open:

1. independent manual reconstruction of 19 selected networks; and
2. independent human review of 19 accepted, excluded, or borderline source
   decisions.

The human-review procedure is documented in
`docs/llm-human-verification-protocol.md`. AI-assisted interpretations are
proposals, not final ecological judgments.

## Provenance and licensing

This is a derived synthesis. `sources`, `derived_products`, and `file_manifest`
identify every upstream dataset, version, retrieval URL, checksum, and reuse
status. The raw archives remain available from their original repositories.

The creators dedicate the rights they control in the harmonization,
organization, metadata, and other original contributions under CC0 1.0. This
does not override third-party rights or upstream terms. Source-level licenses
and required attribution remain in the release tables; notably, the Shinohara
source-derived component retains its CC BY 4.0 attribution requirement. See
`LICENSE.md` and `THIRD_PARTY_NOTICES.md`.

## Citation

This preview has no DOI and should not be cited as the final dataset. If an
exact reference is necessary during review or collaboration, cite the GitHub
repository and tag `v0.1.0-preview.3`. The authoritative release is planned for
the Environmental Data Initiative and will receive a versioned DOI after human
review and repository curation.

Creators, in order:

1. Alex Stevens, University of Denver — ORCID 0009-0003-0431-9289
2. Theo Canji, University of Denver

## Scope limitations

This is a selective benchmark of reusable open studies, not an exhaustive or
representative census of global plant–arthropod interactions. Ecosystem labels
come from the source studies. The preview does not merge external climate,
trait, abundance, or land-use databases.

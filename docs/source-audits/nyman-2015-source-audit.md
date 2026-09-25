# Nyman et al. source audit

## Decision

Exclude Nyman et al. candidate `C016` from both the direct `E0`/`E1`
benchmark and the derived `E3` network layer. Retain the complete CC0 Dryad
package and its API metadata as controlled source-level evidence (`X`) with
zero admitted plant--herbivore network objects.

The decisive distinction is between a population sample and an ecology
network. The released workbook has 22 rows, but every row identifies exactly
one *Pontania* galler, one *Salix* host, and one location. Its 14 numeric
columns are parasitoid species. The 22 rows therefore are 22 single
plant--galler population samples used to construct a herbivore--parasitoid
matrix, not 22 local plant-by-herbivore community matrices.

The row labels provide 22 diagnostic positive plant--galler observations.
They do not provide a sampled community-wide frame for unobserved plant--galler
pairs. Pooling those positives by location or habitat would define new
analyst-chosen networks and would require treating unreported cross-pairs as
sampled or structural zeros without source evidence. That transformation is
not permitted by the locked boundary and interaction-state rules.

## Source identity and openness

- Study: Nyman T, Leppänen SA, Várkonyi G, et al., *Determinants of
  parasitoid communities of willow-galling sawflies: habitat overrides
  physiology, host plant, and space*.
- Article DOI: `10.1111/mec.13369`.
- Data DOI: `10.5061/dryad.km75s`.
- Dryad record: dataset 4425, version 4452, version 1.
- Dryad publication date: 2015-09-03; last metadata modification: 2020-06-24.
- Data license: CC0 1.0.
- Source setting: subarctic and arctic--alpine habitats at three locations in
  northern Fennoscandia.
- Source-stated biota: seven *Pontania* sawfly species on eight *Salix*
  species, with 14 parasitoid species identified from larvae.

The Dryad data and metadata are openly available. The publisher page exposes
the abstract and supporting-information descriptions, including Table S1's
description of 22 population samples and Figure S2's location codes. The full
article methods were not openly accessible during this audit. That methods
limitation is recorded, but it is not the primary exclusion: the acquired raw
objects themselves establish that the target community layer was not
released.

The publisher Table S1 PDF was consulted online to check terminology and
habitat grouping but is not redistributed. The benchmark stores only the CC0
Dryad objects and API captures.

## Raw acquisition and integrity controls

All five Dryad data files and two API captures are immutable under the build.
Every local object is pinned by SHA-256; the five deposited data objects also
match the MD5 digest returned by Dryad.

| Object | Bytes | SHA-256 | Dryad MD5 |
| --- | ---: | --- | --- |
| `Barcode_sequences_of_parasitoid_larvae.nex` | 413,104 | `2321232cf1bb474891cb4a4279d6f6ad44d97f94b6bb9641e20e16253dab0e9d` | `a488bef5e29ee86d0d6eb971fbd1a511` |
| `Barcode_sequences_of_reared_parasitoid_reference_specimens.nex` | 53,920 | `b28fddc3f24d5b470b2971874a13da5a913d1047a291a412c0f0b45008c1c3aa` | `e33f2b9dba822e9fcbde5356244c8a1b` |
| `Commands_and_data_for_GLM_analyses_in_mvabund.txt` | 2,776 | `4564d3e50c4807d81fde0caa21bbe9a480cbff19d1bf8d4fc1e00bab3e0a000e` | `c9e8765f5433cc43db45c3fb2ff15fce` |
| `Commands_and_data_for_test_of_phylogenetic_effects.txt` | 3,111 | `262b94c2e3580ddf2120c5d1333361985d6f30722ce955eee6ace0ec800d2ff0` | `ae800a621dce4b8017ac3da68eaa61a8` |
| `Parasitoid_numbers_raw_data.xlsx` | 14,614 | `40a6a71bafe4acfdfd68da2d28ce10b0a340d73395c6796c0d74579e6ae99a7f` | `21121703d91f3345c3f70aa5e6350324` |
| `dryad_dataset_metadata.json` | 8,057 | `9a9a78d21636b714e9c1e481bcb19753e9c9905ab11e4101b6c0455eba0c3f72` | not supplied |
| `dryad_files.json` | 4,198 | `0cad1d868a085d46756e99568068e4fe7492cbcf2408376b738c2a7fa72a7dd6` | not supplied |

The Dryad file inventory reports five files totaling 487,525 bytes, exactly
matching the dataset metadata's storage size and the acquired data objects.

## Workbook and sequence reconciliation

The deterministic source validator establishes:

- workbook sheets: `Sheet1`, `Sheet2`, and `Sheet3`, with data only in
  `Sheet1`;
- data extent: 22 population rows by 14 parasitoid columns;
- interaction values: 561 parasitoid larvae, 89 positive parasitoid cells,
  and 219 explicit numeric zeros, with no blank cells in the numeric grid;
- sampling locations: eight rows at ABI, seven at KIL, and seven at TRO;
- row-label plant coverage: eight verbatim *Salix* species;
- galler labeling: eight verbatim operational strings, including the source's
  unresolved `aquilonis_or_herbaceae` label; these must not be silently merged
  or resolved even though the abstract describes seven sawfly species;
- larval sequence file: `NTAX=561`, `NCHAR=658`;
- reared reference sequence file: `NTAX=72`, `NCHAR=658`;
- all 561 larval sequence identifiers reconcile exactly to the corresponding
  22 workbook row totals;
- the 21-row GLM input totals 538 larvae, with each `NSEQ` equal to its row's
  parasitoid counts; the omitted *P. arcticornis*--*S. phylicifolia* ABI row
  contains the remaining 23 larvae.

This cross-file agreement is strong evidence that the package is complete for
the study's parasitoid-community analysis. It does not change the trophic
orientation of the numeric layer.

## Boundary audit

| Candidate interpretation | Source support | Benchmark decision |
| --- | --- | --- |
| 22 local plant--herbivore networks | none: each row has only one plant--galler pair | reject |
| 3 location-level plant--herbivore networks | positive row labels can be pooled, but the boundary and non-links are analyst-defined | reject |
| 6 location-by-habitat plant--herbivore networks | habitat grouping is described in supporting information, but pooling and zeros remain analyst-defined | reject |
| local plant--herbivore layer extracted from broader webs (`E3`) | numeric webs are galler--parasitoid population-sample matrices, not bounded multitrophic community webs | reject |
| source-level diagnostic plant--galler observations (`X`) | row labels directly identify sampled plant--galler populations | retain as provenance only |

An `E3` designation would be misleading. `E3` is reserved for selecting an
already observed plant--herbivore layer from a broader field-bounded local food
web. Here, the target link appears in the definition of each population sample,
while the observed matrix is the next trophic layer. There is no released
broader local community adjacency object from which the target layer can be
losslessly extracted.

## Interaction-state discipline

The 219 zeros in the workbook are valid explicit zeros only for parasitoid
species within a named galler--willow population sample. They say nothing about
whether other gallers were sampled on that willow, whether that galler was
sampled on other willows, or whether a nonreported target pair is biologically
impossible. No target-layer blank or absence is converted to a sampled zero,
structural zero, or negative association.

This is why retaining the 22 positive labels without constructing networks is
the conservative and reproducible treatment.

## Eligibility audit

| Criterion | Result | Consequence |
| --- | --- | --- |
| Natural or semi-natural field system | appears to pass | does not supply a target community matrix |
| Location recoverable | pass at three coded locations | locations alone do not define source-released target networks |
| Sampling interval recoverable from open material | insufficient | independently fails the open-methods requirement |
| Habitat recoverable | pass at broad source-described classes | habitat pooling would still be a derivation |
| Feeding evidence | pass for the sample-defining galls | only positive plant--galler population labels are observed |
| Community-scale plant--herbivore edge table | fail | no `E0`/`E1` admission |
| Bounded broader food web with extractable target layer | fail | no `E3` admission |
| Open raw data and reusable license | pass | retain all Dryad objects in `R0` provenance |
| Original study lineage identifiable | pass | register one controlled candidate, not an ingested study |

## Release treatment

- `sources`: one non-ingested source record with the boundary exclusion.
- `candidate_registry`: `C016`, zero candidate target networks after audit.
- `exclusions`: controlled reason
  `population_samples_not_plant_herbivore_community_networks`.
- `file_manifest`: seven immutable objects, with Dryad MD5 and local SHA-256
  where available.
- `qa_results`: file, workbook, sequence, GLM, orientation, and zero-admission
  controls.
- `networks`, `sampling_events`, `taxa`, `interactions`, and `derivations`: no
  Nyman rows.

At the time of this audit, the headline remained unchanged at 125 provisional
direct networks from seven independent original studies. Rejecting this
tempting 22-network count is an important protection against pseudo-replication
and source-boundary inflation.

## Open references

- Dryad data: <https://datadryad.org/dataset/doi:10.5061/dryad.km75s>
- Publisher article and supporting information: <https://onlinelibrary.wiley.com/doi/10.1111/mec.13369>
- PubMed record: <https://pubmed.ncbi.nlm.nih.gov/26340615/>
- Institutional publication record: <https://folia.unifr.ch/global/documents/37928>

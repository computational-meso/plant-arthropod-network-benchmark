# Sousa-Lopes and Del-Claro (2024) source audit

## Decision

Admit one annual ecology network to `R2` as `E0`:

`sousa_lopes_2024_ccpiu_2016_2017`

Do not construct twelve monthly networks from the workbook. The source defines
one annual interaction matrix explicitly. Its plant-specific monthly sheets do
not reconcile to that matrix without new taxon matching and inclusion/exclusion
decisions, so they remain source provenance only.

## Source and version

- Article: Sousa-Lopes B and Del-Claro K (2024), *Temporal distribution of
  endophytic and exophytic insect guilds responds to host plant phenology in the
  Brazilian Savannah*, DOI `10.1111/een.13392`.
- Data: Dryad DOI `10.5061/dryad.zw3r228hj`.
- Controlled release: Dryad dataset 141689, version 322747, version number 9,
  published 2024-10-18 under CC0.
- Deposited workbook: file 3550313, 244,736 bytes, repository SHA-256
  `edc88c0017991fc6c6984e72582eeb92b1a872301ecb289a40ec6af4fda69a0e`.
- Deposited README: file 3550337, 3,478 bytes, repository SHA-256
  `d87f0dee4b3706acf164b2e5de2441c38534564728684ec0351ce7802b08673c`.
- Local Dryad dataset and file-list API captures are also pinned in the release
  manifest.

The workbook is a legacy `.xls` file and is parsed with `xlrd`; it is never
resaved or altered.

## Ecology boundary and direct evidence

The open repository methods recover every required boundary field:

- place: Clube Caça e Pesca Itororó (CCPIU), Uberlândia, southeastern Brazil
  (18°59′S, 48°17′W);
- habitat: a Brazilian Cerrado reserve containing sensu stricto cerrado and
  Vereda vegetation;
- window: monthly sampling from October 2016 through September 2017;
- protocol: all structures of 97 tagged individuals of five Fabaceae species
  were inspected for 30 minutes per plant per month, divided between two
  sessions, for 582 observation hours in the year;
- evidence: the authors retained insects as true herbivores only when they were
  observed feeding on plant structures in the field or laboratory. Collected
  insects were reared with the same plant structure on which they were found.

The source-defined annual matrix therefore represents one place × annual
sampling window × habitat × protocol ecology and passes the direct-evidence
screen. It is `E0`, rather than `E1`, because no repeated or nested network
object is emitted.

## Annual matrix reconciliation

The `Ecological Network` worksheet is oriented as plant rows × herbivore
columns. It contains five plant taxa and 87 unique herbivore labels. All
herbivore columns and all plant rows are active.

| Plant row | Positive links | Annual abundance |
|---|---:|---:|
| *Andira humilis* | 22 | 49 |
| *Bauhinia rufa* | 21 | 51 |
| *Chamaecrista cathartica* | 12 | 153 |
| *Mimosa setosa* var. *paludosa* | 17 | 1,239 |
| *Stryphnodendron polyphyllum* | 22 | 131 |
| **Total** | **94** | **1,623** |

The complete frame has 435 cells. Ninety-four are positive whole-number
frequencies. The other 341 contain `n/a`. The README defines `N/A` as “not
found,” and all five plant species were co-surveyed across the full annual
protocol. These cells are therefore encoded explicitly as `sampled_zero`, not
as structural zero, unknown, or missing. Surrounding whitespace in labels is
trimmed, while source taxon strings otherwise remain unchanged.

## Why monthly network objects are not emitted

The workbook has a cumulative species-over-time sheet and five plant-specific
monthly abundance sheets, but it does not provide one coherent
month × plant × true-herbivore table. A direct audit found:

| Plant sheet | Sum of monthly data rows | Sum printed in its total row | Annual matrix abundance |
|---|---:|---:|---:|
| Andira | 55 | 56 | 49 |
| Bauhinia | 68 | 68 | 51 |
| Chamaecrista | 146 | 146 | 153 |
| Mimosa | 1,530 | 1,530 | 1,239 |
| Stryphnodendron (`Stryp`) | 142 | 141 | 131 |

The monthly tabs also contain ants and other records that are absent from the
annual true-herbivore matrix, use taxon labels that do not match the annual
headers consistently, and have two internal row-versus-total discrepancies.
For example, the `Tourists` sheet separately describes insects that did not
feed on the focal plant phenophases. Promoting the monthly sheets would require
analyst-defined taxon crosswalks and decisions about which records satisfy the
authors' final true-herbivore filter. It would also create twelve temporally
nested objects that the source did not publish as network matrices.

The conservative release therefore preserves the whole workbook in `R0`,
records the monthly mismatch in QA and parser provenance, and emits only the
annual matrix in `R1` and `R2`. Monthly networks can be reconsidered only if the
authors provide a reconciled month-by-plant-by-true-herbivore table or an exact
row-level crosswalk.

## Reproducibility controls

The parser checks:

1. all four local source and API objects against pinned sizes and SHA-256
   digests;
2. exact workbook sheet names and order;
3. the 6 × 88 annual worksheet dimensions and matrix orientation;
4. five expected plant labels and 87 nonempty, unique herbivore labels;
5. 94 positive links, 1,623 individuals, and 341 `n/a` cells;
6. plant-specific annual link and abundance totals;
7. monthly data-row sums and the workbook's printed monthly total rows; and
8. zero admitted monthly network objects.

The generic benchmark checks then cover raw immutability, canonical interaction
states, graph projection, CSV/Parquet agreement, build manifests, and release
determinism. Independent second review and manual reconstruction remain pending
for this provisional source.

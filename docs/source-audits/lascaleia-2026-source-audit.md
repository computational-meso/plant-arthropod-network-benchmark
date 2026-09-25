# LaScaleia et al. 2026 source audit

## Decision

Retain 96 field-bounded site-year networks as `E2` in release layer `R3`. Do
not count them toward the direct E0/E1 headline unless open observation-level
evidence is recovered that confirms active feeding on the recorded plant.

The source is valuable: it supplies standardized sampling, explicit empty-
branch records, plant and caterpillar identities, counts, dates, effort, 32
forest patches, 13 geographic blocks, and three comparable years. However,
caterpillars were recovered by striking branches and the encountered plant was
recorded as the host. Source experts removed known non-host singleton records,
but the retained records do not document feeding for each observation. Under
the benchmark's locked rule, host association is not promoted to direct
feeding evidence.

## Source and files

- Study: LaScaleia MC, Elphick CS, Mickley JG, Singer MS, Wagner DL, Bagchi R
  (2026), *The effect of resource concentration on consumer population
  densities depends on spatial scale and diet breadth*.
- Article DOI: `10.1002/oik.12223`.
- Data DOI: `10.5061/dryad.8931zcs5z`.
- Audited Dryad object: dataset 186201, version 447750, version 4, CC0.
- Analysis archive `repositoryForDryad.zip`: 26,323,566 bytes; SHA-256
  `b6224a51668acab2eed535e308c345837b0a4df8adc7c76a1d6cfaf334137a76`.
- Repository `README.md`: 6,561 bytes; SHA-256
  `aab67883413391966262d09fbb8de95e7620459c7fb13583b4d60788e4d31dea`.
- Retrieved Dryad version wrapper: 26,334,261 bytes; SHA-256
  `0ab9666bf834f624910e53f87d4d1136a707c20cd27602fe21a20af4061c5d97`.

The canonical observation input is
`repositoryForDryad/data/raw/CaterpillarSurveysAllYears-v1_2.csv`. Plant names
come from `repositoryForDryad/data/reference/treeSpecies.csv`; survey geometry
and coordinate validation also use
`repositoryForDryad/data/raw/VegetationSurveys.csv`.

## Boundary reconstruction

The comparable survey contains all 96 combinations of 32 sites and years
2017–2019. Sites are nested in 13 blocks. Every site-year contains 12 plot
identifiers. Ninety-two site-years have one survey date; four span two adjacent
dates. A canonical ecology is therefore:

> site × annual June sampling event × secondary New England forest ×
> standardized branch-strike caterpillar survey.

`independent_site_id` records the source site and `parent_site_id` plus
`independence_cluster_id` record the geographic block. Site coordinates are
the mean of point-level coordinate means because a small number of source
points contain repeated, slightly varying coordinates.

## Lossless and lossy transformations

The raw archive is immutable R0. The parser performs these explicit operations:

1. Omit 2015 because the source code and methods identify it as a preliminary,
   protocol-incompatible sample.
2. Retain 2017–2019, yielding 11,016 source rows.
3. Retain 6,377 empty-branch rows as sampling effort and zero evidence.
4. Exclude 21 rows flagged `BadHost=yes`, representing 23 individuals judged
   by source experts to be non-host encounters.
5. Treat plant code `NA` as the source's no-tree sentinel, not as a taxon.
6. Aggregate retained `Count` values by site, year, plant code, and caterpillar
   code. Preserve count units; derive binary incidence only for cross-study
   projections.
7. Preserve 53 mapped plant codes and all observed caterpillar operational
   identifiers without merging taxa across studies. The raw name for `SHIZUN`
   is retained because that identifier is absent from the separate species
   reference.

One site-year (`MT`, `WSS`, 2019) has no positive caterpillar record. It remains
in the descriptive release because a sampled empty ecology is biologically
different from missing data, but it cannot pass a projection gate.

## Validation result

- Exactly 96 site-year networks, 32 sites, 13 blocks, and three years.
- Plant/herbivore orientation is constructed from named source fields, not
  inferred from matrix position.
- All raw hashes are checked before parsing; the primary archive is checked
  again after the build.
- Each network produces a symmetric nonnegative shared-host projection by
  construction, and the binary projection diagonal equals herbivore host
  breadth.
- The source remains `borderline_second_review_pending`; manual reconstruction
  and independent evidence adjudication are still required.

## Open references

- Dryad record: <https://datadryad.org/dataset/doi:10.5061/dryad.8931zcs5z>
- Oikos article: <https://nsojournals.onlinelibrary.wiley.com/doi/abs/10.1002/oik.12223>
- Open author preprint:
  <https://d197for5662m48.cloudfront.net/documents/publicationstatus/291441/preprint_pdf/f9654ec443f302e7108801e6c4f65388.pdf>
- Related detailed Dryad source:
  <https://datadryad.org/dataset/doi:10.5061/dryad.k3j9kd5k8>

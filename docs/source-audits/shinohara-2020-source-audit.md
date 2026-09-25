# Shinohara et al. 2020 source audit

## Decision

Retain the 36 plot-by-season herbivory networks as `E1` objects in release
layer `R2`. Each object is a directly observed, field-bounded ecology:

> one land-use plot × one seasonal sampling window × semi-natural
> rice-field-edge grassland × the direct feeding-observation protocol.

The 36 objects comprise 12 plots sampled in three seasons. The 12 plots were
arranged as four geographic site clusters, each containing one abandoned, one
extensively managed, and one intensively managed plot. Because plots within a
cluster were less than 500 m apart and the authors explicitly considered
within-cluster nonindependence, the primary independence unit is the four site
clusters, not 12 plots or 36 networks.

Only the herbivory layer is included. The source's pollination records and
plant-composition observations remain immutable R0 material and are not mixed
into the plant--herbivore benchmark.

## Source lineage, access, and license

- Study: Shinohara N, Uchida K, Yoshida T (2019/2020), *Contrasting effects of
  land-use changes on herbivory and pollination networks*.
- Article DOI: `10.1002/ece3.5814`.
- Article-linked data DOI: `10.6084/m9.figshare.10000352.v1`.
- Original audited deposit: Figshare article 10000352, version 1, CC BY 4.0.
- Later registered mirror: Dryad dataset 35155, version 38056, file 170009,
  DOI `10.5061/dryad.gqnk98sh7`, CC0.
- Open methods and taxonomy supplement: Europe PMC `PMC6912900`.

The article's data-availability statement points to Figshare, so Figshare v1
is the primary source. The later Dryad mirror is recorded for lineage and
recovery but is not silently substituted. During this audit the Dryad raw-file
route returned an automated access challenge; no attempt was made to bypass
it because the original open Figshare files and the article's open supplement
were sufficient to reconstruct the networks.

## Pinned source objects

| Object | Bytes | Local SHA-256 | Repository control |
| --- | ---: | --- | --- |
| `Data_Interactions.csv` | 29,370 | `dada046d2635697cfa1c5e82ab97503181ec1b370347be3b6856cd334b0953cb` | Figshare MD5 `5d5a087b0d89bfc354cf3d11cdc55e8a` |
| `Data_Plant_Composition.csv` | 27,349 | `5bd0cceddc31bef3ef7258ecb5edd7b2be25f9b2a6413e20bc3be2b298b93d90` | Figshare MD5 `aea4782e9375e2c19333a355f1fcb742` |
| `ECE3-9-13585-s003.docx` | 66,539 | `108795eb4fad0c4fbc93001af2562cf403d8cee8855f9364f218da188bc33e63` | local pin; Europe PMC supplies no file checksum |
| `PMC6912900.xml` | 129,150 | `44f2cac709a8d7f1dfe2d6159940d19bd5704c64d7ca314dda12c4838244f210` | local pin; Europe PMC supplies no file checksum |
| `PMC6912900_SupplementaryFiles.zip` | 3,996,732 | `2fa24d7b29c15a1e864e84f447380fd6b8e6629e14f5b19c077ff8722a5d19c2` | local pin of dynamically assembled package |

The build verifies every listed byte size and SHA-256. It also verifies the
repository MD5 for both original Figshare CSVs.

## Boundary and evidence reconstruction

The field system was a roughly 40 km² agricultural landscape in Wakasa town,
Fukui Prefecture, Japan, dominated by rice fields with semi-natural grasslands
along field edges. The source reports a study-area coordinate range, not
per-plot coordinates; the release therefore preserves that range in the study
geography and leaves network latitude and longitude blank.

Each plot contained a 2 × 30 m transect. In each season, observers surveyed a
plot once in the morning and once in the afternoon for 150 minutes per visit.
The two visits were combined by the authors, yielding five observer-hours per
plot-season network. Seasonal windows were:

| Source season | Start | End |
| --- | --- | --- |
| spring | 2016-05-29 | 2016-06-11 |
| summer | 2016-06-28 | 2016-07-11 |
| fall | 2016-09-05 | 2016-09-24 |

The methods state that an herbivory interaction was counted only when an
insect was observed consuming the leaves or stems of an identified plant.
This is direct feeding evidence and satisfies the locked E0/E1 criterion. The
repeated seasons make each network `E1`; they do not create new independent
sites.

## Parser controls

The original interaction edge list contains 633 positive rows and 1,802 total
observations across both interaction types:

| Layer | Positive pairs | Observation frequency |
| --- | ---: | ---: |
| herbivory | 287 | 609 |
| pollination | 346 | 1,193 |

The plant-composition table contains 845 rows with a relative-abundance sum of
4,329. Both files form the same complete 4 site × 3 season × 3 land-use grid.
Every herbivory plant ID occurs in the corresponding plot-season composition
record. The supplementary taxonomy table provides all 144 insect IDs and all
131 plant IDs; source-local numeric IDs remain attached to canonical taxon
records after names are resolved.

The parser requires all 36 herbivory groups, rejects duplicate plant--insect
pairs within a group, and reconciles the exact row and frequency totals before
yielding any network. The resulting networks contain 2--11 active plants,
2--12 active herbivores, and 2--20 positive links.

## Interaction-state semantics

The canonical network contains only plant and herbivore taxa with at least one
positive herbivory record in that plot-season. A positive cell preserves the
source frequency and exact CSV row; `source_column=7` identifies the frequency
field. An unrecorded combination of two active taxa in the same exhaustively
observed five-hour plot-season is represented as `sampled_zero`, but has blank
source row and column because the zero is a derived sampling opportunity, not
an explicit edge-list row.

Plant-composition-only species are not added as zero-degree network taxa.
Pollination rows are not reinterpreted as herbivory. Both remain in R0. This
keeps the direct network faithful to the authors' network boundary without
converting blanks into biological zeros.

## Dependencies and validation

- `independent_site_id`: one site × land-use plot, yielding 12 plot IDs.
- `parent_site_id` and `independence_cluster_id`: one of four source site
  clusters.
- three seasonal E1 networks share each plot ID.
- the three land-use plots within a cluster share the conservative cluster ID.

All 36 networks pass the nonnegative symmetric `B^T B` check, and every binary
projection diagonal equals herbivore host breadth. The sparsest and densest
networks enter the deterministic manual-reconstruction queue under the
collection-wide parser stress-test rule.
The source remains `primary_complete_second_pending` until an independent
reviewer completes those reconstructions and the source-level eligibility
review.

## Open references

- Figshare data: <https://figshare.com/articles/dataset/Contrasting_effects_of_land-use_changes_on_herbivory_and_pollination_networks/10000352>
- Open article and methods: <https://pmc.ncbi.nlm.nih.gov/articles/PMC6912900/>
- Later Dryad mirror: <https://datadryad.org/dataset/doi:10.5061/dryad.gqnk98sh7>

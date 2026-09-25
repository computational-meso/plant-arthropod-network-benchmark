# Volf et al. 2017 source audit

## Decision

Retain all nine site-by-guild matrices as `E1` networks in release layer `R2`.
They describe direct, bounded field ecologies, but they are nested within three
site campaigns and two sites overlap the field lineage later represented by
Seifert et al. The nine matrices therefore count as network objects, not as
nine independent replicates.

The ecological boundary is:

> one 0.1 ha forest plot × the 2013--2014 site-specific sampling window ×
> deciduous lowland temperate forest × one herbivore-guild protocol.

Leaf chewers, leaf miners, and gallers remain separate because the source used
different detection and identification procedures for each guild. Combining
them would require resolving source taxa across worksheets and would obscure
protocol-specific observation processes.

## Source and version

- Study: Volf M et al. (2017), *Phylogenetic composition of host plant
  communities drives plant--herbivore food web structure*.
- Article DOI: `10.1111/1365-2656.12646`.
- Data DOI: `10.5061/dryad.818ms`.
- Audited Dryad object: dataset 27309, version 27919, version 2, CC0.
- Retrieved version wrapper: 54,419 bytes; SHA-256
  `35bbb01bd52fedc781ee9bc9cbdc7256377b29d95f47e75f0edd90f33d5f6fc2`.
- Corrected workbook: `Insect_data_corrected_gallers.xlsx`, 51,636 bytes;
  SHA-256
  `662ca6bd11b70ffe4026d74d0cdc382c46be799aa8f35925b5facb8a9074a36d`;
  repository MD5 `f2aaeb273d519662e14d25818faf3818`.
- Correction note: `README_for_Insect_data_corrected_gallers.txt`, 1,116
  bytes; SHA-256
  `517fc5c9945e116cfe764276dcd9c8cc6ed47fba1e9f0d6055a19ff35c08221e`;
  repository MD5 `daa25961598ce245f603b071f9312683`.

Version 2 corrects Mikulčice galler abundances that had been overestimated
using incorrect leaf totals. The corrected version is mandatory for any
abundance analysis. Binary incidence is unchanged only where the correction
does not change a cell's positive/zero state; the parser does not assume this
and pins the corrected workbook itself.

## Boundary and evidence reconstruction

The workbook supplies three matrices at each of three sites:

| Site | Coordinates | Sampling window | Guild matrices |
| --- | --- | --- | --- |
| Tomakomai, Japan | 42°43′N, 141°36′E | mid-May--mid-June, 2013 and 2014 | chewers, miners, gallers |
| Lanžhot, Czech Republic | 48°48′N, 17°05′E | mid-May--August, 2013 and 2014 | chewers, miners, gallers |
| Mikulčice, Czech Republic | 48°41′N, 16°56′E | late May--mid-July, 2013 and 2014 | chewers, miners, gallers |

Each site used one 0.1 ha plot. Trees with diameter at breast height greater
than 5 cm were sampled, with approximately 80% of canopy foliage accessed by
crane, cherry picker, or sampling immediately after felling. Arthropods were
collected by beating, visual search, and hand collection.

- Leaf-chewing larvae were morphotyped, reared, and identified as adults;
  successful rearing confirmed larva--adult associations.
- Active and abandoned leaf mines were identified from diagnostic structures,
  reared material, literature, distributions, and host records.
- Galls were identified using morphology and host records, with rearing and
  dissections as supporting evidence. Very abundant galls were estimated from
  attacked-leaf proportions and inspected-leaf totals.

These methods satisfy the locked direct-evidence rule: the chewer links use
host collection plus rearing, while mines and galls are diagnostic feeding
structures. Counts and estimates remain in source-specific units; only binary
incidence is used in the cross-study projection.

## Worksheet controls

The parser reconciles every worksheet before yielding a network:

| Worksheet | Herbivore rows | Plant columns | Positive cells | Source-value sum |
| --- | ---: | ---: | ---: | ---: |
| `Tomakomai_chewers` | 181 | 19 | 533 | 8,707 |
| `Tomakomai_miners` | 29 | 19 | 30 | 2,190 |
| `Tomakomai_gallers` | 46 | 19 | 46 | 525,560.9638155401 |
| `Lanzhot_chewers` | 132 | 8 | 269 | 4,296 |
| `Lanzhot_miners` | 35 | 8 | 40 | 5,956 |
| `Lanzhot_gallers` | 52 | 8 | 61 | 288,731 |
| `Mikulcice_chewers` | 91 | 7 | 160 | 2,341 |
| `Mikulcice_miners` | 12 | 5 | 12 | 4,763 |
| `Mikulcice_gallers` | 34 | 7 | 34 | 398,264.77910040604 |

All labeled matrix cells are explicit numeric values. They are retained as
`sampled_zero` or `observed_positive`; no blank-to-zero inference is needed.
The unlabeled formula-total column in `Tomakomai_miners` is excluded because
it is not a plant taxon or interaction column.

## Dependency and duplicate audit

Tomakomai and Lanžhot also occur in the Seifert et al. source. The Volf
matrices are not exact copies: they cover one plot and 2013--2014, remain
guild-specific, and have different taxon and value scopes. Seifert pools two
plots over a broader multi-season campaign and contains only caterpillars.

For the chewer matrices, an audit of the common resolved taxa and mapped plant
columns found:

| Site | Common herbivore taxa | Mapped plants | Identical common cells | Differing common cells | Volf sum | Seifert sum |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Tomakomai | 73 | 17 | 1,015 | 226 | 8,707 | 15,511 |
| Lanžhot | 92 | 8 | 568 | 168 | 4,296 | 8,573 |

The sources are consequently retained as distinct observations but assigned
shared dependency identifiers:

- `temperate_field_lineage_tomakomai` for Volf and Seifert Tomakomai;
- `temperate_field_lineage_lanzhot` for Volf and Seifert Lanžhot;
- `temperate_field_lineage_mikulcice` for the new Volf-only site.

This preserves useful networks without treating repeated sampling of the same
field lineage as independent. Study-level analyses must additionally cluster
by original study.

## Transformations and validation

The immutable R0 workbook is transposed from herbivore rows × plant columns
to the canonical plant rows × herbivore columns. The three verbatim taxonomy
cells (`Family`, `Genus`, `Species`) are concatenated with separators and
remain reversible through worksheet row identifiers. Accepted taxonomy is not
overwritten or merged. Interaction provenance records the original worksheet,
row, and column for every cell.

The integrated build verifies wrapper and member checksums, exact archive
membership, sheet names, orientations, dimensions, positive-cell counts, and
source-value sums. Every binary matrix also passes the nonnegative symmetric
`B^T B` check and has a diagonal equal to herbivore host breadth. The complete
release builds deterministically in two independent temporary directories.

The source remains `primary_complete_second_pending`: independent source
review and the prespecified manual reconstructions are still required before
the benchmark is frozen for publication.

## Open references

- Dryad record: <https://datadryad.org/dataset/doi:10.5061/dryad.818ms>
- Free-access article and methods:
  <https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2656.12646>

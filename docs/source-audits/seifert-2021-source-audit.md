# Seifert et al. 2021 source audit

## Decision

Provisionally retain the three site matrices as direct ecology networks (`E0`)
in release layer `R2`. Each matrix is a bounded temperate-forest field ecology
with caterpillars collected from host foliage, reared, identified, and checked
with DNA barcodes.

This is a primary technical decision only. Independent second review and the
prespecified manual reconstructions remain pending before publication.

## Source identity, openness, and controls

- Study: Seifert CL et al. (2021), *Plant-caterpillar interaction matrices of
  temperate broadleaf forests*.
- Article DOI: `10.1002/ece3.7005`.
- Data DOI: `10.5061/dryad.dv41ns1w6`.
- Audited source: Dryad version 107327/version 3, file 596059; published
  2021-02-28.
- Data license: CC0 1.0 under the Dryad reuse policy.
- Open methods: Dryad repository documentation.
- Controlled raw-object SHA-256:
  `82041e16d520301b022b13b0561135726a226555d448398394702f34be13ab73`.
- Field system: natural temperate broadleaf forest plots at Lanžhot in the
  Czech Republic, Toms Brook in the United States, and Tomakomai in Japan.

The builder pins the downloaded Dryad version by checksum and reconciles all
three site matrices before canonicalization.

## Ecology boundary and evidence

Folivorous caterpillars were collected from host-tree foliage as unique field
records, reared, identified, and DNA-barcode verified. These procedures support
direct plant--caterpillar feeding links under the benchmark protocol.

Each site is retained as one `E0` network and one independence cluster. The
release preserves source-local taxa and does not merge morphospecies across
studies.

## Parser and release result

- 3 `E0` networks in `R2`;
- 3 independence clusters;
- 8--20 active plant taxa per network;
- 107--148 active herbivore taxa per network; and
- 351--718 positive links per network.

The source count reconciles exactly: three expected and three emitted.
Verbatim taxonomy, quantitative values, interaction provenance, and all matrix
transformations remain reversible. Binary incidence is used for cross-study
comparisons without erasing source units.

## Dependency and duplicate audit

Tomakomai and Lanžhot overlap field lineages represented by the guild-specific
Volf et al. matrices. They are not exact duplicate networks: the studies use
different taxon, temporal, spatial, and value scopes. The release therefore
retains both sources but assigns shared lineage identifiers:

- `temperate_field_lineage_tomakomai`; and
- `temperate_field_lineage_lanzhot`.

This prevents an analyst from treating repeated sampling of those places as
independent. Toms Brook remains a Seifert-only lineage.

## Human checks remaining

The second reviewer should verify the three site boundaries, plant and
caterpillar orientation, rearing and barcode evidence, CC0 reuse basis, the
Volf overlap treatment, and selected manual reconstructions. Until then the
source remains `primary_complete_second_pending`.

## Open references

- Dryad record: <https://datadryad.org/dataset/doi:10.5061/dryad.dv41ns1w6>
- Article DOI: <https://doi.org/10.1002/ece3.7005>

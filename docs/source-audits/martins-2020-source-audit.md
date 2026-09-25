# Martins et al. 2020 source audit

## Decision

Provisionally retain all 30 source matrices as direct, repeated ecology
networks (`E1`) in release layer `R2`. Each object is a bounded field network
of plants and endophagous arthropod herbivores, but repeated samples from the
same field lineage are not treated as independent studies.

This is a primary technical decision only. Independent second review and the
prespecified manual reconstructions remain pending before the release can be
frozen for publication.

## Source identity, openness, and controls

- Study: Martins LP, Medina AM, Lewinsohn TM, Almeida-Neto M (2020), *The
  effect of species composition dissimilarity on plant-herbivore network
  structure is not consistent over time*.
- Article DOI: `10.1111/btp.12791`.
- Data DOI: `10.5061/dryad.vmcvdncq0`.
- Audited source: Dryad version 56839/version 4, retrieved from the preserved
  Zenodo Dryad import, record 4941372; published 2020-03-11.
- Data license: CC0 1.0 under the Dryad reuse policy.
- Controlled raw-object SHA-256:
  `5f033221a5eef1b0b2723b750b66227b848eea461e835e4494b42618795fafb4`.
- Field system: remnants of Cerrado vegetation in São Paulo state,
  southeastern Brazil; natural or semi-natural field communities.

The builder pins the complete retrieved object by checksum, reads it without
modification, and reconciles all 30 source matrices before yielding canonical
records.

## Ecology boundary and evidence

The retained links join sampled Asteraceae hosts to adult endophagous
herbivores that were reared from collected flower heads. Host collection plus
rearing is feeding-confirmed evidence under the benchmark protocol; incidental
plant occurrence is not used.

The 30 matrices are kept at their source-defined spatial and temporal grains.
They resolve into 10 dependency clusters, so the release contains 30 network
objects but does not pretend to contain 30 independent studies or field
lineages.

## Parser and release result

- 30 `E1` networks in `R2`;
- 10 independence clusters;
- 2--17 active plant taxa per network;
- 3--37 active herbivore taxa per network; and
- 3--65 positive links per network.

Source-normalized tables preserve the source taxonomy and quantitative values.
The cross-study representation is binary incidence. Any absence, zero, blank,
or unsampled state is interpreted only from source structure and parser rules;
no blank is silently converted to a biological zero.

The release-level source count reconciles exactly: 30 expected and 30 emitted.
Every transformation is recorded in the derivations table, and every retained
interaction remains traceable to the controlled raw object.

## Human checks remaining

The second reviewer should verify the study boundary, the field status, the
plant and herbivore orientation, the rearing evidence, the grouping of the 30
objects into 10 dependency clusters, the CC0 reuse basis, and the selected
manual matrix reconstructions. Until then the source remains
`primary_complete_second_pending`.

## Open references

- Dryad record: <https://datadryad.org/dataset/doi:10.5061/dryad.vmcvdncq0>
- Preserved retrieval record: <https://zenodo.org/records/4941372>
- Article DOI: <https://doi.org/10.1111/btp.12791>

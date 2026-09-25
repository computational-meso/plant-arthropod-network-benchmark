# Saavedra et al. 2018 source audit

## Decision

Provisionally retain all 36 source matrices as direct, repeated ecology
networks (`E1`) in release layer `R2`. They are field-bounded plant--caterpillar
networks with feeding confirmed by rearing. Repeated matrices remain separate
network objects while their shared site lineages are made explicit.

This is a primary technical decision only. Independent second review and the
prespecified manual reconstructions remain pending before publication.

## Source identity, openness, and controls

- Study: Saavedra S, Cenci S, del-Val E, Boege K, Rohr RP (2018),
  *Reorganization of interaction networks modulates the persistence of species
  in late successional stages*.
- Article DOI: `10.1111/1365-2656.12710`.
- Data DOI: `10.5061/dryad.5h187`.
- Audited source: Dryad version published 2017-09-19, retrieved from the
  preserved Zenodo Dryad import, record 4941296.
- Data license: CC0 1.0 under the Dryad reuse policy.
- Open methods: author manuscript plus open repository documentation.
- Controlled raw-object SHA-256:
  `e27e03cdfdc4298f7aef68b102b62eea554eaaddbc5199e796011a413d72cf79`.
- Field system: natural successional plots in tropical dry forest at the
  Chamela-Cuixmala Biosphere Reserve, Jalisco, Mexico.

The builder pins the retrieved object by checksum and reconciles all 36 source
matrices before emitting canonical records.

## Ecology boundary and evidence

Lepidopteran larvae were collected from plants in the field and reared to
confirm trophic interactions. This satisfies the benchmark's direct feeding
criterion and is stronger than an association inferred from incidental
capture.

The matrices retain the source-defined plot and sampling-window boundaries.
They resolve to nine dependency clusters. The release therefore represents 36
network objects, one original study, and nine dependent field lineages for
inference rather than 36 fully independent replicates.

## Parser and release result

- 36 `E1` networks in `R2`;
- 9 independence clusters;
- 6--24 active plant taxa per network;
- 14--58 active herbivore taxa per network; and
- 15--78 positive links per network.

Verbatim taxa and source values remain recoverable. Binary incidence is used
for cross-study comparisons, while quantitative values remain in their source
units. Interaction states are parsed explicitly; blanks are not automatically
treated as sampled zeros.

The source count reconciles exactly: 36 expected and 36 emitted. Derivation
records connect every canonical matrix and interaction to the immutable source
object.

## Human checks remaining

The second reviewer should verify the original study identity, plot and
sampling-window boundaries, plant and caterpillar orientation, rearing
evidence, nine-cluster dependency grouping, open-methods record, CC0 reuse
basis, and selected manual reconstructions. Until then the source remains
`primary_complete_second_pending`.

## Open references

- Dryad record: <https://datadryad.org/dataset/doi:10.5061/dryad.5h187>
- Preserved retrieval record: <https://zenodo.org/records/4941296>
- Open author manuscript:
  <https://www.unifr.ch/bio/en/assets/public/Research/Rudolf-Rohr/2017_JAE_Saavedra_et_al.pdf>
- Article DOI: <https://doi.org/10.1111/1365-2656.12710>

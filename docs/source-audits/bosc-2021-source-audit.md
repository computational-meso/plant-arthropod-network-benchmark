# Bosc and Pauw 2020/2021 source audit

## Decision

Retain all 124 field-bounded matrices as locally derived networks (`E2`) in
release layer `R3`, but do not count them in the direct `E0`/`E1` benchmark.
The open materials describe herbivorous insects collected on plant species,
yet do not establish for every link that feeding, rearing, or a diagnostic
feeding structure was observed. Classifying the matrices as direct would
therefore exceed the available evidence.

This one audit supports both the included-study decision and exclusion record
`C003`: no matrix is discarded, but the source is excluded from the direct
headline count. Independent second review remains pending.

## Source identity, openness, and controls

- Study: Bosc C, Pauw A (2020/2021), *Increasing importance of niche versus
  neutral processes in the assembly of plant-herbivore networks during
  succession*.
- Article DOI: `10.1007/s00442-020-04740-7`.
- Data DOI: `10.5061/dryad.4xgxd256v`.
- Audited source: Dryad version 5, retrieved from the preserved Zenodo Dryad
  import, record 3998368; published 2021-04-12.
- Data license: CC0 1.0 under the Dryad reuse policy.
- Open methods: repository documentation; article methods were not openly
  recoverable in this build.
- Controlled raw-object SHA-256:
  `aae3045101d94c4effa7205cfaaf8a67bcf6a00fe9a99b7ad7bd041176b11a87`.
- Field system: natural post-fire fynbos succession in the Jonkershoek valley,
  Western Cape, South Africa.

The builder pins the retrieved object by checksum and reconciles all 124 source
matrices before canonicalization.

## Ecology boundary and evidence

The source provides bounded quadrat--site--valley field matrices across a
post-fire successional system. These boundaries are useful and are preserved,
including their nested dependency structure.

The limiting issue is link evidence, not spatial bounding. The open description
supports plant-associated herbivorous insects, but it does not let the build
distinguish observed feeding from collection on a plant for every interaction.
The conservative `E2` classification keeps the data available without turning
association into feeding confirmation.

## Parser and release result

- 124 `E2` networks in `R3`;
- 7 independence clusters;
- 6--66 active plant taxa per network;
- 5--217 active herbivore taxa per network; and
- 10--1,104 positive links per network.

The source count reconciles exactly: 124 expected and 124 emitted. Verbatim
taxa, values, boundaries, parent identifiers, and derivations remain
traceable. The networks can be used in an explicitly labeled sensitivity or
derived-evidence analysis, but must not be pooled into the direct benchmark
without new source evidence and a recorded reclassification.

## Human checks remaining

The second reviewer should verify the quadrat--site--valley nesting, natural
field status, plant and insect orientation, open methods, CC0 reuse basis, and
whether any accessible source evidence can upgrade specific links or matrices
to direct feeding. In the absence of such evidence, confirm `E2/R3` retention
and exclusion from the direct headline count.

## Open references

- Dryad record: <https://datadryad.org/dataset/doi:10.5061/dryad.4xgxd256v>
- Preserved retrieval record: <https://zenodo.org/records/3998368>
- Article DOI: <https://doi.org/10.1007/s00442-020-04740-7>

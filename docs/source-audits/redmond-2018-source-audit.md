# Redmond et al. 2018 source audit

## Decision

Provisionally retain all nine site-level matrices as direct ecology networks
(`E0`) in release layer `R2`. Each matrix represents a natural tropical
montane forest ecology bounded by field site and sampling campaign, and the
reported links were tested as feeding interactions.

This is a primary technical decision only. Independent second review and the
prespecified manual reconstructions remain pending before publication.

## Source identity, openness, and controls

- Study: Redmond CM et al. (2018), *High specialization and limited structural
  change in plant-herbivore networks along a successional chronosequence in
  tropical montane forest*.
- Article DOI: `10.1111/ecog.03849`.
- Data DOI: `10.5061/dryad.bh2rc50`.
- Audited source: Dryad version published 2018-08-30, retrieved from the
  preserved Zenodo Dryad import, record 4974534.
- Data license: CC0 1.0 under the Dryad reuse policy.
- Open methods: accepted manuscript plus open repository documentation.
- Controlled raw-object SHA-256:
  `4b3f4507089216d4b75233ea7134a71a05d0d8f6f6f6fdb052e48d55f838550c`.
- Field system: primary and secondary tropical montane forest in Yawan,
  Morobe Province, Papua New Guinea; a natural forest chronosequence.

The builder pins the retrieved object by checksum and reconciles all nine
source matrices before canonicalization.

## Ecology boundary and evidence

Live caterpillars were collected on felled trees, and trophic links were
confirmed with 24-hour no-choice feeding trials. The retained links therefore
meet the direct feeding criterion rather than relying on plant association
alone.

Each site matrix remains a separate `E0` object with its own field boundary and
independence cluster. The nine networks belong to one original study, so
study-level analyses must still account for that common provenance.

## Parser and release result

- 9 `E0` networks in `R2`;
- 9 independence clusters;
- 18--39 active plant taxa per network;
- 55--117 active herbivore taxa per network; and
- 70--175 positive links per network.

Verbatim taxa and original quantitative values remain recoverable, while
binary incidence supplies the cross-study representation. Interaction states
are kept explicit, and blanks are never automatically converted to biological
zeros.

The release count reconciles exactly: nine expected and nine emitted. Every
canonical network and interaction is connected to the immutable source through
the derivations and file manifest.

## Human checks remaining

The second reviewer should verify the chronosequence boundary, natural field
status, plant and caterpillar orientation, no-choice feeding confirmation,
site-level independence grouping, open-methods record, CC0 reuse basis, and
selected manual reconstructions. Until then the source remains
`primary_complete_second_pending`.

## Open references

- Dryad record: <https://datadryad.org/dataset/doi:10.5061/dryad.bh2rc50>
- Preserved retrieval record: <https://zenodo.org/records/4974534>
- Open accepted manuscript: <https://centaur.reading.ac.uk/96876/1/ecog.03849.pdf>
- Article DOI: <https://doi.org/10.1111/ecog.03849>

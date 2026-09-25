# Pocock et al. 2012 source audit

## Decision

Retain two source-defined direct plant--arthropod networks as `E0` objects in
release layer `R2`:

1. the whole-farm plant--aphid network sampled during May--August 2008; and
2. the whole-farm plant--insect-seed-feeder network collected during
   August--December 2007 and reared through 30 April 2008.

Both belong to one original study, one independent field site, and one
independence cluster. They remain separate network objects because their
sampling windows and protocols differ. This implements the locked boundary
rule rather than pooling unlike evidence into one nominal herbivory matrix.

The decision does not classify an analyst-invented slice of a generic food web
as direct. The primary article and supporting Table S1 explicitly define the
plant--aphid and seed--insect-seed-feeder systems as two of the study's seven
individual networks, label their interactions trophic, and state that their
interactions came from field sampling. The shared Dryad edge list is only the
distribution format for those source-defined networks.

## Source identity, openness, and controls

- Study: Pocock MJO, Evans DM, Memmott J (2012), *The robustness and
  restoration of a network of ecological networks*.
- Article DOI: `10.1126/science.1214915`.
- Data DOI: `10.5061/dryad.3s36r118`.
- Dryad record: dataset 9224, version 9265, version 1, published 2012-02-24.
- Data license: CC0 1.0.
- Open methods: accepted manuscript and 34-page Supporting Online Material in
  the NERC Open Research Archive, record 17964.
- Field site: 125 ha Norwood Farm, Somerset, United Kingdom, 51.3128 N,
  2.3206 W; a low-intensity organic mixed-use farm with 10 source-defined
  cropped and non-cropped habitat classes.

| Raw object | Bytes | SHA-256 | Repository MD5 |
| --- | ---: | --- | --- |
| `norwood.csv` | 129,466 | `49be776718febf8e73bd5f456244e215978d1e0860dbc0c0f3d484d3cc81f709` | `2725a7eccf43430a1054186b6a7611d6` |
| `README_for_norwood.txt` | 3,099 | `f51812fd51bfc9ed8942fe6056914c04ef93be1e7202991f218d2ead4f6b64c2` | `8b42da3d7174873470f7876c8f556ff8` |

The builder checks the repository MD5 for both objects, pins their SHA-256
hashes, and checks that the raw edge list contains 1,734 rows, of which 1,501
are marked as direct interactions by the source.

## Direct network reconstruction

### Plant--aphid network

The authors sampled aphids and their parasitoids during May--August 2008 in 94
randomly located 9 x 1 m transects across all 10 habitats, using three or four
transects per habitat per month. Whenever an aphid colony was encountered, its
abundance was estimated and specimens were retained for identification. The
plant--aphid rows therefore identify the plant on which each feeding colony was
observed. Habitat-scaled values were summed across habitats and months to the
whole-farm network.

The raw-data controls are:

- 30 plant taxa;
- 28 aphid taxa;
- 39 positive plant--aphid links; and
- source interaction-strength sum `372217783.8`.

### Plant--insect-seed-feeder network

The authors collected up to 50 berries or seed heads per plant species per
transect from selected Carduoideae, Fabaceae, and hedgerow berry hosts during
August--December 2007. Samples were held separately in pots and checked weekly
for insect emergence through 30 April 2008. Emergent taxa were classified as
primary seed feeders or other functional roles using literature. Emergence
from the collected host supplies the required rearing evidence for the retained
plant--seed-feeder links; inferred host assignments used for the parasitoid
layer are not retained.

The raw-data controls are:

- 6 plant taxa;
- 19 insect seed-feeder taxa;
- 20 positive plant--insect links; and
- source interaction-strength sum `1651698.9`.

## Excluded source layers

The broader source includes several layers that do not meet this benchmark's
direct terrestrial arthropod-herbivory criterion. They remain unchanged in R0:

- flower visitors are not treated as herbivory;
- butterfly--plant interactions used prior knowledge and a foraging model;
- vertebrate seed-feeder networks used literature diets and are not arthropods;
- plant--leaf-miner-parasitoid links bypassed unidentified miners and are
  inferred indirect paths;
- aphid and seed-feeder parasitoid layers are higher trophic interactions; and
- rodent ectoparasite links are outside the plant--arthropod feeding layer.

This exclusion is recorded in each retained network's derivation rather than
silently dropping the provenance of the multipartite source.

## Interaction-state semantics and dependencies

The Dryad object is an edge list, not a complete sampling-opportunity matrix.
Every retained positive value maps to the exact raw row and to source column 5.
Unlisted combinations in the plant-by-herbivore cross-product remain
`unknown`; they are never converted to sampled or structural zeros. Binary
incidence uses only the 59 source-listed positive links across the two
networks, while original quantitative estimates remain in the canonical table.

Both networks use:

- `independent_site_id=pocock_norwood_farm`;
- `independence_cluster_id=pocock_norwood_farm`; and
- blank parent-network identifiers because neither direct network is a nested
  or repeated version of the other.

They count as two direct ecology networks but only one original study and one
independent field lineage. Both require independent second review and manual
reconstruction before a journal-ready freeze.

## Open references

- Dryad data: <https://datadryad.org/dataset/doi:10.5061/dryad.3s36r118>
- Open accepted manuscript and supplement: <https://nora.nerc.ac.uk/id/eprint/17964/>
- Article DOI: <https://doi.org/10.1126/science.1214915>

# Woodcock et al. 2026 source audit

## Decision

Register as candidate `C018`, provisionally `E2`, for the derived expansion. Do not count it in the direct E0/E1 headline.

The study supplies valuable, field-bounded woodland networks and openly archived data, but the interaction evidence does not meet the benchmark's direct-feeding rule. The article says that phytophagous insects collected from a sampled tree were assumed to be feeding on that tree. Capture on a plant is not, by itself, feeding confirmation under the frozen protocol.

## Source identity and openness

- Article: Woodcock et al., “Restoration of ecological interactions: the influence of site and landscape factors,” *Agriculture, Ecosystems & Environment* (2026), DOI `10.1016/j.agee.2025.110060`.
- Open article record: <https://nora.nerc.ac.uk/id/eprint/540579/>.
- Data and code: Zenodo concept DOI `10.5281/zenodo.17477385`; audited version DOI `10.5281/zenodo.17477386`.
- License: CC BY 4.0.
- Audited archive: `RestREco_NetworkPaper-V1.1.zip`.
- Archive SHA-256: `3e55dba5f70138fb2d8c7c0ed9a5f2fce6c795d386eb22eb31145eba485c1280`.
- Repository MD5: `8621929a33f69b6f6b82bf373f010c05` (matched).

## Recoverable structure

The article describes UK woodland sampling between June and September, two visits per site, and beating-tray collection from ten trees per site. The positive-edge table `Wood_web_21.csv` contains:

- 60 site identifiers;
- 439 positive site–plant–insect records;
- 1,199 total recorded individuals;
- 23 plant taxa and 40 insect taxa;
- 2–20 positive links per represented site.

The woodland metadata table contains 66 site codes. A later R3 parser must preserve all 66 sampled sites and explicitly represent the six sites missing from the positive-edge table as zero-link, unsampled, or otherwise documented states after checking the source semantics. It must not silently reduce the sampling frame to 60 sites.

## Eligibility assessment

| Rule | Result | Basis |
| --- | --- | --- |
| Natural or semi-natural field community | pass | Restoration and reference woodland sites in the UK |
| Place and protocol recoverable | pass | Site codes, repeated summer visits, and beating protocol reported |
| Plant and arthropod roles recoverable | pass | Tree and phytophagous-insect fields supplied |
| Feeding confirmed | fail for E0/E1 | Feeding was assumed from collection on the sampled tree |
| Raw data and methods open | pass | NORA article plus versioned Zenodo archive |
| Network boundary recoverable | pass with reconciliation note | 60 positive-edge sites; 66 metadata sites |

## Required next action

Ingest as R3 only after resolving the six metadata-only sites and encoding `evidence_method=plant_capture_assumed_feeding`. Promotion to E0/E1 would require observation-level feeding, damage, rearing, gall, or mine evidence not currently present in the open materials.

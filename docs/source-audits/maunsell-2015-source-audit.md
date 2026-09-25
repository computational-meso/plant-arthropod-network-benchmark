# Maunsell et al. source audit

## Decision

Exclude Maunsell et al. from the direct `E0`/`E1` headline and retain it as
candidate `C015` for a prospective `E2` derivation in `R3`. The source is a
valuable, well-bounded field study, but the released local interaction layer is
leaf miner--parasitoid rather than plant--leaf miner. The workbook supplies
plant cover at the same 12 sites, and a companion study supplies a regional
plant--miner host table, but it does not supply the observed plant--miner pairs
at each site.

Consequently, intersecting the regional host table with local plant and miner
occurrence would construct locally filtered possible links. Those links are
inferred, not direct site-level feeding records, so the result would be `E2`,
not `E3`: it is a metaweb-filtering derivation rather than extraction of an
already observed plant--herbivore layer from each local food web.

The companion translocation experiment is outside the locked natural or
semi-natural field-community scope and must not be used to fill the direct
benchmark.

## Source identity and openness

- Primary host--parasitoid study: Maunsell SC et al., *Changes in host--
  parasitoid food web structure with elevation*.
- Primary article DOI: `10.1111/1365-2656.12285`.
- Elevational plant--miner study DOI: `10.1111/aec.12339`.
- Companion regional host-plant study DOI: `10.1111/aen.12252`.
- Data DOI: `10.5061/dryad.352q6`.
- Dryad record: dataset 12150, version 12194, version 1.
- Dryad data license: CC0 1.0.
- Companion accepted manuscript and supplement: Oxford Research Archive UUID
  `335cad3e-763d-47b0-a2e3-0f8ecf7e6391`.
- ORA files: retain retrieval records and hashes; do not redistribute them in
  the benchmark until their source terms are reviewed for that use.

The openly accessible primary article documents 12 rainforest sites across an
elevational gradient, four sampling occasions over a year, and 5,030 collected
leaf-mining insects, including 603 reared parasitoids. The companion regional
host-plant study reports host identities for the leaf-miner assemblage, but its
published host table is not resolved to the same local sampling events.

## Raw acquisition and integrity controls

Five immutable source objects are registered. The Dryad workbook's repository
MD5 agrees with the downloaded file; every object is also pinned locally by
SHA-256.

| Object | Bytes | SHA-256 | Release treatment |
| --- | ---: | --- | --- |
| `dryad_dataset_metadata.json` | 5,305 | `8092b453d0857c3c5b4fc4ec2c85d3b986b65bec356ae477b926cb4d6a97c368` | may redistribute with citation |
| `dryad_files.json` | 1,082 | `4aea1fbb94c7ed6900e5794e8a83e9109d6f0adeadb4c18c17074f9e64673c10` | may redistribute with citation |
| `SMaunsell_Foodweb_and_plant_data_Dryad.xlsx` | 72,330 | `74cd364efdd55f86ee94aaf446502f3b7a8f2ef94cd01db3742d9da76d553427` | CC0; Dryad MD5 `5f18306931b4002be9d62f0d6ad6f352` |
| `AEN-4721_Maunsell_SI.docx` | 399,189 | `b4504a0e651f2087cd7f0316cc2b3edeec2e4579996c710077efba21f32f21b4` | retrieval manifest only pending terms review |
| `Maunsell_2016_host_plants_accepted_manuscript.pdf` | 616,093 | `8231e9ee92a182410cb703e607c51cd6fa123f2c3b72b70ce1fd76c0dd3fe3e3` | retrieval manifest only pending terms review |

The deterministic validator requires exactly two workbook sheets,
`Foodwebs` and `Plant data`; verifies the leaf-miner row by parasitoid column
orientation; rejects duplicate or negative source entries; and reconciles all
site, plant, and grand-total controls below.

## Released site matrices

The 12 local matrices are direct leaf miner--parasitoid networks. They are not
the target plant--herbivore matrices, so none is emitted as an ecology network
in the present benchmark.

| Source site label | Leaf miners | Parasitoids | Positive miner--parasitoid links | Unparasitized miners | Parasitoids | Total insects |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 493 m, Bar Mountain | 12 | 6 | 8 | 84 | 19 | 103 |
| 510 m, Green Mountains | 15 | 11 | 21 | 156 | 82 | 238 |
| 557 m, Sheep Station Creek | 12 | 7 | 9 | 97 | 26 | 123 |
| 706 m, Bar Mountain | 15 | 7 | 10 | 331 | 57 | 388 |
| 757 m, Green Mountains | 15 | 13 | 18 | 166 | 100 | 266 |
| 744 m, Sheep Station Creek | 17 | 10 | 17 | 447 | 63 | 510 |
| 724 m in `Foodwebs`, Bar Mountain | 10 | 4 | 4 | 186 | 47 | 233 |
| 928 m, Green Mountains | 13 | 8 | 14 | 699 | 56 | 755 |
| 947 m, Sheep Station Creek | 11 | 2 | 2 | 506 | 25 | 531 |
| 1128 m, Bar Mountain | 11 | 4 | 4 | 415 | 13 | 428 |
| 1159 m, Green Mountains | 13 | 7 | 7 | 497 | 60 | 557 |
| 1059 m, Sheep Station Creek | 15 | 5 | 5 | 843 | 55 | 898 |
| **Total** |  |  |  | **4,427** | **603** | **5,030** |

The `Plant data` sheet has 86 unique plant rows. The numbers of plants with
positive cover at the 12 corresponding sites are 26, 31, 29, 30, 26, 29, 22,
34, 27, 17, 17, and 24. These cover data establish local plant occurrence but
not which miner used which plant at that site.

## Eligibility audit

| Criterion | Result | Consequence |
| --- | --- | --- |
| Natural or semi-natural field system | pass for the elevational survey | the distinct translocation experiment remains excluded |
| Recoverable local place | pass: 12 sites at three locations | supports candidate site boundaries |
| Recoverable sampling interval | field year recoverable, but month labels conflict among open sources | preserve both verbatim accounts and flag for review |
| Recoverable habitat and protocol | pass for the field survey | sufficient to understand the released miner--parasitoid layer |
| Feeding-confirmed herbivores | pass at regional host-map level | leaf mines diagnose feeding, but local host edges are absent |
| Local plant--herbivore edge table | fail | no direct `E0`/`E1` admission |
| Open raw data | pass for the Dryad workbook | retain in `R0` and `file_manifest` |
| Open methods | pass across the primary article and companion archive for source audit | does not create missing local edge observations |
| Original lineage identifiable | pass | companion studies are linked, not counted as independent network studies |

## Ambiguities that must remain visible

- The `Foodwebs` sheet labels the upper Bar Mountain site as 724 m. The
  `Plant data` sheet and companion site table label it as 924 m. Preserve 724 m
  in `R1`; use 924 m only through an explicit, reversible correction in a
  derived table.
- The primary manuscript describes sampling in August and October 2011 and
  February and May 2012. The companion supplement instead lists August and
  November 2011 and February and June 2012, with extra December and April
  sampling at Sheep Station Creek. Store both accounts and leave the canonical
  sampling window under review.
- The companion abstract reports 50 leaf-miner species, whereas its manuscript
  results report 55 morphospecies plus 162 individuals that could not be
  assigned. Do not silently choose one count.
- Workbook labels such as `M?` are unresolved records, not stable operational
  taxa. Preserve them in source-normalized data, but omit them from a derived
  competition graph unless a documented crosswalk resolves them.
- Regional miner names and workbook miner codes require a reversible crosswalk.
  Neither fuzzy matching nor taxonomic similarity is sufficient evidence for
  an edge.

## Prospective `R3` derivation

If this candidate is later implemented, create one site-filtered `E2` network
per field site using a registered derivation:

1. encode the companion regional plant--miner host table without modifying
   verbatim names;
2. create a reviewed, one-to-one or explicitly ambiguous crosswalk from the
   regional miner names to workbook miner codes;
3. filter the regional links by positive plant cover and observed miner
   occurrence at each site;
4. retain only crosswalk-resolved links, with unresolved records reported as
   exclusions rather than zeros;
5. mark every resulting edge `locally_inferred_from_regional_host_map` and the
   network `E2`/`R3`;
6. keep site repeats nested within the original study and never count these
   objects toward the direct 15-study/300-network target.

No derivation should proceed until the crosswalk and date discrepancy receive
second review. Even then, the result is useful for method sensitivity and
metaweb-filtering analyses, not as direct evidence for the headline corpus.

## Open references

- Dryad data: <https://datadryad.org/dataset/doi:10.5061/dryad.352q6>
- Open primary article: <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/1365-2656.12285>
- Oxford Research Archive companion record: <https://ora.ox.ac.uk/objects/uuid:335cad3e-763d-47b0-a2e3-0f8ecf7e6391>
- Elevational plant--miner article record: <https://eprints.soton.ac.uk/407752/>

# Zhang et al. 2025 source audit

## Decision

Retain Zhang et al. as high-priority candidate `C014`, but do not ingest or
count its networks in the direct benchmark yet. The source defines eight local
quantitative plant--moth matrices that are prospective `E0` site networks. The
raw package is unusually clean, fully open, and internally consistent, but the
openly accessible records do not recover four fields required by the locked
eligibility protocol:

- a sampling date or bounded sampling window;
- habitat information for each site;
- the complete larval collection and rearing protocol; and
- a study-specific observation-level account of why every retained larva--host
  record is a feeding interaction rather than plant association alone.

The publisher page exposed the abstract but required purchase for the full
article when checked on 2026-09-11. The electronic supplement is open but
contains figures and tables rather than the missing field methods. General
evidence that *Epicephala* larvae consume *Glochidion* seeds establishes strong
trophic plausibility, but it cannot replace the candidate study's sampling
methods under a uniform benchmark rule.

If the missing methods are recovered in an open author manuscript, the cited
2017 master's thesis, or an author-supplied methods record, ingest only the
eight site matrices. Keep the three source-provided geographic sums in a
derived or metaweb layer; they are not field-bounded local ecologies.

## Source identity and openness

- Study: Zhang L-J, Hembry DH, Hao K, Wu Y-H, Yao G, Sun Q-L, Liu T-T,
  Luo S-X (2025), *Network structure variation across scales offers clues to
  the macroevolutionary persistence of specialised mutualisms*.
- Article DOI: `10.1098/rspb.2025.0926`.
- PubMed record: `41187913`.
- Data DOI: `10.5061/dryad.3bk3j9kx6`.
- Dryad record: dataset 155648, version 395242, version 4, published
  2025-09-11.
- Data license: CC0 1.0.
- Electronic supplement DOI: `10.6084/m9.figshare.30209193.v1`, file 58258530.
- Earlier methods lead: Zhang L-J (2017), *Variation in network structure of a
  specialized pollination mutualism between leafflower (Phyllanthaceae,
  Glochidion) and leafflower moths (Gracillariidae, Epicephala) across
  different communities*, MSc thesis, University of the Chinese Academy of
  Sciences, South China Botanical Garden. No stable open copy was recovered in
  the completed search.

The Dryad description states that larvae were collected from different host
species at eight sites, preserved or reared, and assigned to minimally
monophyletic moth clades using three genetic loci. Each phylogenetic tip was
then treated as one plant--moth interaction event. The repository README says
matrix rows are *Glochidion* species, columns are operational *Epicephala*
clades, and values are numbers of larval interaction events.

## Raw acquisition and integrity controls

The immutable acquisition is
`data/empirical/raw/zhang_2025_china/zhang_2025_dryad_v4.zip`:

| Control | Value |
| --- | --- |
| Archive bytes | 632,036 |
| Uncompressed member bytes | 629,148 |
| Archive SHA-256 | `50c3090e17340b1f14440d5e0ba9e9b99f381a8710d77c48f174d18bb2b9d979` |
| Dryad members | 21 |
| Member size checks | 21/21 pass |
| Repository SHA-256 checks | 21/21 pass |

The local Dryad dataset response and both paginated file-list responses are
preserved beside the archive. The release `file_manifest` registers the
archive and all 21 individual members. Each member is reconstructed from the
archive and checked against both the size and SHA-256 returned by the Dryad
file API during every build. Dryad does not provide a digest for the ZIP
container, so its SHA-256 is a local acquisition pin while the member digests
are repository controls.

## Prospective local ecology boundaries

The eight matrices use site as the recoverable spatial boundary. Coordinates
come from the source workbook `latlong.xlsx`; taxon and interaction totals come
from the corresponding quantitative CSV. Sampling windows and site habitat
labels remain unresolved and therefore prevent ingestion.

| Site matrix | Latitude | Longitude | Plants | Moth clades | Positive links | Larval events | Projection gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Bawang | 19.084930 | 109.126220 | 5 | 6 | 6 | 47 | pass |
| Daming | 23.514826 | 108.395742 | 4 | 4 | 4 | 32 | fail: no shared host pair |
| Diaoluo | 18.692318 | 109.884617 | 4 | 5 | 6 | 21 | pass |
| Dinghu | 23.170917 | 112.545392 | 3 | 3 | 3 | 8 | fail: no shared host pair |
| Jianfeng | 18.705237 | 108.829064 | 5 | 7 | 8 | 58 | pass |
| Nonghua | 23.335956 | 106.346012 | 4 | 5 | 5 | 19 | pass |
| Xinglong | 18.729946 | 110.193689 | 4 | 7 | 7 | 24 | pass |
| Yingge | 19.030673 | 109.573853 | 4 | 7 | 8 | 30 | pass |
| **Local total** |  |  |  |  | **47** | **239** | **6/8 pass** |

No local matrix reaches the prespecified comparative graph threshold of five
active plants, ten active herbivores, and twenty positive links. Six would
support the minimal shared-host projection if later admitted. Their value is
therefore chiefly as small bounded networks and as a transparent example of
why release eligibility and downstream analysis gates must remain separate.

## Aggregate reconciliation and classification

The three additional CSVs are exact geographic combinations, not additional
local samples:

| Aggregate | Plants | Moth clades | Positive links | Larval events | Release treatment |
| --- | ---: | ---: | ---: | ---: | --- |
| Hainan | 10 | 15 | 21 | 180 | derived geographic sum |
| continent | 7 | 8 | 8 | 59 | derived geographic sum |
| China | 12 | 19 | 25 | 239 | all-site aggregate |

The China event total equals the sum across the eight local matrices
(`239`), while repeated plant--moth pairs collapse from 47 local positive links
to 25 aggregate links. Counting these three objects as ecologies would mix
spatial scales and double-count the same larval observations. They may later
enter `R3` or `R4` with explicit derivations, but never the direct-local
headline.

## Eligibility audit

| Criterion | Current result | Consequence |
| --- | --- | --- |
| Natural or semi-natural field community | probable, not openly documented per site | hold |
| Recoverable site | pass: eight named sites with coordinates | prospective local boundary |
| Recoverable sampling interval | fail: no dates/window in open records | no `E0` admission |
| Recoverable habitat | fail in open records | no `E0` admission |
| Recoverable protocol | partial: larval collection and some rearing stated, operational details absent | no reproducible event boundary |
| Feeding-confirmed plant link | biologically plausible seed herbivory, but study-specific observation rule not fully open | hold rather than infer |
| Raw data openly downloadable | pass | CC0 archive retained in `R0` |
| Raw data internally reconcilable | pass | 21/21 object checks; local and aggregate totals reconcile |
| Methods openly reconstructable | fail at present | explicit exclusion/defer record |
| Original study and compilation lineage | pass | original article-linked Dryad record |

## Resolution request

The minimum sufficient resolution is a citable open record giving:

1. sampling dates or a defensible sampling window for each of the eight sites;
2. site habitat or source-described ecosystem labels;
3. how fruits, flowers, or other plant material were searched or collected,
   how larvae were linked to individual host species, and what was reared; and
4. confirmation that the larvae represented seed or tissue feeding in the
   sampled *Glochidion* hosts.

Once those fields are available, the parser should preserve the quantitative
larval counts, use binary incidence for cross-study projection, retain the
operational clade labels without cross-study taxonomic merging, create one
independence cluster per site unless the methods establish nesting, and record
all three aggregate transformations separately.

## Open references

- Dryad data: <https://datadryad.org/dataset/doi:10.5061/dryad.3bk3j9kx6>
- Article record: <https://pubmed.ncbi.nlm.nih.gov/41187913/>
- Open electronic supplement:
  <https://rs.figshare.com/articles/journal_contribution/Zhang_et_al_Electronic_Supplementary_Material_from_Network_structure_variation_across_scales_offers_clues_to_the_macroevolutionary_persistence_of_specialised_mutualisms/30209193>
- Open background on the *Glochidion*--*Epicephala* life cycle:
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC6103454/>

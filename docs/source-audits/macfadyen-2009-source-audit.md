# Macfadyen et al. 2009 source audit

## Decision

Register as candidate `C021`, provisionally `E2`, for the derived expansion. Do
not count it in the direct E0/E1 headline.

The source is unusually valuable for scale: it contains 20 standardized
whole-farm plant-herbivore-parasitoid webs from 10 matched
organic-conventional farm pairs. However, the open methods explicitly say that
the plant on which an herbivore was found was treated as its *most likely*
host. Sweep-net and beating samples spanning more than one plant were resolved
with literature records, and a generalist was sometimes assigned randomly to
one plausible plant. The released interaction table does not identify which
rows were diagnostic mines, direct feeding observations, literature
resolutions, or random assignments. Those evidence modes therefore cannot be
separated reproducibly.

## Source identity and openness

- Primary article: Macfadyen et al., “Do differences in food web structure
  between organic and conventional farms affect the ecosystem service of pest
  control?”, *Ecology Letters* (2009), DOI
  `10.1111/j.1461-0248.2008.01279.x`.
- Data: Dryad DOI `10.5061/dryad.5fr85`, version 1, published 2013-05-15.
- Data license: CC0 1.0.
- Open methods for the same 20 networks: Macfadyen et al., “Landscape structure
  influences modularity patterns in farm food webs,” *Ecological Applications*
  (2011), DOI `10.1890/09-2111.1`, PMCID `PMC7163691`.
- Audited Dryad version-wrapper SHA-256:
  `145cf13f9e35943872b07da85f039ee94bca21ed43b3251eb2d1bfc4128b89dd`.
- Plant-herbivore CSV SHA-256:
  `eca05f66f026ffd114fcba6b5943f3010cf8eb2fa8dd90335af953bfa34390c1`.
- Repository MD5 for the plant-herbivore CSV:
  `6620da623b9b9670bc68fe089e07bd4a` (matched).

## Recoverable structure

The data and open methods support 20 field-bounded farm networks sampled during
spring and summer of 2005 and 2006 in southwest England:

- farms `A1`-`A10` are organic and farms `B1`-`B10` are their nearby,
  non-adjoining conventional matches;
- sampling effort was matched within each pair;
- the plant-herbivore file contains 1,622 positive farm-plant-herbivore rows
  and an interaction-frequency sum of 38,059;
- 140 source-verbatim plant labels and 366 source-verbatim herbivore labels
  occur across the collection;
- individual farms contain 55-110 positive links, 22-41 represented plant taxa,
  and 47-84 represented herbivore taxa;
- two pooled farm-type webs appearing in later compilations are derived
  composites and must not be treated as independent ecologies.

The README describes a fourth location file, `Location_20farms`, but Dryad
version 1 actually contains three CSV files and three duplicate README files.
Exact coordinates therefore were not recovered from the archived version. Farm
codes, paired design, region, dates, habitat strata, and protocol are still
recoverable.

## Eligibility assessment

| Rule | Result | Basis |
| --- | --- | --- |
| Natural or semi-natural field community | pass | Twenty working mixed farms sampled as whole-farm communities |
| Place, dates, and protocol recoverable | pass with coordinate note | Farm IDs, southwest England, 2005-2006, habitat-stratified transects, beating, and sweep netting are documented |
| Plant and arthropod roles recoverable | pass | Plant, herbivore, and parasitoid fields are explicit |
| Feeding confirmed per interaction | fail for E0/E1 | Some hosts were inferred from literature or randomly selected among plausible hosts; evidence mode is absent from released rows |
| Raw data and sufficient methods open | pass | CC0 Dryad files plus freely accessible methods for the same networks |
| Network boundary recoverable | pass | Twenty farm codes and 10 pairing relationships are explicit |

## Required next action

Retain the 20 farm networks as an R3 ingestion candidate with
`evidence_method=mixed_observed_and_locally_inferred_host_assignment`. Preserve
quantitative `Int` values and the organic-conventional pair identifier. Do not
ingest the two farm-type pooled composites as independent networks. Promotion
of a row or subset to E0/E1 would require an author-provided observation-level
method flag or an equivalent source record that distinguishes confirmed
feeding from inferred host assignment.

# Araújo et al. 2019 source audit

## Decision

Register as high-priority borderline candidate `C019`. The biological and sampling evidence supports 15 prospective E0 networks, but the published supplementary CSV fails source-total reconciliation. Do not ingest or count the networks until a corrected file or an author-confirmed explanation is obtained.

## Source lineage

- Network article: Araújo et al., “Superhost Plants Alter the Structure of Plant–Galling Insect Networks in Neotropical Savannas,” *Plants* (2019), DOI `10.3390/plants8100369`, open full text at <https://pmc.ncbi.nlm.nih.gov/articles/PMC6843997/>.
- Original field study: Araújo, “Can Host Plant Richness be Used as a Surrogate for Galling Insect Diversity?”, *Tropical Conservation Science* (2011), DOI `10.1177/194008291100400405`.
- Supplement package retrieved from the article record: `supplementary.zip`.
- Package SHA-256: `324118413261dbb84b18ff000671bec7c8226d71f67a31a37cf66e9e348db6bd`.
- Interaction file inside package: `plants-08-00369-s001.csv`, 38,366 bytes, semicolon-delimited CP1252 text.

## Prospective ecology boundaries

The original study sampled 15 Brazilian Cerrado sites once between February and May 2010. Each site used ten randomly located 10 × 10 m plots. Woody plants above the stated circumference threshold were surveyed, and leaves, stems, and flowers were inspected for gall morphotypes. These diagnostic structures constitute direct feeding evidence under the frozen protocol, so each site would be an E0 ecology if the raw data reconcile.

## Reconciliation failure

The supplementary CSV has 275 post-header records, of which 14 are embedded copies of the column header. Removing those non-data rows yields:

| Quantity | Article/source claim | Parsed supplementary CSV |
| --- | ---: | ---: |
| Host plant taxa | 64 | 62 |
| Gall taxa/morphotypes | 112 | 110 |
| Positive records | not stated as a corpus total | 261 |
| Local interaction range | 9–36 | 9–32 |

The cleaned table has 15 site identifiers and no duplicate site–plant–gall triples. The discrepancy therefore cannot be repaired merely by dropping embedded headers, and missing cells must not be invented. The original 2011 article also reports 64 plants and 112 gall species, reinforcing that the supplement is incomplete or malformed rather than documenting a later taxonomic convention.

## Eligibility assessment

| Rule | Result | Basis |
| --- | --- | --- |
| Natural field community | pass | Cerrado vegetation sampled in situ |
| Place, time, habitat, and protocol recoverable | pass | Fifteen sites; February–May 2010; plot and inspection methods reported |
| Feeding confirmed | pass | Plant-specific diagnostic galls |
| Raw data openly obtainable | pass, defective | Supplementary CSV is open but internally malformed/incomplete |
| Source totals reconcile | fail | Taxon and local-link totals differ from the publications |
| Safe for canonical ingestion | no | Silent imputation would violate provenance and validation rules |

## Resolution paths

1. Locate a corrected supplement in an author, institutional, or journal repository.
2. Ask the corresponding author or journal for the deposited pre-publication table and an explanation of the missing two plant and two gall taxa.
3. If no corrected file exists, retain the candidate and its checksum in the exclusion registry; do not approximate the missing links.
4. If corrected data are obtained, implement a source-specific parser and manually reconstruct at least two networks before promotion.

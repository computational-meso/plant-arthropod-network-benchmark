# EDI submission plan

## Release decision

Publish the collection as **one Environmental Data Initiative data package with
one versioned DOI**, not as one deposit per upstream study. Within that package,
`derived_products.csv` identifies one source-derived component for every
ingested study and links it to its exact upstream DOI, repository version, and
raw-file checksum.

This arrangement keeps the collection easy to cite and download while making
its multi-source provenance explicit and reversible. It also allows later
versions to add or stratify networks without changing the identity of the
version used by a paper.

## EDI-first source screen

Candidate sources are screened in this order:

1. **Tier A — EDI-native:** prefer an existing EDI/PASTA package and use its
   package identifier as internal provenance.
2. **Tier B — external, versioned, and open:** include the harmonized derived
   component when the upstream DOI, version, license, raw checksums, methods,
   and ecology boundaries are adequate. Record external provenance in EML.
3. **Tier C — restricted, mixed, or not release-ready:** keep citation and
   retrieval provenance, but exclude source files or data entities from the
   initial EDI package until the problem is resolved.
4. **Tier D — out of scope:** retain only a screening or provenance record.

EDI-native placement is a priority, not a substitute for scientific fit. A
large regional metaweb is not promoted to a local field ecology merely because
it is already in EDI, and a well-documented open Dryad dataset is not discarded
merely because its original repository is external.

## Current v0.1 status

- The schema-valid draft EML has been imported into the author's private ezEML
  workspace without errors. No data entities have been attached and the
  package has not been submitted, shared, sent to curation, or published.
- Ten included source-derived components are Tier B external open sources.
- Repository-backed license evidence is recorded for every included component:
  nine Dryad datasets are CC0 and the original Shinohara Figshare item is CC BY
  4.0. The initial EDI entities contain harmonized derived tables rather than
  copies of the upstream raw archives.
- No EDI-native source currently supplies a qualifying bounded E0/E1 network.
- EDI package `edi.1508.3` is registered in R4 as a terrestrial cumulative
  food-web metaweb only; it does not contribute to the local-network counts.
- The Maunsell candidate is Tier C because required companion material has
  mixed redistribution terms and the local plant--miner layer is not released.
- The Zhang candidate is Tier C until the field methods and sampling boundary
  are openly reconstructable.
- The Nyman source is Tier D because its objects are population samples for a
  different trophic layer, not bounded plant--herbivore community networks.

The initial EDI search used the public DataONE index restricted to the EDI
node because the public PASTA search endpoint required authorization during the
search session. The exact search and outcome are recorded in
`search_registry.csv`.

## Package contents

Keep the first submission deliberately small. Its data entities are the 17
canonical CSV tables described in `v0.1.0/edi/eml-draft.xml`. This includes the
source and file manifests, provenance, validation results, exclusions, search
registry, interaction table, taxa, network boundaries, and graph products.
The matching Parquet tables and generated matrices remain deterministic local
convenience exports; attach them later as one clearly documented ancillary
archive only if EDI's curator recommends it. The reproducible code should
likewise be linked as a versioned software release instead of turning every
script into a separately described EDI data entity.

Raw upstream files are not part of the initial EDI entities. Include them in a
later revision only when redistribution rights have been verified explicitly.
Otherwise, retain the stable upstream DOI, retrieval URL, version, byte size,
and checksum already published in the manifests.

The EML record should describe this dataset as a derived synthesis and cite
every upstream dataset. Internal EDI inputs should use their PASTA package IDs;
external inputs should use their DOI and stable landing page. The EML methods
and provenance sections should point to the build version and the corresponding
row in `derived_products.csv`.

## Minimal-GUI submission workflow

Use EDI's curator-supported author route for the first release. EDI states that
most data authors publish through its curation team, and this is a particularly
good fit for a first ecological data publication: the curator checks usability
and metadata, but this is not journal peer review. The package remains a
normal, versioned EDI data publication with a DOI.

The current package does **not** require an external static file host. EDI's
published limit for manual Data Portal uploads is 500 MB per entity. All 17
canonical CSV entities fit under that conservative 500,000,000-byte gate; the
largest is `interactions.csv` at approximately 309 MiB. Manual upload therefore
removes the only reason to partition the canonical table or configure cloud
object storage for version 1.0.

The build creates three submission-control artifacts under `v0.1.0/edi/`:

- `eml-draft.xml`: schema-valid EML 2.2.0 for the 17 canonical CSV entities;
- `entity_manifest.csv`: delivery mode, upload eligibility, MD5 checksums,
  SHA-256 checksums, byte sizes, and row counts; and
- `submission_readiness.json`: a machine-readable stop/go decision for EDI
  evaluation.

Human-facing fields live in `edi_submission_config.draft.json`. Unconfirmed
creator/contact details, the proposed license, and pending scientific reviews
deliberately prevent a false submission-ready state. A final package identifier
is not required before the curator-supported author submission: EDI curation
staff assign it during publication. The assigned identifier and DOI must then
be written back to the configuration and frozen release metadata.

Creator ORCID iDs are optional but recommended. Enter either the bare
`0000-0000-0000-0000` form or its `https://orcid.org/` URL; the build normalizes
the value and validates its check digit before the creator gate can pass. Never
guess an ORCID or infer creator order from the repository history.

The synthesis creators dedicate the rights they control under CC0 1.0, EDI's
default open-data approach. This waiver covers the harmonization, organization,
metadata, and other original contributions; it does not supersede third-party
rights. Source-level terms remain recorded in `sources.csv` and
`derived_products.csv`, including the upstream CC BY 4.0 attribution obligation
for the Shinohara source-derived component.

The first-release sequence is:

1. finish the creator, contact, and license fields in
   `edi_submission_config.draft.json`, and finish the manual-reconstruction and
   independent source-review gates in `human_review_ledger.draft.json` using
   the generated `v0.1.0/review/` packet;
2. rebuild and verify the EML, entity manifest, hashes, and tests;
3. log in to ezEML with Google, GitHub, ORCID, or an EDI account;
4. import `eml-draft.xml` and attach the 17 files from `tables/csv/`;
5. run the ezEML and repository checks and correct every error;
6. submit the package to the EDI Data Curation Team;
7. review the curator's proof and explicitly approve publication; and
8. record the final package identifier, revision, DOI, quality report, and
   checksums in the project and rebuild the frozen release.

This route uses the GUI for file selection, submission, and proof review, while
all substantive metadata and data production remain reproducible in code. No
credentials belong in the repository, and no build command publishes anything.

## Optional API route

Complete headless publication remains technically supported through `EDIutils`
or the REST API. It requires an EDI account/API key and a static, public,
no-redirect HTTPS URL for every entity; the API does not accept the local files
as a multipart bundle. That adds infrastructure without improving the first
release, so it is retained as an optional future route rather than the default.
The generated `edi_api_plan.json` records both the recommended curator route and
the available REST operations. Any direct production creation call must remain
separate and require explicit creator approval.

Official references:

- [EDI REST API](https://edirepository.org/resources/rest-api)
- [Resources for data authors](https://edirepository.org/resources/resources-for-data-authors)
- [ezEML user guide](https://ezeml.edirepository.org/eml/user_guide)
- [Publishing a data package](https://edirepository.org/resources/publishing-a-data-package)
- [Uploading with static data links](https://edirepository.org/resources/uploading-with-static-data-links)
- [EDI Identity and Access Manager](https://edirepository.org/resources/iam)
- [EDIutils evaluation and upload workflow](https://docs.ropensci.org/EDIutils/articles/evaluate_and_upload.html)
- [Creating metadata for publication](https://edirepository.org/resources/creating-metadata-for-publication)
- [Provenance metadata](https://edirepository.org/resources/provenance-metadata)
- [PASTA Data Package Manager API](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html)

# Table guide

The canonical representation is a set of long relational tables. Matrices are
derived views rather than separately curated sources of truth.

## Core analysis path

```text
sources
  └── studies
       └── sampling_events
            └── networks
                 ├── taxa
                 ├── interactions
                 ├── network_metrics
                 └── competition_edges
```

Join keys:

- `sources.source_id` → `studies.source_id`
- `studies.study_id` → `sampling_events.study_id` and `networks.study_id`
- `sampling_events.event_id` → `networks.event_id`
- `networks.network_id` → `taxa`, `interactions`, `network_metrics`, and
  `competition_edges`
- `taxa.taxon_record_id` → plant and herbivore identifiers in interactions and
  projected edges

## The 17 released tables

| Table | Purpose |
| --- | --- |
| `sources` | Original citations, repositories, versions, licenses, methods, and source decisions. |
| `studies` | Original study and field-campaign descriptions. |
| `sampling_events` | Place, dates, habitat, protocol, and source-provided ecosystem labels. |
| `networks` | Ecology boundary, evidence class, parent, dependency cluster, release layer, and analysis gates. |
| `taxa` | Source-local taxon records, verbatim names, roles, resolution, and activity. |
| `taxonomy_map` | Reversible accepted-name mapping; unresolved in this preview. |
| `interactions` | Canonical plant–herbivore cells, states, values, evidence, and provenance. |
| `network_metrics` | Bipartite and projected-graph summary measures and analysis gates. |
| `competition_edges` | Positive off-diagonal shared-host overlaps from binary `B.T @ B`. |
| `derivations` | Filtering, aggregation, extraction, and transformation records. |
| `derived_products` | Mapping from upstream datasets to this synthesis product. |
| `file_manifest` | Upstream retrieval URLs, sizes, checksums, and redistribution status. |
| `qa_results` | Automated and release-level validation results. |
| `manual_review_queue` | Selected manual parser-reconstruction cases and statuses. |
| `candidate_registry` | Screened candidate sources and current disposition. |
| `exclusions` | Exclusion or hold decisions and reasons. |
| `search_registry` | Search resources, queries/actions, dates, and outcomes. |

Complete field types and descriptions are machine-readable in
`metadata/datapackage.json`. Row counts and SHA-256 hashes for the canonical CSV
entities are in `metadata/entity_manifest.csv`.

## Important network fields

- `evidence_class`: E0/E1 direct, E2 derived or conservatively classified, E3
  extracted, M metaweb, or X enrichment/source-only.
- `eligible_direct`: provisional direct-layer inclusion flag.
- `independence_cluster_id`: conservative primary grouping for repeated or
  nested field observations.
- `release_layer`: R2 direct networks or R3 derived/extracted networks in this
  preview.
- `gate_projection`, `gate_comparative`, `gate_spectral`: analysis eligibility,
  not publication or quality scores.
- `canonical_edge_hash`: stable hash used in duplication and reconstruction
  checks.


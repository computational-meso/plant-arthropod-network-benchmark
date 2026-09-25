# Analysis notes

## Primary scientific interpretation

The bipartite data describe plant–arthropod feeding or source-defined host
associations at bounded places, times, habitats, and protocols. For a binary
plant-by-herbivore matrix `B`, the product `C = B.T @ B` counts shared plant
hosts. The diagonal of `C` is herbivore host breadth and is stored separately
from interspecific edges.

An off-diagonal edge is shared-host overlap and potential exploitative
competition. It is not direct evidence that competition occurred, affected
fitness, or structured the community.

## Dependency

The 346 network objects are not 346 independent ecological replicates. Use
`independence_cluster_id` for conservative primary inference and cluster or
otherwise model repeated observations by original study and field lineage.
Report both network-object and independent-cluster counts.

## Suggested analysis strata

- Primary direct layer: `eligible_direct == true` and E0/E1.
- Expansion/sensitivity layer: E2, reported separately.
- Descriptive summaries: all valid network objects, visibly stratified.
- Comparative graph statistics: use `gate_comparative` and repeat under nearby
  thresholds.
- Spectral/community statistics: use `gate_spectral` and report exclusions.

Do not permanently delete valid small networks merely because they fail an
analysis threshold.

## Taxonomy

Use source-local taxon records for within-network calculations. Verbatim names
are preserved. Do not merge morphospecies across studies. The separate
`taxonomy_map` is intentionally unresolved in this preview and must not be
treated as a completed global taxonomic harmonization.

## Interaction values

Binary incidence is the primary cross-study representation. Quantitative
`source_value` fields retain heterogeneous source units and should not be pooled
without a defensible compatibility argument. Preserve the distinction among
positive, sampled-zero, structural-zero, not-sampled, and unknown states.

## Minimum reporting checklist

Report the dataset version, evidence classes, number of studies, number of
networks, number of independence clusters, chosen analysis gate, treatment of
zeros and unknowns, weighting choice, and whether conclusions change under
adjacent thresholds. Cite the relevant original studies as well as the final
dataset DOI when available.


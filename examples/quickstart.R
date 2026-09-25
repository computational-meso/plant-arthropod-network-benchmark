# Read-only quick start for the provisional plant–arthropod benchmark.

library(arrow)
library(dplyr)

networks <- read_parquet("data/parquet/networks.parquet")
interactions <- read_parquet("data/parquet/interactions.parquet")

direct <- networks |>
  filter(eligible_direct, evidence_class %in% c("E0", "E1"))

example_network <- direct |>
  filter(gate_comparative) |>
  arrange(desc(positive_links), network_id) |>
  slice(1) |>
  pull(network_id)

positive <- interactions |>
  filter(
    network_id == example_network,
    interaction_state == "observed_positive"
  )

cat("All network objects:", nrow(networks), "\n")
cat("Provisional direct E0/E1 networks:", nrow(direct), "\n")
cat("Direct independence clusters:", n_distinct(direct$independence_cluster_id), "\n")
cat("Example network:", example_network, "\n")
cat("Observed positive links:", nrow(positive), "\n")


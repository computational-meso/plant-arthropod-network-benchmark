"""Read-only quick start for the provisional plant–arthropod benchmark."""

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "parquet"


def main() -> None:
    networks = pd.read_parquet(DATA / "networks.parquet")
    interactions = pd.read_parquet(DATA / "interactions.parquet")

    direct = networks.loc[
        networks["eligible_direct"]
        & networks["evidence_class"].isin(["E0", "E1"])
    ].copy()
    clusters = direct["independence_cluster_id"].nunique()

    qualifying = direct.loc[direct["gate_comparative"]].sort_values(
        ["positive_links", "network_id"], ascending=[False, True]
    )
    if qualifying.empty:
        raise RuntimeError("No direct network passes the comparative gate")

    network_id = qualifying.iloc[0]["network_id"]
    positive = interactions.loc[
        (interactions["network_id"] == network_id)
        & (interactions["interaction_state"] == "observed_positive")
    ]
    if positive.empty:
        raise RuntimeError(f"No positive interactions for {network_id}")

    incidence = positive.pivot_table(
        index="plant_taxon_record_id",
        columns="herbivore_taxon_record_id",
        values="binary_value",
        aggfunc="max",
        fill_value=0,
    ).astype("int8")
    projection = incidence.T @ incidence
    host_breadth = incidence.sum(axis=0).to_numpy()
    if not np.array_equal(np.diag(projection.to_numpy()), host_breadth):
        raise RuntimeError("Projection diagonal does not equal host breadth")

    off_diagonal = projection.to_numpy(copy=True)
    np.fill_diagonal(off_diagonal, 0)
    projected_edges = int(np.count_nonzero(np.triu(off_diagonal, k=1)))

    print(f"All network objects: {len(networks):,}")
    print(f"Provisional direct E0/E1 networks: {len(direct):,}")
    print(f"Direct independence clusters: {clusters:,}")
    print(f"Example network: {network_id}")
    print(f"B shape: {incidence.shape[0]} plants × {incidence.shape[1]} herbivores")
    print(f"Observed positive links: {len(positive):,}")
    print(f"Projected shared-host edges: {projected_edges:,}")
    print("Projection diagonal equals herbivore host breadth: PASS")


if __name__ == "__main__":
    main()


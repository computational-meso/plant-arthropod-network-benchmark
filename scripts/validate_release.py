#!/usr/bin/env python3
"""Validate the public benchmark checkout or expanded release archive."""

from __future__ import annotations

import csv
import hashlib
import itertools
import json
import math
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PARQUET = ROOT / "data" / "parquet"
CSV = ROOT / "tables" / "csv"
METADATA = ROOT / "metadata"
TABLES = {
    "candidate_registry",
    "competition_edges",
    "derivations",
    "derived_products",
    "exclusions",
    "file_manifest",
    "interactions",
    "manual_review_queue",
    "network_metrics",
    "networks",
    "qa_results",
    "sampling_events",
    "search_registry",
    "sources",
    "studies",
    "taxa",
    "taxonomy_map",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def unique_nonblank(frame: pd.DataFrame, field: str, table: str) -> None:
    require(field in frame, f"{table}.{field} is missing")
    values = frame[field]
    require(values.notna().all(), f"{table}.{field} contains nulls")
    require((values.astype(str).str.len() > 0).all(), f"{table}.{field} contains blanks")
    require(not values.duplicated().any(), f"{table}.{field} is not unique")


def foreign_key(values: pd.Series, parents: pd.Series, label: str) -> None:
    child = set(values.dropna().astype(str)) - {""}
    parent = set(parents.dropna().astype(str))
    missing = child - parent
    require(not missing, f"{label} has {len(missing)} missing parent identifiers")


def validate_metadata(tables: dict[str, pd.DataFrame]) -> None:
    package = json.loads((METADATA / "datapackage.json").read_text(encoding="utf-8"))
    resources = package["resources"]
    require(len(resources) == 34, "datapackage must describe 17 CSV and 17 Parquet resources")
    parquet_resources = [item for item in resources if item["format"] == "parquet"]
    csv_resources = [item for item in resources if item["format"] == "csv"]
    require({item["name"] for item in parquet_resources} == TABLES, "Parquet resource set differs")
    require({item["name"] for item in csv_resources} == TABLES, "CSV resource set differs")
    for item in parquet_resources:
        require((ROOT / item["path"]).is_file(), f"missing resource: {item['path']}")

    tree = ET.parse(METADATA / "eml-draft.xml")
    entity_names = {node.findtext("entityName", "").removesuffix(".csv") for node in tree.findall("dataset/dataTable")}
    require(entity_names == TABLES, "EML entity set differs from the 17 canonical tables")

    with (METADATA / "build_manifest.csv").open(encoding="utf-8", newline="") as stream:
        manifest = list(csv.DictReader(stream))
    require(manifest, "build manifest is empty")
    for row in manifest:
        path = ROOT / row["relative_path"]
        require(path.is_file(), f"manifest path is missing: {row['relative_path']}")
        require(path.stat().st_size == int(row["size_bytes"]), f"size differs: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"checksum differs: {row['relative_path']}")

    if not CSV.is_dir():
        return
    with (METADATA / "entity_manifest.csv").open(encoding="utf-8", newline="") as stream:
        entities = list(csv.DictReader(stream))
    require(len(entities) == 17, "entity manifest must contain 17 CSV tables")
    for row in entities:
        path = ROOT / row["relative_path"]
        require(path.is_file(), f"canonical CSV is missing: {row['relative_path']}")
        require(path.stat().st_size == int(row["size_bytes"]), f"CSV size differs: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"CSV checksum differs: {row['relative_path']}")
        with path.open(encoding="utf-8", newline="") as stream:
            row_count = sum(1 for _ in csv.reader(stream)) - 1
        require(row_count == int(row["row_count"]), f"CSV row count differs: {row['relative_path']}")
        parquet = tables[row["entity_name"]]
        require(row_count == len(parquet), f"CSV/Parquet row counts differ: {row['entity_name']}")


def main() -> None:
    found = {path.stem for path in PARQUET.glob("*.parquet")}
    require(found == TABLES, f"expected 17 Parquet tables; found {len(found)}")
    tables = {name: pd.read_parquet(PARQUET / f"{name}.parquet") for name in sorted(TABLES)}

    primary_keys = {
        "sources": "source_id",
        "studies": "study_id",
        "sampling_events": "event_id",
        "networks": "network_id",
        "taxa": "taxon_record_id",
        "taxonomy_map": "taxon_record_id",
        "interactions": "interaction_id",
        "network_metrics": "network_id",
        "derived_products": "derived_product_id",
        "file_manifest": "file_id",
        "qa_results": "test_id",
    }
    for table, field in primary_keys.items():
        unique_nonblank(tables[table], field, table)

    sources = tables["sources"]
    studies = tables["studies"]
    events = tables["sampling_events"]
    networks = tables["networks"]
    taxa = tables["taxa"]
    taxonomy = tables["taxonomy_map"]
    interactions = tables["interactions"]
    metrics = tables["network_metrics"]
    edges = tables["competition_edges"]

    foreign_key(studies["source_id"], sources["source_id"], "studies.source_id")
    foreign_key(events["study_id"], studies["study_id"], "sampling_events.study_id")
    foreign_key(networks["event_id"], events["event_id"], "networks.event_id")
    foreign_key(networks["study_id"], studies["study_id"], "networks.study_id")
    foreign_key(networks["source_id"], sources["source_id"], "networks.source_id")
    foreign_key(networks["parent_network_id"], networks["network_id"], "networks.parent_network_id")
    foreign_key(taxa["network_id"], networks["network_id"], "taxa.network_id")
    foreign_key(taxonomy["taxon_record_id"], taxa["taxon_record_id"], "taxonomy_map.taxon_record_id")
    foreign_key(interactions["network_id"], networks["network_id"], "interactions.network_id")
    foreign_key(metrics["network_id"], networks["network_id"], "network_metrics.network_id")
    foreign_key(edges["network_id"], networks["network_id"], "competition_edges.network_id")

    require(len(taxonomy) == len(taxa), "taxonomy_map must retain one reversible row per taxon")
    require(set(taxa["trophic_role"]) == {"plant", "herbivore"}, "unexpected trophic role")
    plant_ids = set(taxa.loc[taxa["trophic_role"] == "plant", "taxon_record_id"])
    herbivore_ids = set(taxa.loc[taxa["trophic_role"] == "herbivore", "taxon_record_id"])
    require(set(interactions["plant_taxon_record_id"]) <= plant_ids, "interaction uses a non-plant resource")
    require(set(interactions["herbivore_taxon_record_id"]) <= herbivore_ids, "interaction uses a non-herbivore consumer")

    event_studies = events.set_index("event_id")["study_id"]
    study_sources = studies.set_index("study_id")["source_id"]
    require(
        networks["event_id"].map(event_studies).equals(networks["study_id"]),
        "network study_id differs from its sampling event",
    )
    require(
        networks["study_id"].map(study_sources).equals(networks["source_id"]),
        "network source_id differs from its study",
    )

    taxon_networks = taxa.set_index("taxon_record_id")["network_id"]
    require(
        interactions["plant_taxon_record_id"].map(taxon_networks).equals(interactions["network_id"]),
        "an interaction plant belongs to a different network",
    )
    require(
        interactions["herbivore_taxon_record_id"].map(taxon_networks).equals(interactions["network_id"]),
        "an interaction herbivore belongs to a different network",
    )
    require(
        taxonomy.set_index("taxon_record_id")["name_verbatim"].equals(
            taxa.set_index("taxon_record_id")["name_verbatim"]
        ),
        "taxonomy_map does not preserve verbatim taxon names",
    )

    allowed_states = {"observed_positive", "sampled_zero", "structural_zero", "not_sampled", "unknown"}
    require(set(interactions["interaction_state"]) <= allowed_states, "unexpected interaction state")
    positive = interactions[interactions["interaction_state"] == "observed_positive"].copy()
    sampled_zero = interactions[interactions["interaction_state"] == "sampled_zero"]
    require((positive["binary_value"] == 1).all(), "positive interactions must have binary_value=1")
    require((sampled_zero["binary_value"] == 0).all(), "sampled zeros must have binary_value=0")
    other = interactions[~interactions["interaction_state"].isin(["observed_positive", "sampled_zero"])]
    require(other["binary_value"].isna().all(), "unknown/unsampled states must not be coerced to zero")

    indexed_networks = networks.set_index("network_id")
    role_counts = taxa.groupby(["network_id", "trophic_role"]).size().unstack(fill_value=0)
    active_counts = taxa[taxa["active"]].groupby(["network_id", "trophic_role"]).size().unstack(fill_value=0)
    cell_counts = interactions.groupby("network_id").size()
    positive_counts = positive.groupby("network_id").size()
    for network_id, row in indexed_networks.iterrows():
        require(int(role_counts.loc[network_id, "plant"]) == int(row["plant_count"]), f"plant count differs: {network_id}")
        require(int(role_counts.loc[network_id, "herbivore"]) == int(row["herbivore_count"]), f"herbivore count differs: {network_id}")
        require(int(active_counts.get("plant", pd.Series(dtype=int)).get(network_id, 0)) == int(row["active_plant_count"]), f"active plant count differs: {network_id}")
        require(int(active_counts.get("herbivore", pd.Series(dtype=int)).get(network_id, 0)) == int(row["active_herbivore_count"]), f"active herbivore count differs: {network_id}")
        require(int(cell_counts.get(network_id, 0)) == int(row["plant_count"] * row["herbivore_count"]), f"interaction grid is incomplete: {network_id}")
        require(int(positive_counts.get(network_id, 0)) == int(row["positive_links"]), f"positive link count differs: {network_id}")

    require({"active_plant_count", "active_herbivore_count"} <= set(metrics), "network_metrics must label active taxon counts explicitly")
    joined = indexed_networks.join(metrics.set_index("network_id"), rsuffix="_metric")
    for field in ("active_plant_count", "active_herbivore_count", "positive_links", "gate_projection", "gate_comparative", "gate_spectral"):
        require((joined[field] == joined[f"{field}_metric"]).all(), f"network_metrics.{field} differs from networks")

    expected_edges: Counter[tuple[str, str, str]] = Counter()
    for (network_id, _plant_id), group in positive.groupby(["network_id", "plant_taxon_record_id"], sort=False):
        herbivores = sorted(set(group["herbivore_taxon_record_id"]))
        for herbivore_a, herbivore_b in itertools.combinations(herbivores, 2):
            expected_edges[(network_id, herbivore_a, herbivore_b)] += 1
    observed_edges = {
        (row.network_id, row.herbivore_a_taxon_record_id, row.herbivore_b_taxon_record_id): int(row.shared_host_count)
        for row in edges.itertuples(index=False)
    }
    require(len(observed_edges) == len(edges), "competition_edges contains duplicate endpoint pairs")
    require((edges["shared_host_count"] > 0).all(), "competition edge weights must be positive")
    require(
        (edges["herbivore_a_taxon_record_id"] < edges["herbivore_b_taxon_record_id"]).all(),
        "competition edge endpoints must use canonical sorted order",
    )
    require(
        edges["herbivore_a_taxon_record_id"].map(taxon_networks).equals(edges["network_id"])
        and edges["herbivore_b_taxon_record_id"].map(taxon_networks).equals(edges["network_id"]),
        "a competition edge endpoint belongs to a different network",
    )
    require(dict(expected_edges) == observed_edges, "competition_edges does not equal the positive B.T @ B upper triangle")

    for row in metrics.itertuples(index=False):
        group = positive[positive["network_id"] == row.network_id]
        breadth = group.groupby("herbivore_taxon_record_id")["plant_taxon_record_id"].nunique()
        incident = set()
        for network_id, herbivore_a, herbivore_b in expected_edges:
            if network_id == row.network_id:
                incident.update((herbivore_a, herbivore_b))
        active_plants = group["plant_taxon_record_id"].nunique()
        active_herbivores = len(breadth)
        edge_count = sum(1 for key in expected_edges if key[0] == row.network_id)
        density = 0.0 if active_herbivores < 2 else edge_count / (active_herbivores * (active_herbivores - 1) / 2)
        require(int(row.active_plant_count) == active_plants, f"metric active plants differ: {row.network_id}")
        require(int(row.active_herbivore_count) == active_herbivores, f"metric active herbivores differ: {row.network_id}")
        require(int(row.projected_nodes) == active_herbivores, f"projected nodes differ: {row.network_id}")
        require(int(row.projected_edges) == edge_count, f"projected edges differ: {row.network_id}")
        require(int(row.projected_nonisolates) == len(incident), f"projected nonisolates differ: {row.network_id}")
        require(int(row.host_breadth_min) == int(breadth.min() if len(breadth) else 0), f"minimum host breadth differs: {row.network_id}")
        require(math.isclose(float(row.host_breadth_mean), float(breadth.mean() if len(breadth) else 0), abs_tol=1e-8), f"mean host breadth differs: {row.network_id}")
        require(int(row.host_breadth_max) == int(breadth.max() if len(breadth) else 0), f"maximum host breadth differs: {row.network_id}")
        require(math.isclose(float(row.projected_density), density, abs_tol=1e-8), f"projected density differs: {row.network_id}")

    direct = networks[networks["eligible_direct"] & networks["evidence_class"].isin(["E0", "E1"])]
    require((direct["release_layer"] == "R2").all(), "eligible direct networks must be in R2")
    derived = networks[networks["evidence_class"].isin(["E2", "E3"])]
    require((derived["release_layer"] == "R3").all(), "derived/extracted networks must be in R3")

    summary = json.loads((METADATA / "build_summary.json").read_text(encoding="utf-8"))
    require(summary["network_objects_total"] == len(networks), "build summary network count differs")
    require(summary["direct_E0_E1_provisional"] == len(direct), "build summary direct count differs")
    require(summary["positive_bipartite_links_total"] == len(positive), "build summary positive link count differs")
    qa_counts = tables["qa_results"]["status"].value_counts().to_dict()
    require("FAIL" not in qa_counts, "qa_results contains a failure")
    require(summary["qa_status_counts"] == qa_counts, "build summary QA counts differ")

    validate_metadata(tables)
    csv_note = "CSV layer verified" if CSV.is_dir() else "CSV layer is release-archive-only"
    print(
        f"Validation: PASS — {len(networks):,} networks, {len(interactions):,} interaction cells, "
        f"{len(edges):,} projected edges; {csv_note}."
    )


if __name__ == "__main__":
    main()

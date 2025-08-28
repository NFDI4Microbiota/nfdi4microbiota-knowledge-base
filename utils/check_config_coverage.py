import argparse
import json
import os
import sys
from typing import Dict, List, Set, Tuple

import yaml

TRUTHY_VALUES = frozenset(["true", "yes", "on", "1"])

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "_config.yml")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def extract_collection_orders(cfg: dict) -> Dict[str, List[str]]:
    collections = cfg.get("collections", {}) or {}
    return {
        name: meta.get("order", []) if isinstance(meta, dict) else []
        for name, meta in collections.items()
    }


def parse_boundary_flags(path: str) -> Dict[str, str]:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()

        # Check if file starts with --- boundary
        if not content.startswith("---\n"):
            return {}

        # Find the closing boundary
        end_pos = content.find("\n---\n", 4)
        if end_pos == -1:
            return {}

        yaml_content = content[4:end_pos]
        return yaml.safe_load(yaml_content) or {}

    except (FileNotFoundError, yaml.YAMLError):
        return {}


def is_hidden(flags: Dict[str, str]) -> bool:
    for key in ("hidden", "hide"):
        value = flags.get(key)
        if value is None:
            continue

        # Handle boolean values directly
        if isinstance(value, bool):
            return value

        # Handle string representations
        if isinstance(value, str):
            return value.lower().strip("\"'") in TRUTHY_VALUES

    return False


def collect_markdown_files() -> Tuple[Dict[str, Set[str]], Dict[str, Set[str]]]:
    visible: Dict[str, Set[str]] = {}
    hidden: Dict[str, Set[str]] = {}

    for root, dirs, files in os.walk(DOCS_DIR):
        rel_path = os.path.relpath(root, DOCS_DIR)

        # Skip root directory
        if rel_path == ".":
            continue

        # Only process first-level collection directories starting with underscore
        parts = rel_path.split(os.sep)
        if len(parts) != 1 or not parts[0].startswith("_"):
            continue

        collection_name = parts[0][1:]  # Remove underscore prefix

        for filename in files:
            if not filename.lower().endswith(".md"):
                continue

            full_path = os.path.join(root, filename)
            flags = parse_boundary_flags(full_path)

            target_dict = hidden if is_hidden(flags) else visible
            target_dict.setdefault(collection_name, set()).add(filename)

    return visible, hidden


def analyze() -> dict:
    cfg = load_config()
    cfg_orders = extract_collection_orders(cfg)
    disk_md, hidden_md = collect_markdown_files()

    missing_in_config: Dict[str, List[str]] = {}
    listed_but_missing: Dict[str, List[str]] = {}
    collections_only_on_disk = set(disk_md.keys()) - set(cfg_orders.keys())
    collections_only_in_config = set(cfg_orders.keys()) - set(disk_md.keys())

    # Compare collections present on both disk and config
    for coll in set(disk_md.keys()) & set(cfg_orders.keys()):
        files = disk_md[coll]
        order_set = set(cfg_orders[coll])

        # Files on disk not in order list
        extra_files = sorted(f for f in files if f not in order_set)
        if extra_files:
            missing_in_config[coll] = extra_files

        # Files listed in config but not on disk (excluding hidden files)
        missing_files = [
            f
            for f in order_set
            if f not in files and f not in hidden_md.get(coll, set())
        ]
        if missing_files:
            listed_but_missing[coll] = missing_files

    return {
        "missing_in_config": missing_in_config,
        "listed_but_missing": listed_but_missing,
        "collections_only_on_disk": sorted(collections_only_on_disk),
        "collections_only_in_config": sorted(collections_only_in_config),
        "ok": not any(
            [
                missing_in_config,
                listed_but_missing,
                collections_only_on_disk,
                collections_only_in_config,
            ]
        ),
    }


def print_analysis_results(result: dict) -> None:
    """Print analysis results in human-readable format."""
    sections = [
        (
            "missing_in_config",
            "Markdown files present on disk but missing from config order list:",
        ),
        ("listed_but_missing", "Files listed in config order but missing on disk:"),
        (
            "collections_only_on_disk",
            "Collections present on disk but not defined in _config.yml:",
        ),
        (
            "collections_only_in_config",
            "Collections defined in _config.yml but no directory found in docs/:",
        ),
    ]

    for key, title in sections:
        data = result[key]
        if not data:
            continue

        print(title)
        match data:
            case dict():  # For missing_in_config and listed_but_missing
                for coll, files in data.items():
                    print(f"  {coll}:")
                    for f in files:
                        print(f"  - {f}")
            case list():  # For collections_only_* lists
                for item in data:
                    print(f"- {item}")

    if result["ok"]:
        print("All markdown files are accounted for in _config.yml order lists.")


def main():
    parser = argparse.ArgumentParser(
        description="Validate markdown coverage against _config.yml order lists."
    )
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    result = analyze()

    match args.json:
        case True:
            print(json.dumps(result, indent=2))
        case False:
            print_analysis_results(result)

    if not result["ok"]:
        sys.exit(1)


if __name__ == "__main__":
    main()

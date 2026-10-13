#!/usr/bin/env python3
"""Validate portable *project-owned* historian profile JSON, not EBPro native files."""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/site-profile.schema.json"
EXAMPLES = ROOT / "examples/site-profiles"

AGGREGATIONS = {
    "sample": {"avg_min_max", "raw_only"},
    "counter": {"delta_reset_aware", "raw_only"},
    "state": {"duration_from_transitions", "raw_only"},
    "event": {"event_count", "raw_only"},
    "transaction": {"transaction_sum", "raw_only"},
}
EXPORTS_WITH_SEPARATE_RENDERER = {"pdf", "xlsx"}


def validate_profile(profile: dict, schema: dict) -> list[str]:
    errors = [f"schema at {'.'.join(map(str, e.path)) or '<root>'}: {e.message}"
              for e in Draft202012Validator(schema).iter_errors(profile)]
    if errors:
        return errors
    seen_device_ids = set()
    metric_ids: set[str] = set()
    for device in profile["devices"]:
        dev_id = device["device_id"]
        if dev_id in seen_device_ids:
            errors.append(f"duplicate device_id: {dev_id}")
        seen_device_ids.add(dev_id)
        for metric in device["metrics"]:
            metric_id = metric["metric_id"]
            if metric_id in metric_ids:
                errors.append(f"duplicate metric_id: {metric_id}")
            metric_ids.add(metric_id)
            agg = metric.get("aggregation", "raw_only")
            if agg not in AGGREGATIONS[metric["kind"]]:
                errors.append(f"{metric_id}: {agg} is invalid for kind {metric['kind']}")
            if metric["kind"] == "counter" and agg == "delta_reset_aware" and not metric.get("counter_reset_policy"):
                errors.append(f"{metric_id}: reset policy required for counter energy/quantity deltas")
    report_ids = set()
    for report in profile["reports"]:
        rid = report["report_id"]
        if rid in report_ids:
            errors.append(f"duplicate report_id: {rid}")
        report_ids.add(rid)
        for metric_id in report["metrics"]:
            if metric_id not in metric_ids:
                errors.append(f"{rid}: unknown metric {metric_id}")
        outputs = set(report.get("output", ["screen"]))
        for out in outputs:
            if out not in profile["storage"].get("preferred_export", ["screen"]):
                errors.append(f"{rid}: output {out} absent from storage.preferred_export")
        if profile["storage"]["mode"] == "weintek_native" and outputs & EXPORTS_WITH_SEPARATE_RENDERER:
            errors.append(f"{rid}: native-only route cannot promise XLSX/PDF without external renderer")
        if report.get("availability", "planned") != "planned":
            errors.append(f"{rid}: example not allowed to self-claim verified/accepted status")
    return errors


def validate_all(paths: list[pathlib.Path]) -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    failed = 0
    for path in paths:
        profile = json.loads(path.read_text(encoding="utf-8"))
        errors = validate_profile(profile, schema)
        if errors:
            failed += 1
            print(f"FAIL {path.relative_to(ROOT)}")
            for e in errors:
                print("  - " + e)
        else:
            print(f"PASS {path.relative_to(ROOT)}")
    return failed


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=pathlib.Path)
    args = parser.parse_args()
    sources = args.files if args.files else sorted(EXAMPLES.glob("*.json"))
    if not sources:
        sys.exit("ERROR: no example profiles found")
    sys.exit(1 if validate_all(sources) else 0)

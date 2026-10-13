"""Synthetic reference for UCS kWh report calculations.

THIS IS OFFLINE/QA ONLY, not Weintek Macro/JS nor a native HMI historian adapter.
Rules intentionally fail closed; current sample must explicitly mark rollover/reset.
Do not use as a surrogate for real meter register behavior or energy tariff logic.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

FIXTURES = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "energy_reference_cases.json"


class EnergyFixtureError(ValueError):
    """Invalid or ambiguous metering data."""


def _timestamp(stamp: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    except (ValueError, TypeError, AttributeError) as error:
        raise EnergyFixtureError("INVALID_TIME") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise EnergyFixtureError("MISSING_TIMEZONE")
    return parsed.astimezone(timezone.utc)


def _reading(point: dict) -> Decimal | None:
    if point.get("quality") != "GOOD":
        return None
    value = point.get("value")
    if value is None or isinstance(value, bool):
        raise EnergyFixtureError("INVALID_GOOD_VALUE")
    try:
        numeric = Decimal(str(value))
    except Exception as error:
        raise EnergyFixtureError("INVALID_NUMERIC_VALUE") from error
    if not numeric.is_finite():
        raise EnergyFixtureError("NONFINITE_VALUE")
    return numeric


def _warn_once(items: list[str], warning: str) -> None:
    if warning not in items:
        items.append(warning)


def calculate_case(case: dict) -> dict:
    samples = case.get("samples", [])
    if len(samples) < 2:
        raise EnergyFixtureError("INSUFFICIENT_SAMPLES")
    mode = case.get("method")
    if mode not in ("power", "counter"):
        raise EnergyFixtureError("UNKNOWN_METHOD")
    maxgap = case.get("max_gap_seconds")
    if maxgap is not None and (isinstance(maxgap, bool) or int(maxgap) <= 0):
        raise EnergyFixtureError("INVALID_MAX_GAP")
    modulus = Decimal(str(case["modulus"])) if "modulus" in case else None
    if modulus is not None and (modulus <= 0 or not modulus.is_finite()):
        raise EnergyFixtureError("INVALID_MODULUS")
    result = Decimal("0")
    covered = 0
    warnings: list[str] = []
    for previous, current in zip(samples, samples[1:]):
        start = _timestamp(previous["at"])
        end = _timestamp(current["at"])
        duration = int((end - start).total_seconds())
        if end <= start or duration <= 0 or end - start != timedelta(seconds=duration):
            raise EnergyFixtureError("NON_MONOTONIC_TIME")
        left, right = _reading(previous), _reading(current)
        if left is None or right is None:
            _warn_once(warnings, "BAD_QUALITY_INTERVAL")
            continue

        if mode == "power":
            if maxgap is None:
                raise EnergyFixtureError("POWER_REQUIRES_MAX_GAP")
            if duration > int(maxgap):
                _warn_once(warnings, "POWER_GAP_EXCLUDED")
                continue
            result += (left + right) * Decimal(duration) / Decimal("7200")
            covered += duration
            if left < 0 or right < 0:
                _warn_once(warnings, "SIGNED_DIRECTION_MUST_BE_DECLARED")
            continue

        # Energy register is a cumulative counter, never a sampled kW value.
        if right < left:
            if current.get("reset_before", False):
                _warn_once(warnings, "COUNTER_RESET_INTERVAL_EXCLUDED")
                continue
            if current.get("rollover_before", False) and modulus is not None and 0 <= left < modulus and 0 <= right < modulus:
                delta = modulus - left + right
                _warn_once(warnings, "COUNTER_ROLLOVER")
            else:
                raise EnergyFixtureError("UNEXPLAINED_COUNTER_DROP")
        else:
            if current.get("reset_before") or current.get("rollover_before"):
                raise EnergyFixtureError("INCONSISTENT_COUNTER_EVENT")
            delta = right - left
        if delta < 0:
            raise EnergyFixtureError("NEGATIVE_DELTA")
        result += delta
        covered += duration
        # A valid monotonic end counter can recover aggregate energy over a
        # communications gap, but NOT trustworthy time-resolved allocation.
        if maxgap is not None and duration > int(maxgap):
            _warn_once(warnings, "COUNTER_INTERVAL_DISTRIBUTION_UNKNOWN")

    return {"kwh": result, "covered_seconds": covered, "warnings": warnings}


def all_reference_cases() -> list[dict]:
    with FIXTURES.open(encoding="utf-8") as handle:
        return json.load(handle, parse_float=Decimal)["cases"]


if __name__ == "__main__":
    import sys
    failed = False
    for example in all_reference_cases():
        try:
            result = calculate_case(example)
            if "expected_error" in example or result["kwh"] != Decimal(example["expected_kwh"]) or result["covered_seconds"] != example["covered_seconds"] or result["warnings"] != example["warnings"]:
                print("FAIL:", example["id"], result)
                failed = True
            else:
                print("PASS:", example["id"])
        except EnergyFixtureError as error:
            if str(error) == example.get("expected_error"):
                print("PASS:", example["id"], "(expected rejection)")
            else:
                print("FAIL:", example["id"], str(error))
                failed = True
    sys.exit(1 if failed else 0)

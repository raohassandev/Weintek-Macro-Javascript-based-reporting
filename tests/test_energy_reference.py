"""12 synthetic expected-vs-observed energy examples + negative guards; not HMI evidence."""
from decimal import Decimal
import pathlib
import sys
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from energy_reference import EnergyFixtureError, all_reference_cases, calculate_case  # noqa: E402


class EnergyReferenceCases(unittest.TestCase):
    def test_all_expected_counter_power_outputs(self):
        cases=all_reference_cases()
        self.assertEqual(len(cases),12)
        seen=set()
        for case in cases:
            with self.subTest(fixture=case["id"]):
                self.assertNotIn(case["id"],seen)
                seen.add(case["id"])
                if "expected_error" in case:
                    with self.assertRaisesRegex(EnergyFixtureError,case["expected_error"]):
                        calculate_case(case)
                else:
                    result=calculate_case(case)
                    self.assertEqual(result["kwh"],Decimal(case["expected_kwh"]))
                    self.assertEqual(result["covered_seconds"],case["covered_seconds"])
                    self.assertEqual(result["warnings"],case["warnings"])

    def test_unknown_method_fail_closed(self):
        bad=dict(all_reference_cases()[0])
        bad["method"]="unknown"
        with self.assertRaisesRegex(EnergyFixtureError,"UNKNOWN_METHOD"):
            calculate_case(bad)

    def test_unannotated_rollover_never_inferred(self):
        case=dict(all_reference_cases()[2])
        case["samples"]=[dict(p) for p in case["samples"]]
        case["samples"][-1].pop("rollover_before")
        with self.assertRaisesRegex(EnergyFixtureError,"UNEXPLAINED_COUNTER_DROP"):
            calculate_case(case)

    def test_no_good_value_from_null(self):
        case=dict(all_reference_cases()[0])
        case["samples"]=[dict(p) for p in case["samples"]]
        case["samples"][1]["value"]=None
        with self.assertRaisesRegex(EnergyFixtureError,"INVALID_GOOD_VALUE"):
            calculate_case(case)

    def test_timezone_required(self):
        case=dict(all_reference_cases()[0])
        case["samples"]=[dict(p) for p in case["samples"]]
        case["samples"][1]["at"]="2026-10-10T01:00:00"
        with self.assertRaisesRegex(EnergyFixtureError,"MISSING_TIMEZONE"):
            calculate_case(case)


if __name__=="__main__":
    unittest.main()

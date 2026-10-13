"""Offline validation tests only: not device acceptance."""
import copy
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_site_profiles import validate_profile  # noqa: E402


class ProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "schemas/site-profile.schema.json").read_text())
        cls.profile = json.loads((ROOT / "examples/site-profiles/solar-grid-dg.json").read_text())

    def test_positive_sample(self):
        self.assertEqual(validate_profile(self.profile, self.schema), [])

    def test_unresolved_report_metric(self):
        value = copy.deepcopy(self.profile)
        value["reports"][0]["metrics"].append("unknown_point")
        self.assertTrue(any("unknown metric" in x for x in validate_profile(value, self.schema)))

    def test_counter_must_not_use_avg(self):
        value = copy.deepcopy(self.profile)
        value["devices"][0]["metrics"][1]["aggregation"] = "avg_min_max"
        self.assertTrue(any("invalid for kind" in x for x in validate_profile(value, self.schema)))

    def test_weintek_only_rejects_unverified_pdf(self):
        value = copy.deepcopy(self.profile)
        value["reports"][1]["output"] = ["screen", "pdf"]
        value["storage"]["preferred_export"].append("pdf")
        self.assertTrue(any("unproven on Weintek-only" in x for x in validate_profile(value, self.schema)))

    def test_duplicate_metric_id(self):
        value = copy.deepcopy(self.profile)
        value["devices"][1]["metrics"][0]["metric_id"] = "grid_power_kw"
        self.assertTrue(any("duplicate metric" in x for x in validate_profile(value, self.schema)))


if __name__ == "__main__":
    unittest.main()

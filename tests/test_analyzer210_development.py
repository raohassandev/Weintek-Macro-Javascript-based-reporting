"""Analyzer 210 documentation/offline field-contract tests. Not EBPro/device tests."""
import csv
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"development/screens/analyzer-detail-210"

class Analyzer210Development(unittest.TestCase):
    def test_separate_navigation(self):
        self.assertTrue((ROOT/"planning-context-rnd/INDEX.md").exists())
        self.assertTrue((ROOT/"development/README.md").exists())
        s=(SRC/"README.md").read_text()
        self.assertIn("61",s)
        self.assertIn("OFFLINE",s)
    def test_lw_bounds(self):
        with (SRC/"tags/normalized_lw_61_meter_manifest.csv").open(newline="") as f:r=list(csv.DictReader(f))
        self.assertEqual(len(r),2928)
        self.assertEqual(len({a["MeterSlot"] for a in r}),61)
        self.assertEqual(int(r[0]["StartAddress"]),256)
        self.assertLess(max(int(a["EndAddress"]) for a in r),9000)
        self.assertEqual(int(r[-1]["EndAddress"]),256+60*128+93)
    def test_no_sql_or_device_proof_fabrication(self):
        m=json.loads((SRC/"tags/manifest.json").read_text())
        self.assertIn("BLOCKED",m["sql_local_advanced"])
        self.assertIn("BLOCKED",m["usb_persist"])
        self.assertEqual(m["target"],"cMT-FHDX-220")
        guide=(SRC/"docs/EBPRO_OBJECT_BY_OBJECT.md").read_text()
        self.assertIn("not",guide.lower())
        self.assertIn("Picture",guide)
        self.assertIn("Numeric Display",guide)
    def test_background_source_no_fake_readings(self):
        back=(SRC/"assets/background-only.svg").read_text()
        preview=(SRC/"assets/preview.svg").read_text()
        self.assertIn('width="1920"',back)
        self.assertIn('height="1080"',back)
        self.assertIn("UCS",back)
        self.assertNotIn("ILLUSTRATIVE TREND",back)
        self.assertIn("ILLUSTRATIVE TREND",preview)
    def test_screen_tag_count(self):
        with (SRC/"tags/screen_tag_contract.csv").open(newline="") as f:
            rows=list(csv.DictReader(f))
        self.assertGreaterEqual(len(rows),56)
        self.assertTrue(all(r["Evidence"] in ("NOT_RUN","BLOCKED_Q02","BLOCKED_Q10","OFFLINE") or "NOT" in r["Evidence"] for r in rows))
if __name__=="__main__":unittest.main()

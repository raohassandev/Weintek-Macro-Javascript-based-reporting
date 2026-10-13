"""Original UCS Analyzer 210 artifact contract; OFFLINE only."""
from pathlib import Path
import csv
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"development/screens/analyzer-detail-210"
class OriginalAnalyzerPack(unittest.TestCase):
    def test_108_native_candidate_objects(self):
        with (BASE/"tags/original_ebpro_object_schedule.csv").open(newline="",encoding="utf-8") as fh:
            rows=list(csv.DictReader(fh))
        self.assertEqual(len(rows),108)
        for item in rows:
            self.assertTrue(0<=int(item["OrigX"])<1672)
            self.assertTrue(0<=int(item["OrigY"])<941)
            self.assertTrue(0<=int(item["X1920"])<1920)
            self.assertTrue(0<=int(item["Y1080"])<1080)
            self.assertTrue(item["EBProObjectCandidate"])
            self.assertTrue(item["Evidence"])
    def test_61_meter_48_field_manifest(self):
        with (BASE/"tags/PROPOSED_normalized_lw_61_meter_manifest.csv").open(newline="",encoding="utf-8") as fh:
            rows=list(csv.DictReader(fh))
        self.assertEqual(len(rows),61*48)
        self.assertEqual(int(rows[0]["StartWord"]),256)
        self.assertLess(max(int(r["EndWord"]) for r in rows),9000)
        self.assertEqual(len({r["MeterSlot"] for r in rows}),61)
        self.assertTrue(all(r["Status"]=="PROPOSED_NOT_EBPRO_IMPORT" for r in rows))
    def test_approved_source_guard(self):
        s=(BASE/"APPROVED_ORIGINAL_SOURCE.md").read_text()
        builder=(ROOT/"tools/build_approved_analyzer_assets.py").read_text()
        for sha in ("49d8ebdc07fd5e7c1ee8553be17f4e74bf3dac1c8b63d785238a5834a67c4f69",
                    "7b4b7a5cc7b7e1d341c56a5393e87cd16ea5035bc7ff40c1f883ecb48a89fdac"):
            self.assertIn(sha,s)
            self.assertIn(sha,builder)
        self.assertIn("Image.Resampling.LANCZOS",builder)
    def test_source_and_ebpro_evidence_boundaries(self):
        user=(BASE/"docs/EBPRO_OBJECT_BY_OBJECT.md").read_text()
        self.assertIn("NOT",user)
        self.assertIn("SQL Query",user)
        self.assertIn("Event",user)
        self.assertIn("one",user.lower())
        self.assertIn("PROPOSED_NOT_EBPRO_IMPORT",(BASE/"tags/PROPOSED_normalized_lw_61_meter_manifest.csv").read_text()[:300])
if __name__=="__main__":
    unittest.main()

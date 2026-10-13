"""UCS asset-packs: offline file-integrity & native-HMI handoff lint only."""
from __future__ import annotations
import csv
import json
from pathlib import Path
import struct
import unittest
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
SCREEN_ROOT=ROOT/"designs"/"screens"
SCREENS={"110-operator-home","120-engineer-home","130-management-home","510-resource-manager"}
FILES={"preview.png","background-only.png","preview.svg","background-only.svg",
       "object-map.csv","tag-contract.csv","interaction-flow.md","state-table.md","tests.md"}

class UCSScreenPacks(unittest.TestCase):
    def test_required_1920_1080_png_and_sources(self):
        for name in sorted(SCREENS):
            with self.subTest(screen=name):
                d=SCREEN_ROOT/name
                self.assertTrue(d.is_dir(),name)
                self.assertTrue(FILES.issubset({p.name for p in d.iterdir()}))
                for image in ("preview.png","background-only.png"):
                    raw=(d/image).read_bytes()
                    self.assertGreater(len(raw),10000,image)
                    self.assertEqual(raw[:8],b"\x89PNG\r\n\x1a\n")
                    self.assertEqual(struct.unpack(">II",raw[16:24]),(1920,1080))
                for vector in ("preview.svg","background-only.svg"):
                    e=ET.parse(d/vector).getroot()
                    self.assertEqual(e.attrib["width"],"1920")
                    self.assertEqual(e.attrib["height"],"1080")
                    self.assertEqual(e.attrib["viewBox"],"0 0 1920 1080")
    def test_live_data_not_baked_into_background(self):
        for name in SCREENS:
            with self.subTest(name=name):
                a=(SCREEN_ROOT/name/"background-only.svg").read_text()
                self.assertIn("STATIC BACKGROUND",a)
                self.assertNotIn("CONCEPT • NOT LIVE",a)
                self.assertNotIn("ILLUSTRATIVE / NOT LIVE",a)
                self.assertNotIn("DEMO",a)
                self.assertNotIn("— kWh",a)
                self.assertNotIn("— kW",a)
                self.assertNotIn("SD CARD",a)
                self.assertNotIn("PDF EXPORT",a)
                p=(SCREEN_ROOT/name/"preview.svg").read_text()
                self.assertIn("CONCEPT • NOT LIVE",p)
                for color in ("#F6F6F2","#FFFFFF","#244D3C","#27332D"):
                    self.assertIn(color,p)
    def test_screen_native_object_and_role_distinctions(self):
        for name in SCREENS:
            with (SCREEN_ROOT/name/"object-map.csv").open(newline="",encoding="utf-8") as fh:
                rows=list(csv.DictReader(fh))
            self.assertGreaterEqual(len(rows),7)
            native="\n".join(row["EBPro_Object"] for row in rows)
            for s in ("Numeric Display","Word Lamp","Picture","Function Key"):
                self.assertIn(s,native)
            self.assertFalse(any("HTML" in row["EBPro_Object"] for row in rows))
            with (SCREEN_ROOT/name/"tag-contract.csv").open(newline="",encoding="utf-8") as fh:
                tags=list(csv.DictReader(fh))
            self.assertGreaterEqual(len(tags),8)
            for row in tags:
                self.assertTrue(row["Tag_Name"])
                self.assertTrue(row["EBPro_Import_Status"])
                self.assertNotIn("ALREADY VERIFIED",row["EBPro_Import_Status"])
            self.assertIn("NOT RUN",(SCREEN_ROOT/name/"tests.md").read_text())
            self.assertIn("OFFLINE",(SCREEN_ROOT/name/"interaction-flow.md").read_text())
    def test_golden_kwh_reference_already_merged(self):
        j=json.loads((ROOT/"tests/fixtures/energy_reference_cases.json").read_text())
        self.assertEqual(len(j["cases"]),12)
        self.assertTrue((ROOT/"scripts/energy_reference.py").is_file())
        self.assertTrue((ROOT/"tests/test_energy_reference.py").is_file())
    def test_pilot_exact_allocations_and_no_magic_modbus(self):
        base=ROOT/"planning/2-meter-fhdx220"
        manifest=json.loads((base/"register-allocation.json").read_text())
        canonical=json.loads((ROOT/"contracts/meter-memory-map.json").read_text())
        self.assertEqual(manifest["target_model"],"cMT-FHDX-220")
        self.assertEqual(manifest["shared_LW_blocks"],
                         [{"meter":1,"base":256,"last":383},{"meter":2,"base":384,"last":511}])
        fields=canonical["fields"]
        self.assertEqual(len(manifest["variables"]),len(fields)*2)
        for row in manifest["variables"]:
            field=next(x for x in fields if x["id"]==row["field"])
            expected=256+(row["meter_id"]-1)*128+field["offset_words"]
            self.assertEqual(row["lw_start"],expected)
            self.assertEqual(row["lw_end"],expected+field["words"]-1)
        self.assertIn("NOT_DEFINED",manifest["raw_meter_driver_addresses"])
        for filename in ("SQL_QUERY_TEST_PLAN.md","USB_STORAGE_TEST_PLAN.md",
                         "ACCEPTANCE_CHECKLIST.md","EVIDENCE_TEMPLATE.md","BUILD_HANDOFF.md"):
            self.assertTrue((base/filename).exists())
            data=(base/filename).read_text()
            self.assertTrue("NOT_RUN" in data or "NOT RUN" in data or "not executed" in data.lower() or "NOT AUTHORIZED" in data)
    def test_scope_no_implementation_or_sd(self):
        brief=(ROOT/"docs/SCREEN_DESIGN_BRIEF_FHDX220.md").read_text()
        self.assertIn("1920×1080",brief)
        self.assertIn("NO SD",brief)
        self.assertIn("no compiled",brief.lower())
if __name__=="__main__":
    unittest.main()

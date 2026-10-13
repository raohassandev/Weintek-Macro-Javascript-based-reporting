"""Weintek FHDX-220 model-specific target contract; offline checks only."""
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]

class FHDX220TargetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t=json.loads((ROOT/"contracts/hardware-target.json").read_text())
    def test_owner_selected_exact_model(self):
        self.assertEqual(self.t["target_model"],"cMT-FHDX-220")
        self.assertEqual(self.t["target_status"],"OWNER_SELECTED_NOT_DEVICE_VERIFIED")
    def test_no_sd_or_microsd_or_external_computer(self):
        s=self.t["specification"]
        self.assertFalse(s["sd_card_slot"])
        self.assertFalse(s["microsd_slot"])
        self.assertEqual(s["usb_host_count"],1)
        self.assertEqual(self.t["runtime_scope"],"WEINTEK_ONLY")
    def test_realistic_hmi_canvas_and_supported_objects(self):
        self.assertEqual(self.t["specification"]["recommended_resolution"],[1920,1080])
        self.assertEqual(self.t["software_matrix_v61001"]["js_object"],"DOCUMENTED_Y")
        self.assertEqual(self.t["software_matrix_v61001"]["sql_query"],"DOCUMENTED_Y")
        self.assertIn("NOT_220",self.t["software_matrix_v61001"]["plc_web_browser"])
    def test_no_device_proof_claimed(self):
        self.assertIn("physical_device_present",self.t["unverified"])
        self.assertIn("native_SQLite_Advanced_mode_custom_SQL",self.t["unverified"])
        self.assertIn("USB_historian_61_meter_capacity",self.t["unverified"])
    def test_source_asset(self):
        source=(ROOT/"docs/HARDWARE_TARGET_FHDX_220.md").read_text()
        self.assertIn("NO SLOT",source)
        self.assertIn("1920×1080",source)
        self.assertIn("not yet supplied",source)
if __name__=="__main__":
    unittest.main()

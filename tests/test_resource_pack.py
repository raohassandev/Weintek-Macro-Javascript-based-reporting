"""Offline UCS Resource Manager engineering asset lint (NOT EBPro hardware proof)."""
import csv
import pathlib
import unittest
import xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parents[1]
ASSETS=ROOT/"designs/resource-manager"

class ResourceAssetTests(unittest.TestCase):
    def test_both_svg_assets_are_valid(self):
        for name in ("resource-manager-light.svg","resource-manager-background-only.svg"):
            with self.subTest(asset=name):
                root=ET.parse(ASSETS/name).getroot()
                self.assertEqual(root.attrib["width"],"1600")
                self.assertEqual(root.attrib["height"],"900")

    def test_background_has_no_dynamic_fake_data(self):
        raw=(ASSETS/"resource-manager-background-only.svg").read_text()
        self.assertNotIn("59 / 61",raw)
        self.assertNotIn(">N/A<",raw)
        self.assertNotIn("Connected",raw)
        self.assertIn("BACKUP STATUS",raw)

    def test_tag_dictionary_is_unique_and_respects_reserved_user_region(self):
        with (ROOT/"tags/resource-manager-dictionary.csv").open(newline="") as fh:
            rows=list(csv.DictReader(fh))
        keys=[row["Name"] for row in rows]
        self.assertEqual(len(keys),len(set(keys)))
        byname={row["Name"]:row for row in rows}
        self.assertEqual(byname["UCS_USB_PRESENT"]["Address"],"12048")
        self.assertEqual(byname["UCS_USB_FREE_KB"]["Data_Type"],"UINT32")
        self.assertEqual(byname["UCS_USB_PROBE_STATE"]["Address"],"8250")
        reserved=set()
        for row in rows:
            if row["Address_Type"]=="LW" and row["Access"]=="RW":
                address=int(row["Address"])
                self.assertGreaterEqual(address,8064)
                self.assertLess(address,9000)
                self.assertNotIn(address,reserved)
                reserved.add(address)

    def test_screen_uses_actual_native_object_categories(self):
        with (ASSETS/"screen-object-map.csv").open(newline="") as fh:
            rows=list(csv.DictReader(fh))
        self.assertGreaterEqual(len(rows),14)
        joined=" ".join(r["EBPro_Object"] for r in rows)
        for obj in ("Bar Graph","Word Lamp","Numeric Display","Backup (Global)","Event Display"):
            self.assertIn(obj,joined)

    def test_probe_is_fail_closed_and_non_destructive(self):
        code=(ROOT/"js/ucs_usb_write_read_probe.js").read_text()
        for operation in ('fopen(target, path, "w")','fread(reader, buffer)','data.byteLength','verified ? 2 : 1','fs.remove(target, path)'):
            self.assertIn(operation,code)
        self.assertNotIn("removeAll(",code)
        self.assertIn("Local HMI",code)

if __name__=="__main__":
    unittest.main()

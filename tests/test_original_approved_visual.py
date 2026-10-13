"""Offline audit of exact-image source provenance, not actual EBPro approval."""
from pathlib import Path
import csv,hashlib,unittest
ROOT=Path(__file__).resolve().parents[1]
class OriginalScreenContract(unittest.TestCase):
 def test_source_digests_and_misleading_pr_rejection(self):
  t=(ROOT/"development/screens/analyzer-detail-210/APPROVED_ORIGINAL_SOURCE.md").read_text()
  self.assertIn("49d8ebdc07fd5e7c1ee8553be17f4e74bf3dac1c8b63d785238a5834a67c4f69",t)
  self.assertIn("7b4b7a5cc7b7e1d341c56a5393e87cd16ea5035bc7ff40c1f883ecb48a89fdac",t)
  self.assertIn("NOT YET PRESENT",t)
 def test_12_original_region_boxes_are_within_image(self):
  with (ROOT/"development/screens/analyzer-detail-210/approved-source-region-map.csv").open(newline="") as f:
   r=list(csv.DictReader(f))
  self.assertEqual(len(r),12)
  for x in r:
   xx,yy,w,h=(int(x[k]) for k in ("Original_X","Original_Y","Original_W","Original_H"))
   self.assertTrue(0<=xx<1672 and 0<=yy<941 and xx+w<=1672 and yy+h<=941)
 def test_originals_when_present_have_expected_hash(self):
  folder=ROOT/"development/screens/analyzer-detail-210/assets"
  expected={"APPROVED_ORIGINAL_METER_DETAIL.png":"49d8ebdc07fd5e7c1ee8553be17f4e74bf3dac1c8b63d785238a5834a67c4f69","APPROVED_ORIGINAL_COMPONENT_LIBRARY.png":"7b4b7a5cc7b7e1d341c56a5393e87cd16ea5035bc7ff40c1f883ecb48a89fdac"}
  for name,digest in expected.items():
   p=folder/name
   if p.exists():self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),digest)
if __name__=="__main__":unittest.main()

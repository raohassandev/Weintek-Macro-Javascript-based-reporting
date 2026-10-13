#!/usr/bin/env python3
"""Import precisely the recovered original image pair into this repository.
Does NOT redraw/reinterpret the approved visuals; raises on source mismatch.
Run only where these files and a Git checkout are available.
"""
from pathlib import Path
import hashlib, shutil, sys
DEST=Path(__file__).resolve().parents[1]/"development/screens/analyzer-detail-210/assets"
SOURCES={
 "futuristic_meter_monitoring_dashboard_template.png":("APPROVED_ORIGINAL_METER_DETAIL.png","49d8ebdc07fd5e7c1ee8553be17f4e74bf3dac1c8b63d785238a5834a67c4f69"),
 "industrial_scada_hmi_component_library.png":("APPROVED_ORIGINAL_COMPONENT_LIBRARY.png","7b4b7a5cc7b7e1d341c56a5393e87cd16ea5035bc7ff40c1f883ecb48a89fdac")
}
def run(source_dir):
 DEST.mkdir(parents=True,exist_ok=True)
 for source,(target,digest) in SOURCES.items():
  s=Path(source_dir)/source
  data=s.read_bytes()
  if hashlib.sha256(data).hexdigest()!=digest:raise ValueError("Wrong original binary: "+source)
  (DEST/target).write_bytes(data)
 print("EXACT APPROVED ORIGINALS IMPORTED, NOT A NEW DESIGN")
if __name__=="__main__":
 if len(sys.argv)!=2:raise SystemExit("Usage: python tools/import_approved_ucs_images.py /path/to/ORIGINALS")
 run(sys.argv[1])

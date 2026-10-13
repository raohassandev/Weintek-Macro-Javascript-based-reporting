#!/usr/bin/env python3
"""Source-faithful PNG asset builder for approved UCS Analyzer Detail 210.

REQUIRES BOTH EXACT approved original PNG inputs already present in local folder.
Not a new design, not an EBPro project, not permission to claim DEVICE-PASS.
"""
from __future__ import annotations
from PIL import Image, ImageDraw
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"development/screens/analyzer-detail-210/assets"
EXPECTED={
    "APPROVED_ORIGINAL_METER_DETAIL.png":"49d8ebdc07fd5e7c1ee8553be17f4e74bf3dac1c8b63d785238a5834a67c4f69",
    "APPROVED_ORIGINAL_COMPONENT_LIBRARY.png":"7b4b7a5cc7b7e1d341c56a5393e87cd16ea5035bc7ff40c1f883ecb48a89fdac"
}
for filename,sha in EXPECTED.items():
    p=SRC/filename
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha:
        raise SystemExit("BLOCKED: wrong/missing exact original "+filename)

original=Image.open(SRC/"APPROVED_ORIGINAL_METER_DETAIL.png").convert("RGB")
assert original.size==(1672,941)
static=original.copy()
draw=ImageDraw.Draw(static)
edits=[]
def clear(name,rect,fill):
    draw.rounded_rectangle(rect,radius=min(6,(rect[3]-rect[1])//3),fill=fill)
    edits.append(dict(object=name,box=list(rect),status="STATIC_NEUTRAL_UNTIL_NATIVE_OBJECT"))
clear("meter-status-circle",(25,366,61,400),"#004F50")
clear("meter-status-field",(73,361,203,392),"#00525A")
for i in range(4):
    clear("current-bar-"+str(i),(620+84*i,204,692+84*i,223),"#C5DBE3")
for i in range(3):
    clear("phase-load-"+str(i),(1425,251+22*i,1558,271+22*i),"#C8DFE6")
for i in range(6):
    y=364+27*i
    clear("insight-left-indicator-"+str(i),(1042,y,1067,y+20),"#C9DBDA")
    clear("insight-left-bar-"+str(i),(1068,y+3,1168,y+19),"#C8DFE6")
    clear("insight-right-indicator-"+str(i),(1442,y,1466,y+20),"#C9DBDA")
    clear("insight-right-bar-"+str(i),(1469,y+3,1558,y+19),"#C8DFE6")
clear("live-flag",(939,540,1019,567),"#CCF3E1")
static.save(SRC/"background-only-original-size.png",optimize=True)
static.resize((1920,1080),Image.Resampling.LANCZOS).save(SRC/"background-only-1920x1080.png",optimize=True)
original.resize((1920,1080),Image.Resampling.LANCZOS).save(SRC/"approved-preview-1920x1080.png",optimize=True)

regions=[
("header",(0,0,1672,73)),("selected-analyzer-sidebar",(0,75,225,940)),
("phase-voltage",(231,76,605,318)),("phase-current",(610,77,974,317)),
("phase-power",(978,77,1377,319)),("frequency-demand-loading",(1380,77,1664,319)),
("power-quality",(234,320,860,534)),("computed-maintenance",(865,320,1666,535)),
("24h-trend",(235,536,1063,740)),("7d-energy-comparison",(1068,536,1665,740)),
("historical-snapshot",(235,741,1188,931)),("recent-alarms",(1195,741,1665,931))]
out=SRC/"components";out.mkdir(exist_ok=True)
for name,box in regions:
    original.crop(box).save(out/(name+".png"),optimize=True)
    static.crop(box).save(out/(name+"-background.png"),optimize=True)
(SRC/"background-edit-manifest.json").write_text(json.dumps({
    "source_hashes":EXPECTED,"evidence":"OFFLINE_PIL_REBUILD_NOT_EBPRO",
    "display":[1920,1080],"cleared_dynamic_gauges":edits,
    "sql_advanced_local":"BLOCKED","weintek_macro_compile":"NOT_RUN"
},indent=2)+"\n",encoding="utf-8")
print("PASS: approved-source, 1920×1080 preview, clean background and 24 exact source crops (OFFLINE)")

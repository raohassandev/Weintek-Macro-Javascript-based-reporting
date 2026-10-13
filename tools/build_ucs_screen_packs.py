#!/usr/bin/env python3
"""Deterministic 1920x1080 UCS screen DESIGN assets, not functional EBPro objects.

On-device live values must be native EBPro numeric/lamps/trends over
background-only.png. Preview is illustrative (NEVER production measurements).
Generated packs: window 110, 120, 130 and re-laid-out 510 Resource Manager.
"""
from __future__ import annotations

import argparse
import csv
import html
import io
from pathlib import Path

WIDTH, HEIGHT = 1920, 1080
BG = "#F6F6F2"
WHITE = "#FFFFFF"
FOREST = "#244D3C"
INK = "#27332D"
MUTED = "#68756E"
PALE = "#EAF1E8"
LINE = "#DCE5D9"
AMBER = "#B57C2A"
RED = "#B54F48"
ROOT = Path(__file__).resolve().parents[1]
SCREENS = ROOT / "designs" / "screens"
NAV = ["Operator", "Engineer", "Management", "Meter Detail", "Trends", "Reports", "Diagnostics", "Resources"]
SPECS = {
    "110-operator-home": {
        "title":"OPERATIONS OVERVIEW", "subtitle":"Electrical network / live situational awareness",
        "active":"Operator",
        "kpis":["SITE ACTIVE POWER", "METERS AVAILABLE", "CRITICAL EVENTS", "GRID FREQUENCY"],
        "main":"METER HEALTH / ALL 61 LOGICAL SLOTS",
        "side":"PRIORITY OPERATOR ACTIONS",
        "bottom":"RECENT ALARMS / CIRCUIT ACTIVITY",
        "sample":["— kW", "— / 61", "— active", "— Hz"],
        "tags":[("site_active_kw","Derived site KPI","FLOAT32","GOOD+timestamp"),
                ("meters_online","Quality ledger","UINT16","event ages"),
                ("critical_events","Alarm/event ledger","UINT16","severity/UAC"),
                ("grid_frequency_hz","Site source tag","FLOAT32","GOOD+timestamp"),
                ("meter_tile_quality","Normalized meter blocks 256..8063","ENUM","snapshot age"),
                ("alarms_operator","Event Display role filter","EVENT","persistent incident")],
        "actions":["Meter tile selects PLW-100 for THIS client; supported Private Index computed only after bounds check.",
                   "Operator action opens common detail 210; no change to background logging.",
                   "Critical event opens role-allowed popup 900 and persists before display.",
                   "Operator acknowledges only permitted events; cannot restore/commission."]
    },
    "120-engineer-home": {
        "title":"ENGINEERING DIAGNOSTICS", "subtitle":"Communications / reliability / maintenance",
        "active":"Engineer",
        "kpis":["COMMUNICATIONS HEALTH", "STALE ANALYZERS", "MODBUS FAILURES", "LAST GOOD POLL"],
        "main":"61 ANALYZERS / COMMUNICATION HEALTH MATRIX",
        "side":"FAILURE INVESTIGATION",
        "bottom":"INCIDENT TIMELINE / MAINTENANCE QUEUE",
        "sample":["— valid", "— stale", "— errors", "— age"],
        "tags":[("comm_ok_count","Poll quality ledger","UINT16","actual attempts"),
                ("meters_stale","Quality age checks","UINT16","bounded TTL"),
                ("modbus_failures","Read exception counters","UINT32","per-source"),
                ("last_good_age","Last valid receive time","UINT32","UTC"),
                ("device_health_matrix","Normalized quality mapping","ENUM","per meter"),
                ("incident_log","Event Display","EVENT","persisted evidence")],
        "actions":["Select analyzer from matrix to open the same common detail 210.",
                   "Technical diagnose button opens role-protected Diagnostics 410.",
                   "Commissioning requires Engineer/Manufacturer permissions, independent action check and logged change.",
                   "No device write through read-only report/navigator actions."]
    },
    "130-management-home": {
        "title":"ENERGY & EXECUTIVE REPORTING", "subtitle":"Verified energy performance / coverage / report preparation",
        "active":"Management",
        "kpis":["NET ENERGY", "GRID IMPORT", "MAXIMUM DEMAND", "RECORD COVERAGE"],
        "main":"ENERGY PERFORMANCE / SELECTED PERIOD",
        "side":"COMPARISON & REPORT QUALITY",
        "bottom":"REPORT PREVIEW / VERIFIED EXPORT / MATERIAL EXCEPTIONS",
        "sample":["— kWh", "— kWh", "— kW", "— %"],
        "tags":[("net_energy_kwh","Historian report engine","FLOAT64","source+coverage"),
                ("grid_import_kwh","Counter delta/report","FLOAT64","gap-aware"),
                ("demand_peak_kw","Verified sample/report","FLOAT32","quality+time"),
                ("period_coverage_pct","Expected-vs-valid log ledger","FLOAT32","quality provenance"),
                ("trend_history","Proven native Trend/History query","HISTORY","persisted samples only"),
                ("report_export_csv","Weintek-native backup/export object","ACTION","DEVICE-PASS required")],
        "actions":["Date selector changes only manager's private report request; never historian capture state.",
                   "Preview uses bounded request ID and shows NO DATA/PARTIAL on stale or incomplete results.",
                   "CSV action remains unavailable until actual FHDX-220 on-device file proof.",
                   "Missing PDF generator must NOT create a PDF button; business-impacting exceptions route to Alarm Centre."]
    },
    "510-resource-manager": {
        "title":"RESOURCE & STORAGE MANAGEMENT", "subtitle":"Device capacity / logging assurance / backups (occasional use)",
        "active":"Resources",
        "kpis":["USB CONNECTION", "WRITE / READ PROOF", "HISTORY PERSISTENCE", "BACKUP VERIFICATION"],
        "main":"INTERNAL FLASH & USB1 CAPACITY",
        "side":"RETENTION / BACKUP ASSURANCE",
        "bottom":"RECORDER INCIDENTS / PROOF AGE / RECOVERY",
        "sample":["—", "NOT TESTED", "UNVERIFIED", "—"],
        "tags":[("usb1_present","Weintek system tag LB-12048 candidate","BIT","vendor version check"),
                ("usb_probe_state","Application LW-8250 candidate","UINT16","recent byte-compare"),
                ("recorder_state","Application LW-8252 candidate","UINT16","last persisted record"),
                ("backup_proof_state","Native Backup object + independent evidence","ENUM","verification age"),
                ("cpu_load_pct","Weintek LW-9025 candidate","UINT16","exact OS/system tag check"),
                ("ram_load_pct","Weintek LW-11159 candidate","UINT16","exact model tag"),
                ("usb_free_kb","Weintek LW-9076 candidate","UINT32","USB1 only"),
                ("retention_days","Measured data bytes/day formula","UINT32","N/A if no trend")],
        "actions":["Display three separate statuses: connected, actually writable, historian persisting.",
                   "USB probe is Admin/Engineer on-demand only, not on every screen repaint.",
                   "Backup requires explicit role permission, storage preflight and native file recovery evidence.",
                   "No SD slot, no SD cards/gauges, no unverified SSD SMART data."]
    }
}

def esc(s: object) -> str:
    return html.escape(str(s), quote=True)

def rect(x,y,w,h,fill=WHITE,r=14,stroke=LINE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'

def label(x,y,value,size=20,weight=400,color=INK,anchor="start",opacity=1.0):
    return (f'<text x="{x}" y="{y}" font-family="Arial,DejaVu Sans,sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}" opacity="{opacity}">{esc(value)}</text>')

def pill(x,y,w,txt,fill=PALE,color=FOREST):
    return rect(x,y,w,32,fill,12,fill)+label(x+w/2,y+22,txt,14,700,color,"middle")

def card(x,y,w,h,title):
    return rect(x,y,w,h)+label(x+22,y+35,title,15,700,MUTED)

def draw_grid(preview,mode):
    # 61 DISTINCT logical slots; indicators here are decorative DEMO placeholders only.
    out=[]
    left,top=261,370
    cw,ch=94,56
    for i in range(61):
        x=left+(i%10)*cw; y=top+(i//10)*ch
        out.append(rect(x,y,cw-9,ch-9,PALE if preview and i%13 not in (0,1) else "#F5F5F1",6,LINE))
        if preview:
            out.append(label(x+12,y+21,f"M-{i+1:02d}",13,700,FOREST))
            status=RED if i%19==0 else AMBER if i%13==0 else FOREST
            out.append(f'<circle cx="{x+cw-25}" cy="{y+17}" r="5" fill="{status}"/>')
            out.append(label(x+11,y+39,"DEMO",10,600,MUTED))
    return "".join(out)

def chart_lines():
    out=[]
    for y in [395,475,555,635,715]:
        out.append(f'<line x1="270" y1="{y}" x2="1206" y2="{y}" stroke="{LINE}" stroke-width="1"/>')
    out.append(f'<path d="M 275 665 C 340 610 395 630 450 570 S 600 440 670 510 S 810 580 880 445 S 1040 500 1205 410" fill="none" stroke="{FOREST}" stroke-width="5" stroke-linecap="round"/>')
    out.append(f'<path d="M 275 705 Q 420 668 545 685 T 815 620 T 1205 590" fill="none" stroke="{AMBER}" stroke-width="3" stroke-dasharray="11 9"/>')
    return "".join(out)

def screen_svg(slug,preview):
    a=SPECS[slug]; out=[
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        f'<title>{esc(a["title"])} - {"illustrative preview" if preview else "background-only EBPro Picture"}</title>',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}"/>',
        f'<rect width="205" height="{HEIGHT}" fill="#EEF2EA"/>',
        rect(205,0,1715,86,WHITE,0,"#FFFFFF"),
        label(30,52,"UCS",37,800,FOREST), label(29,72,"ENERGY INTELLIGENCE",11,700,MUTED),
    ]
    for i,item in enumerate(NAV):
        y=147+i*71
        if item==a["active"]:
            out.append(rect(16,y-33,172,46,PALE,10,PALE))
        out.append(label(34,y,item,19,700 if item==a["active"] else 400,
                         FOREST if item==a["active"] else MUTED))
    out += [label(234,40,a["title"],30,750,INK),
            label(234,67,a["subtitle"],15,450,MUTED),
            pill(1650,22,238,"UCS • DESIGN SOURCE"),
            label(234,118,"PERFORMANCE / STATUS",15,700,MUTED)]
    kx=[234,647,1060,1473]
    for i,title in enumerate(a["kpis"]):
        x=kx[i]
        out.append(card(x,142,399,153,title))
        if preview:
            out.append(label(x+23,222,a["sample"][i],35,750,FOREST))
            out.append(label(x+23,265,"ILLUSTRATIVE / NOT LIVE",11,600,MUTED))
    out += [card(234,314,1016,524,a["main"]),card(1266,314,606,524,a["side"]),
            card(234,855,1638,170,a["bottom"])]
    if preview:
        if slug.startswith("110") or slug.startswith("120"):
            out.append(draw_grid(True,slug))
            out += [pill(1290,395,155,"ALERT REVIEW",fill="#F7F0E5",color=AMBER),
                    label(1290,466,"DEVICE: — / SOURCE: —",21,600,INK),
                    label(1290,506,"Last valid sample: —",18,400,MUTED),
                    label(1290,545,"Root cause: UNCONFIRMED",18,400,MUTED)]
        elif slug.startswith("130"):
            out.append(chart_lines())
            out += [label(1290,431,"PERIOD QUALITY",17,700,FOREST),
                    label(1290,480,"—   Valid intervals",20,500,INK),
                    label(1290,521,"—   Missing intervals",20,500,INK),
                    label(1290,565,"Source coverage required",16,500,MUTED),
                    pill(1290,635,220,"REPORT: UNVERIFIED")]
        else:
            for y,title in [(409,"Internal history quota"),(497,"USB1 free capacity"),(585,"CPU / RAM load"),(673,"Recorder-proof freshness")]:
                out.append(label(265,y,title,20,500,INK))
                out.append(rect(265,y+18,890,23,"#E4E8DF",9,"#E4E8DF"))
                out.append(rect(265,y+18,0,23,FOREST,9,FOREST))
            out += [label(1290,429,"Stored since: —",18,500,INK),
                    label(1290,474,"Most recent: —",18,500,INK),
                    label(1290,520,"Retention: UNVERIFIED",18,500,INK),
                    pill(1290,615,265,"BACKUP NOT VERIFIED",fill="#F7F0E5",color=AMBER)]
        out.append(label(260,932,"ALARM / EVENT HISTORY: device data required • action rights enforced in EBPro",18,500,INK))
        out.append(label(260,980,"Visual layout demo only — not connected to any meter, historian or HMI",16,500,MUTED))
        out.append(pill(1540,920,250,"CONCEPT • NOT LIVE",fill="#F7F0E5",color=AMBER))
    else:
        out.append(label(260,1001,"STATIC BACKGROUND / overlay native Numeric, Lamp, Trend & Event EBPro objects",13,500,MUTED))
    out.append("</svg>")
    return "\n".join(out)+"\n"

def csv_text(rows):
    stream=io.StringIO()
    writer=csv.writer(stream,lineterminator="\n")
    writer.writerows(rows)
    return stream.getvalue()

def docs_for(slug):
    a=SPECS[slug]
    lines=[
        f'# Window {slug} — {a["title"]}',
        "**Evidence:** DOC / OFFLINE-generated visuals only. No compiled EBPro object or device test.",
        "**Hardware:** cMT-FHDX-220, 1920×1080, ONE USB2, NO SD, no PLC Web Browser, no PC runtime.",
        "## Role and action workflow",*["- "+x for x in a["actions"]],
        "## Navigation rule","- Common shell only; role access must be enforced at action/data origin, not cosmetic visibility.",
        "- The window does not schedule or stop any meter polling/history; all 61 log independently.",
        "- Preview PNG contains labeled mockups and is never imported as live values.",
        "- Background-only.png has no data, legends with fake values, colored live-status dots or report success indicators."
    ]
    interaction="\n".join(lines)+"\n"
    states="""# Required states (design-only)\n| State | Trigger | UI rendering | Audit requirement |\n|---|---|---|---|\n| LOADING | New selection/request | Animated native indicator if supported, no previous meter data | Request ID bounds and client-private state |\n| FRESH | Correct source+quality+age within measured TTL | Value with unit and timestamp | Device measurement pending |\n| STALE | Last-good age exceeded TTL or read timeout | Stale badge, last-good time and non-current value | Never render stale as current |\n| OFFLINE | Meter comm loss | Offline with failure interval and unknown root cause | Distinguish network/HMI/meter outage |\n| UNSUPPORTED | Driver capability absent | N/A without fake numeric zero | Site profile capability map |\n| NO_HISTORY | Native logger unavailable/no records | No data/partial coverage warning | Missing interval preserved |\n| STORAGE_FAULT | USB disconnected/writer failing/recorder stale | Role-filtered alarm; report validity reduced | Keep event persisted, never rely on USB-present only |\n| PERMISSION_DENIED | UAC denies operation | Hide privileged action AND block execution | Role action test pending |\n"""
    tests="""# Acceptance checklist: never mark HMI PASS from these design files\n| Level | Check | Current status |\n|---|---|---|\n| DOC | 1920×1080 PNGs; role screen purpose, exact native object map; no SD/browser/PDF button | READY FOR OFFLINE CI |\n| OFFLINE | SVG/PNG syntax, contrast, expected CSV columns, no fake data in background | READY FOR OFFLINE CI |\n| EBPRO | Project window built with actual tagged Numeric/Lamp/Trend/Event objects at target version | NOT RUN — owner hold |\n| SIMULATOR | Stale/offline/UAC, target/source selection, date controls | NOT RUN — owner hold |\n| DEVICE | cMT-FHDX-220 OS+EBPro; live 2 meter values, recorder and user sessions | BLOCKED — firmware & owner approval |\n| SITE | 61 meters + USB single-port/backup/fault and report file evidence | BLOCKED — hardware trial |\n| AUDIT | Separate per-screen usability/completeness and release-role security audit | NOT RUN |\n\nPicture/background is a static design aid; native EBPro objects implement ALL live tags.\n"""
    return {"interaction-flow.md":interaction,"state-table.md":states,"tests.md":tests}

def build(out_dir=SCREENS):
    try:
        import cairosvg
    except ImportError as exc:
        raise SystemExit("Need cairosvg (run pip install cairosvg)") from exc
    total=0
    for slug,sp in SPECS.items():
        folder=out_dir/slug
        folder.mkdir(parents=True,exist_ok=True)
        for variant,preview in (("preview",True),("background-only",False)):
            source=screen_svg(slug,preview)
            (folder/(variant+".svg")).write_text(source,encoding="utf-8")
            cairosvg.svg2png(bytestring=source.encode(),write_to=str(folder/(variant+".png")),
                            output_width=WIDTH,output_height=HEIGHT)
            total+=2
        ob_rows=[["Panel","EBPro_Object","Binding","Tag_or_Action","Data_Type","Provenance","Current_Status"]]
        for k,item in enumerate(sp["kpis"]):
            tag,src,typ,qual=sp["tags"][min(k,len(sp["tags"])-1)]
            ob_rows.append([item,"Numeric Display + Word Lamp",src,tag,typ,qual,"DESIGN/NOT EBPRO VERIFIED"])
        ob_rows+= [
            [sp["main"],"Picture + native Numeric/Bit Lamp / History Trend (where supported)","Quality-tagged logical meter window","meter_indexed_data / historian","MIXED","Private Index UI does NOT index native historian","DESIGN"],
            [sp["side"],"Event Display + Word Lamp or supported JS Object Canvas","HMI Event log / bounded report result","event_status","EVENT","Persistent+UAC gating required","DESIGN"],
            [sp["bottom"],"Event/History Data Display + Function Key","Stored log or report","event_log / report_id","EVENT","History source on-device only","DESIGN"],
            ["Navigation","Function Key + supported client-private PLW","PLW-100 / index PLW-9200","client_selected_meter","UINT16","Verify OS + Viewer session behaviour","DESIGN"],
            ["Backdrop","Picture static PNG","Local project asset","background-only.png","PNG","No dynamic values baked in","OFFLINE"]
        ]
        (folder/"object-map.csv").write_text(csv_text(ob_rows),encoding="utf-8")
        tg=[["Tag_Name","Origin","Proposed_Type","Quality_Requirement","EBPro_Import_Status"]]
        tg += [[name,src,typ,qual,"NOT NATIVE IMPORT CSV; requires EBPro exported template"]
               for name,src,typ,qual in sp["tags"]]
        tg += [["selected_meter_client_private","PLW-100 proposed","UINT16","range 1..61 per client","MODEL/OS TEST REQUIRED"],
               ["private_index0","PLW-9200 Weintek private index register 0","UINT16","(meterId-1)*128","MODEL/OS TEST REQUIRED"]]
        (folder/"tag-contract.csv").write_text(csv_text(tg),encoding="utf-8")
        for name,data in docs_for(slug).items():
            (folder/name).write_text(data,encoding="utf-8")
        total+=5
    print(f"Generated {total} files across {len(SPECS)} window packs at {out_dir}")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=SCREENS)
    args=parser.parse_args()
    build(args.output)

if __name__=="__main__":
    main()

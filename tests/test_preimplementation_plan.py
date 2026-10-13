"""Pre-implementation plan completeness and cross-link guards.

OFFLINE DOC REVIEW ONLY: this does not validate EBPro project, HTML, SQLite,
Modbus, USB or actual Weintek device operation.
"""
import csv
import json
import pathlib
import re
import unittest
from urllib.parse import unquote

ROOT=pathlib.Path(__file__).resolve().parents[1]
REPO_DOCS=[ROOT/"README.md", ROOT/"AGENTS.md"]
REPO_DOCS += sorted((ROOT/"docs").glob("*.md"))
REPO_DOCS += sorted((ROOT/"research").glob("*.md"))
REPO_DOCS += sorted((ROOT/"designs").rglob("*.md"))
REPO_DOCS += sorted((ROOT/"tags").glob("*.md"))
LINK=re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')


class PlanFreezeIntegrity(unittest.TestCase):
    def test_relative_references_resolve_inside_repository(self):
        broken=[]
        for doc in REPO_DOCS:
            for match in LINK.finditer(doc.read_text(encoding="utf-8")):
                raw=match.group(1).strip().split("#",1)[0].split("?",1)[0]
                if not raw or raw.startswith(("http:","https:","mailto:","data:","javascript:","/","#")):
                    continue
                # Normal markdown local links (spaces may be URL encoded).
                name=unquote(raw.strip("<>"))
                target=(doc.parent/name).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    broken.append(f"{doc.relative_to(ROOT)}: {raw}")
        self.assertEqual(broken,[],"Repository local markdown links must all exist")

    def test_fhdx220_model_only_no_sd_browser_fantasy(self):
        hw=json.loads((ROOT/"contracts/hardware-target.json").read_text(encoding="utf-8"))
        self.assertEqual(hw["target_model"],"cMT-FHDX-220")
        self.assertFalse(hw["specification"]["sd_card_slot"])
        self.assertFalse(hw["specification"]["microsd_slot"])
        self.assertEqual(hw["specification"]["usb_host_count"],1)
        self.assertEqual(hw["specification"]["recommended_resolution"],[1920,1080])
        self.assertIn("NOT_220",hw["software_matrix_v61001"]["plc_web_browser"])
        with (ROOT/"tags/resource-manager-dictionary.csv").open(newline="",encoding="utf-8") as f:
            names={row["Name"] for row in csv.DictReader(f)}
        self.assertNotIn("UCS_SD_PRESENT",names)
        self.assertNotIn("UCS_SD_FREE_KB",names)

    def test_meter_map_in_valid_nonoverlapping_61_blocks(self):
        mapfile=json.loads((ROOT/"contracts/meter-memory-map.json").read_text(encoding="utf-8"))
        self.assertIn("PROPOSED",mapfile["status"])
        layout=mapfile["memory"]
        self.assertEqual(layout["device_count"],61)
        self.assertEqual(layout["block_words"],128)
        self.assertEqual(layout["base_word"]+61*128-1,8063)
        self.assertLess(layout["highest_used_address"],layout["system_reserved_from"])
        occupied=set()
        widths={"uint16":1,"uint32":2,"float32":2,"float64":4}
        for f in mapfile["fields"]:
            with self.subTest(field=f["id"]):
                self.assertEqual(f["words"],widths[f["type"]])
                self.assertGreaterEqual(f["offset_words"],0)
                self.assertLessEqual(f["offset_words"]+f["words"],128)
                for offset in range(f["offset_words"],f["offset_words"]+f["words"]):
                    self.assertNotIn(offset,occupied)
                    occupied.add(offset)
        # Application registers must be outside the normalized shared meter bank.
        for addr in mapfile["other_app_registers"].values():
            word=int(addr.removeprefix("LW-"))
            self.assertGreater(word,layout["highest_used_address"])
            self.assertLess(word,layout["system_reserved_from"])

    def test_role_purpose_and_implementation_hold(self):
        brief=(ROOT/"docs/SCREEN_DESIGN_BRIEF_FHDX220.md").read_text()
        for snippet in ("Operator Home","Engineer Home","Management Home","Reusable Meter Detail","1920×1080","NO SD","Native EBPro"):
            self.assertIn(snippet,brief)
        freeze=(ROOT/"docs/PLAN_FREEZE_PRE_IMPLEMENTATION_AUDIT.md").read_text()
        for requirement in ("INDEPENDENT","before implementation","single-USB","owner","Advanced","SQL","FHDX-220"):
            self.assertIn(requirement.lower(),freeze.lower())
        agents=(ROOT/"AGENTS.md").read_text()
        self.assertIn("NO IMPLEMENTATION BEFORE INDEPENDENT PLAN AUDIT",agents)

    def test_critical_storage_decision_not_fake_approved(self):
        s=(ROOT/"docs/FHDX220_SINGLE_USB_STORAGE_RISK.md").read_text()
        for content in ("NO SD","ONE USB2","NOT APPROVED","NOT PROVEN","historian","independent backup"):
            self.assertIn(content.lower(),s.lower())


if __name__=="__main__":
    unittest.main()

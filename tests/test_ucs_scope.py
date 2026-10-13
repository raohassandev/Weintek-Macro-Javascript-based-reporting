"""UCS design-level contracts only; not Weintek firmware/EBPro proof."""
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

def read_json(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

class WeintekOnlyPolicyTests(unittest.TestCase):
    def test_runtime_denies_external_pc(self):
        conf=read_json("contracts/ucs-role-ux-policy.json")
        self.assertIs(conf["runtime_scope"]["external_computer_allowed"],False)
        self.assertTrue(all("Weintek" in hw for hw in conf["runtime_scope"]["processing_hardware"]))
        schema=read_json("schemas/site-profile.schema.json")
        self.assertEqual(set(schema["properties"]["storage"]["properties"]["mode"]["enum"]),{"weintek_native","hmi_local_sql_query"})
        for path in (ROOT/"examples/site-profiles").glob("*.json"):
            ex=json.loads(path.read_text(encoding="utf-8"))
            self.assertNotIn(ex["storage"]["mode"],{"external_service","ipc","pc"})
            self.assertFalse(set(ex["storage"].get("preferred_export",[]))&{"pdf","xlsx"})

    def test_all_role_home_and_common_details(self):
        p=read_json("contracts/ucs-role-ux-policy.json")
        self.assertEqual(len({"OPERATOR_HOME","ENGINEER_HOME","MANAGEMENT_HOME"}),3)
        for r in ("operator","engineer","manager"):
            self.assertIn(p["roles"][r]["landing_screen"],p["roles"][r]["can_access"])
            self.assertIn("METER_DETAIL",p["roles"][r]["can_access"])
            self.assertFalse(p["roles"][r]["can_restore"])
        self.assertNotIn("COMMISSIONING",p["roles"]["manager"]["can_access"])

    def test_routed_incidents_always_persist(self):
        conf=read_json("contracts/ucs-role-ux-policy.json")["notification_policy"]
        self.assertTrue(conf["persist_before_notification"])
        self.assertFalse(conf["default_modal_for_all_events"])
        self.assertTrue(all(event["always_log"] for event in conf["events"]))
        self.assertEqual(len({e["id"] for e in conf["events"]}),len(conf["events"]))

    def test_current_diagram_has_no_pc_path(self):
        for path in ("docs/VISUAL_PLAN.md","docs/ARCHITECTURE.md"):
            raw=(ROOT/path).read_text()
            self.assertNotIn("PC / IPC collection + report service",raw)
            self.assertNotIn("external_service",raw)
            self.assertIn("Weintek",raw)

    def test_html_probe_is_offline_not_meter_simulator(self):
        source=(ROOT/"experiments/html-poc/index.html").read_text()
        self.assertIn("offline visual test",source)
        self.assertNotIn('src="http',source)
        self.assertNotIn("fetch(",source)

    def test_demo_project_research_truthful(self):
        demos=read_json("research/demo-catalog.json")
        self.assertGreaterEqual(len(demos["demos"]),10)
        self.assertTrue(all(not i["downloaded"] and not i["hardware_tested"] for i in demos["demos"]))
        self.assertIn("NOT_OBTAINED",demos["download_status"])

if __name__=="__main__":
    unittest.main()

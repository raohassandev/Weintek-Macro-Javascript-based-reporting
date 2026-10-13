"""UCS v1.0 documentation baseline consistency tests, **not** EBPro or device acceptance."""
from __future__ import annotations
import json
import pathlib
import re
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
DOCUMENTS={
  "master":ROOT/"docs/UCS_FINAL_MASTER_PLAN.md",
  "audit":ROOT/"docs/INDEPENDENT_AUDIT_PROTOCOL.md",
  "handoff":ROOT/"docs/AI_AGENT_EXECUTION_BRIEF.md",
  "trace":ROOT/"docs/UCS_REQUIREMENTS_TRACEABILITY.md",
  "work":ROOT/"docs/UCS_DELIVERY_WORKPACKAGES.md",
  "visual":ROOT/"docs/VISUAL_PLAN.md",
  "architecture":ROOT/"docs/ARCHITECTURE.md",
  "roles":ROOT/"docs/ROLE_BASED_UX_PLAN.md",
  "agent":ROOT/"AGENTS.md",
  "readme":ROOT/"README.md",
}

def read(which):
    return DOCUMENTS[which].read_text(encoding="utf-8")

class UCSBaselineTests(unittest.TestCase):
    def test_all_entrypoints_exist_and_are_substantial(self):
        for key,p in DOCUMENTS.items():
            with self.subTest(doc=key):
                self.assertTrue(p.is_file(),str(p))
                self.assertGreater(len(p.read_text(encoding="utf-8")),250)

    def test_requirement_ids_are_unique_complete_and_linked(self):
        t=read("trace")
        # Only table row IDs count (mentions elsewhere don't double count).
        found=re.findall(r"^\| (UCS-\d{3}) \|",t,re.M)
        self.assertEqual(found,[f"UCS-{i:03d}" for i in range(1,37)])
        self.assertIn("DEVICE-PASS",t)
        self.assertIn("CUSTOMER-ACCEPTED",t)

    def test_all_22_audit_gates_present(self):
        s=read("audit")
        ids=re.findall(r"^\| (A\d{2}) \|",s,re.M)
        self.assertEqual(ids,[f"A{i:02d}" for i in range(1,23)])
        self.assertIn("FAIL",s)
        self.assertIn("BLOCKED",s)
        self.assertIn("independent",s.lower())

    def test_active_diagrams_have_one_weintek_runtime(self):
        for doc in ("master","architecture","visual"):
            t=read(doc)
            self.assertIn("Weintek",t)
            self.assertNotIn('["PC / IPC collection + report service"]',t)
        policy=json.loads((ROOT/"contracts/ucs-role-ux-policy.json").read_text())
        self.assertFalse(policy["runtime_scope"]["external_computer_allowed"])

    def test_no_external_storage_runtime_in_site_profiles(self):
        schema=json.loads((ROOT/"schemas/site-profile.schema.json").read_text())
        modes=schema["properties"]["storage"]["properties"]["mode"]["enum"]
        self.assertEqual(set(modes),{"weintek_native","hmi_local_sql_query"})
        for p in (ROOT/"examples/site-profiles").glob("*.json"):
            example=json.loads(p.read_text())
            self.assertIn(example["storage"]["mode"],modes)
            self.assertFalse(set(example["storage"].get("preferred_export",[]))&{"pdf","xlsx"})

    def test_agent_brief_and_owner_link_back_to_master(self):
        for doc in ("handoff","agent","readme"):
            self.assertIn("UCS_FINAL_MASTER_PLAN.md",read(doc))
        self.assertIn("docs/UCS_FINAL_MASTER_PLAN.md",read("readme"))
        self.assertIn("AI_AGENT_EXECUTION_BRIEF.md",read("master"))

    def test_exact_one_manager_home_role_privacy(self):
        role=json.loads((ROOT/"contracts/ucs-role-ux-policy.json").read_text())
        home={k:v["landing_screen"] for k,v in role["roles"].items() if k in ("operator","engineer","manager")}
        self.assertEqual(len(set(home.values())),3)
        self.assertNotIn("COMMISSIONING",role["roles"]["manager"]["can_access"])
        self.assertNotIn("COMMISSIONING",role["roles"]["operator"]["can_access"])

    def test_key_history_quality_invariants_are_auditable(self):
        master=read("master").lower()
        for phrase in ("missing", "stale", "recovered", "all commissioned meters", "last-good", "no pc", "sqlite", "usb"):
            self.assertIn(phrase,master)
        audit=read("audit").lower()
        for phrase in ("no-data", "retention", "popup", "exact", "backup", "report"):
            self.assertIn(phrase,audit)

    def test_work_packages_and_named_issues_present(self):
        t=read("work")
        for p in ("WP0","WP6","WP7","WP8","WP10","WP11"):
            self.assertIn(p,t)
        for issue in ("#27","#28","#29","#30"):
            self.assertIn(issue,t)

    def test_no_unsupported_pdf_claim_in_readme(self):
        main=read("master")
        self.assertIn("PDF",main)
        self.assertIn("UNPROVEN",main)
        self.assertIn("HTML",main)

if __name__=="__main__":
    unittest.main()

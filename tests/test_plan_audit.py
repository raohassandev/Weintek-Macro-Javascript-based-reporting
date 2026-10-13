"""Audit remediation static contract tests; offline-only evidence."""
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]


class PlanAuditIntegrity(unittest.TestCase):
    def test_eight_external_findings_traceable(self):
        audit=(ROOT/"docs/PLAN_AUDIT.md").read_text(encoding="utf-8")
        ids=re.findall(r"^\| (AF-\d{2}) ",audit,re.M)
        self.assertEqual(ids,[f"AF-{i:02d}" for i in range(1,9)])
        for code in ("Q01","Q02","Q04","Q10","Q12","#33","#34"):
            self.assertIn(code,audit)
        self.assertIn("no extra PC/IPC/server",audit)

    def test_m0_m6_canonical_status(self):
        plan=(ROOT/"docs/UCS_FINAL_MASTER_PLAN.md").read_text()
        part=plan.split("## 12. Milestones and exit gates",1)[1].split("## 12A.",1)[0]
        rows=re.findall(r"^\| (M\d) — [^|]+\| \*\*\[([^]]+)\]",part,re.M)
        self.assertEqual([r[0] for r in rows],["M0","M1","M2","M3","M4","M5","M6"])
        self.assertIn("COMPLETED",rows[0][1])
        self.assertIn("BLOCKED",rows[-1][1])
        self.assertNotIn("DEVICE-PASS",rows[0][1])

    def test_wp0_wp11_live_status_flags(self):
        content=(ROOT/"docs/UCS_DELIVERY_WORKPACKAGES.md").read_text()
        table=content.split("## LIVE WORK PACKAGE STATUS SNAPSHOT",1)[1].split("## WP0 —",1)[0]
        ids=re.findall(r"^\| (WP\d{1,2}) [^|]+\|",table,re.M)
        self.assertEqual(ids,[f"WP{i}" for i in range(12)])
        self.assertIn("NOT RUN",table)

    def test_reference_artifacts_exist(self):
        for path in ("tests/fixtures/energy_reference_cases.json","scripts/energy_reference.py",
                     "tests/test_energy_reference.py","docs/PLAN_AUDIT.md"):
            self.assertTrue((ROOT/path).exists(),path)

    def test_plan_audit_linked_from_owner_and_ai(self):
        for path in ("README.md","AGENTS.md","docs/OWNER_DASHBOARD.md",
                     "docs/AI_AGENT_EXECUTION_BRIEF.md","docs/MASTER_PLAN.md"):
            self.assertIn("PLAN_AUDIT.md",(ROOT/path).read_text(),path)


if __name__=="__main__":
    unittest.main()

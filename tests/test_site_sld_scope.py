"""Owner change of design scope: primary HMI view must be actual site SLD. Docs only."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SLDRequirementGuard(unittest.TestCase):
    def test_primary_sld_contract_is_clear_and_missing_site_source_is_not_invented(self):
        contract=(ROOT/"docs/PLANT_SLD_PRIMARY_SCREEN_CONTRACT.md").read_text()
        for text in ("real plant SLD","61 energy analyzers","cMT-FHDX-220",
                     "SOURCE_DRAWING_PENDING","Meter Detail 210","Weintek",
                     "GATE-1 design-change"):
            self.assertIn(text,contract)

    def test_existing_generic_home_art_rejected_not_accepted(self):
        for path in ("README.md","docs/UCS_FINAL_MASTER_PLAN.md",
                     "docs/SCREEN_DESIGN_BRIEF_FHDX220.md",
                     "docs/OWNER_DASHBOARD.md"):
            text=(ROOT/path).read_text()
            self.assertTrue("REJECTED" in text or "rejected" in text,path)
            self.assertIn("PLANT_SLD_PRIMARY_SCREEN_CONTRACT.md",text,path)

    def test_sld_does_not_claim_browser_or_physical_proof(self):
        text=(ROOT/"docs/PLANT_SLD_PRIMARY_SCREEN_CONTRACT.md").read_text()
        self.assertIn("not proven",text.lower())
        self.assertIn("No extra",text) if "No extra" in text else self.assertIn("No",text)
        self.assertIn("real plant SLD",text)

if __name__=="__main__":
    unittest.main()

# Engineer build handoff — cMT-FHDX-220 two-meter pilot
**State: READY-TO-BUILD DOCUMENTATION ONLY / IMPLEMENTATION HOLD.**
Start with [acceptance checklist](ACCEPTANCE_CHECKLIST.md), [LW manifest](register-allocation.json), [SQL plan](SQL_QUERY_TEST_PLAN.md), [USB plan](USB_STORAGE_TEST_PLAN.md), [evidence template](EVIDENCE_TEMPLATE.md), [Screen Design Brief](../../docs/SCREEN_DESIGN_BRIEF_FHDX220.md).

## Before implementation may start
- Owner accepts scope after GATE-1 DOC/OFFLINE PASS and supplies physical HMI System Information + installed EBPro version.
- Freeze actual meter brands/models/register tables and signed source data/quality labels; verify screen 1920x1080 EBPro native project definition.
- Inspect native EBPro address/system tag export for all LW/PLW, UAC, SQL Query, Data Sampling, Backup objects; no magic addresses or assumed Macro APIs.
- Keep all runtime on FHDX-220 with one USB2/no SD. EBPro workstation is *development only*, never a required production collector/server.

## First approved coding iteration (FUTURE; currently NOT AUTHORIZED)
1. Back up original model-specific .cmtp/.emtp/EBPro project if present.
2. Configure **two native Modbus devices** from manufacturer registers; create scale/endian typed read-only mapping.
3. Populate the proposed normalized 128-word blocks (meter 1 LW 256..383, meter 2 LW 384..511) after confirming no collisions. Never allocate historian samples inside the volatile LW cache.
4. Build ONE Meter Detail window with private PLW navigation and verified snapshot meter ID + timestamp/quality.
5. Independently capture **both** meter histories in native Data Sampling regardless of open screen; add quality/incident records.
6. Test SQL Query Basic/Advanced only as supported; gate any custom report until actual row-level proof.
7. Validate USB1 mounted/writable/recording distinctly and backup/restore using qualified passive media.
8. Review 2-meter replay, missing zero/gap, safety and UAC with independent auditor; expand only on documented proof.

## File manifest
- Proposed register addresses: JSON (not native EBPro tag CSV)
- SQL and USB plans: human-readable HMI bench scripts, not executed code
- QA references: ../../tests/fixtures/energy_reference_cases.json and ../../scripts/energy_reference.py (OFFLINE only)
- UI assets: ../../designs/screens/110-operator-home etc (static PNG/native object manifests, no live data).

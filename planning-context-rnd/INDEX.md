# PLANNING · CONTEXT · R&D (AUTHORITATIVE NAVIGATION)
This is a **separate navigation entrypoint**, not a copy or migration. Existing source documents remain in place to preserve issue links, citations and relative Markdown links. No actual proprietary plant data is included.

| Category | Source of truth |
|---|---|
| Master planning | [Final UCS Master Plan](../docs/UCS_FINAL_MASTER_PLAN.md), [work packages](../docs/UCS_DELIVERY_WORKPACKAGES.md) |
| Owner context | [Project Context](../docs/PROJECT_CONTEXT.md), [Decisions](../docs/DECISION_LOG.md), [Activity log](../docs/ACTIVITY_LOG.md) |
| R&D manufacturer sources | [R&D Index](../research/INDEX.md), [Source register](../research/SOURCE_REGISTER.json), [Open questions](../research/OPEN_QUESTIONS.md) |
| FHDX-220 scope | [Hardware target](../docs/HARDWARE_TARGET_FHDX_220.md), [memory](../docs/WEINTEK_MEMORY_CONTRACT.md), [USB risk](../docs/FHDX220_SINGLE_USB_STORAGE_RISK.md) |
| QA/audit | [Requirements](../docs/UCS_REQUIREMENTS_TRACEABILITY.md), [Independent audit](../docs/INDEPENDENT_AUDIT_PROTOCOL.md), [GATE-1](../docs/GATE1_INDEPENDENT_PLAN_AUDIT_RESULT.md) |
| Site-specific electrical SLD | [SLD scope](../docs/PLANT_SLD_PRIMARY_SCREEN_CONTRACT.md); must come from actual site drawing, not generic display |
| Historian/report planning | [Report catalog](../docs/REPORT_CATALOG.md), [SQL/USB pilot plan](../planning/2-meter-fhdx220/) |
| Current working assets | [Development hub](../development/README.md) |

**Architecture:** Real-time, historian, report execution on Weintek cMT-FHDX-220 and qualified passive media only. No external PC/IPC/SQL processing, no SD or PLC Web Browser on 220.

**Current evidence:** DOC/OFFLINE with 4 P0 blockers Q01, Q02, Q10, Q04/Q12. Maintain planning and source research here; do not label a static screen a deployed HMI.

# PRIORITY OVERRIDE — NO IMPLEMENTATION BEFORE INDEPENDENT PLAN AUDIT
Owner ordered full planning first. While [#37 planning](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/37) and [#38 independent audit](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/38) are incomplete, do **not** start EBPro/HMI/JS/Macro implementation lanes, move implementation flags to INPROGRESS or claim a product release. Work only on plan/docs/validation and audit. Wait for actual independent auditor evidence and owner authorization. Primary HMI **cMT-FHDX-220**, one USB2/no SD, 1920×1080 and native EBPro+JS Object only. [Finalization instructions](docs/PLAN_FREEZE_PRE_IMPLEMENTATION_AUDIT.md).

# UCS — AI / HUMAN CONTRIBUTORS
**First: [FINAL MASTER PLAN](docs/UCS_FINAL_MASTER_PLAN.md) → [AI EXECUTION BRIEF](docs/AI_AGENT_EXECUTION_BRIEF.md) → [CC #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1).**
**Auditors:** [Independent audit protocol](docs/INDEPENDENT_AUDIT_PROTOCOL.md), [traceability IDs UCS-001..036](docs/UCS_REQUIREMENTS_TRACEABILITY.md).

## Non-negotiable
- Weintek cMT-SVRX/FHDX HMI hardware with attached USB/SD/qualified USB SSD **only**. No extra PC/IPC, remote SQL/database/Node/report web server, external computation. No arbitrary HTML browser/SQLite/PDF APIs without physical vendor-specific proof.
- Initial 1 site/61 energy analyzers, generic multiple sites, native independent historian and gap/quality evidence, role homes, one reusable Meter Detail with **client-private PLW** selection, screened UAC actions, resource manager as deep screen.
- Exact register/driver maps/tag import format/EBPro project must be taken from supported version/model and reviewed. `LW 256..8063` 61×128 is a proposal; system registers require exact Weintek version confirmation.
- Work on the actual GitHub issue scoped lane; claim ownership, use branch PR, exact-head CI and **real** EBPro/device evidence. Never fabricate tests/reviews/screenshots/merchant/manufacturer claims. CI pass ≠ hardware acceptance.
- Preserve site data quality, coverage and historical downtime as evidence. No placeholder zero for missing. No generic `sum(kW)` as energy kWh.
- User favors light, management-class executive UI; three purpose-built homes, alarms context-based, not a daily storage/CPU dashboard for managers. AI manages R&D/long manuals/tests so owner is asked only essential information.
- Use `research/SOURCE_REGISTER.json`, `research/DEMO_PROJECTS_REVIEW.md`, `docs/PROJECT_CONTEXT.md`, `docs/DECISION_LOG.md`, `docs/ACTIVITY_LOG.md` as durable knowledge and keep updated. This is a **PUBLIC REPO**, exclude personal/customer production data, passwords and proprietary archives.
- Independent audit separate from implementation (issue #30); customer signoff and tested restore needed before 'released/100%'.

# UCS — Universal Control & Supervisory System (Weintek-only)

**Ek engine, multiple sites.** Configurable historical reports for solar / grid / DG, industry, UPS, LPG, HVAC and utilities. **Currently in design/R&D**; no production or hardware acceptance claim.

## FINAL BASELINE v1.0 — primary entrypoint
**Read these first (authoritative, 2026-10-13):**
1. **[UCS FINAL ENGINEERING MASTER PLAN](docs/UCS_FINAL_MASTER_PLAN.md)** — full customer context, architecture, registers, 61-meter historian, UX, reporting, hardware limits, milestones and constraints.
2. **[AI IMPLEMENTATION HANDOFF](docs/AI_AGENT_EXECUTION_BRIEF.md)** — exactly how another AI/engineer resumes and works safely.
3. **[INDEPENDENT AI AUDIT PROTOCOL](docs/INDEPENDENT_AUDIT_PROTOCOL.md)** — evidence gates, findings, security and release criteria.
4. **[36 REQUIREMENTS & EVIDENCE MATRIX](docs/UCS_REQUIREMENTS_TRACEABILITY.md)** — verification not vague percentages.
5. **[PARALLEL EXECUTION WORKPACKAGES](docs/UCS_DELIVERY_WORKPACKAGES.md)** — scoped engineering ownership, dependencies, accepted outputs.
6. **[LIVE COMMAND CENTRE #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1)** — statuses and precise blockers.

Baseline **finalizes plan/scope**, not physical HMI functionality or customer acceptance. Weintek only; no PC/IPC/server runtime.

## External plan audit corrective actions
[External audit findings & response](docs/PLAN_AUDIT.md) · [M0–M6 live flags](docs/UCS_FINAL_MASTER_PLAN.md#12-milestones-and-exit-gates) · [WP0–11 current status](docs/UCS_DELIVERY_WORKPACKAGES.md#live-work-package-status-snapshot--2026-10-13) · [12 energy golden cases](tests/fixtures/energy_reference_cases.json). **Python fixtures are offline oracle tests only**, never HMI proof. [#33](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/33) [#34](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/34).

## Owner quick navigation
| See this | Link |
|---|---|
| **One-page status (Roman Urdu)** | [Owner Dashboard](docs/OWNER_DASHBOARD.md) |
| **Pictorial roadmap / architecture** | [Visual Plan — GitHub-rendered diagrams](docs/VISUAL_PLAN.md) |
| **Resource & Storage Manager screen** | [Executive theme: SVG screen + engineer source pack](designs/resource-manager/README.md) |
| **USB vs Industrial SSD** | [Storage decision & capacity](docs/STORAGE_DECISION_AND_CAPACITY.md) |
| **Which historical reports?** | [22 planned report templates](docs/REPORT_CATALOG.md) |
| **All R&D sources and vendor web links** | [Research Library](research/INDEX.md) |
| **Authoritative issue/task tracking** | [Command Centre #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1) |

## Approved scope (2026-10-13)
**All processing and history are Weintek-only**: cMT-SVRX / cMT-FHDX, attached USB/SD/qualified SSD, no external computer runtime. [Revised architecture](docs/VISUAL_PLAN.md) · [Role-specific home screens](docs/ROLE_BASED_UX_PLAN.md) · [Web HTML feasibility](research/WEINTEK_HTML_FEASIBILITY.md) · [Official demo project review](research/DEMO_PROJECTS_REVIEW.md).

## System at a glance
```mermaid
flowchart LR
  A["Solar / Factory / UPS / LPG / Any Site"] --> B["Site Configuration"]
  B --> C["Universal Historian + Report Definitions"]
  C --> D["HMI History / Trends"]
  C --> E["CSV / Excel-compatible output"]
  C --> F["On-device reports / proven exports"]
```

**Site dependent:** actual devices/register maps, metric types, timezone, sample and retention settings, report selection, output.  
**Reusable:** data semantics, period filters, calculation rules, quality/gap handling, report templates and test contracts.

## Technical source of truth
- [Site profile schema](schemas/site-profile.schema.json), [configuration guide](docs/SITE_PROFILE_GUIDE.md) and [fictional sample sites](examples/site-profiles)
- [Architecture](docs/ARCHITECTURE.md) · [Master Plan](docs/MASTER_PLAN.md) · [Requirements/Acceptance](docs/REQUIREMENTS_AND_ACCEPTANCE.md)
- [Project/chat context](docs/PROJECT_CONTEXT.md) · [Decision Log](docs/DECISION_LOG.md) · [Activity Log](docs/ACTIVITY_LOG.md)
- [Weintek feature matrix](docs/MODEL_COMPATIBILITY.md) · [POC test plan](docs/POC_TEST_PLAN.md) · [Official reference links](docs/REFERENCE_LINKS.md)
- [R&D evidence register](research/SOURCE_REGISTER.json) · [Open questions](research/OPEN_QUESTIONS.md) · [Real experiment log](research/EXPERIMENT_LOG.md)
- [Worker protocol](docs/WORKER_PROTOCOL.md) · [AI/contributor rules](AGENTS.md)

## Safety/feature honesty
Weintek manufacturer release notes confirm SQL Query can access SQLite on USB/SD for supported cMT devices. The exact combination **SQL Query Advanced Mode + Local SQLite** remains unverified; older manuals describe Advanced custom SQL mainly with MySQL/MS SQL. Do not assume unrestricted SQLite APIs in Macro/JavaScript or unrestricted access to HMI native log files. A formatted multipage PDF remains UNPROVEN as an on-device Weintek generation feature; no external PC/IPC is permitted. Never treat `SUM(kW)` as energy kWh.

No real customer data, credentials, fabricated test results, or copied proprietary manuals in this public repository.

**As of:** 2026-10-13.

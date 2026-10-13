# UCS — AI IMPLEMENTATION AGENT / NEW-CHAT HANDOFF (v1.0)
**Repository:** `raohassandev/Weintek-Macro-Javascript-based-reporting`  
**Live Command Centre:** [issue #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1)  
**Immutable direction:** [UCS Final Master Plan](UCS_FINAL_MASTER_PLAN.md) · [Requirements/acceptance](UCS_REQUIREMENTS_TRACEABILITY.md) · [Work packages](UCS_DELIVERY_WORKPACKAGES.md)  
**Project status:** scope/design baseline; actual functioning EBPro project, 61-meter field data, SQL-on-device report and full deployment are NOT delivered.

## MANDATORY HOLD: planning audit before implementation
The owner has explicitly ordered: **finish the cMT-FHDX-220 plan, then independently audit, then authorize EBPro/JS/Macro coding**. Until [plan audit #38](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/38) returns an actual reviewed, accepted verdict and the owner approves start, do **not** claim WP6 coding tasks available to execute. Allowed now: resolve design docs, broken link checks, signed decisions and audit evidence. Read [freeze gate](PLAN_FREEZE_PRE_IMPLEMENTATION_AUDIT.md), [1920×1080 screen brief](SCREEN_DESIGN_BRIEF_FHDX220.md), and [single USB fault decision](FHDX220_SINGLE_USB_STORAGE_RISK.md).

## Copy into a new AI engineering chat
> You are the **Weintek UCS implementation engineer and issue-driven executor** for `raohassandev/Weintek-Macro-Javascript-based-reporting`. **Your authority is GitHub issue #1 and docs/UCS_FINAL_MASTER_PLAN.md baseline v1.0.** Read those plus docs/UCS_REQUIREMENTS_TRACEABILITY.md, docs/UCS_DELIVERY_WORKPACKAGES.md, docs/PROJECT_CONTEXT.md, docs/DECISION_LOG.md, research/INDEX.md and current open issues/PRs before touching code. During PLAN-AUDIT HOLD, only claim planning/audit tasks. After independent plan audit and owner authorization, work in a scoped implementation lane, execute and commit real files/tests, push a PR, report exact SHA, CI runs and evidence in the issue and Command Centre. Never invent HMI logs, firmware/feature support, USB HTML/SQL/PDF support or device proof; distinguish offline/simulator/hardware/customer evidence. **ALL runtime components must stay entirely on Weintek SVRX/FHDX and attached media. NO PC, IPC, external SQL/database/report service/cloud runtime.** Use native EBPro plus verified JS Object/Action and Macro operations, per-client indexed shared UI, always-on 61-meter historian independent of selection, missing-data and provenance reports, supported tag memory and role-based screen flows. Build 2-meter vertical slice first, then 61-meter benchmark; reuse one meter detail. Keep management light executive theme and avoid routine storage telemetry on Management Home; only role-relevant critical popups with persistent event history. Maintain repository docs/R&D sources, decisions, traceability and owner quick view, not chat-only claims. Do not mark 100% until exact-name device test, security, backup/report reconciliation, independent audit and customer acceptance. If blocked on physical equipment/EBPro export, continue independent fixture/doc/driver/UI work, mark precise [BLOCKED: reason], ask owner only one truly essential fact.

## First 15-minute sequence
1. Fetch issue #1 board and the newest main HEAD. Read this brief, master baseline and current work issues. **Do not accept stale external PC/IPC language** in older issues/docs as authorization.
2. Check open PRs, exact commit checks, task flags, assignments and changed files. Avoid parallel ownership collisions; claim with worker ID `W-xxxx` and UTC timestamp in task comment/board when permissions permit.
3. Choose the next safe scoped task: documentation source verification; site-profile validation; two-meter fixture; memory/tag collisions; screen SVG/native object map; JS/Macro compile POC; or blocked physical acceptance prep.
4. Write production-grade type/byte-order and bounds checks. Create automated negative tests; verify with CI on exact branch. **Do not claim a successful EBPro compile** from an external Python test.
5. Push branch/PR with linked issue, explicit files, acceptance IDs, exact SHA, tests/results, physical evidence state and rollback; request independent reviewer. Do not self-mark deployed.
6. Update task and board status, activity/decision logs, and minimal owner summary. If all work blocked, state precise owner gate and continue independent R&D.

## Product boundaries to remember
| Concern | Final decision |
|---|---|
| Hardware | Weintek SVRx/FHDx only, exact model/OS TBD |
| Acquisition | 61 logical meter slots, model-specific read-only register profiles, no copied page logic |
| Continuous history | All configured meters, no dependency on viewed page; outages and failures become evidence |
| UI | Three home screens by Operator, Engineer, Manager; shared Meter Detail/Trend/Reports; occasional Resource Manager |
| Multi-user | Per-client private navigation state/Private Index with actual cMT Viewer device acceptance |
| Registers | Reserved user LW 256..8063 proposal, client PLW, scoped RW/LB, official system tags; verify collisions |
| Report formats | Native HMI display/CSV where tested; PDF/XLSX NOT proven on Weintek-only target |
| SQLite | SQL Query external/local only as documented; generic JS sqlite API & Local Advanced query unproven |
| HTML | Canvas JS Object mainline; raw USB HTML file/browser is POC, not release route |
| Storage | FAT32 USB/SD or **qualified** USB SSD, no computer, fail-closed storage/recorder proofs & verified backup |
| Commissioning | Configurable predeclared slots/drivers through HMI, new unsupported drivers may require EBPro rebuild |
| Human interaction | AI manages R&D/manual reading/tests/code; owner sees visual screens + concise choices |

## Current known repository files (do not recreate without inspection)
- `docs/VISUAL_PLAN.md` with merged Weintek-only Mermaid architecture.
- `docs/ROLE_BASED_UX_PLAN.md`, `contracts/ucs-role-ux-policy.json`: roles, alarm routing.
- `docs/WEINTEK_MEMORY_CONTRACT.md`, `contracts/meter-memory-map.json`: proposed normalized LW 61×128.
- `schemas/site-profile.schema.json`, `examples/site-profiles/*.json`, `scripts/validate_site_profiles.py`, `tests/test_ucs_scope.py`.
- `designs/resource-manager/resource-manager-light.svg`, `resource-manager-background-only.png`, `screen-object-map.csv`.
- `tags/resource-manager-dictionary.csv` (not guaranteed EBPro import-native), `macros/UCS_STORAGE_STATUS.mcr` and `js/ucs_usb_write_read_probe.js` (both device/compilation unverified).
- `research/SOURCE_REGISTER.json`, `research/demo-catalog.json`, `research/WEINTEK_HTML_FEASIBILITY.md`; official demo archives not imported.
- `experiments/html-poc/index.html` visual JS-only test, no meter connection.

## Owners and independent lanes
- HW/Drivers: #2 / #28 / #29 (file ownership `drivers/`, `site/` / selected model HMI assets)
- MEM/Tags: #16 and #29 (reserved addresses and EBPro CSV; coordinate with HW)
- HIST/Data: #4 / #17 (sample/quality schema, tests, true storage)
- RPT/Macro/JS: #3 / #5 / #6 / #8 (bound query handshake and formatting)
- UI/UX: #7 / #15 / #19 (owner screens and resource manager; scoped folders)
- QA: #9 (fixture and verified device tests), AUDIT: #30 (independent)
- RELEASE: #10, GOVERNANCE: #1 / #27
Do not let two workers concurrently rewrite `docs/UCS_FINAL_MASTER_PLAN.md` or a shared tag registry without issue-flag ownership; use branch scoped pull requests and review.

## Evidence quality and status
- DESIGN-PASS: all required docs, stable decisions, machine validators exist.
- OFFLINE-PASS: passing synthetic fixtures, same Git SHA, no hardware assertions.
- EBPRO-COMPILED / SIMULATOR-PASS: real project opens and compiles/runs in named EBPro version, screenshots/logs.
- DEVICE-PASS: exact Weintek HMI model, firmware, USB/SD device, duration, input meter identities and exported records.
- AUDIT-PASS: separate reviewer independently checks evidence, role security, missing data, storage failures and report accuracy.
- CUSTOMER-ACCEPTED: signed functional acceptance. **The project currently has only design and offline CI evidence.**

## Risk log and escalations
P0 open gates: exact SKU/OS/EBPro and firmware; meter brand/register maps and exact sample policy; 61-meter storage throughput; SQL Query native SQLite semantics; correct per-meter long history; resource probe compile; role session isolation; alarms/event retention; backup restore; PDF if contract requires it. No need to ask for all of these simultaneously. A simple photo of the HMI label/version and an EBPro exported tag CSV become needed only at corresponding implementation gate.

## Update & acceptance protocol
- Task flags: `[AVAILABLE]`, `[INPROGRESS @id since UTC]`, `[REVIEW PR#n head:sha]`, `[COMPLETED PR#n/sha]`, `[BLOCKED: reason]`. A **design-only task** can complete without device evidence if explicitly scoped to design; downstream implementation remains OPEN.
- Every PR needs scope, updated source/links, test commands/results, firmware/software assumptions, faults/security cases, and explicit simulator/physical/customer test status. Never fabricate AI/Claude review comments.
- Independent auditor uses [protocol](INDEPENDENT_AUDIT_PROTOCOL.md). A reviewer **cannot** sign off their own deployment evidence as independent.
- A change that reintroduces an external PC/IPC requires fresh explicit owner consent; current design must never silently violate the fixed boundary.

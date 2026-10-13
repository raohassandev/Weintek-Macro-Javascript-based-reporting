# Architecture decision log
All decisions need an owner, date, evidence URL and fallback. Draft assumptions are not decisions.

**ACTIVE DIRECTION:** UCS baseline v1.0 [master plan](UCS_FINAL_MASTER_PLAN.md). D-018 **supersedes** historical/conditional references to separate PC/IPC processing in D-006/D-014; cMT FHDX/SVRX with attached media is the ONLY runtime. Never misread old text as authorization.

| ID | Date | Decision / candidate | State | Rationale / follow-up |
|---|---|---|---|---|
| D-001 | 2026-10-13 | This repository and GitHub issue #1 are project source of truth | ACCEPTED | Owner requests complete plan, track, Command Centre and chat context in GitHub |
| D-002 | 2026-10-13 | Target first to prove SQL Query register bridge on supported cMT Advanced model | PROVISIONAL | Weintek documents SQL Query/USB/SD SQLite; model+EBPro test pending |
| D-003 | 2026-10-13 | Do not claim direct arbitrary SQLite API in Macro or JS | ACCEPTED GUARDRAIL | No verified official public API for `sqlite.open()`; use documented object/register route |
| D-004 | 2026-10-13 | Do not select cMT1106X as on-HMI SQL/JS reporting controller | DOC-SUPPORTED | cMT X Basic; SQL Query feature matrix excludes it |
| D-005 | 2026-10-13 | cMT3102X as benchmark shortlist; cMT3108XH/headless SVRX alternatives | PROVISIONAL | Hardware and exact OS availability pending |
| D-006 | 2026-10-13 | Custom formatted PDF is a distinct deliverable | ACCEPTED GUARDRAIL | Not an automatic consequence of SQLite / HMI history; external service may be required |
| D-007 | 2026-10-13 | Unknown 'cMT1102' identity must be checked | OPEN | May be typo / different model; never silently substitute cMT2102X |
| D-008 | 2026-10-13 | Real user data store and HMI internal historian DB must not be equated | ACCEPTED GUARDRAIL | SQL Query local file access does not prove ability to query any internal logger schema |
| D-009 | 2026-10-13 | Common engine + site-specific profiles and report catalog | ACCEPTED DIRECTION | Owner explicitly wants one solution adaptable to multiple industrial sites; [config design](SITE_PROFILE_GUIDE.md) |
| D-010 | 2026-10-13 | Explicitly treat SQL Query Advanced Mode on Local SQLite as **UNVERIFIED** | ACCEPTED GUARDRAIL | Weintek v6.01.02 local SQLite support vs manuals describing custom Advanced SQL for MySQL/MS SQL; targeted test required [Q02](../research/OPEN_QUESTIONS.md) |
| D-011 | 2026-10-13 | Owner-first visuals and short progress, engineering-managed tests | ACCEPTED WORKFLOW | Human user does not want large text/tests. [Owner view](OWNER_DASHBOARD.md) |
| D-012 | 2026-10-13 | Indexed R&D source ledger with version, authority and evidence | ACCEPTED WORKFLOW | [R&D register](../research/SOURCE_REGISTER.json); don't upload copyrighted manuals by default |

| D-013 | 2026-10-13 | Introduce one UCS Resource/Storage Manager SCADA screen using documented HMI system registers and independent historian/backup metrics | ACCEPTED DIRECTION | [Spec](RESOURCE_STORAGE_MANAGER_SCREEN.md), [#19](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/19); all readouts require actual source/device checks |
| D-014 | 2026-10-13 | Use FAT32 USB/SD for Weintek-native export; prefer IPC industrial SSD + independent backup for 61-meter durable reporting; directly attached USB SSD unqualified | PROVISIONAL STORAGE DECISION | [Storage architecture](STORAGE_DECISION_AND_CAPACITY.md), [#18](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/18), test actual model/enclosure/power |

| D-015 | 2026-10-13 | Light executive green/neutral graphical Resource Manager theme | ACCEPTED DIRECTION | Actual management user dislikes blue; [screen SVGs](../designs/resource-manager/README.md) |
| D-016 | 2026-10-13 | Storage states connected, writable, recording, backup must be independently proven and time bounded | ACCEPTED GUARDRAIL | [JS USB probe](../js/ucs_usb_write_read_probe.js), [status evaluator](../macros/UCS_STORAGE_STATUS.mcr); no verified device run yet |
| D-017 | 2026-10-13 | Native EBPro object feature map + native export CSV compatibility gate | ACCEPTED WORKFLOW | [Objects mapping](../designs/resource-manager/screen-object-map.csv), [tag import guide](../tags/EBPRO_IMPORT_GUIDE.md) |

| D-018 | 2026-10-13 | **No PC/IPC/computer/report server** in UCS runtime; Weintek-only SVRX/FHDX with attached storage | ACCEPTED HARD CONSTRAINT | Owner reviewed erroneous VISUAL_PLAN branch and explicitly rejected it; [new visual](VISUAL_PLAN.md); overrides provisional external server advice in D-006/D-014 |
| D-019 | 2026-10-13 | Three separate purpose-built homes, common indexed meter detail and shared reporting/Resource Manager | ACCEPTED DIRECTION | [Role-based UX](ROLE_BASED_UX_PLAN.md) |
| D-020 | 2026-10-13 | Priority/context-based notification popups; all faults/event history persisted | ACCEPTED DIRECTION | [Event routing matrix](ROLE_BASED_UX_PLAN.md) |
| D-021 | 2026-10-13 | JS Object Canvas preferred for custom UI over generic HTML pages; PLC Web Browser/USB HTML path remains UNVERIFIED | PROVISIONAL TECHNICAL | [Weintek HTML research](../research/WEINTEK_HTML_FEASIBILITY.md) |
| D-022 | 2026-10-13 | Separate cMT-FHDX-820 (W) Chromium model must not be conflated with EBPro FHDX-820 | ACCEPTED GUARDRAIL | [Vendor model](https://www.weintek.com/Product/Model/cMT-FHDX-820-%28W%29); no assumed native historian |

| D-023 | 2026-10-13 | Freeze UCS v1.0 as **execution/scope baseline**, not physical release | ACCEPTED FOR PLANNING | [Final master plan](UCS_FINAL_MASTER_PLAN.md), [36 requirement matrix](UCS_REQUIREMENTS_TRACEABILITY.md), [AI agent brief](AI_AGENT_EXECUTION_BRIEF.md), [independent audit](INDEPENDENT_AUDIT_PROTOCOL.md) |
| D-024 | 2026-10-13 | Every future active plan/issue must flag old PC/IPC proposal as superseded; unsupported Weintek report features remain explicit BLOCKED | ACCEPTED GUARDRAIL | [No-PC runtime policy](UCS_FINAL_MASTER_PLAN.md), [Weintek-only tests](../tests/test_ucs_scope.py) |

| D-025 | 2026-10-13 | External plan audit findings AF-01..08 are tracked against canonical M0–M6 and actual GitHub evidence rather than obsolete old M0–M5 | ACCEPTED AUDIT RESPONSE | [PLAN_AUDIT](PLAN_AUDIT.md), [#33](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/33); old MASTER_PLAN is redirected |
| D-026 | 2026-10-13 | Custom SQL and native basic history/reporting are independent feasibility routes; never claim native fallback works before on-HMI proof | ACCEPTED GUARDRAIL | [Audit decision tree](PLAN_AUDIT.md), vendor SQL manual; Q02 still unverified |
| D-027 | 2026-10-13 | Source-of-truth kWh calculations require fixed synthetic reference cases: counter reset/rollover, bad/missing quality, interval integration, timezone | ACCEPTED QA DIRECTION | [#34](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/34), [fixture](../tests/fixtures/energy_reference_cases.json); offline test is not EBPro proof |

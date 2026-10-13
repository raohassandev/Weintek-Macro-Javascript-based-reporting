# Architecture decision log
All decisions need an owner, date, evidence URL and fallback. Draft assumptions are not decisions.

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

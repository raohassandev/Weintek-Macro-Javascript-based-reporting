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

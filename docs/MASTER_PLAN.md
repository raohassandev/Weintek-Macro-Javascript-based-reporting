# Master execution plan — historical reporting
**Command Centre:** [#1](../issues/1). Task-specific acceptance is authoritative in issues #2–#10. Track with a link to an actual artifact/commit/test, not asserted percentages.

## Parallel lanes
| Lane | Issue | Implementation | Evidence gate |
|---|---|---|---|
| HW | [#2](../issues/2) | Official feature matrix; exact model / EBPro / OS and device capability | Documented + device evidence |
| SQL | [#3](../issues/3) | Sample schema, filtered SQL, query and register contract | SQL fixtures + verified EBPro config |
| HIST | [#4](../issues/4) | Source tags, sampling, backup and retention | Saved EBPro setup + data reconciliation |
| MACRO | [#5](../issues/5) | Macro query orchestration/status/error | Minimal reproducible script + execution |
| JS | [#6](../issues/6) | JS register I/O, UI integration and state machine | Versioned SDK API + functional test |
| UI | [#7](../issues/7) | Date filters, results, paging, loading/errors | Prototype/screens and UX tests |
| EXPORT | [#8](../issues/8) | CSV and separately proven PDF/print | Test files + source-data comparison |
| QA | [#9](../issues/9) | Automated and real-HMI integration tests | CI IDs + named device proof |
| RELEASE | [#10](../issues/10) | Commissioning, training, customer sign-off | Signed acceptance checklist |

## Delivery milestones
### M0 — Reproducible problem definition
Determine installed hardware, target output (on-screen, CSV, PDF), report columns, period/interval, retained history, USB/SD conditions and whether remote clients are needed. Clear unknowns; no feature selection from assumptions.

### M1 — Feature compatibility proof
Freeze specific SKU + firmware + EBPro version. On a supported device, prove SQL Query access to controlled SQLite .db on USB/SD and check query command semantics; validate JS object availability. Alternative if unavailable: external historian/report service, not fictitious macro SQLite functions.

### M2 — Data & query prototype
Agree timestamp convention, schema, data source, indexes and retention; implement safe filters/aggregation/paging; demonstrate query through SQL Query object → HMI mapped registers. Split sample DB from internal history until their true compatibility is proven.

### M3 — Working report HMI
Macro/JS orchestration, cancellation/timeout, paginated results, date range, site/device filter, units, stale/missing-data indication. Record actual device performance rather than estimates.

### M4 — Customer output formats
Verify on-HMI CSV; if needed implement PC/IPC pdf template with pagination and reconciliation. Clearly identify which device/host generates and stores each artifact.

### M5 — QA & acceptance
Regression suite plus real HMI proof on specified model. Failure scenarios, restore, power cut, USB absent/full, clock/DST, long queries, quality flags and report reconciliation. Produce release guide and formal customer acceptance.

## Dependencies and staffing
HW validation gates deployment promises, but SQL schema fixtures and UX prototypes are parallel; reports can be prototyped with synthetic **clearly labeled test** data. JS/macro integration waits on genuine versioned register map. PDF service evaluation is independent of SQL proof.

## Definition of Done
100% means verified functionality on the target hardware, tests/evidence and acceptance documented; not just documentation completed. Each lane maintains [AVAILABLE], [INPROGRESS @owner], [REVIEW PR#... head:sha], [COMPLETED PR#...], or [BLOCKED: reason].

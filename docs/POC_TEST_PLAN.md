# POC bench-test protocol — Weintek SQL reporting
**Status:** NOT RUN, actual model/OS and project unavailable. Owner: [HW #2](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/2), [SQL #3](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/3), [MACRO #5](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/5), [JS #6](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/6).

## Test 0 — identify runtime
Record exact rear-label model, hardware revision, OS build, EBPro release, JS SDK docs used and USB/SD filesystem. Photograph label only with customer permission. Do not log passwords.

## Test 1 — controlled SQLite source (independent of HMI native log)
Create a small database with `readings` table and rows at deliberately chosen boundaries: same-day events, month boundary, zero value, NULL, duplicate, no-data interval, power-meter cumulative energy counter reset. Place it at known USB path supported by HMI SQL Query. Record database integrity check (e.g., `PRAGMA integrity_check` on PC) and SHA-256.

## Test 2 — SQL Query Advanced object
In compatible EBPro model, configure [Data/History] → [SQL Query] per exact version manual, Database = documented Local setting, position USB/SD and static/dynamic known path. Add a read-only command with an explicit command ID, parameter mapping and ordered `SELECT ... WHERE ... ORDER BY ... LIMIT` result. Configure SQL Query Result Viewer if appropriate. Record the actual generated control/register settings. **Do not insert invented addresses, command IDs or undocumented parameters into production code.**

## Test 3 — mapped register handshake
Write filter arguments via on-HMI Numeric/ASCII input or confirmed Macro/JS driver calls. Set command/trigger; observe busy, success, error code and actual result rows. Attempt invalid date, missing database, corrupt media and no results. Record elapsed time with a real clock and whether the request was handled once.

## Test 4 — Macro & JS versions
Implement minimal macro to set known registers and trigger chosen SQL Query command; separate JS prototype to do the same with exact SDK signature. Verify two cMT Viewer sessions do not accidentally double-execute JS Actions. Prove graceful timeout, stale-result clearing and no overlapping requests.

## Test 5 — historian and export
Configure Data Sampling for independently identified tag data, produce native history file, backup CSV using built-in mechanism, and compare source to exported values. **Do not assert native log == controlled SQLite database.** Preserve time zones, day cutover, quality, unit labels, storage path and file naming.

## Test 6 — reporting and faults
Show daily/monthly date filters and page boundary; run 30/90/365-day synthetic fixture queries **clearly labeled test data**. Unplug/reinsert USB; fill media in a safe test environment; restart/recover; verify reports never silently show old data as new.

## Required evidence in linked issues
1. Model and version matrix.
2. EBPro project revision and screenshot (if genuinely captured).
3. Actual register addresses/command IDs copied from EBPro configured settings.
4. SQL test fixture, expected vs observed rows.
5. HMI logs/diagnostics, results, failure-handling notes.
6. CSV and optional PDF actual files + data reconciliation.
7. PASS/FAIL/BLOCKED per test, dated tester and exact changeset.

No instrumented bench pass may be claimed from reading this protocol.

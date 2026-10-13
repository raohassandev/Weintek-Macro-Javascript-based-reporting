# cMT-FHDX-220 SQL Query — Basic vs Advanced Local SQLite bench plan
**Gate Q02: BLOCKED until physical FHDX-220 OS + supported EBPro version; no test has been run.**

## Non-inference
Vendor documents SQL Query object for the FHDX model class, and SQLite Local USB/SD for some EBPro software, but **this 220 has USB1 only / no SD**. Advanced SQL syntax directed at MySQL/MS SQL may not apply to Local SQLite; an on-device query is the ONLY evidence. JS/macros do not have a claimed arbitrary sqlite.open() API.

## Preparation (offline only)
- Use version-controlled **synthetic** fixture SQLite schema with \`device_id\`, timestamp in UTC, numeric value, quality and source event IDs. Exact schema must match chosen documented Basic SQL Query database layout.
- Define distinct fixture rows: two meter IDs, two months, null/bad-quality intervals, counter reset, anomalous timestamp and a genuine numerical zero.
- Explicit expected results for each filtered query, row count, sample coverage, empty period, invalid request, timeouts. No real site personal or commercial data.
- Reserve SQL request/result/command words **only after** actual EBPro SQL Query object configuration export. Do not invent command register value or asynchronous Macro signature.

## Device procedure — NOT RUN
1. Record rear-label model/OS, EBPro release, USB format and FAT32 local file path confirmed in manufacturer UI.
2. Confirm SQL Query object exists and can configure **Local SQLite on USB1** in the **actual FHDX-220 EBPro project**.
3. Run Basic mode documented query/filter against fixture file. Export original rows and compare to offline truth.
4. Independently attempt Advanced mode a bounded parameterized \`SELECT\` for meter A/B, UTC time range, LIMIT and ordering; capture whether Advanced is offered for Local or explicitly disallowed.
5. Repeat: no matching records, disabled USB, invalid syntax, lost USB during request, rapid meter changes and stale responses. Fail closed and show no data; do not reuse previous meter's rows.
6. Record whether SQL Query can reach **native HMI Data Sampling tables**, which is separate from general local SQLite file querying.
7. If Advanced Local mode fails, mark it **UNSUPPORTED** and independently test native History Data Display/Trend Display/Data Sampling + on-Weintek aggregation/CSV for the contracted limited report. Do not claim equivalent custom SQL and do not introduce external server.

## Evidence record required
- Exact model OS + EBPro, query object screenshots & config, actual SQL text/source path, USB1 media identity, timestamps, bytes, expected/observed row sets, error codes, time to complete, no-data behavior.
- Every feature individually \`PASS | FAIL | BLOCKED | NOT_RUN\`; no implied PASS from documentation.
- Feature disposition goes to Q02 / #3, affects customer report acceptance in #8.

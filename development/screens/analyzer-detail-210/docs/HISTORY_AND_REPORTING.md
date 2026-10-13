# History / SQL Query: operator UI vs engineer runtime
Visible operator controls: Analyzer, Parameter, From, To, Show History, verified Export CSV, Results table, quality and missing interval context. **Never show SQL statements, file paths, development registers, Modbus/slave/IP or source credentials on the user-facing screen.**
- Q02: SQL Query object existence is documented, but arbitrary Advanced custom SQL on **USB1 Local SQLite** on cMT-FHDX-220 unverified.
- Bind only to actual persisted historical data with device ID/timestamp/quality; client private selected meter must not retarget logger and old returned results from previous meter must be discarded.
- Date range bounded, maximum result rows paginated, read-only query controls, user role and source authorization; signed numeric time zone.
- N/A, measured zero, communication-gap record, recorder unavailable and missing stored interval are distinct statuses.
- kWh period uses verified cumulative meter counter delta/reset/rollover or bounded kW*time trapezoidal integration with a defined no-data policy. See existing tests/fixtures/energy_reference_cases.json.
- Export CSV unavailable until native on-Weintek USB output/readback verified. No on-device PDF generation proof.
- History Data Display/Trend is a candidate alternative if Advanced Local SQLite fails, **not an assumed equivalent native arbitrary-SQL reporter**.

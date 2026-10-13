# User-facing history reporting and SQL Query architecture

**Operator interface:** Analyzer selector, Parameter selector, From/To Date+Time, Interval, Search, Results table, CSV (only after approved on-device test), 24h Trend, 7-day kWh comparison. NO raw SQL/programming/register addresses on user screen.

**Collector invariant:** all 61 commissioned analyzer data sampling channels and incident quality ledger run independent of which Analyzer Detail 210 is currently selected. Live LW/PLW is a snapshot/navigation cache, never the sole historian.

**Time rules:** ISO 8601 UTC internally; local display time zone and shift calendars site config. Results include sample age, quality, source ID, gap status, covered time. Real measured zero != null/timeout. Counter reset/rollover explicit; when cumulative counter crosses communication gap total may be recovered but sub-period distribution remains unknown. Avoid invented interpolation.

**SQL Basic vs Advanced:** Weintek SQL Query Local SQLite USB support documented on some versions, but custom Advanced SQL against Local may not work. **Q02 BLOCKED until on-device test**. Source-specific sqlite table naming/schema, date filter, LIMIT/Pagination, and write/backup API cannot be assumed. `SELECT` in project may be possible only with supported SQL Query object; never call a made-up JS `sqlite.open()`. No external IPC/PC report server.

**Security/speed:** UAC role, immutable metric allowlist, bounded request time window (example 31 days, not a signed customer limit), row cap/page index, monotonically increasing client-private request ID. Discard stale results from previous meter/period to prevent data leakage. Show dataset coverage, record time and failure reason. Never show stale rows as current success.

**CSV/PDF:** Native Weintek CSV/backup remains NOT_RUN (Q10); PDF Reader does NOT imply a native PDF report generator (Q04/Q12). Physical USB2 host one, SD none. User-approved output contract required.

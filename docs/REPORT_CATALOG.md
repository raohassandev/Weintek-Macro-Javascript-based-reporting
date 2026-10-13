# Universal historian report catalog
**Scope:** Requirements-level catalog / proposed portable templates. No report in this table is production-verified on a target Weintek HMI. [Visual Plan](VISUAL_PLAN.md) · [Site profile](SITE_PROFILE_GUIDE.md) · [Command Centre](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1).

## Report-type primitives (site-independent)
- **Instantaneous sampling:** temperature, kW, Hz, voltage, pressure, flow rate; may aggregate AVG/MIN/MAX over defined time windows.
- **Monotonic/cumulative counter:** import kWh, production counts, operating hours, water m³; calculate period **delta**, accounting for rollover/reset.
- **State and event:** run/off/trip, circuit-breaker events, alarm active/ack/cleared, operator action; compute time durations, counts and event chronologies.
- **Batch/transaction:** LPG fills, production batches, cycle ID, customer, start/stop, quantities; requires transaction records, not only periodically sampled floats.
- **Derived KPI:** efficiency, diesel/gas running load, solar utilization, OEE, runtime, consumption per product. Each formula must be defined and tested with site-specific tags.

## Universal report menu
| ID | Report | Inputs (generic) | Computation | Example site / notes |
|---|---|---|---|---|
| RPT-01 | Raw timestamped history | sampled metrics | rows, timestamp, units, source quality | Any |
| RPT-02 | Trend chart | sampling series | time-series view; zoom/window | Any |
| RPT-03 | Daily readings summary | instantaneous metrics | avg/min/max/sample-count/quality | Temp, power, process |
| RPT-04 | Monthly readings summary | instantaneous metrics | period rollup, missing-data indicator | Any |
| RPT-05 | Day/week/month energy | kWh counters or integrated kW | delta / validated integration | Solar, Grid, DG |
| RPT-06 | Import/export energy | directional counters (or signed kW with integral rule) | import/export separately | Grid / net metering |
| RPT-07 | Generation/load comparison | source kW/kWh | grid/diesel/solar/load aligned period | PV–DG |
| RPT-08 | Peak demand / demand profile | kW instantaneous or demand value | max and timestamp, interval average as defined | Factory |
| RPT-09 | Voltage/current/frequency/PF | V/A/Hz/PF samples | avg/min/max / threshold excursions | Power quality |
| RPT-10 | Equipment run/stop hours | state transitions or hour meter | elapsed ON time and cycles | Generator / pumps |
| RPT-11 | Alarm / trip log | alarm events | raised/cleared/ack, duration, occurrence | Any |
| RPT-12 | Operator audit trail | timestamp, actor, action | event listing/filter | Controlled systems |
| RPT-13 | Production / shift totals | cycle count/counter, shift calendar | per-shift deltas/quantities | Industrial lines |
| RPT-14 | Batch / filling history | transaction records | tare, target, actual, batch start/stop, variance | LPG / weighing |
| RPT-15 | Environmental/process report | temp/pressure/flow/humidity tags | average, excursions, process status | HVAC/process |
| RPT-16 | Consumption vs output | energy + quantity produced | kWh/unit; denominator > 0 | Factory |
| RPT-17 | Generator fuel KPI | fuel volume/rate, energy, status | litres/kWh, runtime, load percentage | DG monitoring |
| RPT-18 | UPS / power outage timeline | power status, battery, alarm | uptime, outages, duration, runtime | UPS fleet |
| RPT-19 | Data quality / missing-data report | quality/stale flags/timestamps | gaps, %coverage, bad-value count | Any |
| RPT-20 | Comparison periods | any validated KPI | today/yesterday, month/month, shift/shift | Any |
| RPT-21 | Custom search & drilldown | report parameters + tag selection | bounded date range, device/site filter, paging | Any |
| RPT-22 | Customer-formatted compliance report | chosen metrics + approved template | controlled layout with signoff | PDF/print via proven route |

## Portability and implementation levels
| Tier | Target | Expected feature family | Caveat |
|---|---|---|---|
| T0 Native | Weintek standard Data Sampling + History Data Display + events | history/trend/alarm/backup, common tag values | Confirm exact HMI model and volume limits |
| T1 Enhanced HMI | Supported cMT + SQL Query object + supported Macro/JS | filtered/paged records and bounded calculated summaries | Local SQLite and Advanced Mode combination **not yet proven**; no direct SQLite API assumed |
| T2 External reporting | PC/IPC collector + SQLite/SQL + report renderer | cross-device/cross-site, longer retention, batch joins, advanced aggregations, XLSX/PDF/scheduled print | Separate runtime, storage backup and support cost; HMI integration proof required |

**Capability labels for actual deployments:** `UNTESTED`, `DOCUMENTED`, `SIMULATOR_PASS`, `DEVICE_PASS`, `CUSTOMER_ACCEPTED`. Actual site report `available=true` only when source tags, formula, storage and renderer are valid and accepted.

## Report query request (abstract, not a Weintek SQL command)
```json
{
  "site_id": "example-solar-a",
  "report_id": "RPT-05",
  "device_ids": ["grid-meter-1", "solar-inverter-1"],
  "metric_ids": ["grid_import_kwh", "solar_generation_kwh"],
  "period": {"type": "calendar_day", "timezone": "Asia/Karachi", "date": "2026-10-12"},
  "page": {"size": 50, "cursor": null},
  "output": "screen"
}
```
This request API is a **proposed contract** for an eventual service, not an implemented API or the syntax of Weintek's SQL Query object.

## Correctness requirements
- **Never SUM(kW) as kWh.** A kW interval integral must use actual elapsed time, coverage and reset/gap policies. Cumulative kWh with reset/rollover must be treated explicitly.
- Averaging power factor and other derived ratios can be misleading; each formula requires documented definition.
- Shift boundaries, local timezone, DST, counter day cutoffs and missing data must be configurable.
- Alarms with unavailable clear time are **ongoing**, not a fabricated duration.
- A report should indicate quantity, unit, time bounds, source devices, computation method and %coverage.

## Practical recommendation
Begin with RPT-01/02/03/05/11/19 as the common core. Additional templates activate through configuration and after source evidence. More advanced presentation cannot be promised on Basic series HMIs.

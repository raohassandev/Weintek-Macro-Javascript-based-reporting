# Requirements and verified acceptance criteria
**Status:** draft baseline. Customer-specific fields, quantities, dates and report templates require confirmation. Unspecified = **TBD**, not implicitly accepted.

| ID | Requirement | Definition of test/acceptance |
|---|---|---|
| R01 | Confirm target Weintek model and EBPro release | Photo of exact SKU + firmware versions; matrix against published feature guide |
| R02 | Acquire and time-stamp values | Known source tag/units/quality, end-to-end 24h test or negotiated representative duration |
| R03 | Keep history and recover power/USB events | Repeatable persistence, power cut and storage failure behavior, no silent false data |
| R04 | Pick historical start/end range | Inclusive/exclusive boundaries specified, invalid ranges rejected |
| R05 | Filter device/tag/site | Only selected device/time data returned; isolation test |
| R06 | Daily/monthly summary | Reference calculation matches independently computed fixture |
| R07 | Energy reports | kWh from kWh counter delta or integrated kW × elapsed time, gaps/resets covered |
| R08 | Paginated history table | Stable order, bounded rows, 30/90/365-day range test |
| R09 | SQL Query control bridge | Versioned HMI addresses, triggers, status, result, timeout and error checks |
| R10 | JavaScript and/or macros | Proof on compatible SKU and EBPro version, no undocumented SQLite APIs |
| R11 | CSV/Excel-compatible export | Valid file opens in spreadsheet and reconciles to dataset |
| R12 | PDF / printing if contracted | Branded multi-page sample with generator identity and explicit dependencies |
| R13 | Security/privacy | Unauthorized access/export rejected; credentials excluded from repo |
| R14 | Deployment and handover | Restore/upgrade guide, full traceable test record and customer signoff |

## Report specification (fill only with customer-confirmed facts)
- Site / industry: **TBD**
- HMI on-site exact model: **TBD** (owner previously wrote “cmt 1102 or 1106”)
- EBPro / OS version: **TBD**
- Tags and units: **TBD**
- Data interval: **TBD**
- Retention / maximum file size: **TBD**
- Reporting windows, max rows, date/time zone: **TBD**
- Required formats: **TBD** (HMI display, CSV, PDF/print not yet selected)
- Report header/footer, logo, user permissions: **TBD**
- Delivery target, acceptance signatory: **TBD**

## Reporting correctness guidance
Real power kW is an instantaneous value. `SUM(kW)` is not kWh. Daily energy from counters needs reset/overflow logic; sampled power requires time integration with irregular sampling and missing periods correctly handled. UTC vs site-local day cutover must be explicit.

## Evidence model
Acceptance item can be **DOC-VERIFIED**, **SIMULATOR-PASS**, **DEVICE-PASS**, **CUSTOMER-ACCEPTED** or **BLOCKED**. Simulator-only evidence cannot be promoted to DEVICE-PASS.

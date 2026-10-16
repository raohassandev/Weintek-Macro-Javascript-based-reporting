# Active pilot decision — Haiwell PLC external tags → native Weintek Historian

**Recorded:** 2026-10-16 (owner direction)  
**Status:** APPROVED DESIGN DIRECTION / PLANNING ONLY. No EBPro project, native Data Sampling or hardware proof has yet been executed here.  
**Supersedes:** [Macro/JS-first polling proposal](EBPRO_MODBUS_MACRO_JS_PILOT_BASELINE.md); this replaces its pilot acquisition design, not the long-term product requirements.  
**Related existing work:** [Historian #4](https://github.com/raohassandev/Weintek-EMS/issues/4), [Always-on 61-meter historian #17](https://github.com/raohassandev/Weintek-EMS/issues/17), [2-meter on-HMI implementation #28](https://github.com/raohassandev/Weintek-EMS/issues/28), [Command Centre #1](https://github.com/raohassandev/Weintek-EMS/issues/1), [Memory contract](../docs/WEINTEK_MEMORY_CONTRACT.md).

## Decision: first bench is one Haiwell PLC
1. The owner will create **one EasyBuilder Pro project** for the previously selected **cMT-FHDX-220** unless they explicitly change HMI model. Exact EBPro version, installed firmware/OS, and real hardware System Info still need to be recorded.
2. Add **Haiwell PLC** as an external device in **System Parameter Settings** using its real verified driver / Modbus TCP or RTU channel; do not assume a particular Haiwell PLC model, port, IP, slave ID or memory/register address.
3. Create **direct external device tags** in EBPro Address Tag Library. Bind native live HMI objects directly to these tags; **do not mirror all live tags into LW** for this pilot.
4. Configure EBPro **native Data Sampling** to acquire the external Haiwell PLC tag set **independently of screen navigation**. Use native Trend Display, History Data Display and documented Backup/CSV workflows as capabilities are demonstrated.
5. **No Macro-based Modbus polling and no JS polling/cache** in pilot H0. Macro/JS are deferred for downstream advanced reporting or specifically justified transformations only. Avoid introducing undocumented SQLite/PDF APIs.
6. Maintain Weintek-only **deployed runtime**; desktop PC may be used for EBPro development/testing, but not as historian/reporting service.
7. Historical-data quality and durability are first-class deliverables. A PLC communication failure can cause a native sampler to log a stale cached value; **this is an acceptance risk to test**, not a claim that native sampling intrinsically encodes NULL/gaps.
8. Prior **implementation HOLD/evidence gates** are not silently lifted by this planning decision. An actual EBPro build/download/test requires the owner's explicit implementation authorization and a known device/software baseline.

## Pilot data contract — exact addresses intentionally TBD
Use a deliberately small, read-only profile first. Never invent device register addresses.

| Logical tag | Source | Type / purpose | Acceptance |
|---|---|---|---|
| `PLC_HEARTBEAT` | Haiwell PLC generated changing value | UInt16 or UInt32; progresses at known interval | Detect frozen/unrefreshed PLC data; verify progression over real wire |
| `PLC_UPTIME_OR_COUNTER` (if available) | Haiwell PLC | Independent monotonically changing evidence | Differentiate actual fresh reads from reused old screen value |
| `LIVE_POWER_KW` | PLC mapped measurement/safe simulated value | Vendor-confirmed type/scaling/sign | Exact read, chart, raw vs engineering units |
| `IMPORT_KWH` | PLC counter, if supported | Proper 32/64-bit register interpretation | Counter delta test; reset/rollover/discontinuity handling |
| `TEST_PROCESS_VALUE` | PLC controllable known value | Safe test input | Values 0, negative where valid, step changes and unchanged |
| `PLC_COMM_STATUS` | EBPro verified driver/system diagnostics (if available) | Quality indicator | Document true proven status; do not fabricate a built-in validity tag |
| `HIST_CONTROL/STATUS` | Local HMI system and user registers | Native Data Sampling status/config, bounded allocation | No collision with existing LW/LB/PLW allocations |

Store physical address, driver, datatype, endianness, scaling, unit, source, expected sample period and proof screenshot in a future `haiwell-tag-map.csv` once actually configured. Never equate a stable process value with a communication timeout.

## H0 plan — historian maturity before scaling
### H0-A: Environment + direct tag proof
- Record HMI nameplate/system info and EBPro version; confirm PLC model, transport and valid register map.
- Establish one Haiwell device in EBPro; verify tagged live screen values on real device/simulator and compare against PLC reference.
- Confirm polling/data update performance and verify heartbeat independently from process value.

### H0-B: Data Sampling + visualization
- Native `Data/History → Data Sampling`, time-based (initial *proposal*: 10-second sample interval, change only after measurement), read direct external tag/addresses as supported by the selected driver.
- Record exact data type, offset and source configuration; verify whether mixed/noncontiguous addresses work on this driver.
- Configure History Data Display and Trend Display for same sampling object; enforce monotonic time and timezone policy.
- Verify sampling **continues without an open meter-detail screen or connected Viewer**; compare record counts/timestamps across screens.

### H0-C: Durable history and restore
- Compare supported internal HMI history options to USB1 storage/sync on real cMT-FHDX-220. It has **one USB2 port and no SD slot**. No assumption that USB SSD is supported until tested.
- Prove first/last persisted timestamp, post-power-cycle retention, data export and re-opened history viewer.
- Test controlled USB unplug/reinsert, media full, safe removal (if supported on exact OS), backup/restore, and write failure notification. Never present a USB-presence bit as proof a record was written.
- Record media state, actual on-device retention behavior and file format; don't assume a user-openable native SQLite database or PDF creation.

### H0-D: Data-integrity fault matrix (mandatory)
| ID | Injected case | Required observation and evidence |
|---|---|---|
| H01 | Stable process value, healthy PLC heartbeat | Repeated same value is **valid**, not automatically fault |
| H02 | Known step change at PLC | Historian follows new value within measured latency |
| H03 | PLC network loss / RTU line interrupted | Document timeout/quality behavior; prove whether sampler wrote stale value; flag uncertain records and never call them measured zero |
| H04 | PLC powered off / restarted | Preserve downtime interval, alarm/event evidence where native features support it; validate reset behavior |
| H05 | HMI screen change / all viewers disconnected | Sampling continues and records remain browseable |
| H06 | HMI reboot / power-cycle | Verify persisted history, restart sequence, gap evidence and no duplicate timestamps |
| H07 | USB absent / removed / full / reinserted | Defined storage error and recovery, compare lost/retained records |
| H08 | HMI date/time change / midnight boundary | Timestamp order and date filtering; explicit timezone |
| H09 | PLC value zero vs invalid communication | Real zero distinguishable from stale/failed acquisition in reports |
| H10 | Counter reset/rollover/negative power | Correct energy delta handling; **never SUM(kW) as kWh** |
| H11 | Native history CSV/backup/reopen | Actual exported rows equal recorded values/timestamps, accounting for documented formats |
| H12 | 24h sustained logging (future bench) | Bounded storage growth, latency distribution, no silent freezes |

If native EBPro sampling cannot faithfully mark bad PLC readings, log the **specific gap in capability** and propose the smallest *separately authorized* heartbeat/quality tagging method or alternate native mechanism. Do **not** quietly add a Macro polling engine.

### H0-E: Exit/scale-up gate
H0 is *not* 'mature' until H01–H11 have **real evidence**, duration/volume H12 is characterized, historian data survive tested restart/storage conditions, and independent reviewer checks exports and faults. Then stage second meter, additional metrics and eventually 61 analyzers. Native record limits, channel-count ceiling, long retention and 61-meter throughput remain unproven until measured.

## Records to produce from actual build
- `H0_ENVIRONMENT.md` — model/firmware/EBPro versions and driver settings without credentials.
- `haiwell-tag-map.csv` — actual EBPro-tested external addresses/types/scales, no guessed registers.
- `H0_DATA_SAMPLING.md` — screenshots/config and storage path/retention details.
- `H0_TEST_RESULTS.md` — each H01–H12 PASS/FAIL/BLOCKED/NOT_RUN, exact test time, machine/model and artifacts.
- Native project (.cmtp/.emtp as applicable), exported CSV sample (redacted if customer/private), USB behavior measurements and reproducible handoff.

## Manufacturer source / limitations
- [Weintek EasyBuilder Pro V6.10.01 — Data Sampling chapter](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter-08-Data-Sampling-UserManual-eng.pdf) describes sampling sources, time/trigger modes, cMT address/data-record settings, HMI/USB history destinations, status words, and native History Data Display/Trend Display. Exact feature availability and behaviors need proof on target firmware.
- [FHDX-220 constraints](../docs/HARDWARE_TARGET_FHDX_220.md); [single USB risk](../docs/FHDX220_SINGLE_USB_STORAGE_RISK.md).

**Explicitly NOT DONE:** We did not create an EBPro project, configure a real PLC, run data sampling, prove communications-loss quality, perform a hardware durability test, or change the approved native hardware. This document is the plan for those tasks, not their result.

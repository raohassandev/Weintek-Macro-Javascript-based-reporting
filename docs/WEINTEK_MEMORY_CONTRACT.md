# UCS FHDX-220 — Weintek Register/Tag Allocation Design (PRE-EBPro)
**Model:** cMT-FHDX-220. **Authority:** EBPro address tag library + [machine-readable proposed map](../contracts/meter-memory-map.json); final offset correctness must be checked on the actual .cmtp project and EBPro version.
**Not a compiled native import map**. [Screen template design](DYNAMIC_SCREEN_ARCHITECTURE.md) · [Hardware](HARDWARE_TARGET_FHDX_220.md).

## Relevant Weintek register families
| Register class | Role in proposed architecture | Caution |
|---|---|---|
| `LW` | Shared, volatile, normalized meter snapshots and application state | User word range considered `0..8999` on referenced EBPro docs; `9000+` system words require documentation; live map only `256..8063` |
| `LB` | Shared bits/status, used only with explicit manufacturer support | System `LB-9000+` not safe as user allocation |
| `PLW` / `PLB` | Viewer client-private selection/filters/popup state | Private indexing does not automatically work on PLW objects; verify across FHDX-220 cMT Viewer clients |
| `RW` / `RW_A` | Bounded infrequent retentive commissioning data where vendor supports | No high-frequency historian writes (endurance) |
| `PRW` | Optional retentive client preference when supported | Not site-wide config / storage |
| `LW_Bit`/`RW_Bit`/`RBI` | Defined bit-on-word variants, only if present in EBPro build | Do **not** assume a universal `RB` memory family |
| `LW-9200` | **Global** Index Register 0, system reserved | Not suitable for separate client navigation |
| `PLW-9200` | **Private** Index Register 0, system reserved | Only documented role and supported client modes |

## Proposed 61 × 128-word normalized LIVE cache (not history)
```text
  METER-001: LW-256  .. LW-383
  METER-002: LW-384  .. LW-511
  METER-037: LW-4864 .. LW-4991
  METER-061: LW-7936 .. LW-8063
  61 × 128 = 7808 words; last address 8063, below 9000 system start
  Active power: base LW-264 + (N-1)×128
```
Metadata offsets, phase voltages/currents, kW/kvar/kVA, PF, Hz, per-phase metrics, THD where available, energy counters and timestamps are specified in the JSON. Every numerical field has an explicit word count/data type. Remaining offsets 94–127 are reserved.

### Separate proposed application state region
- `PLW-100`: selected meter per Viewer (proposal, check for preexisting UAC/SQL objects before allocating).
- `PLW-9200`: *system* Private Index 0, `(meterId−1)×128`, not for ordinary app settings.
- `LW-8250`: USB probe state; `8251`: independent proof age; `8252`: recorder proof; `8253`: last persisted record age; `LW-8270`: combined health. **These are examples already used by earlier proposed Macro**, not proven collision-free in a live EBPro project.
- `LW-8064..8999`: other application words **only after allocation ledger** (do not auto-fill). App memory and JS buffer pressure require actual 220 benchmark.
- System tag examples in [Resource Manager](RESOURCE_STORAGE_MANAGER_SCREEN.md): `LW-9025` CPU, `LW-11159` memory loading, `LW-9076` USB1 free, `LB-12048` USB1 present, `LW-11458/11460` HMI history total/free where exact OS supports. Values/widths need Address Tag Library verification; physical USB with no media is **not** storage working.
- cMT-FHDX-220 **has no SD/microSD**: don't allocate/routinely poll SD-present/free registers for site UI; never show such a panel.

### Data types and field quality
- `UInt16`: 1 word; `UInt32`/`Float32`: 2 words; `Float64`: 4 words (careful word order and precision). A source Modbus 64-bit integer may need safe conversion before HMI display.
- Source Modbus address and word order vary by device driver. Do not map raw register addresses into generic UI offsets directly.
- `UNSUPPORTED` is not zero. `COMM_TIMEOUT`/bad quality marks stale/last good, not current power.
- `RW` retention is not a replacement for a proper history log or FAT32 storage. Site profiles (driver/tag lists) use a versioned schema, safe Apply/Verify/Rollback.
- No identical screens ×61; per-client indexed live data + **separately proven** per-meter historical selector.

## EBPro Commissioning Gate
1. Record exact cMT-FHDX-220 firmware/OS and EasyBuilder Pro version.
2. Inspect EBPro Project → Address Tag Library and System Tags; export **actual native CSV** before generating imports; generic repository `tags/resource-manager-dictionary.csv` is NOT directly import-ready.
3. Reserve used addresses from other objects (SQL query/status, data sampling, UAC/security, alarms, function keys).
4. Compile on exact EBPro and test two independent cMT Viewer clients, 2 meter device drivers, last meter index, invalid 0/62, 32/64-bit field endian and overlay.
5. Produce a tagged register-allocation manifest and objective logs. Until then, memory layout is **PROPOSED**, not device validated.

## Vendor primary references
[Weintek EBPro Index Register manual](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter-11-Index-Register-UserManual-eng.pdf) · [System Register manual](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter-22-System-Registers-UserManual-eng.pdf) · [Address Tag Library manual](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter-16-Address-Tag-Library-UserManual-eng.pdf).

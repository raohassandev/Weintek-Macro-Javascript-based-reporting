# EasyBuilder Pro Object-by-object — Analyzer Detail 210
**Plan only.** No .cmtp/.emtp compiled or actual cMT-FHDX-220 System Information received.

1. Create **one** 1920×1080 EBPro window (proposed #210; check for project ID collisions). Add `assets/background-only.png` as a static full-screen **Picture** with topmost value overlay areas left blank. **Do not** use preview as the live background.
2. Use `tags/native_object_map.csv` coordinates to insert **Numeric Display** objects for 24 phase cells and counter/demand/frequency panels. Format Float32/Float64 with correct vendor endianness and units. Capability missing = **N/A**, never 0.
3. Use **Function Key / Set Word / Combo Box** for client-selected meter slot 1..61 (proposed `PLW-100`). Index private Weintek `PLW-9200` offset = `(meterID-1)*128`; confirm supported local context and two Viewer isolation. **Not** global LW-9200. Macro example is uncompiled.
4. Use **Word/Bit Lamp** for data quality and communication stale status from the *normalized cache*, not LED color baked into the picture. Last valid age/timestamp in separate Numeric/Text display. Do not infer breaker energization from sample age.
5. Use actual **Trend Display / History Data Display** bound to per-device native Data Sampling, not merely indexed live LW. A private index is NOT proof that a historical Trend object retargets automatically.
6. Historical filter widgets: **Combo Box, Date/Time, Numeric Input**, backed by bounded per-client request state. Operator does **not** see raw SQL. Actual **SQL Query object** Basic/Advanced Local path and arbitrary query support Q02 need device proof.
7. Historical results: native **SQL Query result/History Data Display** only after proven on target model, with timestamp, L1/L2/L3, total, unit, quality and period coverage. **Export CSV** via native supported Backup/Function Key ONLY when actual USB1 file and readback succeed. No PDF-generation button.
8. Maintenance computed insight: using GOOD finite phase values and documented formulas only; missing phase, near-zero denominator and unsupported harmonics produce **N/A**. Pure JS reference is **offline logic**, not a deployed JS Object yet.
9. Native **Event/Alarm Display** belongs to Alarm Centre drilldown. Don't simulate alarm persistence with styled HTML or a static PNG.
10. Enforce **Weintek UAC** at action/data boundaries. No device control writes from reporting. USB1 (single port) and SD absence always respected.

**Import caution:** `screen_tag_contract.csv` / `normalized_lw_61_meter_manifest.csv` are engineering registries, not EBPro's native import file formats; match to an **actual EBPro Address Tag Library export** for this software version. Display assets are useful **now**, but all runtime behavior remains **NOT_RUN / BLOCKED** pending owner approval and real firmware data.

**Version-sensitive:** `PLW` Private Index, Macro syntax, SQL Query and JS Action device context must be validated in real EBPro. HMI product model alone does not prove these calls are compiled/tested.

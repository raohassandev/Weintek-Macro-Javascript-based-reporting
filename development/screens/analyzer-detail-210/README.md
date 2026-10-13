# Analyzer Detail 210 — Weintek FHDX-220 reusable UI pack
**Engineering source / OFFLINE concept, NOT a compiled EasyBuilder Pro project.** 1920×1080 optimized for an approximately 44-inch HDMI display with light off-white + deep forest/soft-gradient engineering theme.

**First screen:** [Preview](assets/preview.png) · [Background-only](assets/background-only.png) (when renderer CI has run). The background keeps phase names, units, borders and controls positions but **no fake numerical values, alarms, historic SQL results or chart curves**. Overlay live objects in EBPro.

- Phase L1/L2/L3: V(L-N/L-L), A, kW, kvar, kVA, PF, V-THD, optional other supported parameters only.
- Import/export cumulative counters, peak demand, frequency.
- Historical sample snapshot + persisted trend; missing data always visible, native Data Sampling independent of selected meter.
- User-facing History filters/query results with **no SQL syntax/schema/network credentials displayed**; actual Local SQLite Advanced Mode Q02 unproven.
- Maintenance insight: voltage/current imbalance only if 3 valid phase values and approved formula; coverage only from actual stored history.
- NO operator-facing device health/IP/settings card. Technical metadata lives in authorized Diagnostics 410, not Meter Detail.
- NO generic alarm cards or fictional alarm truth. Use native Weintek Event/Alarm Display in event windows and audited status.
- One shared window selected by **client-private PLW**, not 61 duplicated windows; target PLW-100/PLW-9200 semantics require device proof.
- [Native object mapping](tags/native_object_map.csv), [Tag contract](tags/screen_tag_contract.csv), [all-meter volatile snapshot manifest](tags/normalized_lw_61_meter_manifest.csv), [EBPro object guide](docs/EBPRO_OBJECT_BY_OBJECT.md), [history/SQL limitations](docs/HISTORY_AND_REPORTING.md), [JS pure reference](scripts/meter_analytics.js), [guarded Macro proposals](macros/).

**No physically validated device measurements or EBPro compilation**. Do not claim live HMI deployment. Permission and current GATE-1 approval remain distinct from production acceptance.

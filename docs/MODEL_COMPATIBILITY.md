# Verified/pending model capability matrix — 2026-10-13

**Status keys:** DOCUMENTED means manufacturer material directly indicates support, NOT a physical successful test; RESEARCH means evidence incomplete; NO means excluded by available official feature material; DEVICE-PASS only after actual bench execution. No device has passed testing yet.

| Model | Series | Macro | JS Object/Action | SQL Query | Controlled SQLite on USB/SD through SQL Query | Device tested |
|---|---|---|---|---|---|---|
| cMT1106X | Basic | DOCUMENTED baseline | NO (feature matrix) | NO | NO via SQL Query | NO |
| cMT2102X | Standard (new) | To confirm in exact EBPro | DOCUMENTED (Weintek product news) | RESEARCH (not asserted) | RESEARCH | NO |
| cMT3102X | Advanced | EXPECTED, verify EBPro | DOCUMENTED | DOCUMENTED | FEATURE documented at series level; model bench pending | NO |
| cMT3108XH | Advanced | EXPECTED, verify EBPro | DOCUMENTED from feature matrix, version check | DOCUMENTED | FEATURE documented at series level; model bench pending | NO |
| cMT-SVRX-820/822 | Headless | EXPECTED, verify EBPro | Feature matrix says supported; verify firmware | DOCUMENTED | FEATURE documented at series level; device bench pending | NO |

**Model mismatch:** the owner said `cMT1102`, but the current Weintek download list shows `cMT2102X`, `cMT1106X`, etc. This is **not evidence** that the installed product is cMT2102X. Obtain rear-label/photo.

**Key distinction:** No row endorses general direct SQLite file access from JavaScript or Macro. Separate SQL Query object on a compatible HMI may use selected local SQLite USB/SD files; verify with a deliberately created sample DB and target OS.

## Manufacturer evidence
- https://www.weintek.com/Product/Series/cMT-X-Standard — confirms cMT2102X is cMT X Standard.
- https://www.weintek.com/About/NewsDetail/ProductNews-Vol.64 — cMT2102X JavaScript feature.
- https://www.weintek.com/Product/Model/cMT1106X — cMT1106X official product data.
- https://forum.weintek.com/cmt1106x-basic-hmi-model/ — Basic series guidance to use more advanced models for SQL.
- https://dl.weintek.com/public/cMT/eng/Brochure/cMT_Brochure_ENG.pdf — cMT3102X, cMT3108XH, SVRX SQL Query support.
- https://dl.weintek.com/EBPro/ReleaseNote/EBProV60102_ReleaseNotes_en.pdf — local USB/SD SQLite SQL Query.
- https://dl.weintek.com/public/Document/JS_Object_SDK/Current/index.html — JS SDK boundary.

## Completion blockers (#2)
Exact HMI model; OS version; current EBPro version; readable sample SQLite database and source HMI program. To mark a model DEVICE-PASS, archive reproducible original EBPro project reference, device OS, media type, command results, and error-path run.

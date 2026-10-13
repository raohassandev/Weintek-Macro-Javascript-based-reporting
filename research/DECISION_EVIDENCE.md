# Evidence interpretation — important R&D cautions
## 1. Weintek local SQLite vs advanced custom SQL are not the same claim
- Manufacturer V6.01.02 release notes state **SQL Query gained access to SQLite on USB/SD**.
- EasyBuilder Pro manuals describe **Advanced Mode** as free-written SQL to control MySQL/MS SQL servers and have a separate **Local** SQLite choice on General tab. This is ambiguous as to arbitrary SQL on *Local* SQLite.
- The 2018 feature screenshot shows **Advanced mode unchecked** with local `cMT3090/datalog/TH_data.db`; therefore local SQLite access alone **does not prove** Advanced Mode custom expressions or unrestricted access to arbitrary internal DBs.
- Prior conversation initially described cMT3102X + local SQLite Advanced Mode too confidently; **correct engineering status is pending targeted validation** [Q02](OPEN_QUESTIONS.md).
- Until proven, support HMI-native History Data Display and CSV through officially documented routes, or external SQL reporting service for arbitrary aggregates.

## 2. JavaScript and Macro are not general SQLite runtimes
- The manufacturer JS SDK supports reading/writing device addresses with `driver.getData` / `driver.setData`; no documented `sqlite.open`/arbitrary file access in consulted SDK.
- A WeintekUSA support engineer describes an SQL Query object → HMI registers → Macro operation workflow; not a direct JS database API.
- `RecipeQuery` interacts with **recipe database**, not arbitrary site historian files.

## 3. Native history vs external reporting
- EBPro Data Sampling and History Data Display/Trend Display are documented. Event Log has defined alarm/event source and trigger.
- Native Backup and EasyConverter can provide some CSV exports; file type and version must be proven on target OS and project.
- SQL Sync from native logs to an external SQL server is documented on some cMT/EBPro versions, but HMI model/version/source table details and table naming need validation.
- A branded multipage PDF generally implies separate renderer/printing workflow unless an exact supported feature is proven.

## 4. Portable historian design choices
- A site-specific metric mapping layer must account for Weintek generic `data_format_XX` SQL synchronization columns, if encountered.
- Energy from sampled kW needs interval integration; cumulative kWh uses counter delta with reset/rollover checks. Avoid misleading averages for power factor and alarms.
- Report types and output can be **generally designed** across industries, but no site-specific success can be claimed without actual source data and device proof.

## References
See [SOURCE_REGISTER.json](SOURCE_REGISTER.json) for official links and support qualifications. Research tasks [#2](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/2), [#3](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/3), [#11](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/11), [#12](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/12).

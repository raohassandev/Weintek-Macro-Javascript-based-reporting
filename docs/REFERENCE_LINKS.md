# Weintek reference register
**Use manufacturer-issued documents first.** Feature support is model/firmware/EBPro dependent; do not generalize from an earlier model's brochure.

| Reference | Link | What it supports | Limitation |
|---|---|---|---|
| Current model/download list | https://www.weintek.com/Download/Specification | Lists cMT1106X, cMT2102X, cMT3102X and others | A listed SKU is not proof of site device |
| Quick feature comparison | https://dl.weintek.com/public/cMT/eng/Brochure/cMT_Brochure_ENG.pdf | cMT3102X / Advanced series SQL Query, server features | Published historical version; verify current OS |
| V6.01.02 release notes | https://dl.weintek.com/EBPro/ReleaseNote/EBProV60102_ReleaseNotes_en.pdf | SQL Query support for SQLite DB on USB disk or SD card | Not universal file-system or native historian SQL |
| EBPro user manual V6.10.01 | https://dl.weintek.com/public/EBPro/UserManual/eng/EasyBuilder-Pro-V61001-UserManual-eng.pdf | SQL Query general/advanced configuration and command object | Check exact version and commands |
| SQL Query basic/advanced | https://forum.weintek.com/sql-query-basic-and-advanced-mode/ | Custom SQL filtering, averages and command examples | Verify local SQLite SQL dialect support |
| cMT1106X official product | https://www.weintek.com/Product/Model/cMT1106X | cMT X Basic hardware | Do not infer Advanced SQL/JS |
| cMT1106X official feature discussion | https://forum.weintek.com/cmt1106x-basic-hmi-model/ | Advanced SQL features advised on higher models | An article is not a device test |
| cMT3102X manufacturer feature notes | https://forum.weintek.com/brand-new-10-advanced-hmi-cmt3102x-supports-m02-wifi-expansion-module/ | JS Object and SQL Database called out | Needs firmware/EBPro testing |
| JavaScript SDK | https://dl.weintek.com/public/Document/JS_Object_SDK/Current/index.html | Documented JS Object SDK and register I/O | Do not assume direct SQLite programming |
| Macro reference | https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter-18-Macro-Reference-UserManual-eng.pdf | Macro functions including recipes | RecipeQuery != generic SQLite |

## Verification priority
(1) Confirm installed model label, (2) obtain currently installed EBPro and HMI OS details, (3) consult exact applicable manuals, (4) produce and execute a minimal reproducible EBPro SQL/JS/Macro test, (5) attach real project/evidence to #2/#3/#5/#6.

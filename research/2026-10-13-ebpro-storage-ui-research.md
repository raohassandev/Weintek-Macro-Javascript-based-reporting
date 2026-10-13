# UCS resource monitor — new R&D 2026-10-13
## Actual Weintek-native visual objects
WeintekUSA FAQ documents Bar Graph, Meter Display, XY Plot, Bit Lamp, Word Lamp, Picture View, JS Object and others. EasyBuilder Pro manual documents Trend Display, History Data Display, Data Sampling, Event Display and Backup Trigger-based/Global. **Use genuine supported objects**; attractive chart appearance in a screen concept does not imply a built-in donut chart or arbitrary HTML.

## Practical connected-versus-working matrix
1. Presence = `LB-12048`; no proof of writable filesystem.
2. Available space = `LW-9076` 32-bit KB and `LB-9037` low-space; must show N/A when device absent.
3. Optional **Local HMI** USB file I/O via `@weintek/libc/stdio` + `@weintek/filesystem`, introduced EBPro v6.09.01; copy-bounded readback test in `js/ucs_usb_write_read_probe.js`. Can fail on unsupported FHDX/SVRX model/OS and does not prove disk endurance/durable sync.
4. Writer/recorder success = require independently observed persisted record after storage probe, not simply a USB mount and no error. Tag ages must expire. External historian separate.
5. Backup success = native Backup object, `LB-9039` in-progress; independent verification/proof of backup file, not just started/completed.

## 2026 manufacturer addition: eMMC wear monitoring
**New registers** cMT X with EasyBuilder Pro >= 6.10.02.394 and OS released >= July 15 2026:
- `LW-12835` uint32 internal eMMC write KB/min
- `LW-12837` 16bit measurement status 0..4
- `LW-12824` eMMC health state; specific semantics per model/OS
Only show when System Tag Library supports it; otherwise hide/N/A. Manufacturer warns that sustained high write rate can reduce internal flash life.

## Address Tag CSV import caution
Vendor-confirmed import process is to manually add several known tags, **export** via Address Tag Library with UTF-8, copy exact column formatting and re-import. We will not mark the generic dictionary CSV native-import-ready without actual EBPro export matching target model/release.

## Primary sources
- [WeintekUSA EBPro objects FAQ](https://www.weintekusa.com/faq/)
- [EBPro Address Tag Library manual ch16](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter-16-Address-Tag-Library-UserManual-eng.pdf)
- [Vendor support CSV export/import](https://forum.weintekusa.com/t/why-cant-i-import-my-user-defined-tags-into-easybuilder-pro/624)
- [Weintek JS libc/stdio](https://dl.weintek.com/public/Document/JS_Object_SDK/Current/module-%40weintek_libc_stdio.html)
- [Weintek JS filesystem](https://dl.weintek.com/public/Document/JS_Object_SDK/Current/module-%40weintek_filesystem.html)
- [Weintek eMMC write rate September 2026](https://www.weintek.com/About/NewsDetail/TechNews-Vol.79)
- [EBPro Data Sampling status/error](https://dl.weintek.com/public/EBPro/UserManual/eng/EasyBuilder-Pro-V61001-UserManual-eng.pdf)

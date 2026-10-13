# R&D — HTML / JS rendering **without external PC/IPC** (2026-10-13)
**Research, not a physical device PASS.** Parent [issue #25](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/25).

## Core question
Can an arbitrary `index.html` + CSS/JavaScript on HMI flash/USB/SD be **served, displayed and dynamically connected to meter data**, without another computer?

## Manufacturer-supported categories
| Technology | Renders arbitrary custom HTML? | Weintek model boundary | Verdict for UCS |
|---|---|---|---|
| EasyBuilder **JS Object** | **NO** browser DOM. Canvas, mouse events, customized UI via Weintek JS SDK, register input | cMT X including eligible SVRX/FHDX; compare actual EBPro/OS | **RECOMMENDED**, most portable HMI-only modern UI. Reuses project-native widgets for critical trends/alarm history. |
| **PLC Web Browser** | Can display URL-based web page/PLC web server content; **file:/// USB/SD source unverified** | Advanced cMT X with physical local screen. Appendix A explicitly lists cMT-FHDX-820 in relevant column; SVRX headless/cMT Viewer does NOT imply same embedded browser | **Conditional POC**. CPU intensive and can overlay other objects, incompatibilities. External PLC HTTP source might exist but cannot add separate PC web server. |
| **EasyWeb 2.0 / WebView** | Presents HMI UI to remote browser; not documented arbitrary HTML host/servlet | Both supported on relevant cMT X models | **NOT a custom HTML app hosting route**. |
| `cMT-FHDX-820 (W)` **HTML5 Web Panel** | **YES**, Chromium 132 browser, standard HTML5 websites | **Different product** from EBPro cMT-FHDX-820 | Browser-display device, NOT a proven EBPro historian/data acquisition platform. Needs an HTML source URL. HMI-only offline `file://` or USB web hosting not validated; cannot replace usual SVRX logic by assuming it. |
| USB/SD file | can store data and HTML bytes (model filesystem permissions) | Weintek media support & JS local-file API model/OS dependent | **Storage does not imply an HTML renderer nor HTTP server.** |

**High-risk distinction:** Manufacturer presentation "HTML5 Web Panel" is not a guarantee that the **same hardware** also runs an EasyBuilder Pro HMI project with 61 native meter drivers/Data Sampling. An HTML page can look excellent, but it needs a browser AND authoritative meter-data bindings/historian/report APIs.

## Recommended UCS-only approach
1. Retain cMT-SVRX/FHDX native EBPro acquisition, background historian and event/backup objects.
2. Use JS Object **Canvas** for branded, reusable interactive charts, menus and management cards; bind to normalized LW and client-private selection where SDK supports. Use Native Trend Display, Event Display, Alarm Display when they provide more reliable history/report features; do not force HTML.
3. Keep decorative Picture (SVG rendered to PNG) and live objects separate. JavaScript won't magically interpret HTML/CSS from USB as embedded EBPro objects.
4. POC `PLC Web Browser` on **actual cMT-FHDX-820** only: check `file:///...` URL & USB path, scripted refresh, local permissions, full-screen behavior, overlay/popups, Viewer mode and CPU load. Record PASS/FAIL. Don't deploy unless all relevant capabilities supported. If no local HTML URL, **do not** add an external PC/IPC web server.
5. Separate `cMT-FHDX-820 (W)` option is allowed only as an **additional Weintek display** if owner permits and a Weintek-only local HTTP/HTML source is proven. Without that, no.
6. Browser lacks the deterministic/native path needed for independent 61-device logging; if HTML is accepted for visualization, Weintek HMI historian/alarms remain independent.

## Offline HTML probe included (NOT claimed to run on Weintek)
[html-poc/index.html](../experiments/html-poc/index.html) shows static HTML5/CSS and a local JS heartbeat. It has **no meter data binding** and may be copied to a FAT32 USB test folder for attempted local browser `file://` validation. If it renders, that proves UI rendering **only**, not live register API or history. Change local clock text via JS to verify script runtime; USB writing/caching/refresh still needs individual tests.

## Actual test matrix required
- cMT-FHDX-820 standard: native PLC Web Browser URL, `file:///...`, CSS styling, Canvas animations, JS local fetch, reload, full-screen event overlay, CPU load, retained project operation.
- cMT-SVRX-820/822: via client cMT Viewer, test whether clicking browser object opens **client browser** (not a server-side HTML renderer). Verify multi-user behavior and security.
- cMT-FHDX-820 (W): verify if local USB HTML can be loaded *as a browser start page*, actual path, persisted settings across boot; distinct from EBPro.
- Data access: whether arbitrary HTML can reach HMI registers via documented protected interface **with no other server**, with authenticated role/security enforcement. No made-up REST API.
- Verify 61-meter Data Sampling runs uninterrupted during complex graphics/browser CPU pressure.
- Record actual firmware, EBPro, start URL, errors, tested media, screenshot and logs in [issue #25](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/25).

## Official references
- [EBPro object manual §13.55 PLC Web Browser](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter-13-Objects-UserManual-eng.pdf): local-display-only and CPU intensive.
- [EBPro 6.10.01 Appendix A feature matrix](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Appendix-A-Comparison-of-HMI-Software-Features-UserManual-eng.pdf): model comparison.
- [EBPro JS Object & JS Library](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter_43_JS_Object_and_JS_Library.pdf) and [JS SDK](https://dl.weintek.com/public/Document/JS_Object_SDK/Current/index.html): Canvas API, no browser DOM.
- [Weintek JS webinar: JS Object `window` isn't browser](https://dl.weintek.com/public/Document/JS_Object_SDK/Current/tutorial-webinar/20201210-Introduction_to_JS_Object.pdf).
- [cMT-FHDX-820 (W)](https://www.weintek.com/Product/Model/cMT-FHDX-820-%28W%29): Chromium HTML5 web panel distinct model.
- [Vendor cMT Viewer JS execution behavior 2026-01-20](https://forum.weintekusa.com/t/cmt-viewer-execution-commands-inquiry/4583).
- [Weintek EasyWeb/WebView](https://forum.weintekusa.com/t/accessing-an-hmi-through-its-web-server/843) remote HMI browser access, not app hosting.

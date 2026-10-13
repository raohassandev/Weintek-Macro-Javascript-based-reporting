# Research: Weintek official Demo Projects catalog
Source: [Weintek DemoProject](https://www.weintek.com/Download/DemoProject), inspected 2026-10-13. Our catalog is in [demo-catalog.json](demo-catalog.json). **We did not download/import EBPro project binaries or claim inspected their source**.

## Priorities for 61-meter UCS
| Priority | Official demo (category / date) | Investigate |
|---|---|---|
| P0 | cMT-FHDX-820 Demo (Application, 2026-08-19) | Supported built-in elements; web browser window on actual standard FHDX |
| P0 | cMT-SVRX-820 Demo (Application, 2023-10-05) | Headless cMT Viewer/screens; don't infer -822 parity automatically |
| P0 | JS object x UAC Demo (Part, 2024-07-04) | User roles, login and menu capabilities |
| P0 | Data Log Customized File Handling (Part, 2026-01-23) | Retention and file rotation |
| P0 | Event Log - Statistics (Part, 2025-11-04) | Role-routed alarms, historical exception totals |
| P0 | Index Function (Part, 2025-05-02) | One reusable meter page |
| P1 | SQL Query Multiple Result Demo (Part, 2021-10-06) | Report tables and command-response handshakes |
| P1 | Trend Display (Part, 2025-10-31) & Show Trend Value with JS Object (2022-12-21) | Native/JS historical visualization |
| P1 | Dynamic Meter Demo (Macro, 2016-12-14) | Dynamic meter value selection |
| P1 | JS Object Read/Write Register Value (Part, 2021-08-18) | Register I/O; beware cMT Viewer client-side JS execution |
| P1 | Security Demo Project (System, 2025-10-01) | Permissions and role menus |
| P2 | Picture View / Action Trigger / Energy Demand / PDF Reader | Decorations, button flows, energy demand; PDF Reader ≠ PDF generator |

## Harvest procedure (engineering)
Open manufacturer's page, choose appropriate `Application`, `Part`, `Macro`, `System` groups. Where manufacturer provides direct project archive, download legally via its official UI, record filename, version, SHA256, project type, tags/objects/examples and copy only allowed derived explanations/code into this repo. Do not claim a binary has been examined until a genuine download succeeds. Unknown project formats and model-specific restrictions require EBPro validation.

## Important display pathways
FHDX-820 **standard** Demo Project image shows a **Web Browser** tile. That confirms manufacturer demonstrates an object concept; it does NOT confirm `file:///usb` support nor that SVRX cMT Viewer can render arbitrary embedded HTML. Compare official EBPro v6.10.02 feature matrix and on-unit test.

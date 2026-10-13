# UCS — one-page owner dashboard (Weintek ONLY)

**Plan finalized for implementation/audit as v1.0 (not hardware-deployed):** [Main Plan](UCS_FINAL_MASTER_PLAN.md) · [AI Handoff](AI_AGENT_EXECUTION_BRIEF.md) · [Acceptance](UCS_REQUIREMENTS_TRACEABILITY.md) · [Work Packages](UCS_DELIVERY_WORKPACKAGES.md)
Aap ko lambi technical reports nahi parhni; yeh 1 screen ka status aur decisions hain. [CC #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1) · [Diagram](VISUAL_PLAN.md) · [Role home UX](ROLE_BASED_UX_PLAN.md) · [HTML R&D](../research/WEINTEK_HTML_FEASIBILITY.md).

## Actual progress — current implementation gates
| Milestone | State |
|---|---|
| Baseline planning M0 | **Complete (documents / CI only)** |
| HMI model/firmware & SQL Q02 M1 | **Blocked: exact model + real test** |
| 2-meter live HMI pilot M2 | **Not run** |
| 61-meter quality-aware historian M4 | **Not run** |
| Report output M5 | **Offline energy fixtures in progress; on-device export not run** |
| Production release M6 | **Not ready; independent audit/customer pending** |

[Independent audit findings](PLAN_AUDIT.md) · [Exact M0–M6 table](UCS_FINAL_MASTER_PLAN.md#12-milestones-and-exit-gates).

## Our implementation boundary
**61 energy analyzers**, **Weintek cMT-SVRX/FHDX**, **USB/SD/qualified USB-SSD**. **No additional computer/server.** Site meter brand, register map, energy units, thresholds and retention are configurable.

```mermaid
flowchart LR
 M["61 Meters"] --> W["Weintek UCS"]
 W --> S["Continuous historian • Alarms • Report logic"]
 W --> H["Operator / Engineer / Manager"]
 S --> USB["Weintek USB/SD/qualified SSD"]
```

## Who sees what?
- **Operator:** 61 meter overview, current electricity flow, active actionable alarms.
- **Engineer:** connectivity faults, device diagnostics, commissioning and maintenance.
- **Manager:** energy KPI, date comparisons, report preview, business-impacting exceptions. Storage utilization is **not** always on this screen.
- **Shared windows:** one indexed meter detail, common trends/reports, deep Resource & Storage Manager.
- **Critical exception:** role-directed popup + persistent event log; routine notices do not spam management.

## HTML result: 3 features, not one
- **JS Object Canvas**: supported customizable visuals in EBPro; NOT arbitrary HTML page execution. **Preferred** for rich UCS views.
- **PLC Web Browser**: selected models' local screen displays URL content; local USB HTML file **not proven**, SVRX headless/cMT Viewer not an equivalent browser.
- **cMT-FHDX-820 (W)**: different Weintek HTML5 Web Panel with Chromium. It is not automatically a native EBPro historian; without approved source/Weintek-only data bindings, do not switch to it.
- EasyWeb/WebView **remote HMI rendering**, not custom HTML server.

## Recent real work (2026-10-13)
- Previous source packs: light-theme management screen SVG, background PNG, object map and register dictionary, USB file test JS; these are *engineering assets*, not fully loaded EBPro project.
- New correction: no PC/IPC; role-specific homes, alarm routing, Weintek demo catalog, [HTML offline experiment](../experiments/html-poc/index.html), pending acceptance.
- Real meter/acquisition, USB HTML, physical HMI file writing, 61-device performance, report completeness **NOT YET ACCEPTED**.

## Human input when needed
Model label and EBPro/firmware when practical; engineering handles vendor manuals, tests, code and board. Do not ask user to type long test logs.

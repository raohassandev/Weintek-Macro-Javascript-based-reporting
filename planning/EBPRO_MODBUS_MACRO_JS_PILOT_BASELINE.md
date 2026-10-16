# EasyBuilder Pro pilot — Modbus channels + Macro/JavaScript architecture (decision draft)

**Date:** 2026-10-16 | **Status:** PLANNING ONLY — no EBPro project or physical device test yet  
**Owner workflow:** Owner creates one EasyBuilder Pro project and configures Modbus communication channels/devices in **System Parameter Settings**. We will then discuss and implement program logic in **Weintek Macro and JavaScript**, subject to the chosen hardware/EBPro version's supported APIs.

## Decisions recorded now
1. **One native EasyBuilder Pro project** is the first implementation vehicle; keep target cMT-FHDX-220 unless owner explicitly changes model.
2. **Communications configuration is owner-managed in EBPro.** The owner will add required Modbus TCP/RTU devices/channels, interface settings, slave IDs, TCP endpoints, timeouts and vendor-specific register drivers as applicable. Do **not** create an imaginary Modbus-stack implementation inside Macro/JS.
3. **All custom application logic is planned in Macro and JS.** Data acquisition bridge, normalization, state management, calculations, user interactions, history/report orchestration and fault handling will be discussed **before coding**. EBPro native device drivers, native HMI objects, data sampling, alarms and other platform facilities may still be necessary; 'all logic in Macro/JS' does not mean replacing unsupported native HMI subsystems.
4. Define an explicit **tag/register contract** between the owner's EBPro communications and our Macro/JS modules; no unverified Modbus addresses or invented EBPro API signatures.
5. Keep the **Weintek-only runtime** requirement: no PC/IPC, Node server or remote database as a runtime dependency.
6. Preserve the approved original Analyzer Detail 210 UI and plant-authentic SLD requirement; do not use rejected generic screen designs.
7. **Implementation remains gated** by available actual EBPro version, device System Info, supported model/API verification, independent review and explicit owner authorization. This document records an approach; it does not override existing implementation HOLDs.

## Proposed separation of responsibilities — for next discussion
| Layer | Responsibility | Proposed owner/implementation |
|---|---|---|
| Physical Modbus transport | Interface, protocol, device address, comms parameters, basic driver | Owner in EBPro System Parameter Settings |
| Raw register tags | EBPro device mappings, scaling assumptions, types/endianness from vendor manuals | Reviewed device/tag specification |
| Acquisition / validity | Freshness, quality, communication timeout, stale vs zero, timestamp, read/write guards | Macro + JS architecture TBD; verify native read status access |
| Normalized meter model | Stable meter ID, canonical metrics, LW/PLW isolation, scaling | Macro/JS + documented tag contract |
| Logic | Calculations, energy counter handling, derived values, validations | Macro vs JS decision pending |
| Presentation | Native EBPro screens and JS Object where supported, shared Analyzer Detail | Native objects + supported JS |
| Historian/SQL/export | Native HMI data sampling, persistence, SQL Query/USB/report orchestration | Feasibility gate: no unsupported direct SQLite/PDF claims |
| Safety | Read-only-first pilot; no Modbus writes or live control until authorized | Explicit approval and interlocks |

## Discussion agenda before any code
- Confirm target HMI model, installed firmware/OS, EBPro version, screen resolution and JS Object/JS Action support.
- Which first **two actual meters** and protocols (TCP or RTU)? Owner supplies communication setup, driver/addresses, datatype/word order and permitted read-only tags.
- Define common raw→normalized memory map, meter selection context (LW/PLW), rate, schedules, scaling, unit conversions.
- Decide which computations live in Macro vs JavaScript, message/state handoff through HMI registers, triggers, busy/done/error, race protection.
- Define offline/disconnect/timeout behavior and logging evidence; no missing-value-as-zero.
- Decide historical sample intervals, long-term storage, USB behavior, CSV deliverables; physically prove disputed features.
- Define minimal first pass: **two-meter read-only bench → live display → quality handling → basic trend/report → evidence**.

## Explicitly not done
- No EBPro `.emtp/.cmtp` created, compiled or downloaded to actual HMI.
- No Modbus channel or device has yet been configured or verified by us.
- No actual Macro/JS architecture or code approved.
- No 61-meter performance, SQLite Advanced Local, PDF creation or USB endurance claims.

**Next step:** review responsibilities and choose Macro-vs-JS orchestration before writing runtime logic. Refer to existing #28 (2-meter slice), #29 (commissioning), #30 (audit) and Command Centre #1.

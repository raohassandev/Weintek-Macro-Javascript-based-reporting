# UCS VISUAL PLAN — WEINTEK-ONLY ARCHITECTURE
**Current approved deployment rule (2026-10-13): no external PC/IPC, server or SQL computer.** Owner-selected **cMT-FHDX-220**; OS/firmware and 61-meter benchmark pending. [Hardware plan](HARDWARE_TARGET_FHDX_220.md). [Command Centre #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1) · [Role-based UI](ROLE_BASED_UX_PLAN.md) · [HTML evaluation](../research/WEINTEK_HTML_FEASIBILITY.md).

## A. Runtime / physical topology
```mermaid
flowchart TB
    M["61 different energy analyzers (Modbus TCP / RTU via supported gateways)"]
    subgraph HMI["WEINTEK UCS — cMT-FHDX-220 • only runtime"]
       DRIVER["Preconfigured device drivers + site-to-meter mapping"]
       ACQ["Always-on polling; value + quality + timestamps"]
       HIST["Native Data Sampling, event/operation log, macros"]
       VIEW["Screens: operator / engineer / management / shared detail"]
       REPORT["On-device historian query/report workflows • prove capability"]
       DRIVER --> ACQ
       ACQ --> HIST
       ACQ --> VIEW
       HIST --> REPORT
       REPORT --> VIEW
    end
    M --> DRIVER
    HIST --> MEDIA["FHDX-220 USB1 / qualified USB-SSD; NO SD"]
    REPORT --> MEDIA
    ALARM["Critical exception"] --> ROUTE["UCS severity + role routing / popup"]
    HIST --> ALARM
    ROUTE --> VIEW
```
**No external computer.** The native HMI historian's query/aggregation capability is NOT equivalent to unrestricted SQLite/HTML-server support. Complex/long-retention reports and 61-meter throughput require physical benchmarks before customer commitments.

## B. Screens follow user purpose
```mermaid
flowchart TD
    LOGIN["Weintek UAC / role"] --> R{"Active role"}
    R -->|Operator| OP["Operator Home • live alarms, 61 meter status, loads"]
    R -->|Engineer| EN["Engineer Home • comms, faults, maintenance actions"]
    R -->|Management| MG["Management Home • KPI, trends, ready reports"]
    OP --> SAME["Shared Meter Detail • one indexed template"]
    EN --> SAME
    MG --> SAME
    OP --> TRENDS["Reusable Meter Trends"]
    EN --> DIAG["Diagnostics / Commissioning"]
    MG --> REPORT["Historical Reports"]
    EN --> RESOURCE["Resource & Storage Manager"]
    MG -. "only when requested" .-> RESOURCE
    ROUTER["Role-aware alarm/event router"] -->|Actionable problem only| OP
    ROUTER -->|Technical incident| EN
    ROUTER -->|Business-impacting or report/backup failure| MG
```
Home is a **purpose-complete summary**, not a dump of CPU/RAM/storage gauges. Resource and backup administrative views remain deep navigation; critical problems appear as notifications. All events must also appear in log and historian.

## C. One reusable meter screen / background historian
```mermaid
flowchart LR
    BTN["Selected meter 1..61"] --> ID["Per-client private selection + index"]
    ID --> DETAIL["ONE Meter Detail screen"]
    ACQ["Independent polling of ALL 61"] --> CACHE["61 fixed normalized meter blocks"]
    CACHE --> DETAIL
    ACQ --> LOG["HMI 61-meter all-channel logging • never depend on selection"]
    LOG --> T["History/trend selection: separate proof from live index"]
```

## D. Weintek-only storage lifecycle
```mermaid
flowchart TD
   USB["FHDX-220 USB1 present?"] --> YES{"Writable & capacity valid?"}
   YES -->|No| ALERT["Record storage incident • show role-directed warning"]
   YES -->|Yes| REC{"Persisted historical records advancing?"}
   REC -->|No| ALERT
   REC -->|Yes| OK["Recording verified with freshness + backup status"]
   OK --> BAK["Verify backups on an independent removable media or supported destination"]
   BAK --> CAP["Estimate actual remaining retention from measured bytes/day"]
```
Presence is not proof of write or persistence; backup on the same disk is not independent recovery.

## E. Engineer work phases
```mermaid
flowchart LR
 A["Source & model capabilities"] --> B["2-meter pilot + shared template"]
 B --> C["61-meter continuous historian / fault ledger"]
 C --> D["Three user homes + events & alarms"]
 D --> E["Date/period reports + export"]
 E --> F["Storage/backup/failure acceptance on real Weintek"]
```

## Not supported as proven (yet)
- Arbitrary HTML `file:///usb1/index.html` via **PLC Web Browser**; HTML5 web panel `(W)` is browser-focused, not demonstrated direct EBPro historian runtime.
- Generic direct SQLite API in Macro/JS, or Advanced Mode custom SQL on Local SQLite for the exact target.
- Dynamic Trend Display index from client-private live index; proper history querying must be tested.
- Guaranteed zero missing samples under meter/device power loss; instead record explicit evidence of missing intervals.

# Visual project plan — site-independent historian
**Owner entry point:** [One-screen dashboard](OWNER_DASHBOARD.md) · [Report catalog](REPORT_CATALOG.md) · [Command Centre #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1)

## 1. The complete system — one engine, different sites
```mermaid
flowchart TB
    subgraph SITE["SITE LAYER — varies by customer"]
      A["Solar / DG / Grid"] ~~~ B["Factory / HVAC / Utilities"] ~~~ C["UPS / LPG / Other"]
    end
    SITE --> CONFIG["Site Profile: devices, tags, units, sample/retention, time zone"]
    CONFIG --> ACQ["Data Acquisition & Quality: Modbus / PLC / native HMI"]
    ACQ --> D{Capability gate: chosen HMI?}
    D -->|"Native historian + documented features"| N["HMI Data Sampling / Events / Backup"]
    D -->|"Complex reports / cross-site / PDF"| E["PC / IPC collection + report service"]
    N --> H["HMI History Data Display / supported query path"]
    N --> CSV["Backup CSV / verified conversion"]
    E --> DB["Controlled SQLite/SQL DB + indices"]
    DB --> Q["Generic report query / aggregation"]
    Q --> OUT["Report templates & file exports"]
    H --> VIEW["HMI historical view"]
    OUT --> PDF["CSV / XLSX / styled multi-page PDF / print"]
    OUT -. "only after supported integration proof" .-> VIEW
    classDef source fill:#eef4ff,stroke:#6b93be,color:#14253b;
    classDef report fill:#e5f3ed,stroke:#499678,color:#17362b;
    class A,B,C,CONFIG source;
    class H,CSV,VIEW,OUT,PDF report;
```
> Architecture shows **two valid implementation routes**, not a claim that all features run on the HMI. Local USB/SD SQLite SQL Query and Advanced Mode combinations require explicit versioned proof.

## 2. Site differences affect configuration — not the universal platform
```mermaid
flowchart LR
    S1["Site A\nSolar + Grid + DG"] --> P1["Site profile A"]
    S2["Site B\nProduction machines"] --> P2["Site profile B"]
    S3["Site C\nUPS + Power Quality"] --> P3["Site profile C"]
    P1 --> CORE["COMMON REPORTING ENGINE"]
    P2 --> CORE
    P3 --> CORE
    CORE --> T1["Trends"]
    CORE --> T2["Period totals"]
    CORE --> T3["Events"]
    CORE --> T4["Daily / Monthly / Custom"]
    CORE --> T5["CSV / Optional PDF"]
```

## 3. Historical report operator flow
```mermaid
flowchart LR
    A["Choose site"] --> B["Device / metric"]
    B --> C["Date range / shift / batch"]
    C --> D["Preview table + graph"]
    D --> E["Summary + quality indication"]
    E --> F["Export supported format"]
```

## 4. Execution roadmap and owner touch-points
```mermaid
flowchart LR
    M0["M0: Scope and generic configuration"] --> M1["M1: Weintek actual capabilities"]
    M1 --> M2["M2: Historian + SQL fixture"]
    M2 --> M3["M3: Macro/JS + report UI"]
    M3 --> M4["M4: Exports / PDF if required"]
    M4 --> M5["M5: Real HMI QA and handover"]
```
Owner needs to decide only **(i) which HMI/device is actually available** and **(ii) whether customer mandates styled PDF/print vs on-HMI + CSV**. Engineering team owns reading manuals, building fixtures, tests and issue/PR tracking.

## Current status
- Diagram/report catalog/config model: **DESIGN baseline**.
- Model support: manufacturer docs gathered; physical model/OS and local SQLite Advanced Mode **unverified**.
- Source code/report application/hardware acceptance: **NOT DELIVERED**. Do not sell all catalog reports as available today.

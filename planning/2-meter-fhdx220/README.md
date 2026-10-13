# 2-meter cMT-FHDX-220 Vertical Slice — READY TO BUILD SPECIFICATION, NOT BUILT
**Evidence: DOC/OFFLINE ONLY. No native EasyBuilder project, no real meter, no HMI simulation or device acceptance.**
**Execution HOLD:** The owner's GATE-1 design audit PASS does **not** authorize coding/EBPro. Wait for exact physical System Information (OS/firmware), EBPro version, the owner's implementation approval and P0 feasibility disposition.

## Goal and smallest demonstrator
Commission **two different manufacturer analyzer profiles** in a fixed reusable Weintek HMI template, without inventing raw meter registers. Validate window 210 client-private switching while BOTH normalized devices are independently polled and persisted with per-meter timestamp/quality. Show NOT SUPPORTED and error gaps rather than zero. Produce only on-device, proven native CSV; document missing USB/SQL capabilities with precise BLOCKED result.

## What can be prepared now
1. Exact normalized 2-meter proposed LW manifest in [register-allocation.json](register-allocation.json) (all field word widths and start/end addresses; raw vendor registers deliberately absent).
2. [SQL Query Basic & Advanced bench script](SQL_QUERY_TEST_PLAN.md) for USB1/local SQLite with exact evidence categories.
3. [USB write/read/persist resilience trial](USB_STORAGE_TEST_PLAN.md) reflecting ONE USB2 port, **NO SD** and touchscreen conflict.
4. [Acceptance checklist](ACCEPTANCE_CHECKLIST.md) that keeps every hardware validation NOT_RUN.
5. [Test session evidence template](EVIDENCE_TEMPLATE.md) for reviewer and engineer to attach device-recorded results.
6. [Engineer starting sequence](BUILD_HANDOFF.md) with native EBPro/UAC/JS/memory guardrails.

## Conditional 2-meter experiment flow
~~~mermaid
flowchart TD
  SYS["Real FHDX-220 System Info + installed EBPro version"] --> PERMIT{"Owner authorizes implementation?"}
  PERMIT -->|No| HOLD["HOLD — planning assets only"]
  PERMIT -->|Yes| CFG["Create valid manufacturer Modbus devices and normalized LW mapping"]
  CFG --> LOG["Independent background 2-meter sampling + gap/event ledger"]
  LOG --> UI["ONE Meter Detail: client-private meter 1/2 selection"]
  UI --> SQL["Qualified SQL Local SQLite / native historic query trial"]
  SQL --> USB["USB1 write/read + persisted history, disconnect/fault tests"]
  USB --> QA["Real evidence + independent reviewer, not offline CI PASS"]
~~~

Do not change runtime scope to any PC/IPC/Linux/Node/remote database. Desktop EBPro is a **development workstation** to compile/download HMI project, not a deployed processor. Device-family feature claims are not OS/device-level PASS.
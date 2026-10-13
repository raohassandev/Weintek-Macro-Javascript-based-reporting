# Weintek Macro & JavaScript Historical Reporting

**Purpose:** Industrial historical reporting on Weintek cMT HMIs, with validated model/firmware compatibility, SQL Query object, macros, JavaScript register-based interaction, historical-data browsing and export.

> **Project phase:** Bootstrap / technical feasibility. No production-ready solution or hardware verification claimed.

## Start here
- [Command Centre — Issue #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1): authoritative live board, owners, status, blockers.
- [Project context](docs/PROJECT_CONTEXT.md): customer request, previous chat findings and continuation procedure.
- [Master plan](docs/MASTER_PLAN.md): independent implementation lanes and acceptance gates.
- [Technical architecture](docs/ARCHITECTURE.md): trusted API boundaries and reporting options.
- [Requirements & acceptance](docs/REQUIREMENTS_AND_ACCEPTANCE.md): verifiable functionality.
- [Decision log](docs/DECISION_LOG.md): confirmed choices vs pending questions.
- [Activity log](docs/ACTIVITY_LOG.md): durable work and evidence chronology.
- [Model compatibility](docs/MODEL_COMPATIBILITY.md): manufacturer evidence and pending tests.
- [POC test protocol](docs/POC_TEST_PLAN.md): step-by-step device acceptance.
- [Weintek references](docs/REFERENCE_LINKS.md): official manuals, SDK and feature matrices.
- [Worker protocol](docs/WORKER_PROTOCOL.md): issue/PR ownership and handoff.

## Important technical boundary
Do **not** interpret `JavaScript` or `Macro` support as a direct unrestricted SQLite programming API. The documented route on compatible Advanced models is EasyBuilder Pro's **SQL Query object** (including supported external/local USB/SD SQLite configuration) and mapped HMI registers, which may be coordinated from Macro / JS. HMI internal logger database schema and access are **not assumed**. PDF generation/printing must be proven separately.

## Delivery workstream
Discovery → bench-test compatible HMI → history storage and schema → SQL Query/register contracts → Macro/JS control → report UI → CSV/PDF path → commissioning and customer acceptance.

See the [Command Centre](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1) for live work, not stale status copied here.

## Working standard
Small scoped PRs, truthful CI and physical-device evidence, explicit error handling, no leaked credentials, no silent degradation. When revisiting in a new chat, use issue #1 plus `docs/PROJECT_CONTEXT.md` as entry points.

**Maintained:** 2026-10-13.

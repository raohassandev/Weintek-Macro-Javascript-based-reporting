# Research & Development Library — Weintek Historian
**Maintained since:** 2026-10-13 | **Owner:** engineering | [Command Centre](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1)

## Why this exists
Capture **all relevant R&D links, decisions, experiments, version scopes and technical evidence** so engineers can continue the project without asking the human owner to reread long manuals. Store source metadata and concise engineering conclusions; do not redistribute copyrighted manuals in the public repo unless licensed.

## Quick navigation
| Folder/file | Use |
|---|---|
| [SOURCE_REGISTER.json](SOURCE_REGISTER.json) | Source URL, manufacturer/forum authority, topic, verified claim, caveat, issue |
| [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) | High-risk uncertainties and smallest experiment to close each one |
| [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md) | Real bench log template and verified run list (none as of bootstrap) |
| [DECISION_EVIDENCE.md](DECISION_EVIDENCE.md) | Evidence versus assumptions, disputed feature interpretation |
| [Official references](../docs/REFERENCE_LINKS.md) | Familiar HTML table of manual links |
| [Compatibility matrix](../docs/MODEL_COMPATIBILITY.md) | Models and what is documented vs tested |
| [POC procedure](../docs/POC_TEST_PLAN.md) | Repeatable local SQLite, query and macro/JS test |
| [Report catalog](../docs/REPORT_CATALOG.md) | Site-independent report capabilities and formula prerequisites |

## October 13 additional manufacturer research
- [Official Weintek Demo Projects catalog — curated R&D](DEMO_PROJECTS_REVIEW.md); [machine-readable demo list](demo-catalog.json). Demo archives are **not** represented as already downloaded.
- [Weintek-only HTML and JS rendering feasibility](WEINTEK_HTML_FEASIBILITY.md) with separate cMT-FHDX-820 (W), PLC Web Browser, EBPro JS Object and EasyWeb/View.
- [Offline HTML UI probe fixture](../experiments/html-poc/index.html) — test input only, not physical HMI pass.
- Current UCS boundary excludes any PC/IPC/server runtime. Prior IPC storage direction is superseded. Details [Visual plan](../docs/VISUAL_PLAN.md).

## R&D knowledge categories
- **A — Hardware/firmware/feature matrix:** cMT Basic, Standard, Advanced and SVRX; supported EBPro; native OS.
- **B — Native historian:** sampling, event/operation log, history displays, backup, retention, file formats.
- **C — SQL and storage:** local USB/SD SQLite, advanced query commands, server SQL sync, schema, indexing, performance.
- **D — Macro/JavaScript:** supported SDK API, register control/query feedback, JS Object runtime constraints.
- **E — Output:** CSV via native backup/EasyConverter, Excel import, rendered PDF/print via proven mechanism.
- **F — Reliability:** no media, low space, reboot, counter resets, time zones, missing data, security.
- **G — Deployment:** HMI-only versus headless + IPC/PC and customer total cost.

## New material intake (engineering owns this)
1. Add one `SRC-xxx` entry to [SOURCE_REGISTER.json](SOURCE_REGISTER.json) including exact link, date inspected, manufacturer vs third party, quote-length-safe summary, applies-to version, evidence/uncertainty.
2. Add or close question in [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) and link issue.
3. If significant design choice, update [DECISION_LOG](../docs/DECISION_LOG.md) and Command Centre.
4. For any actual experiment, fill [EXPERIMENT_LOG](EXPERIMENT_LOG.md) with hardware, software, steps, real outputs, repeatability and source files.
5. Every work cycle: task issue → evidence → activity log → Command Centre. Owner receives short visual summary, not a document dump.

## Evidence confidence
- `MANUFACTURER_DOCUMENTED`: exact statement in Weintek manual/site (not necessarily current device).
- `VENDOR_SUPPORT`: vendor forum answer; scoped to its own version/example.
- `THIRD_PARTY`: community article; corroboration required.
- `DESIGN_PROPOSAL`: architecture proposal, not a demonstrated Weintek feature.
- `DEVICE_VERIFIED`: genuine results on target SKU/firmware, **NONE YET**.

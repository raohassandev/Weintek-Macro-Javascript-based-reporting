# Project context — handoff document
**Last updated:** 2026-10-13. **Source:** project owner conversation and verified product references. **Command Centre:** [#1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1).

## Latest owner directive — 2026-10-13
- Make the project a **generalized reusable industrial historian** across solar, DG, factory, UPS, LPG, HVAC and other sites; each site varies only by device/tag/rules/profile.
- Research must be **completely indexed**: source URLs, vendor manuals, caveats, validation state, failed/successful experiments, decisions and new chat handoff.
- Owner is human and **will not read extensive documents or execute repetitive tests**. Engineer/AI must proactively research/implement/validate and show only a one-page status, clear diagram, working previews and single essential decision when required.
- Visual roadmap: docs/VISUAL_PLAN.md. Reports: docs/REPORT_CATALOG.md. Owner quick view: docs/OWNER_DASHBOARD.md. R&D library: research/INDEX.md.
- The site profiles and registry are designs, not direct EBPro-native imports or completed actual hardware commissioning.

## The customer problem
A customer requires **historical reports** on a Weintek industrial HMI, not just live values or general data logging. The engineering objective is filtering by date/period/device, reporting summary statistics, showing historical table/pages, exporting CSV/Excel-compatible data, and deciding whether customer also requires branded multipage PDF/print. Exact final output specification, tag list and report templates are **not supplied yet**.

## Relevant conversation so far
1. Requested **which Weintek models support complete SQLite via JavaScript or macros** for customer historical reporting. Do not confuse having JavaScript/macros with direct unrestricted SQLite access.
2. Compared Advanced series cMT3102X, cMT3108XH, cMT3072 family, cMT3092X, cMT3152X/3162X and cMT-SVRX with cMT1106X Basic.
3. Asked `cmt 1102 or 1106?`; exact `cMT1102` label not validated. Current Weintek downloadable model list mentions **cMT2102X**, not proof the owner's device is that model. **Require rear-label photo** before choosing.
4. Main feasible route from official release notes: **SQL Query object** supports SQLite database on USB or SD for eligible cMT models. Macro and JS may operate HMI registers to trigger configured SQL Query objects; direct `sqlite.open()` /`db.execute()` API is **not confirmed**.
5. HMI native historical recording/data backup is a distinct workflow. Access to arbitrary **internal historian files** from SQL Query is **not assumed**.
6. Feature scope changed from mere model selection to **maintaining this dedicated GitHub repo as complete plan, Command Centre, task tracker and chat/project context** on 2026-10-13.
7. Owner expects implementation evidence and an actionable approach, not generic options.

## Known vs unknown
**Documented candidate:** cMT3102X supports SQL Database/JS Object according to Weintek marketing/spec material, subject to actual EBPro/firmware checks. **Basic exception:** cMT1106X not recommended for on-HMI SQL Query/JS report work. **Unknown:** the actual installed model, EBPro, firmware, exact database location, report fields, output formats, number of meters, sampling interval, report duration and export method.

## Non-negotiable engineering cautions
- No unverified API or register addresses; copy exact mapping from the relevant EBPro manual and reproduce on selected model.
- Do not equate `History Data Display`, `RecipeQuery()` or `SQL Query` with fully general internal SQLite file access.
- `SQL Query` and backup/CSV are independent features; prove the connection path.
- Multipage branded PDF requires a **separately verified** generator (possibly PC/IPC service).
- Energy kWh reports must use counters/deltas or time integration with gaps accounted for; simple `SUM(kW)` is wrong.
- Preserve raw timestamps, time zone and data quality.

## New-session continuation procedure
1. Read [Command Centre #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1), this document, [MASTER_PLAN.md](MASTER_PLAN.md), [DECISION_LOG.md](DECISION_LOG.md), open GitHub issues and PRs.
2. State current task ID, previous verified evidence, exact next action and dependencies.
3. Pick only [AVAILABLE] work in authorized lane, claim it before changing shared files.
4. Commit work in scope; link commit/PR, CI/hardware evidence; update issue flag, [ACTIVITY_LOG.md](ACTIVITY_LOG.md), and decision log if applicable.
5. If blocked, document exact missing device/input and continue independent work. Never fill unknowns with guesses.

## Repository links
- [#1 Command Centre](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1)
- [#2 Model compatibility](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/2)
- [#3 SQL/query](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/3)
- [#4 Historian](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/4)
- [#5 Macro](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/5)
- [#6 JavaScript](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/6)
- [#7 HMI UI](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/7)
- [#8 Export/PDF](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/8)
- [#9 QA](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/9)
- [#10 Release](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/10)

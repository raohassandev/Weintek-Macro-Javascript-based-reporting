# AI and human contributor instructions
This repository tracks a commercial Weintek HMI historical-reporting implementation. **Read [Command Centre #1](https://github.com/raohassandev/Weintek-Macro-Javascript-based-reporting/issues/1) before changes.**
- Read `docs/PROJECT_CONTEXT.md`, `docs/MASTER_PLAN.md`, `docs/DECISION_LOG.md` and scoped issue.
- Claim lane; never duplicate unowned parallel work.
- Distinguish documented SQL Query object from unverified direct SQLite APIs in Macro/JS.
- No fabrication of version compatibility, HMI hardware execution, SQL results, CI or customer acceptance.
- Preserve true source-of-data, timestamp/timezone, units and energy calculations.
- Minimize file scope; submit PRs with tests/evidence; update Command Centre/ACTIVITY_LOG and decision log.
- Keep credentials and customer-specific production data out of public GitHub.
- Current work is feasibility/implementation setup, **not commissioned production**.

- This project is **site-independent**. Core report definitions must never embed real site tags, IPs, device addresses or sample intervals.
- Explain progress to human owner with [Owner Dashboard](docs/OWNER_DASHBOARD.md) and [Visual Plan](docs/VISUAL_PLAN.md), not walls of engineering logs; ask only decisions that require actual human facts.
- Keep research/source URL index in `research/SOURCE_REGISTER.json` current; distinguish evidence vs assumptions and update experiments only for actual runs.
- Validate any site profile against portable schema and cross-reference rules; a JSON/schema pass is **NOT** HMI acceptance.
- **Advanced SQL on Local SQLite** is a documented ambiguity and a P0 verification question; do not assert it works without model/version proof.

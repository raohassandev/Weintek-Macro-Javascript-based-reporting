# Collaboration / worker protocol

## Entrypoint
Open [Command Centre #1](../issues/1) and read current live table, related task issue and docs before work. GitHub is durable coordination; chat discussions become project context only when the associated docs/issues are updated.

## Task lifecycle
- `[AVAILABLE]`: scoped, unclaimed.
- `[INPROGRESS @owner since YYYY-MM-DDTHH:MMZ]`: claimed; owner records files/assumptions.
- `[REVIEW PR#N head:<sha>]`: actual PR with reproducible tests, exact commit and pending independent review.
- `[COMPLETED PR#N/<sha>]`: merge + acceptance evidence.
- `[BLOCKED: concise root cause]`: specific missing input, device, CI or permission; independent work may proceed.

## Claim and ownership
Read live issue before claiming. Set owner flag as issue comment and update Command Centre; re-read to avoid collision. One worker owns one file group/task at a time; announce overlaps and request exclusive access. Shared docs have designated maintainer; propose edits by scoped PR where possible.

## Change and evidence policy
- No unverified model features, API functions, register addresses, CI, fabricated dataset called real, fake screenshots, or untested production promises.
- Use smallest PR with issue number, test procedure, results, log/screenshot/video link, limitations and rollback.
- Hardware validation means named device/firmware, date, reproducible steps, observed output. Simulator is a separate category.
- Never store credentials or customer-sensitive logs in public repository.
- After each meaningful action, update **issue flag, Command Centre, ACTIVITY_LOG.md**; record accepted design decisions in DECISION_LOG.md.
- Before merging, check reviews and the exact PR head's required passing checks. Don't claim pass if checks absent.
- Upon blockage, log root cause, missing input, what was tried and next owner; do independent work without overwriting others.

## Minimum new-chat instruction
> Continue `raohassandev/Weintek-Macro-Javascript-based-reporting` from [Command Centre #1](../issues/1). Read README, docs/PROJECT_CONTEXT.md, docs/MASTER_PLAN.md, docs/DECISION_LOG.md and open issues/PRs. Do the next available scoped engineering work, push genuine code/tests, update issues/board/log with evidence. Do not claim direct Macro/JS SQLite APIs or device test results without verification. Do not ask for data already recorded in the repo.

# 2-meter FHDX-220 acceptance and evidence ladder
**Gate-1 PLAN AUDIT: PASS (owner-provided independent verdict, DOC/OFFLINE).** This does NOT authorize implementation.

| ID | Criterion | Current state |
|---|---|---|
| P-01 | Exact model cMT-FHDX-220 documentation and no-SD / one-USB contract | DOCUMENTED/SELECTED |
| P-02 | Rear-label / actual System Information + OS/firmware/EBPro version | **BLOCKED Q01 — NOT_RUN** |
| P-03 | Owner explicitly authorizes EBPro work after plan audit and prerequisites | **BLOCKED — NO APPROVAL** |
| P-04 | Real EBPro project opens/compiles and Weintek tag import template verified | **NOT_RUN** |
| P-05 | Actual two supported meter models mapped from vendor register manuals, read-only and correct endian/scaling | **NOT_RUN** |
| P-06 | LW 256..383, LW 384..511, PLW-100/PLW-9200 conflict & private index check | DOC/OFFLINE verified math; **native test NOT_RUN** |
| P-07 | Live selection 1/2 doesn't interfere with second logged meter or another Viewer | **NOT_RUN** |
| P-08 | Both meter Data Sampling timestamps and persistent quality/error ledger independent of UI | **NOT_RUN** |
| P-09 | Communication timeout, recovery, recorded zero, unobservable HMI outage and incident reasons distinct | **NOT_RUN** |
| P-10 | SQL Query Basic Local USB1, Advanced Local SQL disposition and native historian path verified | **BLOCKED Q02 — NOT_RUN** |
| P-11 | USB1 media write/read/TTL and actual durable record advancement independently detected | **BLOCKED Q10 — NOT_RUN** |
| P-12 | Export CSV from Weintek and reconcile to raw meter history with timestamp/units/coverage | **NOT_RUN** |
| P-13 | Signed contracted PDF/XLSX format decision; on-Weintek generator only if mandatory | **BLOCKED Q04/Q12** |
| P-14 | Independent offline golden-energy fixture suite (counter reset, rollover, null/zero, irregular integration) | **DOC/OFFLINE merged; not EBPro PASS** |
| P-15 | 61-meter load and retention/backup/procurement acceptance on selected legacy HMI | **BLOCKED — NOT_RUN** |

**Acceptance gate:** only named model, firmware/EBPro, observed results, screenshots/logs and validated file outputs can upgrade to DEVICE-PASS. If unsupported, write UNSUPPORTED rather than invent results.

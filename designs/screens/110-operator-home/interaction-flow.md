# Window 110-operator-home — OPERATIONS OVERVIEW
**Evidence:** DOC / OFFLINE-generated visuals only. No compiled EBPro object or device test.
**Hardware:** cMT-FHDX-220, 1920×1080, ONE USB2, NO SD, no PLC Web Browser, no PC runtime.
## Role and action workflow
- Meter tile selects PLW-100 for THIS client; supported Private Index computed only after bounds check.
- Operator action opens common detail 210; no change to background logging.
- Critical event opens role-allowed popup 900 and persists before display.
- Operator acknowledges only permitted events; cannot restore/commission.
## Navigation rule
- Common shell only; role access must be enforced at action/data origin, not cosmetic visibility.
- The window does not schedule or stop any meter polling/history; all 61 log independently.
- Preview PNG contains labeled mockups and is never imported as live values.
- Background-only.png has no data, legends with fake values, colored live-status dots or report success indicators.

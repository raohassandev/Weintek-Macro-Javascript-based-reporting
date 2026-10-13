# Acceptance checklist: never mark HMI PASS from these design files
| Level | Check | Current status |
|---|---|---|
| DOC | 1920×1080 PNGs; role screen purpose, exact native object map; no SD/browser/PDF button | READY FOR OFFLINE CI |
| OFFLINE | SVG/PNG syntax, contrast, expected CSV columns, no fake data in background | READY FOR OFFLINE CI |
| EBPRO | Project window built with actual tagged Numeric/Lamp/Trend/Event objects at target version | NOT RUN — owner hold |
| SIMULATOR | Stale/offline/UAC, target/source selection, date controls | NOT RUN — owner hold |
| DEVICE | cMT-FHDX-220 OS+EBPro; live 2 meter values, recorder and user sessions | BLOCKED — firmware & owner approval |
| SITE | 61 meters + USB single-port/backup/fault and report file evidence | BLOCKED — hardware trial |
| AUDIT | Separate per-screen usability/completeness and release-role security audit | NOT RUN |

Picture/background is a static design aid; native EBPro objects implement ALL live tags.

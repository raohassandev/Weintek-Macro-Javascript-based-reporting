# FHDX-220 USB1 / historian persistence and backup tests — BENCH PLAN ONLY
**Gate Q10: BLOCKED.** One physical USB 2.0 host, **no SD/microSD**. Full 4 GB internal flash is NOT promised usable historian allocation. No tested SSD/hub or CPU metrics.

## Risk map
- First identify whether USB1 is occupied by touch-interface/mouse and whether manufacturer supports any hub. Do not assume a hub or remote input works.
- **Preferred candidate A:** native internal Data Sampling continues when USB temporarily absent, and a scheduled/controlled native Backup object exports a consistent snapshot to USB, with validated restore and retention. Internal quota, endurance and recoverability remain unknown.
- **High-risk candidate B:** USB1 mounted as primary historian destination. Removing it for backup may stop all 61 logs; cannot call this a continuous system without proven buffering/replay and independent media verification. Do not prescribe hot-swapping until fully tested.
- USB SSD enclosure is a candidate only: bus current, format, mounting, reconnect, media wear and sustained writing all require physical proof.

## Named safety cases (all NOT_RUN)
| Case | Stimulus | Expected **design** state / negative assertion |
|---|---|---|
| U-01 | No USB at power-up | ABSENT, no false WRITABLE; historian destination identified |
| U-02 | USB inserted / FAT32 present | PRESENT only, not recorder-PASS |
| U-03 | Engineer-authorized small write, reopen, byte-compare | WRITABLE only after actual complete match; TTL expires |
| U-04 | File read/write okay but native logging stalled | WRITABLE and HISTORIAN_NOT_PERSISTING separate |
| U-05 | Remove USB during recording | Persistent storage event, lost/pending interval, never fictitious backfill |
| U-06 | Full/read-only media | ERROR, not green; source quality/history coverage impacted |
| U-07 | Power loss, reboot and restore | Missing unobservable interval explicitly acknowledged; no invented meter fault |
| U-08 | Long report query with active 2-meter polling | Capture continues independent of viewed page, query bounded |
| U-09 | Native backup to different removable storage | File checksum/re-read, consistent snapshot, restore drill with permissions |
| U-10 | Touch input competing for USB1 | BLOCKED if no manufacturer-qualified simultaneous usage |
| U-11 | Qualified USB SSD if owner selects | Confirm physical power/filesystem/reconnect/performance before ACCEPTED |
| U-12 | 61-meter scale phase ONLY AFTER 2-meter success | Measure actual growth/poll loss/CPU/memory and retention; no guessed values |

## Separation of status
USB_PRESENT != USB_WRITE_READ_VERIFIED != NATIVE_HISTORY_ADVANCING != BACKUP_VERIFIED. Old PASS cannot stay active after removal/reboot. Log media incidents with start/end and uncertainty, not invented false zero. Managers receive popup only when report trust is materially compromised; detailed capacity stays in Resources 510.

## Resource constraints
Internal flash write endurance/history quotas need supported manufacturer documentation and on-unit observation. Retention forecast needs measured bytes per day, available quota after safety reserve and proven cleanup/backup. Single USB port means no simultaneous independent second-media copy without proven hardware solution.

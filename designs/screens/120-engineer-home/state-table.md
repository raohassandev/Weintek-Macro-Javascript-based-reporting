# Required states (design-only)
| State | Trigger | UI rendering | Audit requirement |
|---|---|---|---|
| LOADING | New selection/request | Animated native indicator if supported, no previous meter data | Request ID bounds and client-private state |
| FRESH | Correct source+quality+age within measured TTL | Value with unit and timestamp | Device measurement pending |
| STALE | Last-good age exceeded TTL or read timeout | Stale badge, last-good time and non-current value | Never render stale as current |
| OFFLINE | Meter comm loss | Offline with failure interval and unknown root cause | Distinguish network/HMI/meter outage |
| UNSUPPORTED | Driver capability absent | N/A without fake numeric zero | Site profile capability map |
| NO_HISTORY | Native logger unavailable/no records | No data/partial coverage warning | Missing interval preserved |
| STORAGE_FAULT | USB disconnected/writer failing/recorder stale | Role-filtered alarm; report validity reduced | Keep event persisted, never rely on USB-present only |
| PERMISSION_DENIED | UAC denies operation | Hide privileged action AND block execution | Role action test pending |

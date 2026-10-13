# UCS cMT-FHDX-220 — ORIGINAL Analyzer Detail 210 (source-faithful)

**Approved visual is `APPROVED_ORIGINAL_METER_DETAIL.png` (1672×941, SHA256 49d8ebdc07fd5e7c1ee8553be17f4e74bf3dac1c8b63d785238a5834a67c4f69).** Companion component library original SHA256 7b4b7a5cc7b7e1d341c56a5393e87cd16ea5035bc7ff40c1f883ecb48a89fdac. Neither must be redrawn as a generic white dashboard. Prior PR#46 was REJECTED.

**Developer handoff source:** `original_ebpro_object_schedule.csv` lists 108 original coordinate/candidate native HMI objects, 61×48 (2,928) normalized LW tag fields are in `PROPOSED_normalized_lw_61_meter_manifest.csv` (NOT imported EBPro tags), and `docs/EBPRO_OBJECT_BY_OBJECT.md` maps screens to native controls. Device-memory headroom/reservation remains subject to commissioned EBPro project check.

**Original image binary state:** Visual screenshots and full source-faithful static bundle were recovered into ChatGPT final ZIP, but as of this commit the two full approved PNG binaries and final ZIP have not been transferred into GitHub binary blobs. The `tools/import_approved_ucs_images.py` SHA verifier and forthcoming packaging process use the exact approved bytes. **Do not treat this folder as a complete native visual handover without those assets.**

Background-only PNG (final ZIP): native overlay fields stay blank; static units, labels, section borders, icons and grid axes remain. No fake green healthy lamps, colored indicator bars or 'Live' promise. All device values from HMI Numeric/Word/History/Alarm objects, never baked into pixels. Positioning is source-derived and scaled to 1920×1080, not a physically tested 44-inch viewer.

**P0 hardware gates remain:** Q01 actual FHDX-220 System Info/EBPro, Q02 Advanced SQL Local SQLite, Q10 one-USB1 61-meter history/backup, Q04/Q12 contracted PDF/native report. No .emtp/.cmtp, physical hardware, or production Device-PASS claim.

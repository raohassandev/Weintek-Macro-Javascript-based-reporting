// UCS_STORAGE_STATUS.mcr
// EBPro Macro proposal. Run periodically on Local HMI after selecting compatible
// cMT-SVRX/FHDX and verifying GetData/SetData in real EBPro.
// No writes to Weintek SYSTEM registers. Reads known system bits only.
// User LW-8250..8253 must be supplied by trusted IO probe + historian watchdog:
// LW-8250 Probe: 0 never checked, 1 fail, 2 byte-for-byte pass
// LW-8251 Probe age in seconds (independent clock tick; stale defaults >120)
// LW-8252 Recorder: 1 only when actual persisted history confirmed
// LW-8253 Latest persisted record age in seconds (independent clock tick)
// LW-8270 Combined status: 0 ABSENT, 1 CONNECTED_UNVERIFIED,
// 2 VERIFIED, 3 LOW_SPACE, 4 IO_FAILURE. 
// **Important:** without independent age updater set LW-8251 and LW-8253
// to 65535 at project startup so a stale previous PASS cannot be reused.
macro_command main()
    bool usb_present, usb_low
    short probe_state, probe_age_sec, recorder_state, last_record_age_sec
    short combined_state

    GetData(usb_present, "Local HMI", LB, 12048, 1)
    GetData(usb_low, "Local HMI", LB, 9037, 1)
    GetData(probe_state, "Local HMI", LW, 8250, 1)
    GetData(probe_age_sec, "Local HMI", LW, 8251, 1)
    GetData(recorder_state, "Local HMI", LW, 8252, 1)
    GetData(last_record_age_sec, "Local HMI", LW, 8253, 1)

    combined_state = 1
    if usb_present == false then
        combined_state = 0
    else
        if usb_low == true then
            combined_state = 3
        else
            if probe_state == 1 then
                combined_state = 4
            else
                if probe_state == 2 and probe_age_sec >= 0 and probe_age_sec <= 120 then
                    if recorder_state == 1 and last_record_age_sec >= 0 and last_record_age_sec <= 120 then
                        combined_state = 2
                    end if
                end if
            end if
        end if
    end if

    SetData(combined_state, "Local HMI", LW, 8270, 1)
end macro_command

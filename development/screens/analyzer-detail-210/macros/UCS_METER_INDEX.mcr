// PROPOSED Weintek EBPro Macro. NOT compiled or tested on FHDX-220.
// Private Index on PLW-9200 must be verified per cMT Viewer client.
macro_command main()
    short meter_id, offset_word
    GetData(meter_id, "Local HMI", PLW, 100, 1)
    if meter_id >= 1 and meter_id <= 61 then
        offset_word = (meter_id - 1) * 128
        SetData(offset_word, "Local HMI", PLW, 9200, 1)
    end if
end macro_command

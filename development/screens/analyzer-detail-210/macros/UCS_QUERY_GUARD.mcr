// PROPOSED Macro, NOT compiled or tested. LW-8300 app register must be reserved
// against all project/SQL macro collisions. It does NOT run a SQL Query.
macro_command main()
    short meter_id, query_state
    GetData(meter_id, "Local HMI", PLW, 100, 1)
    query_state = 2
    if meter_id >= 1 and meter_id <= 61 then
        query_state = 0
    end if
    SetData(query_state, "Local HMI", LW, 8300, 1)
end macro_command

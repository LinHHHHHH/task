def run_formula(dv, param = None):
    defult_param = {'t1':9}
    if not param:
        param = defult_param
    
    KDJ_K = dv.add_formula('KDJ_K_1', 
           '''(2*If(Delay(KDJ_K,2)==0,50,Delay(KDJ_K,2)) + (close - Ts_Min(low,%s))/(Ts_Max(high,%s)-Ts_Min(low,%s)) * 100)/3'''%(param['t1'],param['t1'],param['t1']),
           is_quarterly=False)

    return KDJ_K
def run_formula(dv):
    PEHIST601 = dv.add_formula('PEHIST601','-PE/Ts_Mean(PE,60)', is_quarterly=False,add_data=True) 

    return PEHIST601

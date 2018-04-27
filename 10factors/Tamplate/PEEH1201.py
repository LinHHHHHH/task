def run_formula(dv):
    PEEH1201 = dv.add_formula('PEEH1201','-PE/Ewma(PE,20)', is_quarterly=False,add_data=True) 

    return PEEH1201

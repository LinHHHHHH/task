def run_formula(dv):
    dv.add_formula('DPO1','(close-Delay(Ts_Mean(close,20),11))',is_quarterly=False,add_data=True)
    MADPO1 = dv.add_formula('MADPO1','-Ts_Mean(DPO1,6)',is_quarterly=False,add_data=True)

    return MADPO1

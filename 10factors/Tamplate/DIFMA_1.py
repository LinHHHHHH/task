def run_formula(dv):
    dv.add_formula('DIF_11','(Ts_Mean(close,10)-Ts_Mean(close,50))',is_quarterly=False,add_data=True)
    DIFMA_1 = dv.add_formula('DIFMA_1','-(Ts_Mean(DIF_11,10))',is_quarterly=False,add_data=True)


    return DIFMA_1

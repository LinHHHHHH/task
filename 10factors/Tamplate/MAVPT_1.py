def run_formula(dv):
    dv.add_formula('VPT_1','Ts_Sum(volume*(close-Delay(close,1))/Delay(close,1),51)',is_quarterly=False,add_data=True)
    MAVPT_1 = dv.add_formula('MAVPT_1','-Ts_Mean(VPT_1,6)',is_quarterly=False,add_data=True)

    return MAVPT_1

def run_formula(dv):
    dv.add_formula('MTM_1','close - Delay(close,12)',is_quarterly=False,add_data=True)
    MTM_2 = dv.add_formula('MTM_2','-Ewma(MTM_1,6)',is_quarterly=False,add_data=True)

    return MTM_2

def run_formula(dv):
    dv.add_formula('MTR_1','Max(Max((high-low),Abs(Delay(close,1)-high)),Abs(Delay(close,1)-low))',is_quarterly=False,add_data=True)
    MTR_2 = dv.add_formula('MTR_2','-Ewma(MTR_1,14)',is_quarterly=False,add_data=True)

    return MTR_2

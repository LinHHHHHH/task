def run_formula(dv):
    dv.add_formula('DIF2','Ewma(close,12)-Ewma(close,26)',is_quarterly=False,add_data=True)
    dv.add_formula('MACD2','Ewma(DIF2,9)',is_quarterly=False,add_data=True)
    DDIF2 = dv.add_formula('DDIF2','-(DIF2-MACD2)',is_quarterly=False,add_data=True)

    return DDIF2

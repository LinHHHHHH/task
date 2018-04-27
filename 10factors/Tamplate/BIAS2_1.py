def run_formula(dv):
    BIAS2_1 = dv.add_formula('BIAS2_1','-(close-Ewma(close,12))/Ewma(close,12)*100',is_quarterly=False,add_data=True)

    return BIAS2_1

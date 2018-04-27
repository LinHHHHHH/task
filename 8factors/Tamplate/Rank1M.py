def run_formula(dv):
    Rank1M = dv.add_formula('Rank1M_1','Rank(close/Delay(close,20))', is_quarterly=False,add_data=True)
    return Rank1M
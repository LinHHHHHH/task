def run_formula(dv):
    TVMA201 = dv.add_formula('TVMA201','-Ts_Mean(turnover,20)',is_quarterly=False,add_data=True)
    return TVMA201

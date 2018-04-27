def run_formula(dv):
    dv.add_formula('DTM_1','If(open<=Delay(open,1),0,Max((high-open),(open-Delay(open,1))))',is_quarterly=False,add_data=True)
    dv.add_formula('DBM_1','If(open>=Delay(open,1),0,Max((open-low),(open-Delay(open,1))))',is_quarterly=False,add_data=True)
    dv.add_formula('STM_1','Ts_Sum(DTM_1,23)',is_quarterly=False,add_data=True)
    dv.add_formula('SBM_1','Ts_Sum(DBM_1,23)',is_quarterly=False,add_data=True)
    dv.add_formula('ADTM_1','If(STM_1>SBM_1,(STM_1-SBM_1)/STM_1,If(STM_1==SBM_1,0,(STM_1-SBM_1)/SBM_1))',is_quarterly=False,add_data=True)
    MAADTM_1 = dv.add_formula('MAADTM_1','-Ewma(ADTM_1,8)',is_quarterly=False,add_data=True)

    return MAADTM_1

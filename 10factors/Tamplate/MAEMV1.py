def run_formula(dv):
    dv.add_formula('VOLUME11','Ts_Mean(volume,14)/volume',is_quarterly=False,add_data=True)
    dv.add_formula('MID11','100*(high+low-Delay(high+low,1))/(high+low)',is_quarterly=False,add_data=True)
    dv.add_formula('EMV1','Ts_Mean(MID11*VOLUME11*(high-low)/Ts_Mean(high-low,14),14)',is_quarterly=False,add_data=True)

    MAEMV1 = dv.add_formula('MAEMV1','-Ts_Mean(EMV1,9)',is_quarterly=False,add_data=True)

    return MAEMV1

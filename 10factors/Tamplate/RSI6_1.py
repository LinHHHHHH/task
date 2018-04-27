def run_formula(dv):
    dv.add_formula('DIF_1','close-Delay(close,1)',is_quarterly=False,add_data=True)
    dv.add_formula('VU_1','If(DIF_1>=0,DIF_1,0)',is_quarterly=False,add_data=True)
    dv.add_formula('VD_1','If(DIF_1<0,-DIF_1,0)',is_quarterly=False,add_data=True)
    dv.add_formula('MAU1_1','Ewma(VU_1,10)',is_quarterly=False,add_data=True)
    dv.add_formula('MAD1_1','Ewma(VD_1,10)',is_quarterly=False,add_data=True)
    dv.add_formula('MAU2_1','Ewma(VU_1,6)',is_quarterly=False,add_data=True)
    dv.add_formula('MAD2_1','Ewma(VD_1,6)',is_quarterly=False,add_data=True)
    dv.add_formula('RSI10_1','Ewma(100*MAU1_1/(MAU1_1+MAD1_1),10)',is_quarterly=False,add_data=True)
    RSI6_1 = dv.add_formula('RSI6_1','-(Ewma(100*MAU2_1/(MAU2_1+MAD2_1),6))',is_quarterly=False,add_data=True)

    return RSI6_1

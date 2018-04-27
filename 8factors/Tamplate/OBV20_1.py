def run_formula(dv):
    dv.add_formula('kk5','If(close>Delay(close,1),volume,-volume)',is_quarterly=False,add_data=True)            
    kk = dv.add_formula('kk6','Ts_Sum(If(close==Delay(close,1),0,kk5),20)',is_quarterly=False,add_data=True)            
    return kk





#def nice(dv):
#    close = dv.get_ts('close')
#    volume = dv.get_ts('volume')
#    a = len(close)
#    b = len(close.T)
#    kk = pd.DataFrame(np.zeros((a,b)))
#    for i in range(a):
#        for j in range(b):
#            if close.iloc[i,j] > close.iloc[i-1,j]:
#                kk.iloc[i,j] = volume.iloc[i,j]
#            elif close.iloc[i,j] < close.iloc[i-1,j]:
#                kk.iloc[i,j] = -volume.iloc[i,j]
#            elif close.iloc[i,j] == close.iloc[i-1,j]:
#                kk.iloc[i,j] = 0
#    kk.columns = close.columns
#    dv.append_df(kk,'kk')
#    OBV_1 = dv.add_formula('kk1','Ts_Sum(kk,20)',is_quarterly=False,add_data=True)
#    return OBV_1



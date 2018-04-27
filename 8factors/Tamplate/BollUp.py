def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
    dv.add_formula('bollmd',"Ta('MA',0,close,close,close,close,close,%s)"%(param['t']), is_quarterly=False,add_data=True)
    BollUp = dv.add_formula('BollUp',"(bollmd - StdDev(bollmd,%s))"%(param['t']),is_quarterly=False)
    return BollUp
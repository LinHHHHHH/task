#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter


def run_formula(dv):
    LCAP = dv.add_formula('LCAP_1','Log(total_mv)', is_quarterly=False)
    return LCAP
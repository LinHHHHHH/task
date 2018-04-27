def run_formula(dv):
    dv.add_formula('ret','((close-Delay(close,1))-1)', is_quarterly=False,add_data=True)  #(MIN(PROD(RANK(RANK(LOG(SUM(TSMIN(RANK(RANK((-1 * RANK(DELTA((CLOSE - 1), 5))))), 2), 1)))), 1), 5) +TSRANK(DELAY((-1 * RET), 6), 5))
    alpha157 = dv.add_formula('alpha157',"-(Min(Ts_Product(Rank(Rank(Log(Ts_Sum(Ts_Min(Rank(Rank((-1 * Rank(Delta((close - 1), 5))))), 2), 1)))), 1), 5) +Ts_Rank(Delay((-1 * ret), 6), 5))",is_quarterly=False)
    return alpha157

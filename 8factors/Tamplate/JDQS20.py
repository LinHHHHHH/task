from jaqs.data import DataView
from jaqs.data import RemoteDataService
import os
import numpy as np
import warnings
import pandas as pd

warnings.filterwarnings("ignore")
os.chdir(r'C:\Users\Administrator\Desktop')

data_config = {
    "remote.data.address": "tcp://data.tushare.org:8910",
    "remote.data.username": "13535519788",
    "remote.data.password": "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MjE5NDY4Njc2MDQiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTM1MzU1MTk3ODgifQ._s8G8xPgI-mTDnjScbOax7lwrSQo9hd_bHTZAd4AbQM"
}

ds = RemoteDataService()
ds.init_from_config(data_config)

def run_formula(dv):
    close = dv.get_ts('close')
    a = len(close.T)
    b = len(close)
    open_adj = dv.get_ts('open')
    
    zz800_open = ds.daily('000906.SH', 20160101, 20180101, fields="open", adjust_mode=None)
    zz800_op = zz800_open[0][['trade_date','open']].set_index('trade_date')
    for i in range(1,a):
        zz800_op[i] = zz800_op['open']
    zz800_op.columns = close.columns
    
    zz800_close = ds.daily('000906.SH', 20160101, 20180101, fields="close", adjust_mode=None)
    zz800_cl = zz800_close[0][['trade_date','close']].set_index('trade_date')
    for i in range(1,a):
        zz800_cl[i] = zz800_cl['close']
    zz800_cl.columns = close.columns
    #dv.append_df(zz800_op,'zz800_op')
    #dv.append_df(zz800_cl,'zz800_cl')
    kk3 = pd.DataFrame(np.zeros((b,a)))
    for i in range(b):
        for j in range(a):
            if zz800_cl.iloc[i,j] < zz800_op.iloc[i,j] and close.iloc[i,j] > open_adj.iloc[i,j]:
                kk3.iloc[i,j] = 1
    kk4 = pd.DataFrame(np.zeros((b,a)))     
    for i in range(b):
        for j in range(a):
            if zz800_cl.iloc[i,j] < zz800_op.iloc[i,j]:
                kk4.iloc[i,j] = 1
    kk3.index = close.index
    kk3.columns = close.columns
    kk4.index = close.index
    kk4.columns = close.columns
    dv.append_df(kk3,'kk3')
    dv.append_df(kk4,'kk4')
    jdqs20 = dv.add_formula('jdqs20_1','Ts_Sum(kk3,20)/Ts_Sum(kk4,20)',is_quarterly=False,add_data=True)

    return jdqs20




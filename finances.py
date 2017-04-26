# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:25:22 2017

@author: abdoup
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('TSLA','yahoo', start, end)
print(df.head())
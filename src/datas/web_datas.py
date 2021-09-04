import numpy as np
import pandas as pd
import pandas_datareader.data as web

start = '2007-01-01'
end = '2015-01-01'
get_px = lambda x: web.DataReader(x, 'yahoo', start = start, end = end)['Adj Close']

symbols = ['SPY', 'TLT', 'MSFT']
data = pd.DataFrame({sym: get_px(sym) for sym in symbols})
lrets = np.log(data/data.shift(1)).dropna()
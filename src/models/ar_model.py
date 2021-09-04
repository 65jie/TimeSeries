import os
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import scipy.stats as scs
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
from arch import arch_model
from numpy.core.shape_base import block
from statsmodels.tsa.stattools import pacf



np.random.seed(1)
n_samples = 1000
a = 0.6

x = w = np.random.normal(size=n_samples)
# random walk without a drift
for t in range(n_samples):
    x[t] = a * x[t-1] + w[t]

# First difference of simulated Random Walk series
# _ = tsplot(np.diff(data.SPY), lags=30)

# p("Random Series\n\
# ----------\n\
# mean:{:.3f}\n\
# variance:{:.3f}\n\
# standard deviation:{:.3f}"\
# .format(x.mean(), x.var(), x.std()))

mdl = smt.AR(x).fit(maxlag=30, ic='aic', trend='nc')
est_order = smt.AR(x).select_order(maxlag=30, ic='aic', trend='nc')

true_order = 1
# p('\nalpha estimate: {:3.5f} | best lag order = {}'\
#     .format(mdl.params[0], est_order))
# p('\ntrue alpha = {} | true order = {}'\
#     .format(a, true_order))

n = int(1000)
alphas = np.array([.666, -.333])
betas = np.array([0.])

ar = np.r_[1, -alphas]
ma = np.r_[1, betas]

ar2 = smt.arma_generate_sample(ar=ar, ma=ma, nsample=n)
# _= tsplot(ar2, lags=30)

max_lag = 30
# mdl = smt.AR(lrets.MSFT).fit(maxlag=max_lag, ic='aic', trend='nc')
# est_order = smt.AR(lrets.MSFT).select_order(maxlag=30, ic='aic', trend='nc')

print('best estimated lag order = {}'.format(est_order))

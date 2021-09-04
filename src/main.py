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

print('Machine: {} {}\n'.format(os.name, os.name))
print(sys.version)
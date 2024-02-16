# import clean dataframe
from data_clean import df_prediction as df


# libraries
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from pandas.plotting import register_matplotlib_converters

from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()


# Code
# plt.figure(figsize=(10,4))
# plt.plot(df.Longitude)
# plt.ylabel('long')


acf_plot = plot_acf(df.Longitude)
acf_plot.show()

"""
Based on ACF plot, 
"""
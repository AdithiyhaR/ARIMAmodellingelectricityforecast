import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import itertools
from statsmodels.tsa.statespace.sarimax import SARIMAX
import os


#We will do tuning of seasonal arima parameters
#Paramters will be selected which minimizes the AIC criterion
def get_best_parameters(series,seasonality_period):
    p = d = q = range(1,4)
    pdq = list(itertools.product(p, d, q)) 
    seasonal_pdq = [(x[0], x[1], x[2], seasonality_period) for x in pdq]
    AIC_df = pd.DataFrame({}, columns = ['param', 'param_seasonal', 'AIC'])
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = SARIMAX(series, order = param, seasonal_order = param_seasonal, enforce_stationarity = False, enforce_invertibility = False)
                results = mod.fit()
                print('ARIMA{}x{}-AIC:{}'.format(param, param_seasonal, results.aic))
                temp = pd.DataFrame([[param, param_seasonal, results.aic]], columns = ['param', 'param_seasonal', 'AIC'])
                AIC_df = AIC_df.append(temp, ignore_index = True)
                del temp
            except:
                continue
            
        
    min_aic = AIC_df.sort_values(by = 'AIC').iloc[0]    #Row with minimum AIC value
    model = SARIMAX(series, order = min_aic.param, seasonal_order = min_aic.param_seasonal, enforce_stationarity = False, enforce_invertibility = False)
    
    return model,min_aic.param,min_aic.param_seasonal
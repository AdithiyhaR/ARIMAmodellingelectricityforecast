#utility functions
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf,pacf

def plot_rolling_stats(series):
	rolling_mean = series.rolling(window = 3).mean()
	rolling_std = series.rolling(window = 3).std()
	plt.figure(figsize = (22,10))
	plt.plot(series,color = 'blue',label = 'RRP')
	plt.plot(rolling_mean,color = 'green',label = 'Rolling mean')
	plt.plot(rolling_std, color = 'red', label = 'Rolling standard deviation')
	plt.title('Rolling statistics')
	plt.legend()
	plt.show()
	
	
def plot_acf_pacf(time_series,n_lags):
	#autocorrelation and partial autocorrelation functions
	#Critical values at lag 0 are used, at subsequent lags, the confidence interval increases
	#95% cfonfidence interval is considered
	series = time_series.dropna()
	acf_values = acf(series,nlags = n_lags)
	pacf_values = pacf(series,nlags = n_lags)
	plt.figure(figsize = (20,10))
	plt.subplot(121)
	plt.plot(acf_values)
	plt.yticks(np.linspace(0.0,1.0,10))
	plt.xticks(np.linspace(0,n_lags,n_lags/4+1))
	plt.axhline(y = 0, linestyle = '--', color = 'gray') #Add a horizontal line across the axis at y = 0.
	plt.axhline(y = -1.96/np.sqrt(len(series)), linestyle = '--', color = 'gray')
	plt.axhline(y = 1.96/np.sqrt(len(series)), linestyle = '--', color = 'gray')
	plt.title('Autocorrelation Function')
	plt.show()

	#Plot PACF:
	plt.figure(figsize = (20,10))
	plt.subplot(122)
	plt.plot(pacf_values)
	plt.yticks(np.linspace(0.0,1.0,10))
	plt.xticks(np.linspace(0,n_lags,n_lags/4+1))
	plt.axhline(y = 0, linestyle = '--', color = 'gray')
	plt.axhline(y = -1.96/np.sqrt(len(series)), linestyle='--', color = 'gray')
	plt.axhline(y = 1.96/np.sqrt(len(series)), linestyle='--', color = 'gray')
	plt.title('Partial Autocorrelation Function')
	plt.tight_layout()
	plt.show()
	
	
	
	
	


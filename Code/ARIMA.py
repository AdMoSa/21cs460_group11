#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


get_ipython().run_line_magic('cd', 'F:\\Fantasy-Premier-League-master')


# In[ ]:





# In[ ]:





# In[6]:


import pandas as pd

import numpy as np 
import matplotlib.pyplot as plt
import math

# Reading the data

df = pd.read_csv("awb.csv")

print(df.shape)

print(df.info())


# In[ ]:





# In[ ]:





# In[7]:





# In[7]:


from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(df["Points"].iloc[13:],lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df["Points"].iloc[13:],lags=40,ax=ax2)


from statsmodels.tsa.arima.model import ARIMA
model=ARIMA(df["Points"],order=(1,0,1))
model_fit=model.fit()
model_fit.summary()


# In[8]:


from matplotlib import pyplot
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
# density plot of residuals
residuals.plot(kind='kde')
pyplot.show()
# summary stats of residuals
print(residuals.describe())


# In[9]:


df['Predict']=model_fit.predict(start=90,end=119,dynamic=True)
df[["Points",'Predict']].plot(figsize=(12,8))


# In[10]:


import statsmodels.api as sm
model=sm.tsa.statespace.SARIMAX(df["Points"],order=(1, 1, 1),seasonal_order=(0,1,2,12))
results=model.fit()
results.summary()


# In[76]:


from matplotlib import pyplot
residuals = pd.DataFrame(results.resid)
residuals.plot()
pyplot.show()
# density plot of residuals
residuals.plot(kind='kde')
pyplot.show()
# summary stats of residuals
print(residuals.describe())


# In[11]:


df['forecast']=results.predict(start=90,end=120,dynamic=True)

df[["Points",'forecast']].plot(figsize=(12,8))
print(results.predict(start=90,end=120,dynamic=True))
print(results.predict(start=121,dynamic=True))


# In[ ]:





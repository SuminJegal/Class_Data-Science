
# coding: utf-8

# In[6]:

import csv
import datetime
import calendar
import json
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib')


# # 1번

# In[112]:

tashu_csv = pd.read_csv('/Users/jegalsumin/Documents/Data Science/Data set/test/1/tashu.csv', dtype={'RENT_DATE': str, 'RETURN_DATE': str})


# In[113]:

tashu_csv = tashu_csv.dropna()
tashu_csv['RENT_DATE'] = pd.to_datetime(tashu_csv['RENT_DATE'], format = '%Y%m%d%H%M%S')
tashu_csv['RETURN_DATE'] = pd.to_datetime(tashu_csv['RETURN_DATE'], format = '%Y%m%d%H%M%S')


# In[114]:

tashu_csv['use_time'] = tashu_csv.RETURN_DATE - tashu_csv.RENT_DATE
tashu_csv['use_time'].astype('timedelta64[s]')
tashu_csv[:10]


# In[115]:

tashu_csv['year'] = tashu_csv['RENT_DATE'].apply(lambda x: x.year)
tashu_csv['month'] = tashu_csv['RENT_DATE'].apply(lambda x: x.month)
tashu_csv['day'] = tashu_csv['RENT_DATE'].apply(lambda x: x.day)
tashu_csv['hour'] = tashu_csv['RENT_DATE'].apply(lambda x: x.hour)


# In[137]:

tashu_csv['date'] = pd.DatetimeIndex(tashu_csv['RENT_DATE']).date


# In[116]:

tashu_csv['weekday_name'] = pd.DatetimeIndex(tashu_csv['RENT_DATE']).weekday_name
tashu_csv['weekday'] = pd.DatetimeIndex(tashu_csv['RENT_DATE']).weekday


# In[117]:

tashu_csv['week'] = pd.DatetimeIndex(tashu_csv['RENT_DATE']).week


# In[138]:

tashu_csv[:3]


# In[139]:

tashu_csv.to_csv('/Users/jegalsumin/Documents/Data Science/Data set/tashu/tashu_cleaned.csv',index=False, encoding='utf-8')


# In[ ]:




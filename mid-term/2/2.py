
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


# # 2번

# In[7]:

total_day = list([['Date','step_count','sleep_time']])
dates = pd.date_range("20160401","20160520")
for date in dates :
    personal_steps = 0
    personal_sleep = 0
    for person_number in range(1,98):
        try:
            str_tmp1 = "/Users/jegalsumin/Documents/Data Science/Data set/test/2/sokulee/A0"+str(person_number)+"/A0"+str(person_number)+"_20"+str(date.strftime("%y%m%d"))+"_steps.json"
            str_tmp3 = "/Users/jegalsumin/Documents/Data Science/Data set/test/2/sokulee/A0"+str(person_number)+"/A0"+str(person_number)+"_20"+str(date.strftime("%y%m%d"))+"_sleep.json"
            json_temp = open(str_tmp1).read()   
            day_steps = json.loads(json_temp)
            json_temp2 = open(str_tmp3).read()   
            day_sleep = json.loads(json_temp2)
            try:
                personal_steps = personal_steps + int(day_steps['activities-steps'][0]['value'])
                personal_sleep = personal_sleep + int(day_sleep['summary']['totalMinutesAsleep'])
            except KeyError: 
                continue
        except FileNotFoundError:
            continue
    str_tmp2 = date
    person = list()
    person.append(str_tmp2)
    person.append(personal_steps/98)
    person.append(personal_sleep/98)
    total_day.append(person)


# In[8]:

with open('/Users/jegalsumin/Documents/Data Science/Data set/fitbit/personal_total.csv', 'w', newline='') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerows(total_day)


# In[11]:

total = list()
for person_number in range(1,98):
    dates = pd.date_range("20160401","20160520")
    personal_steps = 0
    personal_sleep = 0
    try:
        for date in dates : 
            str_tmp1 = "/Users/jegalsumin/Documents/Data Science/Data set/test/2/sokulee/A0"+str(person_number)+"/A0"+str(person_number)+"_20"+str(date.strftime("%y%m%d"))+"_steps.json"
            str_tmp2 = "/Users/jegalsumin/Documents/Data Science/Data set/test/2/sokulee/A0"+str(person_number)+"/A0"+str(person_number)+"_20"+str(date.strftime("%y%m%d"))+"_sleep.json"
            json_temp = open(str_tmp1).read()   
            day_steps = json.loads(json_temp)
            json_temp2 = open(str_tmp2).read()   
            day_sleep = json.loads(json_temp2)
            try:
                personal_steps = personal_steps + int(day_steps['activities-steps'][0]['value'])
                personal_sleep = personal_sleep + int(day_sleep['summary']['totalMinutesAsleep'])
            except KeyError: 
                continue
    except FileNotFoundError:
        continue
    else:
        str_tmp2 = "A0"+str(person_number)
        person = list()
        person.append(str_tmp2)
        person.append(personal_steps/51)
        person.append(personal_sleep/51)
        total.append(person)


# In[14]:

total = pd.DataFrame(total)
total = total.rename(columns={0: 'user', 1: 'steps', 2: 'sleep'})


# In[15]:

total


# In[9]:

import math
from operator import itemgetter
from scipy.spatial import distance

def distance_cosine(a,b):
    return 1-distance.cosine(a,b)
def distance_correlation(a,b):
    return 1-distance.correlation (a,b)
def distance_euclidean(a,b):
    return 1/(distance.euclidean(a,b)+1)


# In[19]:

total.sort(['sleep'], ascending=[1])


# In[ ]:

def predictRating(userid, movie, nn=20000, simFunc=distance_euclidean) :
    neighbor = nearest_neighbor_user(userid,nn,simFunc)
    neighbor_id = [id for id,sim in neighbor]
    ## neighboorhood's movie : al least 4 ratings
    neighbor_movie = UM_matrix_ds.loc[neighbor_id]        .dropna(1, how='all', thresh = 4 )
    #neighbor_movie.head()
    neighbor_dic = (dict(neighbor))
    ret = [] # ['movieId', 'predictedRate']
    ## rating predict by my similarities
    for movieId, row in neighbor_movie.iteritems():
        jsum, wsum = 0, 0
        for v in row.dropna().iteritems():
            sim = neighbor_dic.get(v[0],0)
            jsum += sim
            wsum += (v[1]*sim)
        ret.append([movieId, wsum/jsum])
        if(movieId == movie):
            return [movieId, wsum/jsum]
    
    return ret 


# In[ ]:




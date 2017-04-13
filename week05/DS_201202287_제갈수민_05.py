
# coding: utf-8

# In[129]:

get_ipython().magic('matplotlib inline')

import matplotlib
from matplotlib import pyplot as plt
import json
import datetime
import pandas as pd
import csv


# In[130]:

json_test = open("/Users/jegalsumin/Documents/Data Science/sokulee/A01/A01_20160411_steps.json").read()


# In[131]:

data = json.loads(json_test)


# In[132]:

data


# In[133]:

total_steps = list([['Person','step_count']])
for person_number in range(1,98):
    dates = pd.date_range("20160401","20160520")
    personal_steps = 0
    try:
        for date in dates : 
            str_tmp1 = "/Users/jegalsumin/Documents/Data Science/sokulee/A0"+str(person_number)+"/A0"+str(person_number)+"_20"+str(date.strftime("%y%m%d"))+"_steps.json"
            json_temp = open(str_tmp1).read()   
            day_steps = json.loads(json_temp)
            try:
                personal_steps = personal_steps + int(day_steps['activities-steps'][0]['value'])
            except KeyError: 
                continue
    except FileNotFoundError:
            continue
    else:
        str_tmp2 = "A0"+str(person_number)
        person = list()
        person.append(str_tmp2)
        person.append(personal_steps)
        total_steps.append(person)


# In[134]:

total_steps


# In[135]:

with open('/Users/jegalsumin/Documents/Data Science/Class_Data-Science/week05/personal_total_steps.csv', 'w', newline='') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerows(total_steps)


# In[136]:

json_test = open("/Users/jegalsumin/Documents/Data Science/sokulee/A01/A01_20160411_heart.json").read()
data = json.loads(json_test)
data
#data["activities-heart"][0]['value']['heartRateZones'][1]['minutes']


# In[137]:

total_hearts = list([['Person','heart_total_minutes']])
for person_number in range(1,98):
    dates = pd.date_range("20160401","20160520")
    personal_hearts = 0
    try:
        for date in dates : 
            str_tmp1 = "/Users/jegalsumin/Documents/Data Science/sokulee/A0"+str(person_number)+"/A0"+str(person_number)+"_20"+str(date.strftime("%y%m%d"))+"_heart.json"
            json_temp = open(str_tmp1).read()   
            day_hearts = json.loads(json_temp)
            try:
                personal_hearts = personal_hearts + int(day_hearts["activities-heart"][0]['value']['heartRateZones'][1]['minutes'])
            except KeyError: 
                continue
    except FileNotFoundError:
            continue
    else:
        str_tmp2 = "A0"+str(person_number)
        person = list()
        person.append(str_tmp2)
        person.append(personal_hearts)
        total_hearts.append(person)
        
total_hearts


# In[138]:

with open('/Users/jegalsumin/Documents/Data Science/Class_Data-Science/week05/personal_total_hearts.csv', 'w', newline='') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerows(total_hearts)


# In[ ]:




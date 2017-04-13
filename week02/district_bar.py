
# coding: utf-8

# In[ ]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import pylab
import datetime
import numpy
import matplotlib.image
import matplotlib.pyplot as plt

tashu_file = open('/Users/jegalsumin/Documents/Class_Data-Science/week02/tashu.csv','r')
tashu_dict = csv.DictReader(tashu_file)
station_file = open('/Users/jegalsumin/Documents/Class_Data-Science/week02/station.csv','r')
station_dict = csv.DictReader(station_file)

max_station = 226

station = [""]*(max_station+1)
for row_station in station_dict:
    station[int(row_station['키오스크번호'])] = row_station['구별']

total_station = [0]*(max_station+1)
for count_station_row in tashu_dict:
    if(count_station_row['RENT_STATION']) is '':
        continue
    if(count_station_row['RETURN_STATION']) is '':
        continue
    total_station[int(count_station_row['RENT_STATION'])] +=1
    total_station[int(count_station_row['RETURN_STATION'])] +=1
    
region_gu = [0]*5
for k in range(0,max_station+1,1):
    if station[k] == '유성구':
        region_gu[0] += total_station[k]
    elif station[k] == '서구' :
        region_gu[1] += total_station[k]
    elif station[k] == '대덕구' :
        region_gu[2] += total_station[k]
    elif station[k] == '동구' :
        region_gu[3] += total_station[k]
    elif station[k] == '중구' :
        region_gu[4] += total_station[k]
        

region_gu = pd.Series(region_gu)

#plt.xticks((0,1,2,3,4),('Yusung-gu','Seo-gu','Daeduk-gu','Dong-gu','Jung-gu'))
plt.title('Num of stations per district')
region_gu.plot(kind='bar')
plt.axhline(0,color='k')
plt.show()


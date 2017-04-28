
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
from matplotlib import rcParams
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
import matplotlib.patches as mpatches
import matplotlib
import time 
from __future__ import print_function
get_ipython().magic('matplotlib inline')


# In[3]:

def movieLensDataLoad():
    ## user 영화 별점 data
    ratings = pd.read_csv("/Users/jegalsumin/Documents/Data Science/Data set/week06/ratings.csv")
    ## movie meta(타이틀,장르) data
    movies = pd.read_csv("/Users/jegalsumin/Documents/Data Science/Data set/week06/movies.csv")
    ## user가 영화에 tag를 기입한 data
    tags = pd.read_csv("/Users/jegalsumin/Documents/Data Science/Data set/week06/tags.csv")
    # tags = pd.read_csv("/Users/goodvc/Documents/data-analytics/movie-recommendation/ml-20m/tags.csv")
    return ( ratings, movies, tags )

#ratings, movies, tags = movieLensDataLoad('ml-20m')
ratings, movies, tags = movieLensDataLoad()


# In[37]:

prediction_list = pd.read_csv("/Users/jegalsumin/Documents/Data Science/Data set/week06/prediction.csv")
prediction_list


# In[19]:

prediction_list['userId'][0]


# In[4]:

ratings


# In[5]:

type(ratings)


# In[6]:

UM_matrix_ds = ratings.pivot(index='userId', columns='movieId', values='rating')


# In[7]:

UM_matrix_ds


# In[8]:

## 유사하면 1, 다르면 0으로 수렴
import math
from operator import itemgetter
from scipy.spatial import distance

def distance_cosine(a,b):
    return 1-distance.cosine(a,b)
def distance_correlation(a,b):
    return 1-distance.correlation (a,b)
def distance_euclidean(a,b):
    return 1/(distance.euclidean(a,b)+1)


# In[9]:

def nearest_neighbor_user( user, topN, simFunc ) :
    u1 = UM_matrix_ds.loc[user].dropna()
    ratedIndex = u1.index
    nn = {}
    
    ## Brute Force Compute
    for uid, row in UM_matrix_ds.iterrows():
        interSectionU1 = []
        interSectionU2 = []
        if uid==user:
            continue

        for i in ratedIndex:
            if False==math.isnan(row[i]):
                interSectionU1.append(u1[i])
                interSectionU2.append(row[i])
        interSectionLen = len(interSectionU1)


        ## At least 3 intersection items
        if interSectionLen < 3 :
            continue

        ## similarity functon
        sim = simFunc(interSectionU1,interSectionU2)


        if math.isnan(sim) == False:
            nn[uid] = sim

    ## top N returned
    return sorted(nn.items(),key=itemgetter(1))[:-(topN+1):-1]


# In[16]:

st=time.time()
print(nearest_neighbor_user(11, 3, distance_euclidean))
print(time.time()-st, 'sec')


# In[17]:

st=time.time()
print(nearest_neighbor_user(18, 3, distance_euclidean))
print(time.time()-st, 'sec')


# In[18]:

st=time.time()
print(nearest_neighbor_user(24, 3, distance_euclidean))
print(time.time()-st, 'sec')


# In[32]:

#test for list
b =[]
test1 = [(137735, 1.0), (137587, 1.0), (137546, 1.0)]
#test2 = [1]
test3 = 1
b.append([test3] + test1)
a1 = [(137688, 1.0), (129691, 1.0), (123539, 1.0)]
a2 = [2]
a3 = a2 + a1
b.append(a3)
b


# In[45]:

for index in range(0,10):
    userId = prediction_list['userId'][index]
    print(userId)


# In[46]:

st=time.time()
similar_user = []
for index in range(0,10):
    userId = prediction_list['userId'][index]
    similar_user.append([userId] + nearest_neighbor_user(userId, 3, distance_euclidean))
print(time.time()-st, 'sec')


# In[47]:

similar_user


# In[60]:

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


# In[61]:

st=time.time() 
print(predictRating(11,500))
print(time.time()-st, 'sec')


# In[79]:

st=time.time()
predict = []
for index in range(0,10):
    userId = prediction_list['userId'][index]
    movieId = prediction_list['movieId'][index]
    list_format = [userId] + predictRating(userId,movieId)
    predict.append(list_format)
print(predict)
print(time.time()-st, 'sec')


# In[63]:

prediction_list


# In[80]:

temp = predict
temp = [['userId','movieId','rating']]+temp
temp


# In[91]:

test_df = pd.DataFrame(predict)
test_df.columns = ['userId','movieId','rating']
print(test_df)
print(prediction_list)


# In[99]:

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
true = []
pred = []
for i in range(0,10) : 
    true = true + [prediction_list['rating'][i]]
    pred = pred + [test_df['rating'][i]]
print("squared error : "+str(mean_squared_error(true, pred)))
print("absolute error : "+str(mean_absolute_error(true, pred)))
#print("error : "+str(((pred-true)**2).mean()))


# In[ ]:




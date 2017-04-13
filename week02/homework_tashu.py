
# coding: utf-8

# In[1]:

import csv
from operator import itemgetter

def get_top10_station(tashu_dict, station_dict):
    """
    [역할]
    정류장 Top10 출력하기
    대여 정류장과 반납정류장을 합한 총 사용빈도수 Top10

    [입력]
    tashu_dict : csv.DictReader 형태의 타슈대여정보
    station_dict : csv.DictReader 형태의 정류장 정보

    [출력]
    Top10 정류장 리스트
    ex.) [[정류장 이름1, 정류장 번호1, 정류장1 count], [정류장 이름2, 정류장 번호2, 정류장2 count], .....] 형태
    """
    max_station = 226
    """    for row in tashu_dict:
        i = row['RENT_STATION']
        j = row['RETURN_STATION']
        if i is '':
            continue
        if j is '':
            continue
        if int(i) > max_station:
            max_station = int(i)
        if int(j) > max_station:
            max_station = int(j)"""


    total_station = [0]*(max_station+1)
    for count_station_row in tashu_dict:
        if(count_station_row['RENT_STATION']) is '':
            continue
        if(count_station_row['RETURN_STATION']) is '':
            continue
        total_station[int(count_station_row['RENT_STATION'])] +=1
        total_station[int(count_station_row['RETURN_STATION'])] +=1

    station = [""]*(max_station+1)
    for row_station in station_dict:
        station[int(row_station['키오스크번호'])] = row_station['명칭']
    
    for k in range(0,max_station+1,1):
        total_station_tuple = [station[k],str(k),total_station[k]]
        total_station[k] = total_station_tuple 
    
    return sorted(total_station, key=itemgetter(2), reverse=True)[:10]

def get_top10_trace(tashu_dict, station_dict):
    """
    [역할]
    경로 Top10 출력하기
    (대여정류장, 반납정류장)의 빈도수 Top10

    [입력]
    tashu_dict : csv.DictReader 형태의 타슈대여정보
    station_dict : csv.DictReader 형태의 정류장 정보

    [출력]
    Top10 경로 리스트
    ex.) [[출발정류장 이름1, 출발정류장 번호1, 반납정류장 이름1,
        반납정류장 번호2, 경로 count], [출발정류장 이름2, 출발정류장 번호2,
        반납정류장 이름2,  반납정류장 번호2, 경로count2], .....] 형태
    """
    max_station = 226
    trace = [[0 for x in range(max_station+1)] for y in range(max_station+1)]

    for count_trace_row in tashu_dict:
        if count_trace_row['RENT_STATION'] is '':
            continue
        if count_trace_row['RETURN_STATION'] is '':
            continue
        trace[int(count_trace_row['RENT_STATION'])][int(count_trace_row['RETURN_STATION'])] +=1
    
    station = [""]*(max_station+1)
    for row_station in station_dict:
        station[int(row_station['키오스크번호'])] = row_station['명칭']
    
    k=0
    total_trace = ['']*((max_station+1)*(max_station+1))
    for i in range(0,max_station+1,1):
        for j in range(0,max_station+1,1):
            trace_list = [station[i],str(i),station[j],str(j),trace[i][j]]
            total_trace[k] = trace_list
            k += 1
            
    return sorted(total_trace, key=itemgetter(4), reverse=True)[:10]


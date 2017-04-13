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
    return None

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
    return None

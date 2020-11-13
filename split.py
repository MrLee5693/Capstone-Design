import pandas as pd
import numpy as np
import warnings
import random
from random import sample 
from collections import Counter
from datetime import datetime
warnings.filterwarnings("ignore")

# 데이터 불러오기
train = pd.read_json("/daintlab/data/music_rec/train.json")
song_meta = pd.read_json("/daintlab/data/music_rec/song_meta.json")

# 필터링 기준 : 전체 플레이리스트에서 몇 번 이상 등장한 곡을 사용할 것인지
filtering = 25

# 발매일을 datetime 형태로 변환시키는 사용자 정의 함수, 결측치가 중간에 존재하여 try-except문으로 지정
def to_date(x):
    try:
        y = pd.to_datetime(x, format = "%Y%m%d")
    except:
        y = None
    return y

# 곡을 필터링하기 위한 전처리
train_song = train['songs']
song_counter = Counter([song for songs in train_song for song in songs])
song_dict = {x: song_counter[x] for x in song_counter}
song_dict = dict(filter(lambda x : x[1]>=filtering, song_dict.items())) # Counter를 통해 빈도를 구한 value의 값이 특정 기준을 넘는지 여부로 필터링

# 새로 전처리된 곡들에게 새로운 index를 준다.
song_id_sid = dict()
for i, song_id in enumerate(song_dict): 
    song_id_sid[song_id] = i 

# 각각의 곡들의 발매일을 구하기 위한 작업
song_meta = song_meta[song_meta["id"].notnull()] # 결측치 제거
song_meta["id"] = song_meta["id"].astype(int)
song_meta["issue_date"] = song_meta["issue_date"].astype(str)
# 19800000 같은 데이터를 19800101 같은 데이터로 바꿔 줌
song_meta["issue_date"] = song_meta["issue_date"].apply(lambda x : x[:4] + x[4:6].replace("00","01") + x[6:].replace("00","01"))
song_meta["issue_date"] = song_meta["issue_date"].apply(lambda x : to_date(x)) # datetime으로 바꿔줌
song_meta = song_meta[song_meta["issue_date"].notnull()] # 결측치 제거
song_meta["timestamp"] = song_meta["issue_date"].apply(lambda x : datetime.timestamp(x)) 
song_meta["itemId"] = song_meta["id"].apply(lambda x : song_id_sid.get(x))
song_meta = song_meta[song_meta["itemId"].notnull()]

issue_date = dict(zip(song_meta["itemId"],song_meta["timestamp"])) # 곡들과 timestamp를 매치시키기 위해

items = set(issue_date.keys())
print(max(song_id_sid.values()))
num_items = max(issue_date.keys()) + 1
print("n_items = {}".format(num_items))
# 새로운 index 주기
train['itemId'] = train['songs'].apply(lambda x: [song_id_sid.get(item) for item in x if song_id_sid.get(item) != None])
train['itemId'] = train['itemId'].apply(lambda x: [item for item in x if issue_date.get(item) != None])
train.loc[:,'num_items'] = train['itemId'].map(len) # 각 user당 가지고 있는 곡들의 개수 정보를 가진 컬럼 만들기
train = train[train["num_items"]>1] # leave one out 방식을 위해 최소 2개 이상 데이터를 가진 user들만 필터링
n_data = len(train)
train["userId"] = range(n_data)


train["timestamp"] = train["itemId"].apply(lambda x: [issue_date.get(item) for item in x if issue_date.get(item) != None]) # timestamp 적용
# test data 생성
train["test_index"] = train["timestamp"].apply(lambda x : np.array(x).argmax())
train["test_rating"] = train.apply(lambda x: x["itemId"][x["test_index"]], axis = 1)
train["test"] = train["itemId"].apply(lambda x : list(items - set(x)))

# Train Negative & Test Negative Split
train["test_negative"] = train["test"].apply(lambda x : random.sample(x,99))
train["train_negative"] = train.apply(lambda x : list(items - set(x["itemId"]) - set(x["test_negative"])), axis = 1)

train.apply(lambda x : x["itemId"].remove(x["test_rating"]), axis = 1) # Train dataset에서 Test data 제거
train.rename(columns = {"itemId":"train_positive"}, inplace = True)

# 각각의 user에 따라 각각의 집단을 묶어서 리스트로 저장
train = train[["userId","train_positive","train_negative","test_rating","test_negative"]].reset_index()
print(train)

# 파일 저장
#https://towardsdatascience.com/the-best-format-to-save-pandas-data-414dca023e0d
train.to_feather("melon_"+str(num_items)+".ftr")
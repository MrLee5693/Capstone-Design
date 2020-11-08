# Capstone Design
## 딥러닝을 활용한 음악 추천 시스템 연구<br>
* Dataset : Melon playlist
## 곡 35919개 사용 
### dataframe columns = ["userId","train_positive","train_negative","test_rating","test_negative"]<br>
* userId : user id
* train_positive : interacted song
* test_rating : Leave one out으로 고른 test song (곡 발매일 기준 가장 최신 곡을 test song으로 분류)
* test_negative : train_positive와 test_rating에 없는 곡들 중 랜덤하게 뽑은 각 유저당 99개의 곡들의 집합
(테스트할 때 한 번도 못 보게 하기 위해 따로 분류) 
* train_negative : 각 interacted song당 num_negative 만큼 샘플링하기 위해 train_positive, test_rating, test_negative와 겹치지 않는 모든 곡들의 집합 
(학습을 진행할 때 train_negative에서 num_negative 만큼 매 에폭마다 뽑아주면서 학습)

## 실험결과
* 업데이트 예정


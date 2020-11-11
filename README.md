# Capstone Design
## 딥러닝을 활용한 음악 추천 시스템 연구<br>
* Dataset : [Melon playlist](https://arena.kakao.com/c/8)
- [x] **Users : 105141** 
- [x] **Songs : 35919**  <br>
* Model : [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031)[![GitHub stars](https://img.shields.io/github/stars/hexiangnan/neural_collaborative_filtering.svg?logo=github&label=Stars)]
<img width='768' src='https://user-images.githubusercontent.com/52492949/98676852-7edb3700-239f-11eb-91e3-e6f40c2ece45.png'>

### Metric 

- [x] **NDCG@10**
- [x] **HR@10** 

---

## How to use 

### Dependencies

- [x] **Pytorch** 


## Experiment results

- [x] **Num of Neg : 1,5,10**<br> 
>
- [x] **Num Factor : 8,16,32**<br> 
>
- [x] **Num Layer : 1,2,3**<br>


<details>
<summary> Total Experiment results </summary>
<div markdown="1">

| HR@10 | NDCG@10 | Num of Neg | Num Factor | Num Layer |
|:-----:|:-------:|:----------:|:----------:|:---------:|
| 0.7912|   0.5140|      1     |      8     |     1     |
| 0.8013|   0.5444|      5     |      8     |     1     |
| 0.7469|   0.5026|      10    |      8     |     1     |
| -     |  -      |      1     |      16    |     1     |
| -     |  -      |      5     |      16    |     1     |
| -     |  -      |      10    |      16    |     1     |
| -     |  -      |      1     |      32    |     1     |
| -     |  -      |      5     |      32    |     1     |
| -     |  -      |      10    |      32    |     1     |
| -     |  -      |      1     |      8     |     2     |
| -     |  -      |      5     |      8     |     2     |
| -     |  -      |      10    |      8     |     2     |
| -     |  -      |      1     |      16    |     2     |
| -     |  -      |      5     |      16    |     2     |
| -     |  -      |      10    |      16    |     2     |
| -     |  -      |      1     |      32    |     2     |
| -     |  -      |      5     |      32    |     2     |
| -     |  -      |      10    |      32    |     2     |
| 0.8030|   0.5412|      1     |      8     |     3     |
| 0.8026|   0.5524|      5     |      8     |     3     |
| 0.7696|   0.5324|      10    |      8     |     3     |
| 0.8155|   0.5590|      1     |      16    |     3     |
| 0.8152|   0.5732|      5     |      16    |     3     |
| 0.7860|   0.5465|      10    |      16    |     3     |
| -     |  -      |      1     |      32    |     3     |
| -     |  -      |      5     |      32    |     3     |
| -     |  -      |      10    |      32    |     3     |

</div>
</details>
# Capstone Design
## -딥러닝을 활용한 음악 추천시스템 연구-
---
* Dataset : [Melon playlist](https://arena.kakao.com/c/8)<br>
`Users` : **105141** <br>
`Songs` : **35919**  <br>
* Model : [Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031)[![GitHub stars](https://img.shields.io/github/stars/hexiangnan/neural_collaborative_filtering.svg?logo=github&label=Stars)]
<img width='768' src='https://user-images.githubusercontent.com/52492949/98676852-7edb3700-239f-11eb-91e3-e6f40c2ece45.png'>

---

### Performance Metrics

- [x] **NDCG@10**
- [x] **HR@10** 

---

## How to use 
### Languages 

<p align="left">
  <a href="#">
    <img src="https://github.com/MikeCodesDotNET/ColoredBadges/blob/master/svg/dev/languages/python.svg" alt="python" style="vertical-align:top; margin:6px 4px">
  </a> 

</p>

### Tools
<p align="left">
  <a href="#">
    <img src="https://github.com/MikeCodesDotNET/ColoredBadges/blob/master/svg/dev/tools/docker.svg" alt="docker" style="vertical-align:top; margin:6px 4px">
  </a> 

  <a href="#">
    <img src="https://github.com/MikeCodesDotNET/ColoredBadges/blob/master/svg/dev/tools/bash.svg" alt="bash" style="vertical-align:top; margin:6px 4px">
  </a> 

  <a href="#">
    <img src="https://github.com/MikeCodesDotNET/ColoredBadges/blob/master/svg/dev/tools/visualstudio_code.svg" alt="visualstudio_code" style="vertical-align:top; margin:6px 4px">
  </a> 

</p>

---

## Files
> `split.py`: prepare train/test dataset
>
> `Data_Loader.py`: preprocess
>
> `metrics.py`: evaluation metrics including hit ratio(HR) and NDCG
>
> `model.py`: NCF model
>
> `evaluate.py`: evaluate
>
> `main.py`: main file

---

## Experiment results
<details>
    <summary>  Num Neg : 1,5,10 
    </summary>
<div markdown="1">

| HR@10 | NDCG@10 | Num of Neg | Num Factor | Num Layer |
|:-----:|:-------:|:----------:|:----------:|:---------:|
| 0.7502|   0.4697|      1     |      4     |     1     |
| 0.7328|   0.4705|      5     |      4     |     1     |
| 0.6362|   0.4021|      10    |      4     |     1     |
| 0.7912|   0.5140|      1     |      8     |     1     |
| 0.8013|   0.5444|      5     |      8     |     1     |
| 0.7469|   0.5026|      10    |      8     |     1     |
| 0.8224|   0.5610|      1     |      16    |     1     |
| 0.8193|   0.5795|      5     |      16    |     1     |
| 0.7984|   0.5598|      10    |      16    |     1     |
| 0.7678|   0.4896|      1     |      4     |     2     |
| 0.7757|   0.5152|      5     |      4     |     2     |
| 0.7064|   0.4631|      10    |      4     |     2     |
| 0.7965|   0.5266|      1     |      8     |     2     |
| 0.8000|   0.5527|      5     |      8     |     2     |
| 0.7481|   0.5055|      10    |      8     |     2     |
| 0.8152|   0.5576|      1     |      16    |     2     |
| 0.8193|   0.5795|      5     |      16    |     2     |
| 0.7898|   0.5530|      10    |      16    |     2     |
| 0.7824|   0.5097|      1     |      4     |     3     |
| 0.7882|   0.5372|      5     |      4     |     3     |
| 0.7185|   0.4769|      10    |      4     |     3     |
| 0.8030|   0.5412|      1     |      8     |     3     |
| 0.8026|   0.5524|      5     |      8     |     3     |
| 0.7696|   0.5324|      10    |      8     |     3     |
| 0.8155|   0.5590|      1     |      16    |     3     |
| 0.8152|   0.5732|      5     |      16    |     3     |
| 0.7860|   0.5465|      10    |      16    |     3     |

</div>
</details>


<details>
    <summary>  Num Factor : 4,8,16
    </summary>
<div markdown="1">

</div>
</details>

<details>
    <summary>  Num Layer : 1,2,3
    </summary>
<div markdown="1">

</div>
</details>


<details>
    <summary>  Total Experiment results
    </summary>
<div markdown="1">



</div>
</details>
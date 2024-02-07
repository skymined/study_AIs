import numpy as np

## 1. 1차원 배열 두 개 기본 연결

a_1 = np.array([1, 2, 3])
b_1 = np.array([4, 5, 6])

array_1 = np.concatenate((a_1,b_1))
pass
## 2. 2차원 배열 두 개를 행으로 연결 :두 개의 2차원 배열이 주어졌을 때, 이를 행(axis 0)을 따라 연결하세요.

a_2 = np.array([[1, 2], [3, 4]])
b_2 = np.array([[5, 6], [7, 8]])

array_2 = np.concatenate((a_2, b_2), axis=0)


## 3. 2차원 배열 두 개를 열로 연결

a_3 = np.array([[1, 2], [3, 4]])
b_3 = np.array([[5, 6], [7, 8]])

array_3 = np.concatenate((a_3, b_3), axis=1)


## 4. 다른 차원의 배열을 np.newaxis를 사용하여 연결
## 1차원 배열과 2차원 배열이 주어졌을 때, `np.newaxis`를 사용하여 1차원 배열을 수정한 후, 2차원 배열과 새로운 축을 따라 연결하세요.


a_4 = np.array([1, 2, 3])
b_4 = np.array([[4, 5, 6], [7, 8, 9]])

# 새로운 축을 추가하기
a_4 = a_4[np.newaxis, :]
array_4 = np.concatenate((a_4, b_4), axis=1)
pass
## 5. 혼합 차원의 세 배열 연결
## 1차원 배열 두 개와 2차원 배열 하나가 주어졌을 때, 모든 배열을 연결하세요. 두 1차원 배열은 연결 전에 행으로 처리되어야 합니다.

a_5 = np.array([1, 2, 3])
b_5 = np.array([4, 5, 6])
c_5 = np.array([[7, 8, 9], [10, 11, 12]])


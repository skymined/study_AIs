py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list

import numpy as np

np_array = np.array([[7, 8]
                    ,[9,10]
                    ,[11,12]])  # 행렬 = array

pass

# 구분 위한 type 확인
type(py_list)
# <class 'list'> .sum() 쓸 수 없음
type(np_array)
# <class 'numpy.ndarray'>  .sum() 쓸 수 있음 -> 상호 편리성

np_array.sum(axis=0) # row 단위 연산
# array([27, 30]) axis는 row단위..?
np.sum(np_array, axis=0)
# array([27,30])
np_array.sum(axis=1) # 열 단위 연산
# array([15, 19, 23])

# py_list를 array 형태로 바꾸기
np_array_second = np.array(py_list)
np.concatenate((np_array, np_array_second), axis=0)
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])

np.concatenate((np_array, np_array_second), axis=1)
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])
import numpy as np

arr_1 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])


arr_2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

mul_arr = arr_1 @ arr_2

print(mul_arr)
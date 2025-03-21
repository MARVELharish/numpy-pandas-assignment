import numpy as np

arr_1 = np.random.randint(1,10,5)
arr_2 = np.random.randint(11,20,5)

print(arr_1,"\n", arr_2)

hori_arr = np.hstack((arr_1,arr_2))
verti_arr = np.vstack((arr_1,arr_2))

print(hori_arr)
print(verti_arr)
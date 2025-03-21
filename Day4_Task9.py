import numpy as np

arr = np.random.randint(1,40,10)
# arr = np.random.rand(10)
print(arr)

max_arr = np.max(arr)
min_arr = np.min(arr)

max_index_arr = np.argmax(arr)
min_index_arr = np.argmin(arr)

print(max_index_arr)
print(min_index_arr)



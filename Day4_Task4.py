import numpy as np

arr = np.random.randint(1,10,10)

print(arr)
print(np.median(arr).round(2))
print(np.mean(arr).round(2))
print(np.std(arr).round(2))
print(np.var(arr).round(2))
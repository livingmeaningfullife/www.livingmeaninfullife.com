import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]) # where values are even
x = np.where(arr%2 == 0)
print(x)

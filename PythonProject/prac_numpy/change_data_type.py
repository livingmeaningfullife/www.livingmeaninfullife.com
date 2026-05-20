import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

# or use int as primitive data type
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
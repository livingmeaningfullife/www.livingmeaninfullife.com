import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)


import numpy as np
try:
    arr = np.array([1, 2, 3, 847462133], dtype='i2')
except OverflowError:
    print('overflow error') # throws error
print(arr)
print(arr.dtype)

try:
    arr = np.array(['a', '2', '3'], dtype='i')
except ValueError:
    print('ValueError error')
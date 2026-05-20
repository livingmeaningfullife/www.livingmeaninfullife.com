# The searchsorted() method is assumed to be used on sorted arrays.

import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7) # index where 7 should be inserted to remain in sorted order: output = 1
print(x)

x = np.searchsorted(arr, 7, side='right') # where from right side : output = 2
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6]) # where to insert 2,4,6 respectively : returns array corresponding to it
print(x)


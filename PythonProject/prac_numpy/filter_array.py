import numpy as np

# filtering based on boolean array - boolean index list
#  If the value at an index is True that element is contained in the filtered array,
#  if the value at that index is False that element is excluded from the filtered array.

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)



arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42 # filter array - boolean filter array => [False False True True]

newarr = arr[filter_arr] # filtering => [43 44] as rest all become filtered out

print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

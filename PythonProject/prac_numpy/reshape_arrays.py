import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3) # 4 is no of rows and 3 is no of columns, 4*3 = 12

print(newarr)


# from 1D to 3D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
try:
    newarr = arr.reshape(3, 3)
except:
    print("error")
else:
    print(newarr)

#reshape just gives a view, not a copy
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) # gives [1 2 3 4 5 6 7 8] - hence view, not copy


# Pass -1 as the value, and NumPy will calculate this number for you.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

# flatten arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

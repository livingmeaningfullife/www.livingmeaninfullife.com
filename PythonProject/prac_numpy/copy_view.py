import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)






# view should be affected if we make changes - it just let us view the current array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)
# so in both, first element is 42 instead of being 1

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)
# array is also affected by the view, both become 31

# now let's check if the location of both arrays is the same
print(id(arr))
print(id(x))
# they are different, hence they don't point to same location



# copies own the data, but views don't own the data - let's check
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base) # None
print(y.base) # [1 2 3 4 5]
# if base is None, then it means the array owns the data, it has no base, it is itself the base
# if base is some value, then it means the array doesn't own the data, it has some base
# slicing
str1 = "Hello World"
str2 = str1[1:5] #1 is starting index and 5 is ending index + 1, or ending index is 4
print(str2)

#negative slicing
"""
H     e    l   l   o       w   o   r   l   d
-11  -10   -9 -8  -7  -6  -5  -4  -3  -2  -1  
"""
print(str1[-4:-1]) #shall print: orl

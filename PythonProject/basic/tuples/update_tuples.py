# change tuple values - convert from tup to list and then back to tuple
tup = ('apple', 'banana', 'cherry')
y = list(tup)
y[0] = 'mango'
tup = tuple(y)
print(tup)

# add items to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# add tuple to tuple
tt = ("apple", "banana", "cherry")
y = ("orange",)
tt += y
print(tt)


th = ("apple", "banana", "cherry")
y = list(th)
y.remove("apple")
th = tuple(y)

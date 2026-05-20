thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # adds to the end
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # adds to particular index
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# del removes list item
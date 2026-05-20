# syntax:: newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# example: add items from fruits list to newlist (empty initially), add only those items which have the letter 'a' in them
# primitive approach
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# using list comprehension
newlist = [x for x in fruits if "a" in x]
print(newlist)

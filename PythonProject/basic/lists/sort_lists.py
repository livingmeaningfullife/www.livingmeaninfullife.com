thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#reverse a list - reverses items
thislist = ["orange", "mango", "kiwi", "pineapple"]
thislist.reverse()
print(thislist)

# descending sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

#custom sort function
# ex: sort according to how close a number is to 50
def myfunc(n):
    return abs(n-50)
thislist = [100,50,65,82,23]
thislist.sort(key=myfunc) # key takes a function with one parameter of the current data and expects a return value which will be used to compare with other similar values

print(thislist)

# by default, in strings sorting is case-sensitive, to make it case-insensitive :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = lambda str: str.lower())
print(thislist)

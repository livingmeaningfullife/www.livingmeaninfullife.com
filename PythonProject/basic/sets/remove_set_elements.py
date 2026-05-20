# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove "banana" by the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Difference b/w remove & discard: if item to remove does not exist - remove() raise error
# if item to remove does not exist - discard() does not raise any error

thisset = {"apple", "banana", "cherry"}
thisset.clear() # clears the set entirely
print(thisset)

ll = ["apple", "banana", "cherry"]
ll[1:2] = ["blackcurrant", "watermelon"]
print(ll) # banana is replaced by blackcurrant and an extra item watermelon is added
#Note: The length of the list will change when the number
# of items inserted does not match the number of items replaced.



"""If you insert less items than you replace, the new items will be
 inserted where you specified, and the remaining items will move accordingly:"""
tl = ["apple", "banana", "cherry"]
tl[1:3] = ["watermelon"]
print(tl)
# output : ['apple', 'watermelon']
# means banana was replaced by watermelon and the last item was removed because it was nil
# hence we can see this expression as tl[1:3] = ["watermelon", nil] - which removes the 3rd element hence
# now let's try when there is another item at end called mango
tl = ["apple", "banana", "cherry", "mango"]
print(tl)
tl[1:3] = ["watermelon"]
print(tl)
# hence here mango remains and banana and cherry are replaced by watermelon
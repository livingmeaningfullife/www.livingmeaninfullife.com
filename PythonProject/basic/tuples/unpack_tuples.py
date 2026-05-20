fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits # red is a list here which is preceded by asterik - it will get all remaining values inside itself

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits # tropic is a list which will get middle values
# only one starred element is allowed in statement, because else it will create ambiguity how much should one list hold
print(green)
print(tropic)
print(red)


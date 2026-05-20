tl = ["apple", "banana", "cherry"]
for i in range(len(tl)):
    print(tl[i])

i = 0
while i < len(tl):
    print(tl[i])
    i = i + 1


# list comprehension - shorthand
[print(x) for x in tl]
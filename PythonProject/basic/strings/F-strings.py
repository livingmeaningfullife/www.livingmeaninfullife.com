age = 36
name = f"My Name is John, I am {age} years old"
print(name)

# it can include modifiers as well
price = float(input("Price: ")) # taking custom input
txt = f"The price is {price:.2f} dollars"
print(txt)

# we can also perform math operation in placeholder { }
count = float(input("Count: "))
total = f"The price is {count * price:.2f} dollars"
print(total)
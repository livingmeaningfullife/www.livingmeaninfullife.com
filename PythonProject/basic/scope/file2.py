# changing value of global variable inside function

x = 300
def myfun():
    global x
    x = 200

myfun()
print(x)
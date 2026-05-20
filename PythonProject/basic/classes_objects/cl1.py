class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

    def __str__(self):
        return f"{self.name}({self.age})"
    #It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:



p1 = Person("John", 36)
print(p1)
p1.myfunc()


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x # hence refers to upper x and doesn't redefine an x variable
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

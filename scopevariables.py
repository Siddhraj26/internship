def num():
  x = 300
  print(x)

num()       #local variable


def num():
  x = 300
  def mynum():
    print(x)      #nonlocal variable
  mynum()

num()


x = 300
def num():
  print(x)            #global variable
num()
print(x)

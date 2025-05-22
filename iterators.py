mytuple = ("bmw" ,"porsche" ,"jaguar")
myit = iter (mytuple)
print(next(myit))
print(next(myit))
print(next(myit))                  #iterator for a tuple


mytuple = ("jaguar")
myit = iter (mytuple)
print(next(myit))
print(next(myit))
print(next(myit))                  #iterrator for a string


mytuple = ("bmw" ,"porsche" ,"jaguar")
for x in (mytuple):
    print(x)                        #iterator for using in() loop


mytuple = ("jaguar")
for x in (mytuple):
    print(x)                        #iterrator for a string


class a:
    def __iter__(self):
        self.num=1
        return self
    
    def __next__(self):
        x=self.num
        self.num+=1
        return x
myclass= a()
myiter= iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))                            #using the loop and iterator function


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)                            #terminating the iterator using the loop



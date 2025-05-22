#A Decorator in Python is a function that receives another function as argument.
#The argument function is the one to be decorated by decorator.
#The behaviour of argument function is extended by the decorator without actually modifying it.
def my_function(x):
   print("The number is=",x)

def my_decorator(some_function,num):
   def wrapper(num):
      print("Inside wrapper to check odd/even")
      if num%2 == 0:
         ret= "Even"
      else:
         ret= "Odd!"
      some_function(num)
      return ret
   print ("wrapper function is called")
   return wrapper

no=10
my_function = my_decorator(my_function, no)
print ("It is ",my_function(no))


#@classmethod Decorator
#The classmethod is a built-in function. It transforms a method into a class method.
#A class method is different from an instance method. 
#Instance method defined in a class is called by its object.
#The method received an implicit object referred to by self.
#A class method on the other hand implicitly receives the class itself as first argument.
class counter:
   count=0
   def __init__(self):
      print ("init called by ", self)
      counter.count=counter.count+1
      print ("count=",counter.count)
   @classmethod
   def showcount(cls):
      print ("called by ",cls)
      print ("count=",cls.count)

c1=counter()
c2=counter()
print ("class method called by object")
c1.showcount()
print ("class method called by class")
counter.showcount()



#@staticmethod Decorator
#The staticmethod is also a built-in function in Python standard library.
#It transforms a method into a static method.
#Static method doesn't receive any reference argument whether it is called by instance of class or class itself.
#Following notation used to declare a static method in a class −
class counter:
   count=0
   def __init__(self):
      print ("init called by ", self)
      counter.count=counter.count+1
      print ("count=",counter.count)
   @staticmethod
   def showcount():
      print ("count=",counter.count)

c1=counter()
c2=counter()
print ("class method called by object")
c1.showcount()
print ("class method called by class")
counter.showcount()



#@property Decorator
#Python's property() built-in function is an interface for accessing instance variables of a class. 
#The @property decorator turns an instance method into a "getter"
#for a read-only attribute with the same name, and it sets the docstring for the property to 
#"Get the current value of the instance variable."

#You can use the following three decorators to define a property −
#@property − Declares the method as a property.
#@<property-name>.setter: − Specifies the setter method for a property that sets the value to a property.
#@<property-name>.deleter − Specifies the delete method as a property that deletes a property.
class car:
   def __init__(self, speed=40):
      self._speed=speed
      return
   @property
   def speed(self):
      return self._speed
   @speed.setter
   def speed(self, speed):
      if speed<0 or speed>100:
         print ("speed limit 0 to 100")
         return
      self._speed=speed
      return

c1=car()
print (c1.speed) #calls getter
c1.speed=60 #calls setter
#Function annotations
#Annotations are not enforced by Python; they are purely informational.
#You can use any object as an annotation, but type hints (like str, int, list) are common.
#Annotations are stored in the function's __annotations__ attribute.

def myfunction(a: int, b: int):
   c = a+b
   return c
   print (myfunction(10,20))
print (myfunction("Hello ", "Python"))


#Function Annotations With Return Type
#Annotations are ignored at runtime, but are helpful for the IDEs and static type checker libraries such as mypy.
#You can give annotation for the return data type as well.
#After the parentheses and before the colon symbol, put an arrow (->) followed by the annotation.

def myfunction(a: int, b: int) -> int:
   c = a+b
   return c
print(myfunction(56,88))
print(myfunction.__annotations__)


#Function Annotations With Expression
#As using the data type as annotation is ignored at runtime, you can put any expression which acts as the metadata for the arguments.
#Hence, function may have any arbitrary expression as annotation.

def total(x: 'marks in Physics', y: 'marks in chemistry'):
   return x + y
print(total(86, 88))
print(total.__annotations__)


#Function Annotations With Default Arguments
#If you want to specify a default argument along with the annotation,
#you need to put it after the annotation expression. Default arguments must come after the required arguments in the argument list.

def myfunction(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c
print (myfunction(10))
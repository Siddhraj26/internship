#Normal argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


#Arbitary Argument
#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")


#Keyword argument
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Arbitrary Keyword Arguments
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")


#Positional-Only Arguments
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):
  print(x)
my_function(3)


#Keyword-Only Arguments
#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)
my_function(x = 3)


#Combine Positional-Only and Keyword-Only
#You can combine the two argument types in the same function.
#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)
#Recursive Function
#In Python, we know that a function can call other functions. It is even possible for the function to call itself.
#These types of construct are termed as recursive functions.
#The following image shows the working of a recursive function called recurse.

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))

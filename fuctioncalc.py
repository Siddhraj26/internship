def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def modulus(a,b):
    return a%b

def exponentiation(a,b):
    return a**b

def floordivision(a,b):
    return a//b

def calculator():
    print("Enter the operation to be performed")
    print("1. Add")
    print("2. Subtarct")
    print("3. Multiply")
    print("4. divide")
    print("5. modulus")
    print("6. exponentiation")
    print("7. floordivision")

choice = float(input("Enter choice (1/2/3/4): "))

if choice in ('1','2','3','4','5','6','7'):
    num1=float(input("Enter the number 1:"))
    num2=float(input("Enter the number 2:"))

if choice == '1':
    print("The result is:",{add(num1, num2)})

elif choice == '2':
    print("The result is:",{subtract(num1, num2)})

elif choice == '3':
    print("The result is:",{multiply(num1, num2)})

elif choice == '4':
    print("The result is:",{divide(num1, num2)})

elif choice == '5':
    print("The result is:",{modulus(num1, num2)})

elif choice == '6':
    print("The result is:",{exponentiation(num1, num2)})

elif choice == '7':
    print("The result is:",{floordivision(num1, num2)})

else:
    print("Invalid input")

calculator()
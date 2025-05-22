value1 = float(input("enter the value 1:"))
value2 = float(input("enter the value 2:"))
operation = input("enter the operation to be performed (add/subtract/multiply/divide/modulus):")

if operation == "add":
    result = value1 + value2
    print("The result of addition is:", result)
    
elif operation == "subtract":
    result = value1 - value2
    print("The result of subtraction is:", result)

elif operation == "multiply":
    result = value1 * value2
    print("The result of multiplication is:", result)
    
elif operation== "divide":
    result = value1 / value2
    print("The result of division is:", result)

elif operation == "modulus":
    result = value1 % value2
    print("The result of modulus is:", result)
    
else:
    print("Invalid operation")
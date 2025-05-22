# '''
# 1. Python Data Types & Type Casting
# Question:
# You receive a JSON API response with mixed types for numeric fields. Write a function that parses
# this response and ensures all numeric fields are float, even if they come as strings or integers.
# Handle nested dictionaries and lists.
# '''
# import json
# x = {
    # "a": 10,
    # "b": 20.5,
    # "c": -1
# }
# print(type(x["a"]))  
# print(type(x["b"]))  
# print(type(x["c"]))  
# y = json.dumps(x)
# print(y)
# 
'''
2. Python Strings & String Formatting
Question:
 Write a function extract_emails(text: str) -> List[str] that uses regular expressions to find and return all 
 valid email addresses from a given string. Then format the output as:
 Found emails: email1, email2, ...
'''

import re 
def extract_emails(text: str):
    email_pattern =f"[a-zA-Z]*{9}*@[a-zA-Z]*.[a-zA-Z]*"
    return re.findall(email_pattern, text)
def main():
    user_input = input("Enter a string to extract emails: ")
    emails = extract_emails(user_input)
    
    if emails:
        print("This is the right format")
    else:
        print("The input format is wrong")
if __name__ == "__main__":
    main()

'''
3. Python Lists & List Comprehension    
Question:
 Given a 2D list of integers, write a one-liner list comprehension to flatten it and return only unique even numbers sorted in descending order.
'''
 
matrix = [[1, 2, 3], [4, 4, 5], [6, 7, 8]]
result = sorted({num for row in matrix for num in row if num % 2 == 0},reverse=True)
print(result)
 
'''
4. Python Dictionaries
Question:
 You have a list of student records like:
python
CopyEdit
[{"name": "A", "score": 90}, {"name": "B", "score": 80}, {"name": "A", "score": 85}]

Write a function to return a dictionary where each student name maps to the average of their scores.
''' 

def average_scores(records):
    scores = {}  
    counts = {}  
    for record in records:
        name = record["name"]
        score = record["score"]
        if name in scores:
            scores[name] += score      
            counts[name] += 1          
        else:
            scores[name] = score       
            counts[name] = 1           
    averages = {}
    for name in scores:
        averages[name] = scores[name] / counts[name]  
    return averages
records = [{"name": "Krishna", "score": 90}, {"name": "Siddhraj", "score": 80}, {"name": "Krishna", "score": 85}]
print(average_scores(records))

'''
5. Python For Loops & Conditionals
Question:
 Write a function that takes a list of integers and returns a dictionary grouping them 
 by "even" and "odd" keys, with each value being a list of numbers that are also divisible by 3.
'''

def divisible_three(numbers):
    result = {"even": [], "odd": []}
    for num in numbers:
        if num % 3 == 0:
            if num % 2 == 0:
                result["even"].append(num)
            else:
                result["odd"].append(num)
    return result
numbers = [1, 2, 3, 6, 9, 12, 15, 18, 20]
print(divisible_three(numbers))

'''
6. Python Functions & Lambda
Question:
 Create a higher-order function apply_to_list(func, lst) that applies a lambda to a list. Demonstrate it with a lambda that removes vowels from strings in the list.
'''

def list(func, lst):
    return [func(item) for item in lst]
remove_vowels = lambda a: ''.join(char for char in a if char.lower() not in 'aeiou')
strings = ["hello", "world", "python", "lambda"]
result = list(remove_vowels, strings)
print(result)

'''
7. Python Classes/Objects & Inheritance
Question:
Design a base class Shape with an abstract method area().
Then, implement two subclasses Rectangle and Circle that compute their respective areas
and demonstrate polymorphism with a list of shape instances.
'''

from abc import ABC
import math 

class Shape(ABC):
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius **2

if __name__=="__main__":
    shapes=[]

    print("Enter the details of Rectangle")
    width=float(input("Width:"))
    height=float(input("Height:"))
    shapes.append(Rectangle(width,height))

    print("Enter the Details of Circle")
    radius=float(input("Radius:"))
    shapes.append(Circle(radius))

    print("Areas of the shapes:")
    for shape in shapes:
        print (f"{type(shapes).__name__}:{shape.area()}")

'''
8. Python Try...Except & JSON
Question:
Write a robust function that:
Loads a JSON string,
Validates the presence of required fields ("name", "age"),
Raises custom exceptions for missing or malformed fields,
Returns a Python dict on success.
'''

import json

class MissingFieldError(Exception):
    pass

class MalformedFieldError(Exception):
    pass

def load_and_validate_json(json_string):
  
    static_value = {"name": "John Doe", "age": 30}

    try:
        print("hello")
        data = json.loads(json_string)
        
        print (data)

      
        if "name" not in data:
            raise MissingFieldError("Missing required field: 'name'")
        if "age" not in data:
            raise MissingFieldError("Missing required field: 'age'")

        
        if not isinstance(data["name"], str):
            raise MalformedFieldError("'name' must be a string")
        if not isinstance(data["age"], int):
            raise MalformedFieldError("'age' must be an integer")

        if data["name"] != static_value["name"]:
            print(f"Provided name is not correct. Correct name is: {static_value['name']}")
            data["name"] = static_value["name"]
        if data["age"] != static_value["age"]:
            print(f"Provided age is not correct. Correct age is: {static_value['age']}")
            data["age"] = static_value["age"]

        return data

    except json.JSONDecodeError:
        print("Invalid JSON format")
    except (MissingFieldError, MalformedFieldError) as e:
        print(f"Validation error: {e}")


user_input = input("Enter a JSON string: ")
user_age   = int(input("Enter a JSON string: "))
a= {"name": user_input, "age": user_age}
json_string = json.dumps(a)
result = load_and_validate_json(json_string)
if result:
    print("Validated JSON:", result)

'''
9. Python Modules & Scope
Question:
Create a module config.py with global variables. Then, in another module, write functions
that safely access and update these variables using global
'''
import myconfig
myconfig.greeting("sid")
a=myconfig.person1["age"]
print(a)                     

'''
10. Python Iterators & Generators
Question:
Write a custom iterator class PrimeIterator(n) that yields the first n prime numbers. 
'''

class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.current += 1
        while not self._is_prime(self.current):
            self.current += 1
        self.count += 1
        return self.current

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

user_input = int(input("Enter the number of primes to generate: "))
primes = PrimeIterator(user_input)
for prime in primes:
    print(prime)
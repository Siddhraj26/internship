#Using Generator Functions
#The generator function uses 'yield' statement for returning the values all at a time.
#Each time the generators __next__() method is called the generator resumes where it left off i.e. from right after the last yield statement.
def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1
counter = count_up_to(5)
for number in counter:
    print(number)


#Using Generator Expressions
#Generator expressions provide a compact way to create generators. 
# They use a syntax similar to list comprehensions but used parentheses i.e. "{}" instead of square brackets i.e. "[]"
gen_expr = (x * x for x in range(1, 6))
for value in gen_expr:
    print(value)


#Exception Handling in Generators
#We can create a generator and iterate it using a 'while' loop with exception handling for 'StopIteration' exception.
#The function in the below code is a generator that successively yield integers from 1 to 5.
#When this function is called, it returns an iterator.
#Every call to next() method transfers the control back to the generator and fetches next integer.
def generator(num):
   for x in range(1, num+1):
      yield x
   return
   
it = generator(5)
while True:
   try:
      print (next(it))
   except StopIteration:
      break

#Asynchronous Generator
#An asynchronous generator is a co-routine that returns an asynchronous iterator.
#A co-routine is a Python function defined with async keyword, and it can schedule and await other co-routines and tasks.
#Just like a normal generator, the asynchronous generator yields incremental item in the iterator for 
#every call to anext() function, instead of next() function.
import asyncio
async def async_generator(x):
   for i in range(1, x+1):
      await asyncio.sleep(1)
      yield i
      async def main():
       async for item in async_generator(5):
        print(item)
       asyncio.run(main())
       
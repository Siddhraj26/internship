#print's the original string
name=" USE python array"
print("original string") 
print(name)


#capitalize() Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize() 
print (x)


#casefold() Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


#center() Returns a centered string
txt = "banana"
x = txt.center(20)
print(x)


#count() Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


#encode() Returns an encoded version of the string
txt = "My name is Ståle"
x = txt.encode()
print(x)


#endswith() Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)


#expandtabs()	Sets the tab size of the string
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)


#find()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


#format()	Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


#isalnum()	Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)


#isalpha()	Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)


#isascii()	Returns True if all characters in the string are ascii characters
txt = "Company123"
x = txt.isascii()
print(x)


#isdecimal()	Returns True if all characters in the string are decimals
txt = "1234"
x = txt.isdecimal()
print(x)


#isdigit()	Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)


#isidentifier()	Returns True if the string is an identifier
txt = "Demo"
x = txt.isidentifier()
print(x)


#islower()	Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x)


#isnumeric()	Returns True if all characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x)


#isprintable()	Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)


#isspace()	Returns True if all characters in the string are whitespaces
txt = "   "
x = txt.isspace()
print(x)


#istitle()	Returns True if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)


#isupper()	Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)


#join()	Converts the elements of an iterable into a string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)


#ljust()	Returns a left justified version of the string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")


#lower()	Converts a string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)


#lstrip()	Returns a left trim version of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")


#maketrans()	Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))



#partition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)


#replace()	Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)


#rfind()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)


#rindex()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)


#rjust()	Returns a right justified version of the string
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")


#rpartition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)


#rsplit()	Splits the string at the specified separator, and returns a list
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)


#rstrip()	Returns a right trim version of the string
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")


#split()	Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
x = txt.split()
print(x)


#splitlines()	Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)


#startswith()	Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)


#strip()	Returns a trimmed version of the string
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")


#swapcase()	Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)


#title()	Converts the first character of each word to upper case
txt = "Welcome to my world"
x = txt.title()
print(x)


#translate()	Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


#upper()	Converts a string into upper case
txt = "Hello my friends"
x = txt.upper()
print(x)


#zfill()	Fills the string with a specified number of 0 values at the beginning
txt = "50"
x = txt.zfill(10)
print(x)


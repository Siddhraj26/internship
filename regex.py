import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")                       #Basic re fuction             



import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")                       #findall dunction returns the list containing all matches 



import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print("The first white-space character is located in position:", x.start())  # return a match object if there is a match anywhere in a string


import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)                              #returns a list where the string has been split each matche




import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)                                #replaces onr or mant matches with a string



import re
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)     
print(x)                               #Find all lower case characters alphabetically between "a" and "m":



import re
txt = "That will be 59 dollars"
x = re.findall("\d", txt)                          #Find all digit characters
print(x)



import re
txt = "hello planet"
x = re.findall("he..o", txt)
print(x)                                      #Search for a sequence that starts with "he", followed by two (any) characters, and an "o"



import re
txt = "hello planet"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")                        #Check if the string starts with 'hello'



import re
txt = "hello planet"
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")                          #Check if the string ends with 'planet'



import re
txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)                           #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o"



import re
txt = "hello planet"
x = re.findall("he.+o", txt)
print(x)                             #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o"



import re
txt = "hello planet"
x = re.findall("he.?o", txt)
print(x)                              #Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o"



import re
txt = "hello planet"
x = re.findall("he.{2}o", txt)
print(x)                              #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o"



import re
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")                      #Check if the string contains either "falls" or "stays"

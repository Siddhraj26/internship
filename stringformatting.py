#Using the % 
name = "Tutorialspoint"
print("Welcome to %s!" % name)


#Using the {}
str = "Welcome to {}"
print(str.format("Tutorialspoint"))

#Using the f
item1_price = 2500
item2_price = 300
total = f'Total: {item1_price + item2_price}'
print(total)

#Using the template function over here 
from string import Template
str = "Hello and Welcome to $name !"
templateObj = Template(str)
new_str = templateObj.substitute(name="Tutorialspoint")
print(new_str)




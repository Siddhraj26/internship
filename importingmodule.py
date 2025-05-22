import mymodules
mymodules.greeting("sid")
a=mymodules.person1["age"]
print(a)                        # importing modules 



import mymodules as mm
a=mm.person1["age"]
print(a)                          # changing the name of the file for current file only



import platform
x = platform.system()
print(x)                          # It's the in-built function for showing which kind of system are you using



import platform
x = dir(platform)
print(x)                          # It's the in-built function for showing your directory 





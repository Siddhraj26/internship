import datetime
x = datetime.datetime.now()
print(x)                        #shows the current time



import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))         #shows the year and day



import datetime
x = datetime.datetime(2020, 5, 17)
print(x)                                 #to create a object by our own



import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))            #The method is called strftime(), and takes one parameter, format to specify the format of the returned string

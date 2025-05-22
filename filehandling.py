#To create a file:
#f=open("myfile.txt","x")

#To write in a file:

#Here the file is getting some content in it written by the written as "w" function
with open("myfile.txt", "w") as f:
  f.write("Written content!")


#Here the file is getting new content written by the append as "a" function
with open("myfile.txt", "a") as f:
  f.write("\nNow the file has more content!,\nHi I'm learning Python,\nThis is File Handling,\nPython 1234,\n1234")


#Here the content which is got append will be replaced by the content written 
# over here as written will earse the all conetent in file and start with new
#with open("myfile.txt", "w") as f:
#  f.write("Woops! I have deleted the content!")


#To read a file we'll use read function
with open("myfile.txt") as f:
  print(f.read())


#Read Only Parts of the File
#Return the 5 first characters of the file:
with open("myfile.txt") as f:
  print(f.read(5))

#Read Lines
#You can return one line by using the readline() method:
with open("demofile.txt") as f:
  print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)


#Close Files
#It is a good practice to always close the file when you are done with it.
f = open("demofile.txt")
print(f.readline())
f.close()


#Delete a File:

#To delete a file, you must import the OS module, and run its os.remove() function
#import os
#os.remove("demofile.txt")

#Check if File exist:
#To avoid getting an error, you might want to check if the file exists before you try to delete it:
#import os
##if os.path.exists("demofile.txt"):
#  os.remove("demofile.txt")
#else:
#  print("The file does not exist")

#Delete Folder
#To delete an entire folder, use the os.rmdir() method:
#import os
#os.rmdir("myfolder")
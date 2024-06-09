"""File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.
Open a file on a different location:

"""
print("Opening the File to Print")
f = open("C:\VS Code\Python\demofile.txt", "r")
print(f.read())
#Read Only Parts of the File
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f = open("C:\VS Code\Python\demofile.txt", "r")
#to read first 15 Characters 
#print(f.read(15))

#You can return one line by using the readline() method:
print(f.readline())
#By calling readline() two times, you can read the two first lines:
print(f.readline())
print(f.readline())
#Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
f.close()
#By looping through the lines of the file, you can read the whole file, line by line:
print("Using For Loop, Reading all the lines one by one")
f = open("C:\VS Code\Python\demofile.txt", "r")
for x in f: 
    print(x)
#Write to an Existing File
"""To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""
f.close()
#Let's open the file and add/append more content in it 
f=open("C:\VS Code\Python\demofile.txt", 'a')
f.write("\n\nNow the file has got more content!")
f.close()
#open and read the file after the appending:
f = open("C:\VS Code\Python\demofile.txt", "r")
print(f.read())
f.close()
#Open the file "demofile3.txt" and overwrite the content:
f = open("C:\VS Code\Python\demofile.txt", "w")
f.write("Whoops, I've deleted all the content as its overridden in 'w' mode")
f.close()
f = open("C:\VS Code\Python\demofile.txt", "r")
print(f.read())
"""
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

Example
Create a file called "myfile.txt":


"""
#f = open("C:\VS Code\Python\myfile.txt", "x")
#Create a new file if it does not exist:

#f = open("C:\VS Code\Python\myfile.txt", "w")
#Delete a File
#To delete a file, you must import the OS module, and run its os.remove() function:

#Remove the file "myfile.txt":
import os
#os.remove("C:\VS Code\Python\myfile.txt")

#Check if File exist:
#To avoid getting an error, you might want to check if the file exists before you try to delete it:

#Check if file exists, then delete it:
import os
if os.path.exists("C:\VS Code\Python\myfile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
#To delete an entire folder, use the os.rmdir() method:
#Remove the folder "myfolder":

import os
#os.rmdir("myfolder")
#Note: You can only remove empty folders.

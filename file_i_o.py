""" #File i/o in python (python can be used to perform operations on a file.(read & write data))

#Character - meaning
# 'r' - open for reading
# 'w' - open for writing, trumcating the file first
# 'x' - create a new file & open it for writing
# 'a' - open for writing, appending to the end of the file if it exists
# 'b' - binary mode
# 't' - text mode
# '+' - open a disk file for updating
# 'r+' - read + overwrite (pointer at start) - no truncate
# 'w+' - read + overwrite - truncate
# 'a+' - read + append (pointer at end) - no truncate

f=open("demo.txt","r")
#data = f.read() #reads entire file
line1 = f.readline() #reads one line at a time
#print(data)
print(line1)
line2 = f.readline()
print(line2)
#print(type(data))
f.close() 

f = open("demo.t((xt","w")
f.write("I want to learn javascript tomorrow. 123")
f.close()

f = open("demo.txt","a")
f.write("\nthen I'll move to ReactJS")
f.close() 

f = open("demo.txt","r+")
f.write("Hello")
f.close() 

# with syntax
with open("demo.txt","r")as f:
    data = f.read()
    print(data)
    
with open("demo.txt","w")as f:
    f.write("new data")

#Deleting a file

import os
os.remove("sample.txt") 

#Practice
#Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File i/o
# using Java.
# I like programming in java

with open("practice.txt","w") as f:
    f.write("Hi everyone\n we are learning filei/o\n")
    f.write("using java.\n I like programming in java")

# WAF that replaces all occurrences of "java" with "python" in above file.

with open("practice.txt","r")as f:
    data = f.read()
    
new_data = data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#Search if the word "learning" exists in the file or not. 

word = "learning"
with open("practice.txt","r") as f:
       data = f.read()
       if(data.find(word) != -1):
          print("Found")
       else:
          print("not found") 
          
#WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found

def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
       data = f.read()
       if(data.find(word) != -1):
          print("Found")
       else:
          print("not found") 
    
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
            
    return -1

print(check_for_line()) """

# From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("practices.txt","r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) %2 == 0):
            count += 1
            
print(count)
    
"""
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]  """










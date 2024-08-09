""" # string is data type that stores a sequence of characters.
( types to write string
str1 = "this is a string "
str2 = 'Darshan' """
# str3 = """this is a string""" ) 
""" str4 = "This is a string. \n we are creating it in python."
print(str4) 

# Concatenation
# \n is used for next line  & \t is used for tab space

str1 = "welcome"
str2 = "Darshan"
final_str = str1 +" " + str2
print(final_str) 

# length of string(str)

print(len(final_str)) 

#indexing (idx)

str = "Darshan Jain"
# ch = str[3]
print(str[3]) 

# Slicing (str[starting_idx : ending_idx]) ending idx is not included

str = "Darshanjain"
print(str[1:4]) # is ars
print(str[4:]) # is same as str[1: len(str)]
print(str[:4]) # is same as str[0:4] 

# slicing negative index

str = "Darshan"
print(str[-7:-1]) 

# string function

str = "i am studying python from youtube"
# str = str.capitalize()   # use for changing the original str
print(str.endswith("ube"))  # returns true if string ends with substr
print(str.endswith("app"))
print(str.capitalize()) # capitalizes 1st Char
print(str)
print(str.replace("o","a")) # replace all occurrences of old str to new str
print(str.replace("python","java"))
print(str.find("o")) # returns 1st index of 1st occurrer
print(str.find("from"))
print(str.count("am")) # counts the occurrence of substr
print(str.count("o")) """

# practice 
# wap to input user's first name and print its length

name = input("enter your name: ")
print("length of your name is", len(name))

#wap to find the occurrence of '$' in a string

str1 = "Hi, I $am the $ symbol $88.22"
print(str1.count("$"))




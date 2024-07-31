""" Traffic lights code

Light = input("Light color : ")

if(Light == "red"):
    print("stop")
elif(Light == "yellow"):
    print("look")
elif(Light == "green"):
    print("go")
else:
    print("light is broken") 
    
# Grades of students

marks = int(input("marks :"))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")  
    
# Practice Time

A = int(input("A :"))
G = input("M/F :")
if ((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif((A == 3 or A == 4) or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee") 
    
# Single line if/ ternary operator (var = variable , stt = statement )
# <var>=<var1>if<condition>else<var2> 

food = input("food :")
eat = "yes" if food == "cake" else "no"
print(eat)

# <stt1>if<condition>else<stt2>

food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet") """

# Clever if/ ternary operator
# <var>=(false_val,true_val)[<condition>]

age = int(input("age :"))
vote = ("yes" ,"no") [age < 18]
print("Person is eligible to vote",vote)

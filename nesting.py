""" # nesting

age = 88

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive") 
    
# practice

# wap to check if a number entered by the user is odd or even

number = int(input("enter the number:"))
if(number % 2 == 0):
    print("the number is even")
else:
    print("the number is odd") 
    
# wap to find the greatest of 3 or 4 numbers entered by the user.

num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
num3 = int(input("enter 3rd number: "))
num4 = int(input("enter 4th number: "))
if(num1 >= num2 and num1 >= num3):
    print("1st number is largest", num1)
elif(num2 >= num3 and num2 >= num4):
    print("2nd number is largest", num2)
elif(num3 >= num4 ):
    print("3rd number is largest", num3)
else:
    print("4th number is largest", num4) """
    
# wap to check if a number is a multiple of 7 or not

num = int(input("enter the number: "))
if(num % 7 == 0):
    print("the number is multiple of 7")
else:
    print("the number is not multiple of 7")
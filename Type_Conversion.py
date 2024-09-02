"""# Type conversion

a = 2
b = 4.25
sum = a + b #2.0 + 4.25 => 6.25
print(sum)
print(type(a)) 

# Type casting

a,b = 1 , "2.0"
c = float(b)
sum = a+ c
print(sum) 

# input (result for input() is always a str)

name = input("enter your name: ")
print("welcome ", name ) 

val = int(input("enter some value: "))
print(type(val), val) """

name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks:"))

print("welcome", name)
print("age = ", age)
print("marks =", marks)

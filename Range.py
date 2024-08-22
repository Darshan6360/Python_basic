"""# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number.
# range(start?,stop,steo?)

for i in range(10): # range(stop)
    print(i)
    
for i in range(2, 10): # range(start, stop)
    print(i)
    
for i in range(2, 10, 2): # range(start, stop, step)
    print(i)  
 
# print even number in range 
for i in  range(2, 101, 2):
    print(i) 
    
# print odd number in range
for i in range(1, 101, 2):
    print(i) 

# practice using for & range()

#Print numbers from 1 to 100.
for i in range(1, 101):
    print(i) 
    
# print number from 100 to 1.
for i in range(100, 0, -1):
    print(i)
    
# print the multiplication table of a number n.
n = int(input("enter number :"))

for i in range(1, 11):
    print(n * i)
    
# pass statement
# pass is a null statement that does nothing. it is used as a placeholder for future code.

for i in range(5):
    pass

if i > 5:
    pass  
    
# practice 
#WAP to find the su of first n natural numbers. (using while)

n = int(input("enter the number : "))
sum = 0
i = 1
while i <= n:
    sum += i 
    i +=1
    
print("total sum = ", sum)

#WAP to find the factorial of first n natural numbers. (using for) """

n = int(input("enter the number:"))
fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial =", fact)


   
    
    
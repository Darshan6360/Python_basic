"""# Block of statements that perform a specific task. 

def sum(a,b): 
    s = a + b
    print(s)
    return s

sum(5,10)

def sub(a,b):
    su = a - b
    print(su)
    return su
sub(15,10)

def print_hello():
    print("hello")
    
print_hello() 

# average of 3 numbers

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
calc_avg(10,20,30)

# Built-in functions like print, len, type, range 

print("darshan", end=" ") #sep = " "
print("python") #end = "\n" 

#Default parameters (Assigning a default value to parameter, which is used when no argument is passed)

def cal_prod(a, b=1):
    print(a * b)
    return a * b

cal_prod(2) 

# Let's practice
#1. WAF to print the length of a list.(list in the parameter)
cities = ["delhi","gurgaon","noida","pune","mumbai"]

def print_len(list):
    print(len(list))
    
print_len(cities)  

#2. WAF to print the elements of a list in a single line.(list is the parameter)
cities = ["delhi","gurgaon","noida","pune","mumbai"]

def print_list(list):
    for item in list:
        print(item, end=" ")
        
print_list(cities)
print()  

#3. WaF to find the factorial of n (n is the parameter)
n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *=  i
    print(fact)
    
cal_fact(6)  """

#4. waF to convert USD to INR.

def converter(usd_va):
    inr_va = usd_va * 83
    print(usd_va, "USD =", inr_va, "INR" )
    
converter(2)











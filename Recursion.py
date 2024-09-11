""" #Recursive function
def show(n):
    if(n==0): #Base case
        return
    print(n)
    show(n-1)
    
show(5) 

#returns n!
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(6)) 

# Write a recursive function to calculate the sum of first n natural numbers
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
    
print(calc_sum(5)) """

# Write a recursive function to print all elements in a list (Hint : use list & index as parameters.)
def print_list(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
fruits = ["mango","litchi","apple","banana"]

print_list(fruits)













"""# Loops are used to repeat instructions.

# while loop

count = 1
while count <= 5 :  # stopping condition
    print("hello")
    count += 1
    
print(count)

#or

i = 1  # initialization
while i <= 10 :
    print("hello world")
    i +=1
print(i) 

# print numbers from 1 to 5
i = 1
while i<= 5:
    print(i)
    i += 1
    
print("Loop ended")

#print numbers from 10 to 1

j = 10
while j >= 1:
    print(j)
    j -= 1
    
print("loop ended") 

# let's practice 

# print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1
print("Loop ended") 

# print numbers from 100 to 1

j = 100
while j >= 1:
    print(j)
    j -= 1
    
print("loop ended") 

# print the multiplication  table of a number n

n = int(input("enter number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1 
    
# print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx]) #nums[0], nums[1], nums[2], ..
    idx +=1 
    
# search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("enter the number: "))
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
        break
    else:
        print("number not found")
    i += 1
print("end of loop") """

# Break : used to terminate the loop when encountered.
# Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration.

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        break
    print(i)
    i += 1
 
print("end of loop")   

# &

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1






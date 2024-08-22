"""# For loops : are used for sequential traversal. For traversing list, string, tuples etc.
# for list
nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

# for tuples 
tup = (1, 2, 3, 4, 5, 6, 7)

for num in tup:
    print(num)

# for string
str = "darshan"

for  char in str:
    if(char == 's'):
        print("s found")
    print(char)
else:
    print("End")

# practice using for loop   
# print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el) """

# search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]    

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("enter the number : "))

idx = 0
for el in nums:
    if(el == x):
       print("number found at idx", idx)
       break
    idx += 1 
    

    

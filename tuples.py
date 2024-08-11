"""# tuple : A built in data type that lets us create immutable sequences of values

Tup = (1,2,3,4)
print(type(Tup)) 
print(Tup[0])
print(Tup[1])

tup = ()
print(tup)
print(type(tup)) 

tup = (1,) # kept , at the last of the single tuple value but in multiple tuple value it's optional
print(tup)
print(type(tup)) 

# Tuple Methods

tup = (2,1,3,1)
print(tup.index(1))  #returns index of first occurrence  
print(tup.count(1))  #counts total occurrences  

# practice
# Wap to ask the user to enter names of their 3 favorite movie & store them in a list

Movie_names = []
mov = input("enter 1st movie: ")
Movie_names.append(mov)
mov = input("enter 2nd movie: ")
Movie_names.append(mov)
mov = input("enter 3rd movie: ")
Movie_names.append(mov)

print(Movie_names)

#  or direct mrthod 

Movie_names = []
Movie_names.append(input("enter 1st movie: "))
Movie_names.append(input("enter 2nd movie: "))
Movie_names.append(input("enter 3rd movie: "))
print("The 3 favorite movies are :", Movie_names)

# Wap to check if a list contains a palindrome of elements. (Hinr: use copy() method) 

list1 = [1,2,3]
list2 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list1 == list1):
    print("list 1 is palindromr")
elif(copy_list2 == list2):
    print("list 2 is palindrome")
else:
    print("Both the lists are not a palindrome") """
    
# Wap to count the numbeer of students with the "A" grade in the following tuple. ("c","D","A","A","B","B","A")

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

# store the above value in a list & sort them from "A" to "D"

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)

 
  




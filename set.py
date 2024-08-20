"""# set : is the collection of the unordered items.
# Each element in the set must be unique & immutable

collection = {1,2,3,4,4,4, "hello","hello","world"}

print(collection)
print(type(collection)) 
print(len(collection)) # total number of items

collection = set() # empty set; syntax
print(collection) 

# set methods

collection = set()
collection.add(1) # adds an element
collection.add(2)
collection.add(2)
collection.add("Darshan")
collection.add((1,2,3))
collection.remove(1) # removes the element
collection.clear() #empties the set

print(collection)
print(len(collection))

code = {"hello", "Darshan", "world", "coding","python"}
code.pop() #removes a random value

print(code)
print(code.pop())
print(code) 

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) #(output{1,2,3,4}) combines both set values & returns new
print(set1)
print(set2)
print(set1.intersection(set2)) #(output{2,3}) combines common values & returns new 

#Let's practice

# store following word meanings in a python dictionary:
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

word = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(word["table"]) 

#you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students
# "python","java","c++","python","javascript","java","python","java","c++","c"

classroom = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(classroom)
print("Number of classroom needed :",len(classroom)) 

# WAP to enter marks of 3 subjects from the user and sotre them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("enter phy :"))
marks.update({"phy" : x})
x = int(input("enter chem :"))
marks.update({"chem ": x})
x = int(input("enter math :"))
marks.update({"math" : x})

print(marks) 

# Figure out a way to store 9 & 9.0 as separate values in the set. (you can take help of built-in data types)

values = {9, "9.0"}
print(values)
# or """
values = {
    ("float",9.0),
    ("int",9)
}
print(values)





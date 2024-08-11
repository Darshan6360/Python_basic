"""# list : A built in data tpye that stores set of values

marks = [56,25,89,65]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

student = ["karan",25,"Bangalore"]
print(student[0])
student[0] = "arjun" # for changing any thing in list use the index of the word or letter
print(student)

# list slicing : similar to string slicing
# list_name[starting_idx : ending_idx] (the ending idx is not included)

marks = [52,85,95,36,25]
print(marks[1:3])
print(marks[:4])
print(marks[0:])
print(marks[-3:-1])

# list Method

list = [1,2,3,4,5,6]
list.append(7) # adds one element at the edd
print(list)  """
num = [8,6,2,1,4,3,7,1]
num.reverse() #reverses list
print(num)
num.sort()  # sorts in ascending order
print(num)
num.sort(reverse = True)  #sort in descending order
print(num)
word = ["a","b","z","x","c"]
word.sort(reverse=True) #sorting can be also done in strings
print(word)
num.reverse() #reverses list
print(num)
num.insert(0,9) #insert element at index
print(num)
num.remove(1) #removes first occurrence of element
print(num)
num.pop(2) #removes element at idx
print(num)

# python documentation on google 



"""#To map with real world scenarios, we started using object in code. This is called object oriented programming.
# Class is a blueprint for creating objects

#creating class
class Student:
    name = "Darshan"
    
#creating object (instance)
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name) 

class car:
    color = "blue"
    brand = "mercedes"
       
car1 = car()
print(car1.color)
print(car1.brand) 

#Constructor = All classes have a function called __init__(), which is always executed when the class or object is being initiated.

class Student:
    
    def __init__(self, name, marks):  #the self parameter is a reference to the current instance of the class, & is used to access variables that belongs to the class.
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
        
s1 = Student("karan", 97)
print(s1.name, s1.marks)
s2 = Student("Arjun", 84)
print(s2.name, s2.marks) 

# Class & Instance Attributes

class Student:
    college_name = "Jain University" #class attr
    
    def __init__(self, name, marks):
        self.name = name  #obj attr > class attr
        self.marks = marks #obj attr
        print("adding new student in Database..")
        
s1 = Student("karan", 97)
print(s1.name, s1.college_name) 

# Methods : are functions that belong to objects.
class Student:
    college_name = "jain college"
    
    def __init__(self, name, marks) :
        self.name = name
        self.marks = marks
        
    def welcome(self):  #Method
        print("welcome student,", self.name)
        
    def get_marks(self):
        return self.marks
        
s1 = Student("Darshan",98)
s1.welcome()
print(s1.get_marks()) 

#Let's practice
#Create student class that takes name &marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class student: 
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)
        
s1 = student("Tony",[99, 98, 97])  
s1.get_avg() 

#Static Methods: Methods that don't use the self parameter(work at class level)

class Student:
    @staticmethod
    def hello():
        print("hello")
s1 = Student
s1.hello() 

#Abstraction : Hiding the implementation details of a class & only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")
        
Car1 = Car()
Car1.start() """

#Encapsulation : Wrapping data and functions into a single unit(object).

#Let's practice
#Create Account class with 2 attributes - balance & account no.
#create methodds for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())
        
    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())
        
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)




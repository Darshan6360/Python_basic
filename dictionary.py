"""# Dictionary are used to store data values in key value pairs

info = {
    "name" : "Darshan",
    "learing" : "coding",
    "subjects" : ["python","c","java"],
    "topics" : ("dict","set"),
    "age" : 22,
    "is_adult" : True,
    "marks" : 94.4
}
print(info)
print(type(info))
print(info["name"])
# print(info["surname"])
info["name"] = "Jain university"  # to change any data or value 
info["surname"] = "Darshan"   # to add a new key in the dict
print(info)

null_dict = {}
null_dict["name"] = "Darshan"
print(null_dict) 

# Nested dictionaries

student = {
    "name" : "Darshan jain",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student)
print(student["subject"])
print(student["subject"]["chem"]) """

# Methods in dictionary

student = {
    "name" : "Darshan jain",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student.keys()) # returns all keys
print(list(student.keys()))
print(student.values()) # returns all values
print(student.items()) # returns all (key , values) pairs as tuples
print(student.get("subject")) # returns the key according to value
student.update({"city" : "Delhi" }) # inserts the specified items to the dictionary
student.update({"age" : 25 , "gender" : "Male"})
print(student)  



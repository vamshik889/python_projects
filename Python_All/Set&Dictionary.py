#Sets
# 1.it is Unordered - means it doesn't stores the elements in the memory in the order
# 2.Not indexed
# 3. Not mutable(Elements are not mutable- means existing items/elements cannot be replacable but they can be
#    permanantly removed and also we can add new elements to the Sets)
# 4.Duplicates not allowed
#Dictionaries
# 1.These are ordered now(Till the Python version 3.6 Dictionary is unordered and from 3.7 it is Ordered)
# 2.Indexed
# 3. Mutable
# 4. Duplicates not allowed
a= {1,2,3.5,"Vamshi"}
print(type(a))
print(a)
# print(a[0]) Output:TypeError: 'set' object is not subscriptable
print(len(a))

#Iterating
for i in a:
    print(i, end=",")

#Adding the element to Set
#Add function
a.add("Krishna")
print(a)
#remove function
a.remove(3.5)
print(a)

#Dictionaries ( Key(property) and Value(Data) )

Student ={"name":"Vamshi","roll":33,"age":23, "Marks": 100 }
print(type(Student))

# Accessing using keys

print(Student.get("roll"))
#To print all keys from dict as a list
x= Student.keys()
print(x)   #Output : dict_keys(['roll', 'age', 'Marks'])
#now we can iterate this
for i in x:
     print(Student.get(i))

#To get values easily
y=Student.values()
print(y)

#to get both Keys and values
z= Student.items()
print(z)
#also we can check the keys are present are not

z= "vamshi" in Student
print(z) #Output: False, bacause we can only check the keys not values, here "vamshi" is a value

c= "name" in Student
print(c) # Output : True

#To Update the values in Dictionary

Student.update({"age":25})
print(Student)

#To add new items

Student["hobbies"] = ["Playing games", "Reading books"]
print(Student)
#To remove
Student.pop("hobbies")
print(Student)

#Create an Empty set
print(set())
#Create an empty dictionary
k= {}
print(k)









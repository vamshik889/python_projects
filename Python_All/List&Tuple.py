#List, Tuple, Set and Dictionaries are collection based data types -These 4 are varies with 4properties .They are
#1. ordered or not -Ordered is nothing but how we create a list or Tuple, the same order it will be stored in the memory
#2. Indexed or not  - it starts with zero and till length-1
#3. mutable or not  -Can we able to change the elements or not
#4. Duplicate allowed or not

#if any data type is Ordered then it will be automatically indexed -eg: List ,Tuple

# LIST - we can have diff data types in List and denoted with square brackets
#List is ordered, Mutable, allow duplicate and indexed
#Tuple is ordered, immutable, allow duplicate and indexed

#The only diff b/w List and tuple is , List is mutable and where Tuple is not mutable


L1 = ["John", 102, "USA" , "USA"]      #Example for list
L2 = [1, 2, 1, 3.4, 4, 5, 6 , "Vamshi"]       #Example for list
print(type(L1))

# tuple_1 = ("Python", "tuples", "immutable", "object", 1)    # Ex ofTuple
# tuple_2 = (23, 42, 12, 53, 64, 64, 64)                            # Ex ofTuple
# tuple_3 = "Python", "Tuples", "Ordered", "Collection"
# print(type(tuple_3))

#finding index
print(L1[3])
print(L1[-1])
# print(tuple_1[3])
# print(tuple_2[-1])
print(L2.index(2))
#Slicing - To print the desired range of elements -and it will return the same data type like list or tuple on which we performing the operation
# print(tuple_1[0:3]) # Means it will prints from 0 index to till index2, the last given is not included

print(L1[:3])  #1
print(L1[0:3]) #2
#1 and 2 are same
print(L2[::-1])

#in keyword in List

a=1 in L1
print(a) #false
#mutable
L1[0] = True
print(L1) #output: [True, 102, 'USA', 'USA']
# tuple_1[0] = 5
# print(tuple_1) #Output:TypeError: 'tuple' object does not support item assignment
#Changing multiple elements
L1[0:3] = [3,33,34]
print(L1) #Output : [3, 33, 34, 'USA']
#Insert - to insert at specific index in list we use this function
L1.insert(2,55)
print(L1) #Output: [3, 33, 55, 34, 'USA']
#Append function -To add an element at the end of the list
L1.append("appended")
print(L1) #Output :[3, 33, 55, 34, 'USA', 'appended']
#Pop function - To remove a particular element from the List
L1.pop(5)
print(L1)
#Concatinate two lists
L3=L1+L2
print(L3)

#Extend function

p=[199,888]
L1.extend(p)
print(L1) #Output : [3, 33, 55, 34, 'USA', 199, 888]

# Iterating through List and Tuples

# for i in L1:
#     print(i, end=",")
#
# for i in tuple_1:
#     print(i, end=",")
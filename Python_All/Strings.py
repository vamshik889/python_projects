#Collection of characters
# # Strings can be denoted with 'vamshi',"vamshi" and """vamshi"""
# a="vamshi"
# print(type(a))  #Type of variable
a="vamshi"
#index   - we cannot modify the existing string
            # Indexing will starts from 0 to n

# print(a[0])
# print(a[-1])  #Negative indexing
print(len(a))  #Length of string
# del a  #To delete the string
# print(a)
#Concatinating the strings
a="vamshi"
b="Krishna"

# print(a +" "+ b)

c=a+ " " +b
print(c)
#Iterating the String
# for i in c:
#     print(i,end=" ")

# print("a" in c)  #checking wether a is there in the string c or not
#
# print("a" not in c)
# print("vamshi \nkrishna") #New line
# print(r"\n")  #r means raw ,it will print everything that v enters in string
#Formatting a String
# name=input("Enter your name")
# print("Hi, Your name is {}".format(name))
#
#
# print(f"Hi, your name is {name}") #F-string

#STRING METHODS
#c="VamShI krishna"
# print(c.upper())
# print(c.lower())
# print(c.isupper())
# print(c.islower())
# print(c.isnumeric())
# d="a b c d"
# print(d.split())  #To split the words and convert into a list
#
# e="a-b-c-d-e f g h"
# print(e.split("-")) # Dash based split(only the letters with - gets splitted)

q="vamshi krishna"
print(q.find("a")) #To find the wether the given is element is there or not ,it outputs the index of the searched element












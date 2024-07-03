# import math  #METHOD1:UASING MATH
# x = int(input("enter a number to find the factorial"))
# y = math.factorial(x)
# print(y)
#METHOD2:
# x = int(input("enter a number to find the factorial"))
# y=1
# for i in range(1, x+1):
#     y=y*i
# print(y)
# Problem: Find factorial ,if the num is negative throw an error, if it is zero ans would be 1.
x=int(input("Enter a number"))
if x==0:
    print("1")
elif x<0:
    print("Error")
else:
    y=1
    for i in range(1, x+1):
        y=y*i
    print(y)
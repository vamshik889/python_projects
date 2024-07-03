numbers = "0,1,2,3,4,5,6,7,8,9"
x= input("Enter a word with numeric values")
num = 0
for i in x:
    if i in numbers:
        num+=1
print(num)
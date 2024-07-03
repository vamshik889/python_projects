x = int(input("enter a number"))
counter = 0

for i in range(1,x+1):
    if x%i ==0:
        counter+=1
if counter==2:
    print("prime", x)
else:
    print("Given number is not prime",x)

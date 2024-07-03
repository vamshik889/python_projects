x=int(input("Enter a number"))
ans=0
for i in range(1,x+1): #x+1 because in for loop it leaves last value of the range
    if(i%2==0):
        ans+=i
print(ans)

#sum of Odd

y = int(input("enter a value"))
ans = 0
for i in range(1, y+1):
    if i%2 !=0:
        ans+=i
print(ans)
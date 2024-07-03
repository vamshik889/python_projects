a=input("Enter a sentence to count the words")
ans=1
for i in a:

    if i == " ":
        ans+=1
print(ans)

v = a.split()
print(v)
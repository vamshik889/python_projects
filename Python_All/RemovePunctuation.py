# punc='''~!@#$%^&*()"?><`'''
# ans=""
# a=input("Enter a string with Punctuation")
# for i in a:
#     if i not in punc:
#         ans=ans+i
#
# print(ans)

#Removing numbers from a String

a = input("Enter a string with numbers")
ans=""
num = "0123456789"
for i in a:
    if i not in num:
        ans+=i
print(ans)
print(type(num))
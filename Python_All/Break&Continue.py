# Break and continue are keywords
# n=0
# while n<=6:
#     if n == 5:            #In continue only current iteration will be exited
#         n = n + 1
#         continue
#     print(n)
#     n=n+1
# n=int(input("enter a number"))
# while n<=6:                 #In break whole Loop will be exited
#     if n == 5:
#         n = n + 1
#         break
#     print(n)
#     n=n+1
#
# for x in range(1,5):
#     if x==3:
#         continue
#     print(x)
#     x+=1

# for i in range(30):
#     if i == 20:
#
#         continue
#     print(i)

#
# for x in range(1,5):
#     if x == 3:
#         break
#     print(x)
#     x += 1
#
# x = [1,2,3,"vamshi"]
# for i in x:
#     if i==3:
#         continue
#     print(i)
while True:
    try:
        num=int(input("Enter a number"))
        if num > 10:
            print("You entered",num , ".")
            break
        else:
            print("please enter a num greater than 10")

    except ValueError as e:
        print(e)















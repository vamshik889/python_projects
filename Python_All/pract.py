# # # import sys
# # #
# # # # class area:
# # # #     def __init__(self,*args):
# # # #         print(" hi")
# # # #     def area_sq(self,l,b):
# # # #         return l*b
# # # # a1=area()
# # # # y=a1.area_sq(2,3)
# # # # print(y)
# # # #
# # # # #
# # # # def func(a,b,c,d):
# # # #     print(a,b,c,d)
# # # # args = [1,2,3,5]
# # # # kwargs = {"a":1, 'b':2,"c":3, "d":5}
# # # # func(*args)
# # # # func(**kwargs)
# # #
# # # print(44%55)
# # # print(sys.version)
# # print(1<<2)
# # print(2 ** (3 ** 2))
# # 2 ** (3 ** 2)
# # (2 ** 3) ** 2
# # 2 ** 3 ** 2
# l=[1, 0, 2, 0, 'hello', '', [],True]
# print(list(filter(bool, l)))
# print(filter(int, l))

# for i in [1, 2, 3, 4][::-1]:
#     print (i)
def foo(x):
    x[0] = ['def']
    x[1] = ['abc']
    return id(x)
q = ['abc', 'def']
print(id(q) == foo(q))


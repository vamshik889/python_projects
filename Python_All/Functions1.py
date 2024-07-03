# def myfunc(name):
#      print("hi "+name)
#
# myfunc("vamshi")
class calculator:
    number=100
    def __init__(self):    #Constructor
        print("Auto called")
    def getData(self):
        print("Hi from class")
obj = calculator()
obj.getData()
print(obj.number)


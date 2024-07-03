# class person:
#     def Setvalue(self,name,age):
#         self.name = name
#         self.age=age
#
#     def Getvalue(self):
#         print(f"My name is {self.name} and age is {self.age}")
#
#
# p1= person()
# p1.Setvalue("Vamshi",23)
# p1.Getvalue()

#Constructors: At the time of object creation we can set properties by use of Constructor without any function

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Getvalue(self):
        print("Name is {} and age is{}".format(self.name,self.age))
p2=Person("vamshi",23)   #Passing argumets while creating the object
p2.Getvalue()




#In a class we have methods, variables
#variables also called as data members and attributes

#Two types of attributes in a class in python
#Instance Attributes/object attributes;differently for every object
#Class attributes: Same for all objects of a class
#
# class Person:
#     city="hyderebad"  #Class attribute
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def Getvalue(self):
#         print("Name is {} and age is{} and from {}".format(self.name,self.age,Person.city))
# p2=Person("vamshi",23)    #Instance Attributes
# p3=Person("Vk",23)  #Instance Attributes
# p2.Getvalue()
# p3.Getvalue()
#
# class Car:
#     def __init__(self,name,color,country):
#         self.name= name
#         self.color=color
#         self.country=country
#     def getvalue(self):
#         print(f"The car name is {self.name} and color is {self.color}")
# x =  Car("Maruti","Red","India")
# x.getvalue()
class odc:
    ac=True
    def __init__(self,ppl,city,*args):
        self.ppl = ppl
        self.city = city
    def x(self,a,b):
        print(f"the name of ppl is {self.ppl} and city{self.city}")
        return a+b
xy=odc("vk","hyd")
y=xy.x(11,22)
print(y)
# class Rectangle:
#  def area(self, length, width):
#   return length*width
#  def perimeter(self, length, width):
#      return 2*(length+width)
# Re1=Rectangle()
# area=Re1.area(22,33)
# perimeter=Re1.perimeter(33,22)
# print(f"{area},{perimeter}")

class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area = 3.14*self.radius*self.radius
        print(f"The area of circle with {self.radius} is {area}")

a1 = circle(20)
a1.area()
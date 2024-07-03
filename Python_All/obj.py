class car:
    def __int__(self,color,brand):
        self.color = color
        self.brand =brand
    def cardetails(self):
        print(f"Car brand is {self.brand} and color is {self.color}")

car1 = car("Tata","Red")
car1.cardetails()

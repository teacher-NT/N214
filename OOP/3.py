import os
os.system("cls")

class Car:
    brand = "BMW"
    model = "E69"
    price = 120000
    color = "black"
    year = 2015

    def info(self):
        print(f"{self.brand} {self.model} {self.price} {self.color}")

car1 = Car()

car1.info()

car2 = Car()
car2.model = "M5"
car2.info()
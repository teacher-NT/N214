import os
os.system("cls")

class Car:
    def __init__(self, b, m, p, c, y):
        self.brand = b
        self.model = m
        self.price = p
        self.color = c
        self.year = y

    def info(self):
        print(f"{self.brand} {self.model} {self.price} {self.color}")

car1 = Car("BMW", 'E69', 120000, 'red', 2015)
car1.info()

car2 = Car('Toyota', 'Landcruser', 45000, 'blue', 2023)
car2.info()

# ============= User input
b = input('Brand: ')
m = input("Model: ")
p = int(input("Price: "))
c = input("Color: ")
y = int(input("Year: "))

car3 = Car(b,m,p,c,y)
car3.info()
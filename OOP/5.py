import os
os.system("cls")

class Animal:
    def __init__(self,n,t,y):
        self.nom = n
        self.tur = t
        self.yosh = y

    def eat(self):
        print(f"{self.nom} nomli hayvon ovqatlanmoqda...")

class Dog(Animal):
    pass

dog1 = Dog("Bobik", "It", 4)
dog1.eat()
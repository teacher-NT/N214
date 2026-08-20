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
    def run(self):
        print(f"{self.nom} yugurmoqda...")

    def eat(self):
        print(f"{self.nom} sasiska yemoqda...")


dog1 = Dog("Bobik", "It", 4)
dog1.eat()
dog1.run()
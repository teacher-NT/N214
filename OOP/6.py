import os
os.system("cls")

class Flyable:
    def fly(self):
        print("Flying...")

    def swim(self):
        print("Flyable is swiming...")

class Swimmable:
    def swim(self):
        print("Swimming...")



class Duck(Swimmable, Flyable):
    def walk(self):
        print("Walking...")

duck1 = Duck()
duck1.walk()
duck1.swim()
duck1.fly()
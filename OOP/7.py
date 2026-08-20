import os
os.system("cls")

class Animal:
    def eat(self):
        print("Animal is eating...")

    def sleep(self):
        print("Animal is sleepping...")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Duck(Animal):
    pass

dog1 = Dog()
cat1 = Cat()
duck1 = Duck()

dog1.eat()
cat1.eat()
duck1.eat()
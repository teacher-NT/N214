import os
os.system("cls")

class Animal:
    def sound(self):
        print("Animal is speaking")

class Dog:
    def sound(self):
        print("Dog is barking")

class Cat(Animal):
    def sound(self):
        print("Cat is miov")

a1 = Animal()
d1 = Dog()
c1 = Cat()

a1.sound()
d1.sound()
c1.sound()
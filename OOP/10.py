import os
os.system("cls")

class Animal:
    def sound(self):
        print("Animal is speaking")

class Dog:
    def sound(self):
        print("Dog is barking")

a1 = Animal()
d1 = Dog()

a1.sound()
d1.sound()
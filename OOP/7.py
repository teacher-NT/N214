import os
os.system("cls")

class Boat:
    def swim(self):
        print("Boat is swimming...")

class Plane(Boat):
    def fly(self):
        print("Plane is flying...")

class Damas(Plane):
    def run(self):
        print("Damas is running...")

d1 = Damas()
d1.run()
d1.fly()
d1.swim()
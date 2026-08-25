import os
os.system("cls")

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def jump(self):
        pass

    @abstractmethod
    def shoot(self):
        pass


class Ironman(Player):
    def fly(self):
        print("Ironman is flying...")

    def run(self):
        print("Ironman is running...")

    def jump(self):
        print("Ironman is jumping...")

    def shoot(self):
        print("Ironman is shooting...")

iron1 = Ironman()
iron1.fly()
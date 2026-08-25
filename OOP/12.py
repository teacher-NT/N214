import os
os.system("cls")

class BankAccount:
    def __init__(self, n, b):
        self.name = n
        self.__balans = b



user1 = BankAccount("Avazbek", 2000)
user1.name = "Avazbek Ismoilov"
print(user1.name)

print(user1.__balans)
        
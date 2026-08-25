import os
os.system("cls")

class BankAccount:
    def __init__(self, n, b):
        self.name = n
        self.__balans = b

    def get_balans(self, key):
        if key == "qwerty":
            print(self.__balans)
        else:
            print("Kalit xato")

    def set_balans(self, new, key):
        if key == "qwerty":
            self.__balans = new
        else:
            print("Kalit xato")


user1 = BankAccount("Avazbek", 2000)
user1.name = "Avazbek Ismoilov"
print(user1.name)

# user1.get_balans("qwerty")
# user1.set_balans(5000, "qwerty")
# user1.get_balans("qwerty")


# user1.__balans = 8000
# print(user1.__balans)

# user1.get_balans("qwerty")
        
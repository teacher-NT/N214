import os
os.system("cls")

class Car:
    def __init__(self, b,m,p):
        self.brand =  b
        self.model = m
        self.price = p
        self.colors = ['red','green','blue','black','white']

    def __str__(self):
        return f"{self.brand} {self.model} {self.price}$"

    def __gt__(self, n):
        return self.price > n

    def __lt__(self, n):
        # print(" < operatori ishladi")
        return self.price < n

    def __eq__(self, n):
        return self.price == n

    def __mul__(self, n):
        self.price *= n

    def __truediv__(self, n):
        self.price /= n

    def __contains__(self, item):
        for i in self.colors:
           if item.lower() == i.lower():
               return True
        return False 

    def __len__(self):
        return len(self.colors)
    
    
c1 = Car("GM", "Cobalt", 13000)
# c1.info()

# print(c1.__str__())
# print(c1)

# print(c1 > 1000)
# print(c1 < 1000)
# print(c1 == 13000)

# c1 * 4
# c1 / 10
# print(c1)


# if "Qora" in c1:
#     print("Yes")
# else:
#     print("No")

print(len(c1))


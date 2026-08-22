import os
os.system("cls")

# print(4*5)
# print("Hello "*5)
# print([1,2,3]*5)

class Person:
    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.address = m

    def __gt__(self, n):
        if isinstance(n, int):
            return self.age > n
        elif  isinstance(n, (Person, Employee)):
            return self.age > n.age
        else:
            return "Error"

class Employee:
    def __init__(self, n, a, m, l, s):
        self.name = n
        self.age = a
        self.address = m
        self.level = l
        self.salary = s

    def __gt__(self, n):
        return self.salary > n

p1 = Person("Ali", 19, "Samarqand")
e1 = Employee("Vali", 15, "Namangan", "Manager", 500)

print(p1 > 20)
# print(e1 > 20)

p2 = Person("Hasan", 30, "Qo'qon")
print(p1 > p2)
print(p1 > e1)
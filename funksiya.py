import os
os.system("cls")

def say_hello(ism, familya=""):
    print(f"Salom {ism} {familya}")

def add(a:int, b:int):
    print(a+b)

# say_hello("Sevinch")
# say_hello("Sanjar", "Muhammadiyev")
# say_hello("Muhammadolim", "Abidov")
# say_hello(4, 5)

# add(4, 5)


def square(a:int) -> int:
    return a**2

# print(square(4))

def func(a):
    return a**2, a**3, a**0.5

# print(func(9))
# n,m,k = func(9)
# print(n,m,k)

# =============================================
# def func2(a,b,c):
#     print(a+b+c)
# func2(2,4,5)

def func3(*n):
    print(sum(n))

# func3(1,2,3,4,5,6,7,8,9)


def func4(**n):
    print(n)

# func4(ism='Ali', yosh=14, manzil='Toshkent')

def add1(a, b):
    return a + b

add2 = lambda a,b: a+b

# print(add1(4,5))
# print(add2(4,5))

# func5 = lambda n: list(print(i, end=" ") for i in range(1,n) if i%2==0)
# func5(10)


names = ['Abdulla', 'Samandar', 'Mahliyo', 'Sardor', 'Dilshod', 'Avazbek', 'Sanjar']

# new = []
# for i in names:
#     if i[0] == 'S':
#         new.append(i)

# print(new)

def check_name(n):
    return n[0]=='S'
new = list(filter(check_name, names))
print(new)

new2 = list(filter(lambda n: n[0]=='S', names))
print(new2)

import os
os.system("cls")

try:
    a = int(input("Son kiriting: "))
    b = int(input("Son kiriting: "))
    print(a / b)
except ValueError:
    print("Iltimos to'g'ri son kiriting")
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas")
else:
    print("Kod muvafaqqiyatli ishladi!")
finally:
    print("Try except tugadi")







# a = int(input("Son kiriting: "))
# b = int(input("Son kiriting: "))
# print(a / b)
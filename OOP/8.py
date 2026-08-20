import os
os.system("cls")
# Diamond problem

class A:
    def func1(self):
        print("A class")

class B(A):
    pass

class C(B):
    def func1(self):
        print("C class")

class D:
    def func1(self):
        print("D class")

class F(B, C):
    pass

class E(F, B):
    pass

e1 = E()
e1.func1()
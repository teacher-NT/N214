import os
os.system("cls")

import random as rd

print(rd.randint(1, 10))
print(rd.uniform(1, 10))

names = ['Jasmina', 'Avazbek', 'Oygul', 'Farruh', 'Sevinch', 'Saida']
# a = rd.choice(names)
# print(a)
# a = rd.choices(names, k=3)
# print(a)

# b = rd.sample(names, k=3)
# print(b)

rd.shuffle(names)
print(names)
import os
os.system("cls")

set1 = {34,5,12,21,43,52,48,12,5,34,12}
# set1[3] = 6
# print(set1[3])
# print(set1)


set2 = {"Apple", 'Peach', 'Cherry', 'Mango'}
# if "Apple" in set2:
#     print("Yes")
# else:
#     print("No")

# for i in set2:
#     print(i)

# print(len(set2))


set3 = {"Rus", 'Ingliz', 'Ispan', 'Turk'}
# set3.add("Xitoy")

# set3.remove("Ispan")

# set3.discard("Ispan")

# a = set3.pop()
# print(a)

# set3.clear()

# set4 = set3.copy()
# print(set4)

lst = ['Arab', 'Koreys', 'Nemis', 'Ingliz', 'Rus']
# set3.update(lst)

# set4 = set3.union(lst)
# print(set4)

# print(set3)

# ============================================================

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

# set3 = set1.intersection(set2)
# print(set3)
# print(set1)

# set1.intersection_update(set2)
# print(set1)

# set3 = set1.difference(set2)
# print(set3)

# set1.difference_update(set2)
# print(set1)

# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1.symmetric_difference_update(set2)
# print(set1)

set1 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14}
set2 = {3,4,5,6}
print(set2.issubset(set1))
print(set1.issuperset(set2))

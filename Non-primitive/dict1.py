import os
os.system("cls")

mahsulot = {
    "nomi": "Muzqaymoq",
    "kategoriyasi": "Sut mahsuloti",
    "narxi": 8000,
    "ICh": "Imkon Plus",
    "muddati": "6 oy"
}
# mahsulot["narxi"] = 7000
# mahsulot['tarkibi'] = ['Sut', 'Shakar', 'Shokolad', 'Moloko']
# print(mahsulot["nomi"], mahsulot['narxi'])
# print(mahsulot)


# if "narxi" in mahsulot:
#     print("yes")
# else:
#     print("no")

# for i in mahsulot:
#     print(i, mahsulot[i])

# print(mahsulot.get("narx",  "Bunday kalit yo'q"))
# print(mahsulot['narx'])

# print(mahsulot.keys())
# print(mahsulot.values())
# if "Muzqaymoq" in mahsulot.values():
#     print("Yes")
# else:
#     print("No")

# a = mahsulot.pop("nomi")
# print(a)
# print(mahsulot)

# lst = mahsulot.items()
# print(lst)
# print(list(mahsulot))
# for k, v in mahsulot.items():
#     print(k, v)

a = mahsulot.popitem()
print(a)
print(mahsulot)
import os
os.system("cls")

with open("./N214/Fayl/panda.jpeg", "rb") as file:
    baytlar = file.read()
    # print(len(list(baytlar)))

    # for i in list(baytlar):
    #     print(i, end=" ")

with open("./N214/Fayl/kunfupanda.jpeg", "wb") as file:
    file.write(baytlar)
    print("Faylga yozildi")
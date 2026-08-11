import os
os.system("cls")

with open("panda.jpeg", "rb") as file:
    baytlar = file.read()
    print(len(list(baytlar)))
    
    # for i in list(baytlar):
    #     print(i, end=" ")

import os
os.system("cls")

f = open("myfile.txt", "w")

# text = input("Nimadir deng: ")
# f.write(text)

# print("Kiritilgan text faylga yozildi.")

ismlar = ['Ali', 'Vali', 'Hasan', 'Husan']
f.writelines(map(lambda n: n+"\n", ismlar))
print("Ismlar faylga yozildi")

f.close()


with open("myfile2.txt", "w") as file:
    file.write("Bu oddiy fayl")

print("Fayl yopiq")

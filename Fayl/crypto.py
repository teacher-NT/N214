import os
os.system("cls || clear")

def get_file_data():
    name = input("Fayl nomini kiriting: ")
    try:
        with open(name) as file:
            data = file.read()
    except:
        print("\n!!! Fayldan o'qishda xatolik !!!")
        data = None
    return data, name

def shifring():
    data, name = get_file_data()
    if data is None:
        return
    with open(name, "w") as file:
        for i in data:
            n_i = ord(i)
            if 32 <= n_i <= 123:
                ch_i = chr(n_i + 3)
                file.write(ch_i)
            else:
                file.write(i)
        print("Fayl shifrlandi.")




def deshifring():
    data, name = get_file_data()
    if data is None:
        return
    with open(name, "w") as file:
        for i in data:
            n_i = ord(i)
            if 35 <= n_i <= 126:
                ch_i = chr(n_i - 3)
                file.write(ch_i)
            else:
                file.write(i)
        print("Fayl shifrlandi.")

print("="*50, "\n\tSHIFRLASH DASTURIGA XUSH KELIBSIZ\n", "="*50)


while True:
    print("\nTanlang:")
    choice = int(input("1. Shifrlash\n2. Deshifrlash\n3. Chiqish\n>>> "))
    if choice == 1:
        shifring()
    elif choice == 2:
        deshifring()
    else:
        print("Raxmat!")
        break


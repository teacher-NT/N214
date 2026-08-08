import os
os.system("cls")

import json
# students = [
#     {
#         "Ism": "Bobur",
#         "Yosh": 14,
#         "Manzil": "Farg'ona"
#     }, 
#     {
#         "Ism": "Sardor",
#         "Yosh": 19,
#         "Manzil": "Andijon"
#     },
# ]

# with open("myfile.json", "w") as file:
#     # file.writelines(students)
#     json.dump(students, file, indent=4)

with open("myfile.json") as file:
    data = json.load(file)
print(data)
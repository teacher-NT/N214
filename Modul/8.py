import os
os.system("cls")

import cv2

camera = cv2.VideoCapture("https://10.10.2.150:8080/video")

while True:
    is_valid, image = camera.read()
    if is_valid:
        # cv2.imwrite("rasm.jpg", image)
        cv2.imshow("Kamera", image)
        # print("Rasm saqlandi")
    else:
        print("Kameradan o'qishda xatolik")

    if cv2.waitKey(1) & 0xfff == 32:
        break
    

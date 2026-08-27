import os
# os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit
)
from PyQt5.QtGui import QFont


app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Dastur")
oyna.setGeometry(1400, 100, 400, 700)
oyna.setStyleSheet("background-color: #acd5fc;")

edit1 = QLineEdit(oyna)
edit1.setGeometry(30, 50, 340, 50)
edit1.setStyleSheet("""
    font-size: 18px;
    border: 2px solid black;
    border-radius: 15px;
    background-color: #d7e7f5;
""")
edit1.setPlaceholderText("Namuna, 2 + 3")


matn1 = QLabel(oyna)
matn1.setGeometry(30, 110, 340, 50)
matn1.setStyleSheet("""
    font-size: 18px;
    border: 2px solid black;
    border-radius: 15px;
""")

def hisob():
    text = edit1.text()
    son1, amal, son2 = text.split()
    if amal == "+":
        try:
            matn1.setText(f"{int(son1) + int(son2)}")
        except:
            matn1.setText("Error!")
    elif amal == "-":
        try:
            matn1.setText(f"{int(son1) - int(son2)}")
        except:
            matn1.setText("Error!")
    elif amal == "/":
        try:
            matn1.setText(f"{int(son1) / int(son2)}")
        except:
            matn1.setText("Error!")
    elif amal == "*":
        try:
            matn1.setText(f"{int(son1) * int(son2)}")
        except:
            matn1.setText("Error!")
    else:
        matn1.setText("Xato amal!")

btn1 = QPushButton(oyna)
btn1.setGeometry(100, 170, 200, 50)
btn1.setStyleSheet("""
    font-size: 18px;
    border: 2px solid black;
    border-radius: 15px;
    background-color: #f7a86f;
""")
btn1.setText("Hisoblash")
btn1.clicked.connect(hisob)


oyna.show()
app.exec_()

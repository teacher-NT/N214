import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dastur")
        self.setGeometry(1400, 100, 400, 700)
        self.matn1 = QLabel(self)
        self.matn1.setText("Salom Dunyo")
        self.matn1.move(100, 100)
        self.matn1.setStyleSheet("""
            font-size: 28px;
            color: blue;
            font-weight: bold;
        """)

        self.btn1 = QPushButton(self)
        self.btn1.setText("Change Text")
        self.btn1.move(100, 200)
        self.btn1.setFixedSize(200, 50)
        self.btn1.setStyleSheet("""
            font-size: 18px;
            color: black;
            background-color: #b3b9ba;
            border: 2px solid black;
            border-radius: 20px;
        """)
        self.btn1.clicked.connect(self.btn1_func)

        self.show()

    def btn1_func(self):
        self.matn1.setText("Hello World")


app = QApplication([])
win = Window()
app.exec_()
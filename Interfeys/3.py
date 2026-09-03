import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur")
        self.setGeometry(1400, 100, 400, 700)
        self.matn1 = QLabel()
        self.matn1.setText("Salom Dunyo")
        self.matn1.setStyleSheet("""
            font-size: 28px;
            color: blue;
            font-weight: bold;
        """)

        self.vbox.addWidget(self.matn1)

        self.btn1 = QPushButton()
        self.btn1.setText("Change Text 1")
        # self.btn1.setFixedSize(200, 50)
        self.btn1.setStyleSheet("""
            font-size: 18px;
            color: black;
            background-color: #b3b9ba;
            border: 2px solid black;
            border-radius: 20px;
        """)
        self.btn1.clicked.connect(self.btn1_func)
        self.vbox.addWidget(self.btn1)

        self.btn2 = QPushButton()
        self.btn2.setText("Change Text 2")
        # self.btn2.setFixedSize(200, 50)
        self.btn2.setStyleSheet("""
                    font-size: 18px;
                    color: black;
                    background-color: #b3b9ba;
                    border: 2px solid black;
                    border-radius: 20px;
                """)
        self.btn2.clicked.connect(self.btn1_func)
        self.vbox.addWidget(self.btn2)

        self.btn3 = QPushButton()
        self.btn3.setText("Change Text 3")
        # self.btn3.setFixedSize(200, 50)
        self.btn3.setStyleSheet("""
                    font-size: 18px;
                    color: black;
                    background-color: #b3b9ba;
                    border: 2px solid black;
                    border-radius: 20px;
                """)
        self.btn3.clicked.connect(self.btn1_func)
        self.vbox.addWidget(self.btn3)
        self.setLayout(self.vbox)
        self.show()

    def btn1_func(self):
        self.matn1.setText("Hello World")


app = QApplication([])
win = Window()
app.exec_()
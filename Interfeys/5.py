import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton,
    QMessageBox
)
from PyQt5.QtCore import Qt



style_body2 = """
    background-color: #b1b5b5;
"""

style_matn2 = """
    font-size: 32px;
    font-weight: bold;
"""

style_btn2 = """
    font-size: 18px;
    background-color: red;
    border: 2px solid black;
    border-radius: 20px;
    padding: 10px;
"""

class AboutWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setGeometry(1400, 100, 400, 700)
        self.setStyleSheet(style_body2)
        self.vbox = QVBoxLayout()

        self.matn1 = QLabel("About us!")
        self.matn1.setStyleSheet(style_matn2)
        self.matn1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.vbox.addWidget(self.matn1)

        self.btn1 = QPushButton("Back")
        self.btn1.setStyleSheet(style_btn2)
        self.btn1.clicked.connect(self.back_main)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)

    def back_main(self):
        self.hide()
        self.main.show()

style_body = """
    background-color: #99c6f0;
"""

style_matn1 = """
    font-size: 32px;
    font-weight: bold;
"""

style_btn1 = """
    font-size: 18px;
    background-color: green;
    border: 2px solid black;
    border-radius: 20px;
    padding: 10px;
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1400, 100, 400, 700)
        self.setStyleSheet(style_body)
        self.vbox = QVBoxLayout()

        self.matn1 = QLabel("Welcome to Dastur")
        self.matn1.setStyleSheet(style_matn1)
        self.matn1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.vbox.addWidget(self.matn1)

        self.btn1 = QPushButton("Next")
        self.btn1.setStyleSheet(style_btn1)
        self.btn1.clicked.connect(self.open_next)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)
        self.show()

    def open_next(self):
        self.next_win = AboutWindow(self)
        self.next_win.show()
        self.hide()

app = QApplication([])
win = MainWindow()
app.exec_()
import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox
)

style_combo = """
    font-size: 22px;
    background-color: #3a7ae8;
    padding: 10px;
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur")
        self.setGeometry(1400, 100, 400, 700)
        self.matn1 = QLabel()
        self.matn1.setText("Tanlangan taom: ?")
        self.matn1.setStyleSheet("""
            font-size: 28px;
            color: blue;
            font-weight: bold;
        """)
        self.vbox.addWidget(self.matn1)

        self.add_combo()

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
        self.setLayout(self.vbox)
        self.show()

      
    def btn1_func(self):
        self.matn1.setText("Hello World")

    def add_combo(self):
        self.menu = QComboBox()
        self.menu.addItems(["Osh", "Manti", "Shashlik", "Qozonkabob", "Somsa", "Lag'mon"])
        self.menu.setStyleSheet(style_combo)
        self.menu.currentTextChanged.connect(self.change_food)
        self.vbox.addWidget(self.menu)

    def change_food(self):
        name = self.menu.currentText()
        self.matn1.setText(f"Tanlangan taom: {name}")


app = QApplication([])
win = Window()
app.exec_()
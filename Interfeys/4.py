import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox  
)

style_combo = """
    font-size: 22px;
    background-color: #3a7ae8;
    padding: 10px;
"""

style_check = """
    font-size: 18px;

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

        self.matn2 = QLabel("Tanlangan ichimliklar: ?")
        self.matn2.setStyleSheet("""
                    font-size: 28px;
                    color: blue;
                    font-weight: bold;
                """)
        self.vbox.addWidget(self.matn2)
        self.add_combo()
        self.add_checkbox()

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

    def add_checkbox(self):
        self.ch1 = QCheckBox("Choy")
        self.ch1.setStyleSheet(style_check)
        self.ch1.stateChanged.connect(self.choose_drink)
        self.vbox.addWidget(self.ch1)

        self.ch2 = QCheckBox("Coffee")
        self.ch2.setStyleSheet(style_check)
        self.ch2.stateChanged.connect(self.choose_drink)
        self.vbox.addWidget(self.ch2)

        self.ch3 = QCheckBox("Cola")
        self.ch3.setStyleSheet(style_check)
        self.ch3.stateChanged.connect(self.choose_drink)
        self.vbox.addWidget(self.ch3)

        self.ch4 = QCheckBox("Pepsi")
        self.ch4.setStyleSheet(style_check)
        self.ch4.stateChanged.connect(self.choose_drink)
        self.vbox.addWidget(self.ch4)  

        self.ch5 = QCheckBox("Moxito")
        self.ch5.setStyleSheet(style_check)
        self.ch5.stateChanged.connect(self.choose_drink)
        self.vbox.addWidget(self.ch5)      

    def choose_drink(self):
        drinks = ""
        if self.ch1.isChecked():
            drinks += f"{self.ch1.text()}, "
        if self.ch2.isChecked():
            drinks += f"{self.ch2.text()}, "
        if self.ch3.isChecked():
            drinks += f"{self.ch3.text()}, "
        if self.ch4.isChecked():
            drinks += f"{self.ch4.text()}, "
        if self.ch5.isChecked():
            drinks += f"{self.ch5.text()}, "
        self.matn2.setText(f"Tanlangan ichimliklar:\n{drinks}")

app = QApplication([])
win = Window()
app.exec_()
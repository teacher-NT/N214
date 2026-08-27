import os
os.system("cls")

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont


app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Dastur")
oyna.setGeometry(1400, 100, 400, 700)
oyna.setStyleSheet("background-color: #d9d1bd;")

matn1 = QLabel(oyna)
matn1.setText("Ilovamizga Xush kelibsiz")
matn1.setStyleSheet("font-size: 28px; color:blue; font-weight:bold;")
matn1.setFont(QFont("Ink Free", 18))
matn1.move(30, 20)


oyna.show()
app.exec_()


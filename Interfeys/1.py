import os
os.system("cls")

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Dastur")
oyna.setGeometry(1400, 100, 400, 700)
oyna.show()

app.exec_()


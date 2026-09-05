import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton,
    QMessageBox
)
from PyQt5.QtCore import Qt
from translate import Translator

style_body = """
    background-color: #F4F6F8;
"""

style_title = """
    font-size: 32px;
    color: #1E293B;
    padding: 20px;
    font-family: MV Boli;
"""

style_input = """
    font-size: 18px;
    padding: 10px;
    background-color: #FFFFFF;  
    color: #0F172A;
    border: 1px solid #6366F1;
"""

style_combo = """
    font-size: 22px;
    background-color: #FFFFFF;
    color: #475569;
    border: 1px solid #E2E8F0;
    border-radius: 5px;
    padding: 10px;
"""

style_btn = """
    font-size: 18px;
    color: #FFFFFF;
    background-color: #6366F1;
    border: 2px solid black;
    border-radius: 20px;
    padding: 10px 20px;
    hover: {
        background-color: #4F46E5;
    }
"""

LANGS = {"O'zbek":"uz", "Ingliz":"en", "Rus":"ru", "Fransuz":"fr", "Ispan":"es", "Nemis":"de", "Italya":"it", "Xitoy":"zh", "Yapon":"ja", "Koreys":"ko"}

class Tarjimon(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(600)
        self.vbox = QVBoxLayout()
        self.title = QLabel("Tarjimon")
        self.title.setStyleSheet(style_title)
        self.title.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.title)

        self.from_ = QComboBox()
        self.from_.addItems(LANGS.keys())
        self.from_.setStyleSheet(style_combo)
        self.vbox.addWidget(self.from_)

        self.from_input = QTextEdit()
        self.from_input.setPlaceholderText("Matnni kiriting...")
        self.from_input.setStyleSheet(style_input)
        self.vbox.addWidget(self.from_input)

        self.to_ = QComboBox()
        self.to_.addItems(LANGS.keys())
        self.to_.setStyleSheet(style_combo)
        self.vbox.addWidget(self.to_)

        self.to_output = QTextEdit()
        self.to_output.setReadOnly(True)
        self.to_output.setPlaceholderText("Tarjima...")
        self.to_output.setStyleSheet(style_input)
        self.vbox.addWidget(self.to_output)

        self.translate_btn = QPushButton("Tarjima qilish")
        self.translate_btn.setStyleSheet(style_btn)

        self.translate_btn.clicked.connect(self.translate)
        self.vbox.addWidget(self.translate_btn)

        self.setLayout(self.vbox)
        self.show()

    def translate(self):
        from_lang = LANGS[self.from_.currentText()]
        to_lang = LANGS[self.to_.currentText()]
        text = self.from_input.toPlainText()

        translator = Translator(from_lang=from_lang, to_lang=to_lang)
        translated_text = translator.translate(text)
        self.to_output.setPlainText(translated_text)

app = QApplication([])
window = Tarjimon()
app.exec_()

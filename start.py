import pygame
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Names(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.first = ''
        self.second = ''

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Игра Баше')

        self.label = QLabel(self)
        self.label.setText("Добро пожаловать в Bache's Game!")
        self.label.move(390, 20)

        self.label2 = QLabel(self)
        self.label2.setText('Представьте, что вы перенеслись во времени на 200 тысяч лет назад и'
                            ' единственным развлечением для вас является "перекладывание камешков".\n'
                            'Перебирать камни одному - скучно, поэтому вы с товарищем решили сыграть в такую игру:\n'
                            'Из кучи камней необходимо поочередно брать от 1 до n камней (n будет задано позднее).\n'
                            'Выиграет тот, кто возьмет последний камень.')
        self.label2.move(30, 60)

        self.button_1 = QPushButton(self)
        self.button_1.move(390, 140)
        self.button_1.setText("Ввести имя первого игрока")
        self.button_1.clicked.connect(self.run1)

        self.button_2 = QPushButton(self)
        self.button_2.move(390, 180)
        self.button_2.setText("Ввести имя Второго игрока")
        self.button_2.clicked.connect(self.run2)
        self.show()

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)

        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())

    def run1(self):
        #self.load_image('woman.png')
        i, okBtnPressed = QInputDialog.getText(self, "Bache", "Как тебя зовут?")
        if okBtnPressed:
            self.button_1.setText('')
            self.first = i

    def run2(self):
        i, okBtnPressed = QInputDialog.getText(self, "Bache", "Как тебя зовут?")
        if okBtnPressed:
            self.button_2.setText('')
            self.second = i


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Names()
    print(ex.first, ex.second)
    sys.exit(app.exec_())


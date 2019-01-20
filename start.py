import pygame
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


class Names(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.first = 'Первый'
        self.second = 'Второй'

    def initUI(self):
        fon_pic = QPixmap("sand.jpg")
        fon = QLabel(self)
        fon.setPixmap(fon_pic)
        fon.move(0, 0)

        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowIcon(QtGui.QIcon("label.png"))

        self.label = QLabel(self)
        self.label.setText("Добро пожаловать в")
        self.label.move(390, 20)

        pic = QPixmap("label.png")
        lbl_pic = QLabel(self)
        lbl_pic.setPixmap(pic)
        lbl_pic.move(530, 14)

        pic_first = QPixmap("people.png")
        lbl_pic_first = QLabel(self)
        lbl_pic_first.setPixmap(pic_first)
        lbl_pic_first.move(100, 300)

        self.label2 = QLabel(self)
        self.label2.setText('Представьте, что вы перенеслись во времени на 200 тысяч лет назад и'
                            ' единственным развлечением для вас является "перекладывание камешков".\n'
                            'Перебирать камни одному - скучно, поэтому вы с товарищем решили сыграть в такую игру:\n'
                            'Из кучи камней необходимо поочередно брать от 1 до n камней (n будет задано позднее).\n'
                            'Выиграет тот, кто возьмет последний камень.')
        self.label2.move(30, 60)

        self.button_1 = QPushButton(self)
        self.button_1.move(390, 160)
        self.button_1.setText("Ввести имя первого игрока")
        self.button_1.clicked.connect(self.run1)

        self.button_2 = QPushButton(self)
        self.button_2.move(390, 200)
        self.button_2.setText("Ввести имя второго игрока")
        self.button_2.clicked.connect(self.run2)

        self.label_name1 = QLabel(self)
        self.label_name1.move(380, 380)
        self.label_name1.setText('                ')

        self.label_name2 = QLabel(self)
        self.label_name2.move(540, 380)
        self.label_name2.setText('                ')

        pic_rock = QPixmap("huge_rock.png")
        lbl_pic_rock = QLabel(self)
        lbl_pic_rock.setPixmap(pic_rock)
        lbl_pic_rock.move(425, 650)

        self.btn = QPushButton('START', self)
        self.btn.move(450, 700)
        #self.btn.clicked.connect(self.hello)
        self.show()


    def run1(self):
        i, okBtnPressed = QInputDialog.getText(self, "Bache", "Как тебя зовут?")
        if okBtnPressed:
            self.button_1.setText('Ввести имя повторно')
            self.first = i
            self.label_name1.setText(i)


    def run2(self):
        i, okBtnPressed = QInputDialog.getText(self, "Bache", "Как тебя зовут?")
        if okBtnPressed:
            self.button_2.setText('Ввести имя повторно')
            self.second = i
            self.label_name2.setText(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Names()
    print(ex.first, ex.second)
    sys.exit(app.exec_())


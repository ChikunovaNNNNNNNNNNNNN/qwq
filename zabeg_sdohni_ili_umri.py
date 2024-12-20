import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QRadioButton
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6 import QtCore
from PyQt6 import QtGui, QtCore
import pygame
from PyQt6.QtCore import QUrl, Qt

import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel

d = 100


class Kirpich(QMainWindow):
    def __init__(self):
        super(Kirpich, self).__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 1024, 768)
        self.media_player = QMediaPlayer()
        self.media_player.setSource(QUrl.fromLocalFile("C:/Users/Andrey/Desktop/qq2.mp4"))
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setVideoOutput(self.video_widget)
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.media_player.play()


class Sosiska(QMainWindow):
    def __init__(self):
        super(Sosiska, self).__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 1024, 768)
        self.media_player = QMediaPlayer()
        self.media_player.setSource(QUrl.fromLocalFile("C:/Users/Andrey/Desktop/qq1.mp4"))
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setVideoOutput(self.video_widget)
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.media_player.play()


class Raspili_menya_bolgarkoj(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.setFixedSize(280, 300)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('АБ vs Шаурма')

        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/Andrey/Desktop/und.mp3")
        pygame.mixer.music.play()

        self.setStyleSheet("""
                    QWidget {
                        background-color: #333333;
                        color: #ffffff;
                    }
                    QPushButton {
                        background-color: #2a4238;
                        color: #ffffff;
                        border: none;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #7b917b;
                    }
                """)

        self.layout = QHBoxLayout(self)

    def initUI(self):
        ss = 0
        label = QLabel(self)
        pixmap = QPixmap('C:/Users/Andrey/Desktop/фон1.gif')
        label.setGeometry(0, 0, 280, 300)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        self.button1 = QPushButton('', self)
        self.button1.setGeometry(40, 70, 50, 50)
        self.button2 = QPushButton('', self)
        self.button2.setGeometry(110, 70, 50, 50)
        self.button3 = QPushButton('', self)
        self.button3.setGeometry(180, 70, 50, 50)
        self.button4 = QPushButton('', self)
        self.button4.setGeometry(40, 130, 50, 50)
        self.button5 = QPushButton('', self)
        self.button5.setGeometry(110, 130, 50, 50)
        self.button6 = QPushButton('', self)
        self.button6.setGeometry(180, 130, 50, 50)
        self.button7 = QPushButton('', self)
        self.button7.setGeometry(40, 190, 50, 50)
        self.button8 = QPushButton('', self)
        self.button8.setGeometry(110, 190, 50, 50)
        self.button9 = QPushButton('', self)
        self.button9.setGeometry(180, 190, 50, 50)
        # кнопки окна 3х3

        self.kurva1 = QPushButton('', self)
        self.kurva1.setGeometry(30, 70, 50, 50)
        self.kurva2 = QPushButton('', self)
        self.kurva2.setGeometry(90, 70, 50, 50)
        self.kurva3 = QPushButton('', self)
        self.kurva3.setGeometry(150, 70, 50, 50)
        self.kurva4 = QPushButton('', self)
        self.kurva4.setGeometry(210, 70, 50, 50)
        self.kurva5 = QPushButton('', self)
        self.kurva5.setGeometry(30, 130, 50, 50)
        self.kurva6 = QPushButton('', self)
        self.kurva6.setGeometry(90, 130, 50, 50)
        self.kurva7 = QPushButton('', self)
        self.kurva7.setGeometry(150, 130, 50, 50)
        self.kurva8 = QPushButton('', self)
        self.kurva8.setGeometry(210, 130, 50, 50)
        self.kurva9 = QPushButton('', self)
        self.kurva9.setGeometry(30, 190, 50, 50)
        self.kurva10 = QPushButton('', self)
        self.kurva10.setGeometry(90, 190, 50, 50)
        self.kurva11 = QPushButton('', self)
        self.kurva11.setGeometry(150, 190, 50, 50)
        self.kurva12 = QPushButton('', self)
        self.kurva12.setGeometry(210, 190, 50, 50)
        self.kurva13 = QPushButton('', self)
        self.kurva13.setGeometry(30, 250, 50, 50)
        self.kurva14 = QPushButton('', self)
        self.kurva14.setGeometry(90, 250, 50, 50)
        self.kurva15 = QPushButton('', self)
        self.kurva15.setGeometry(150, 250, 50, 50)
        self.kurva16 = QPushButton('', self)
        self.kurva16.setGeometry(210, 250, 50, 50)
        # кнопки окна 4х4

        self.button1.setVisible(False)
        self.button2.setVisible(False)
        self.button3.setVisible(False)
        self.button4.setVisible(False)
        self.button5.setVisible(False)
        self.button6.setVisible(False)
        self.button7.setVisible(False)
        self.button8.setVisible(False)
        self.button9.setVisible(False)

        self.kurva1.setVisible(False)
        self.kurva2.setVisible(False)
        self.kurva3.setVisible(False)
        self.kurva4.setVisible(False)
        self.kurva5.setVisible(False)
        self.kurva6.setVisible(False)
        self.kurva7.setVisible(False)
        self.kurva8.setVisible(False)
        self.kurva9.setVisible(False)
        self.kurva10.setVisible(False)
        self.kurva11.setVisible(False)
        self.kurva12.setVisible(False)
        self.kurva13.setVisible(False)
        self.kurva14.setVisible(False)
        self.kurva15.setVisible(False)
        self.kurva16.setVisible(False)
        # делаем их не видимыми

        self.aaa = QRadioButton('', self)
        self.aaa.move(50, 10)
        self.aaa.setVisible(False)
        # скрытый выбор скина аб

        self.sss = QRadioButton('', self)
        self.sss.move(200, 10)
        self.sss.setVisible(False)
        # скрытый выбор скина шаурмы

        self.pr = QPushButton(self)
        self.pr.move(90, 20)
        self.pr.setText("Продолжить")
        self.pr.setVisible(False)
        # скрытая кнопка продолжения

        self.button_2 = QPushButton(self)
        self.button_2.move(90, 20)
        self.button_2.setText("Играть")
        self.button_2.clicked.connect(self.buttonn_2)
        # кнопка начала

        self.banan1 = QPushButton(self)
        self.banan1.move(0, 80)
        self.banan1.setText("Cкин А")
        # 1аб + 1шаурма

        self.banan1.clicked.connect(self.q)

        self.banan2 = QPushButton(self)
        self.banan2.move(90, 80)
        self.banan2.setText("Cкин Б")
        # 2аб + 2шаурма
        self.banan2.clicked.connect(self.w)

        self.banan3 = QPushButton(self)
        self.banan3.move(180, 80)
        self.banan3.setText("Cкин В")
        # 3аб + 3шаурма
        self.banan3.clicked.connect(self.e)

        self.banan44 = QPushButton(self)
        self.banan44.move(0, 120)
        self.banan44.setText("Поле 3х3")
        self.banan44.setVisible(False)

        self.banan55 = QPushButton(self)
        self.banan55.move(180, 120)
        self.banan55.setText("Поле 4х4")
        self.banan55.setVisible(False)
        # выбор размера поля

        if ss == 1:
            self.banan3.setEnabled(True)
            self.banan2.setEnabled(True)
            self.banan1.setEnabled(True)

        else:
            self.banan3.setEnabled(False)
            self.banan2.setEnabled(False)
            self.banan1.setEnabled(False)
        # видимость
        print(ss)

    def buttonn_2(self):
        self.button_2.deleteLater()
        ss = 1
        print(ss)
        self.banan(ss)

    def banan(self, ss):
        if ss == 1:
            self.banan3.setEnabled(True)
            self.banan2.setEnabled(True)
            self.banan1.setEnabled(True)

        else:
            self.banan3.setEnabled(False)
            self.banan2.setEnabled(False)
            self.banan1.setEnabled(False)

        print(ss)

    def q(self):
        self.pr.setVisible(True)
        self.pr.clicked.connect(self.prr)
        print(99)

        self.aaa.setVisible(True)
        icon = QIcon('C:/Users/Andrey/Desktop/sticker.png')
        self.ab = icon
        self.aaa.setIcon(icon)

        self.sss.setVisible(True)
        icon = QIcon('C:/Users/Andrey/Desktop/шаурмама.webp')
        self.shaur = icon
        self.sss.setIcon(icon)
        # иконки для выбора скина

        print(8)

    def w(self):
        self.pr.setVisible(True)
        self.pr.clicked.connect(self.prr)
        print(99)

        self.aaa.setVisible(True)
        icon = QIcon('C:/Users/Andrey/Desktop/sticker0.webp')
        self.aaa.setIcon(icon)
        self.ab = icon

        self.sss.setVisible(True)
        icon = QIcon('C:/Users/Andrey/Desktop/шаурма.png')
        self.sss.setIcon(icon)
        self.shaur = icon
        print(8)

    def e(self):
        self.pr.setVisible(True)
        self.pr.clicked.connect(self.prr)

        print(99)

        self.aaa.setVisible(True)
        icon = QIcon('C:/Users/Andrey/Desktop/stickerr.png')
        self.aaa.setIcon(icon)
        self.ab = icon

        self.sss.setVisible(True)
        icon = QIcon('C:/Users/Andrey/Desktop/шаурма1.png')
        self.sss.setIcon(icon)
        self.shaur = icon
        print(8)

    def prr(self):
        self.banan55.setVisible(True)
        self.banan44.setVisible(True)
        self.pr.setVisible(False)

        self.banan1.setVisible(False)
        self.banan2.setVisible(False)
        self.banan3.setVisible(False)
        # сокрытие

        self.banan55.clicked.connect(self.kur)
        self.banan44.clicked.connect(self.but)

    def but(self):
        self.a = 0

        self.banan55.setVisible(False)
        self.banan44.setVisible(False)

        self.button1.setVisible(True)
        self.button2.setVisible(True)
        self.button3.setVisible(True)
        self.button4.setVisible(True)
        self.button5.setVisible(True)
        self.button6.setVisible(True)
        self.button7.setVisible(True)
        self.button8.setVisible(True)
        self.button9.setVisible(True)
        # открытие 3х3

        self.button9.clicked.connect(lambda: self.zubochistka(9))
        self.button8.clicked.connect(lambda: self.zubochistka(8))
        self.button7.clicked.connect(lambda: self.zubochistka(7))
        self.button6.clicked.connect(lambda: self.zubochistka(6))
        self.button5.clicked.connect(lambda: self.zubochistka(5))
        self.button4.clicked.connect(lambda: self.zubochistka(4))
        self.button3.clicked.connect(lambda: self.zubochistka(3))
        self.button2.clicked.connect(lambda: self.zubochistka(2))
        self.button1.clicked.connect(lambda: self.zubochistka(1))
        self.baton9 = 0
        self.baton8 = 0
        self.baton7 = 0
        self.baton6 = 0
        self.baton5 = 0
        self.baton4 = 0
        self.baton3 = 0
        self.baton2 = 0
        self.baton1 = 0

    def kur(self):
        self.a = 0

        self.banan55.setVisible(False)
        self.banan44.setVisible(False)

        self.kurva1.setVisible(True)
        self.kurva2.setVisible(True)
        self.kurva3.setVisible(True)
        self.kurva4.setVisible(True)
        self.kurva5.setVisible(True)
        self.kurva6.setVisible(True)
        self.kurva7.setVisible(True)
        self.kurva8.setVisible(True)
        self.kurva9.setVisible(True)
        self.kurva10.setVisible(True)
        self.kurva11.setVisible(True)
        self.kurva12.setVisible(True)
        self.kurva13.setVisible(True)
        self.kurva14.setVisible(True)
        self.kurva15.setVisible(True)
        self.kurva16.setVisible(True)
        # открытие 4х4
        self.bober1 = 0
        self.bober2 = 0
        self.bober3 = 0
        self.bober4 = 0
        self.bober5 = 0
        self.bober6 = 0
        self.bober7 = 0
        self.bober8 = 0
        self.bober9 = 0
        self.bober10 = 0
        self.bober11 = 0
        self.bober12 = 0
        self.bober13 = 0
        self.bober14 = 0
        self.bober15 = 0
        self.bober16 = 0

        self.kurva1.clicked.connect(lambda: self.loshad(1))
        self.kurva2.clicked.connect(lambda: self.loshad(2))
        self.kurva3.clicked.connect(lambda: self.loshad(3))
        self.kurva4.clicked.connect(lambda: self.loshad(4))
        self.kurva5.clicked.connect(lambda: self.loshad(5))
        self.kurva6.clicked.connect(lambda: self.loshad(6))
        self.kurva7.clicked.connect(lambda: self.loshad(7))
        self.kurva8.clicked.connect(lambda: self.loshad(8))
        self.kurva9.clicked.connect(lambda: self.loshad(9))
        self.kurva10.clicked.connect(lambda: self.loshad(10))
        self.kurva11.clicked.connect(lambda: self.loshad(11))
        self.kurva12.clicked.connect(lambda: self.loshad(12))
        self.kurva13.clicked.connect(lambda: self.loshad(13))
        self.kurva14.clicked.connect(lambda: self.loshad(14))
        self.kurva15.clicked.connect(lambda: self.loshad(15))
        self.kurva16.clicked.connect(lambda: self.loshad(16))

    def zubochistka(self, k):
        pygame.mixer.music.load("C:/Users/Andrey/Desktop/tresk.mp3")
        pygame.mixer.music.play()

        if self.a == 0:
            exec(f'self.button{k}.setIcon(QtGui.QIcon(self.ab))')
            exec(f'self.button{k}.setIconSize(QtCore.QSize(25, 25))')
            exec(f'self.button{k}.setEnabled(False)')
            exec(f'self.baton{k} = 1')
            # символ "крестика"

            self.a = 1
        else:
            exec(f'self.button{k}.setIcon(QtGui.QIcon(self.shaur))')
            exec(f'self.button{k}.setIconSize(QtCore.QSize(25, 25))')
            exec(f'self.button{k}.setEnabled(False)')
            exec(f'self.baton{k} = 2')
            # символ "нолика"
            self.a = 0
        print('010')
        if (self.baton1 == self.baton2 == self.baton3 != 0 or \
                self.baton4 == self.baton5 == self.baton6 != 0 or \
                self.baton7 == self.baton8 == self.baton9 != 0 or \
                self.baton1 == self.baton5 == self.baton9 != 0 or \
                self.baton3 == self.baton5 == self.baton9 != 0 or \
                self.baton1 == self.baton4 == self.baton7 != 0 or \
                self.baton2 == self.baton5 == self.baton8 != 0 or \
                self.baton3 == self.baton6 == self.baton9 != 0):
            if (self.baton1 == self.baton2 == self.baton3 == 1 or \
                    self.baton4 == self.baton5 == self.baton6 == 1 or \
                    self.baton7 == self.baton8 == self.baton9 == 1 or \
                    self.baton1 == self.baton5 == self.baton9 == 1 or \
                    self.baton3 == self.baton5 == self.baton9 == 1 or \
                    self.baton1 == self.baton4 == self.baton7 == 1 or \
                    self.baton2 == self.baton5 == self.baton8 == 1 or \
                    self.baton3 == self.baton6 == self.baton9 == 1):
                print('0000000101010101010101011')
            else:
                print('020202020202002')
            if self.a == 0:
                print('Шаурма')
                self.dialog = Kirpich()
                self.dialog.show()
                pygame.mixer.init()
                pygame.mixer.music.load("C:/Users/Andrey/Desktop/Day.mp3")
                pygame.mixer.music.play()

            if self.a == 1:
                print('АБ')

                self.dialog = Sosiska()
                self.dialog.show()
                pygame.mixer.init()
                pygame.mixer.music.load("C:/Users/Andrey/Desktop/Day.mp3")
                pygame.mixer.music.play()

    def loshad(self, k):
        pygame.mixer.music.load("C:/Users/Andrey/Desktop/tresk.mp3")
        pygame.mixer.music.play()

        if self.a == 0:
            exec(f'self.kurva{k}.setIcon(QtGui.QIcon(self.ab))')
            exec(f'self.kurva{k}.setIconSize(QtCore.QSize(25, 25))')
            exec(f'self.kurva{k}.setEnabled(False)')
            exec(f'self.bober{k} = 1')

            self.a = 1
        else:
            exec(f'self.kurva{k}.setIcon(QtGui.QIcon(self.shaur))')
            exec(f'self.kurva{k}.setIconSize(QtCore.QSize(25, 25))')
            exec(f'self.kurva{k}.setEnabled(False)')
            exec(f'self.bober{k} = 1')
            self.a = 0
        print('010')
        if (self.bober1 == self.bober2 == self.bober3 == self.bober4 != 0 or \
                self.bober5 == self.bober6 == self.bober7 == self.bober8 != 0 or \
                self.bober9 == self.bober10 == self.bober11 == self.bober12 != 0 or \
                self.bober13 == self.bober14 == self.bober15 == self.bober16 != 0 or \
                self.bober9 == self.bober1 == self.bober5 == self.bober13 != 0 or \
                self.bober2 == self.bober6 == self.bober10 == self.bober14 != 0 or \
                self.bober3 == self.bober7 == self.bober11 == self.bober15 != 0 or \
                self.bober4 == self.bober8 == self.bober12 == self.bober16 != 0 or \
                self.bober1 == self.bober6 == self.bober11 == self.bober16 != 0 or \
                self.bober4 == self.bober10 == self.bober7 == self.bober13 != 0):
            if (self.bober1 == self.bober2 == self.bober3 == self.bober4 == 1 or \
                    self.bober5 == self.bober6 == self.bober7 == self.bober8 == 1 or \
                    self.bober9 == self.bober10 == self.bober11 == self.bober12 == 1 or \
                    self.bober13 == self.bober14 == self.bober15 == self.bober16 == 1 or \
                    self.bober9 == self.bober1 == self.bober5 == self.bober13 == 1 or \
                    self.bober2 == self.bober6 == self.bober10 == self.bober14 == 1 or \
                    self.bober3 == self.bober7 == self.bober11 == self.bober15 == 1 or \
                    self.bober4 == self.bober8 == self.bober12 == self.bober16 == 1 or \
                    self.bober1 == self.bober6 == self.bober11 == self.bober16 == 1 or \
                    self.bober4 == self.bober10 == self.bober7 == self.bober13 == 1):
                print('0000000101010101010101011')
            else:
                print('020202020202002')
            if self.a == 0:
                print('Шаурма')
                self.dialog = Kirpich()
                self.dialog.show()
                pygame.mixer.init()
                pygame.mixer.music.load("C:/Users/Andrey/Desktop/Day.mp3")
                pygame.mixer.music.play()

            if self.a == 1:
                print('АБ')
                self.dialog = Sosiska()
                self.dialog.show()
                pygame.mixer.init()
                pygame.mixer.music.load("C:/Users/Andrey/Desktop/Day.mp3")
                pygame.mixer.music.play()


def main():
    app = QApplication(sys.argv)
    main = Raspili_menya_bolgarkoj()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

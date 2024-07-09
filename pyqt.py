from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
import sys


class Window(QMainWindow):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.setGeometry(x, y, 128, 128)

        # Налаштування вікна
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute(0x78))
        self.setAutoFillBackground(True)

        # Ставимо зображення
        self.img = QLabel(self)
        transparent_img = QImage()
        transparent_img.load('cat128.png')
        self.img.setPixmap(QPixmap.fromImage(transparent_img))
        self.img.resize(self.width(), self.height())

        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window(1800, 895)
    sys.exit(App.exec())

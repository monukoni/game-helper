from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
import sys

mascot_size = [128, 128]
taskbar_size = 57

class Window(QMainWindow):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.setGeometry(x, y, *mascot_size)

        # Налаштування вікна
        self.setWindowTitle('Steppy')
        self.setWindowIcon(QtGui.QIcon('cat256.png'))
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute(0x78)) # Не шарю шо це
        self.setAutoFillBackground(True)

        # Ставимо зображення
        self.img = QLabel(self)
        transparent_img = QImage()
        transparent_img.load(f'cat{mascot_size[0]}.png')
        self.img.setPixmap(QPixmap.fromImage(transparent_img))
        self.img.resize(self.width(), self.height())

        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window(1920-mascot_size[0], 1080-mascot_size[1]-taskbar_size)
    sys.exit(App.exec())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
import sys



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mascotSize = [128, 128]
        
        self.taskbarSize = (QDesktopWidget().screenGeometry().height() -
                            QDesktopWidget().availableGeometry().height())

        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry()

        self.currentPosition = QPoint(*[self.screenSize.width()-self.mascotSize[0],
                                        self.screenSize.height()-self.mascotSize[1]-self.taskbarSize])

        self.setGeometry(self.currentPosition.x(),
                         self.currentPosition.y(),
                         *self.mascotSize)

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
        transparent_img.load(f'cat{self.mascotSize[0]}.png')
        self.img.setPixmap(QPixmap.fromImage(transparent_img))
        self.img.resize(self.width(), self.height())

        self.show()

    def mousePressEvent(self, event):
        self.currentPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.currentPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.currentPosition = event.globalPos()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

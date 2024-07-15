from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mascot_size = [128, 128]
        self.taskbar_size = (QDesktopWidget().screenGeometry().height()
                             - QDesktopWidget().availableGeometry().height())
        self.screen_size = QtWidgets.QDesktopWidget().screenGeometry()

        self.popup_menu = PopupMenu(self)

        self.current_position = QPoint(*[self.screen_size.width() - self.mascot_size[0],
                                         self.screen_size.height() - self.mascot_size[1] - self.taskbar_size])
        self.setGeometry(self.current_position.x(),
                         self.current_position.y(),
                         *self.mascot_size)

        # Налаштування вікна
        self.setWindowTitle('Steppy')
        self.setWindowIcon(QtGui.QIcon('cat256.png'))
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute(0x78))
        self.setAutoFillBackground(True)

        # Ставимо зображення
        self.img = QLabel(self)
        transparent_img = QImage()
        transparent_img.load(f'cat{self.mascot_size[0]}.png')
        self.img.setPixmap(QPixmap.fromImage(transparent_img))
        self.img.resize(self.width(), self.height())

        self.show()

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        self.current_position = event.globalPos()

        if event.button() == QtCore.Qt.RightButton:
            self.popup_menu.show()
            self.popup_menu.set_pos(QPoint(event.globalPos().x(),
                                           self.pos().y() - self.popup_menu.height()))

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        delta = QPoint(event.globalPos() - self.current_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.current_position = event.globalPos()


class PopupMenu(QtWidgets.QMenu):
    def __init__(self, parent=None):
        super(PopupMenu, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)

        widgets = [
            PopupButtonLabel("search", self.showMenu, self), # пхаємо функцію на лейбл
            PopupButtonLabel("create tips", None, self),
            PopupButtonLabel("make notes", None, self),
            ExitButton("Exit", self)
        ]
        for widget in widgets:
            self.layout.addWidget(widget)
        self.layout.addStretch()
        self.setLayout(self.layout)

    def showMenu(self):
        aboba = QMenu(self)
        aboba.setGeometry(500, 500, 500, 500)
        aboba.show()

    def set_pos(self, point: QPoint):
        self.setGeometry(point.x() - 50, point.y() - 10, 100, 100)


class PopupButton(QPushButton):
    def __init__(self, text: str, parent=None):
        super(PopupButton, self).__init__(parent)
        self.setText(text)


class PopupButtonLabel(QLabel):
    def __init__(self, text: str, func=None, parent=None):
        super(QLabel, self).__init__(parent)
        self.setText(text)
        self.func = func

    def mousePressEvent(self, event):
        if self.func is not None:
            self.func()


class ExitButton(PopupButtonLabel):
    def __init__(self, text: str, parent=None):
        super(PopupButtonLabel, self).__init__(text, parent)

    def mousePressEvent(self, event, q_mouse_event=None):
        sys.exit()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

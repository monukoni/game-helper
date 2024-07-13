from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.new_window = None
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
        self.setAttribute(QtCore.Qt.WidgetAttribute(0x78))  # Не шарю шо це
        self.setAutoFillBackground(True)

        # Ставимо зображення
        self.img = QLabel(self)
        transparent_img = QImage()
        transparent_img.load(f'cat{self.mascot_size[0]}.png')
        self.img.setPixmap(QPixmap.fromImage(transparent_img))
        self.img.resize(self.width(), self.height())

        self.show()

    def moveEvent(self, event):
        if self.new_window is not None:
            # TODO bug
            self.new_window.move(self.x()-int((self.new_window.width() - 128/1.5)), self.y()-120)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        self.current_position = event.globalPos()

        if event.button() == QtCore.Qt.RightButton:
            if self.new_window is not None:
                if self.new_window.isVisible() is False:
                    self.new_window = None

            if self.new_window is None:
                self.popup_menu.set_pos(QPoint(event.globalPos()))
                self.popup_menu.show()
                # self.new_window = SpeechBubble(self.x(), self.y())
                # self.new_window.show()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        delta = QPoint(event.globalPos() - self.current_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.current_position = event.globalPos()

    def closeEvent(self, event: QtGui.QCloseEvent):
        pass


class SpeechBubble(QtWidgets.QMenu):
    def __init__(self, x, y):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel(self)
        self.label.setText("А ви знали, що в туалеті можна какати?")
        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label)

        self.close_button = QPushButton(self)
        self.close_button.setText("×")
        # self.close_button.setAlignment(QtCore.Qt.AlignCenter)
        # self.close_button.setGeometry(180, 0, 20, 20)
        self.close_button.clicked.connect(self.buttonClose)

        self.move(x-int((self.width()-128)/10), y-120)

    def buttonClose(self):
        self.close()


class PopupMenu(QtWidgets.QMenu):
    def __init__(self, parent=None):
        super(PopupMenu, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        widgets = [
            # QTextEdit
            # QInputDialog
        ]
        for widget in widgets:
            self.layout.addWidget(widget())
        self.setLayout(self.layout)
        # self.setGeometry(self.currentPosition.x(),
        #                  self.currentPosition.y(),
        #                  *self.mascotSize)


    def set_pos(self, point: QPoint):
        self.setGeometry(point.x() - 200, point.y()-400, 100, 100)

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

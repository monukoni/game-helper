from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class SpeechBubble(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.set_window_flags()
        self.set_image_background()
        # todo: Add normal geometry
        self.setGeometry(2200, 800, 500, 500)

    def set_window_flags(self):
        self.setWindowTitle('Steppy talking')
        # self.setWindowIcon(QIcon('assets/cat256.png'))
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute(0x78))
        self.setAutoFillBackground(True)

    def set_image_background(self):
        pixmap = QtGui.QPixmap(f'C:\\Users\\tehfv\\PycharmProjects\\game-helper\\assets\\speech_bubble_right.png')

        # Create a QPainter to draw text on the image
        # painter = QtGui.QPainter(pixmap)
        # painter.setPen(QtGui.QPen(QtGui.QColor("white")))
        # painter.setFont(QtGui.QFont("Arial", 30))
        #
        # # Draw text on the image
        # painter.drawText(pixmap.rect(), QtCore.Qt.AlignCenter, "Hello brother")
        # painter.end()

        # Set the modified image to the label
        # self.label.setPixmap(pixmap)
        self.img = QLabel(self)
        transparent_img = QImage()
        transparent_img.load(f'C:\\Users\\tehfv\\PycharmProjects\\game-helper\\assets\\speech_bubble_right.png')
        self.img.setPixmap(QPixmap.fromImage(transparent_img))
        self.img.resize(self.width(), self.height())

    def set_text(self, text):
        ...
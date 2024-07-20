from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt


class SpeechBubble(QtWidgets.QWidget):
    def __init__(self, app: QMainWindow):
        super().__init__()
        self.app = app
        # todo: Add normal geometry
        self.setFixedSize(200, 200)

        self.move(app.pos().x() - int(self.width() / 2),
                  app.pos().y() - self.height())

        self.set_window_flags()
        self.set_image_background()


    def set_window_flags(self):
        self.setWindowTitle('Steppy talking')
        self.setWindowIcon(QIcon('assets/speech_bubble_right.png'))
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute(0x78))
        self.setAutoFillBackground(True)

    def set_image_background(self):
        self.img = QLabel(self)
        transparent_img = QImage()
        transparent_img.load(f'assets/speech_bubble_right.png')
        image = QPixmap.fromImage(transparent_img)
        image = image.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.img.setPixmap(image)
        self.img.resize(self.width(), self.height())


    def set_text(self, text):
        ...
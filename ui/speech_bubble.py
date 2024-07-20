from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt, QRect, QTimer
from db.database import Database
import random

MARGIN_TOP = 20


class SpeechBubble(QtWidgets.QWidget):
    def __init__(self, app: QMainWindow):
        super().__init__()
        database = Database()

        self.TIPS = database.get_tips()

        self.app = app
        self.setFixedSize(200, 200)
        self.move(app.pos().x() - int(self.width() / 2),
                  app.pos().y() - self.height())
        self.label = QLabel(self)
        self.set_window_flags()
        # self.pixmap = QPixmap(f'assets/speech_bubble_right.png')
        # self.set_image_background()
        self.set_text(self.TIPS[0])
        self.timer = QTimer()
        self.timer.setInterval(self.app.settings.delay*1000)
        self.timer.timeout.connect(self.rotate_tips)
        self.timer.start()

    def set_window_flags(self):
        self.setWindowTitle('Steppy talking')
        self.setWindowIcon(QIcon('assets/speech_bubble_right.png'))
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute(0x78))
        self.setAutoFillBackground(True)

    # def set_image_background(self):
    #     self.pixmap = self.pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    #     self.label.setPixmap(self.pixmap)
    #     self.label.resize(self.width(), self.height())

    def set_text(self, text):
        self.pixmap = QPixmap(f'assets/speech_bubble_right.png')
        self.pixmap = self.pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width(), self.height())
        painter = QtGui.QPainter(self.pixmap)
        painter.setPen(QtGui.QPen(QtGui.QColor("black")))
        painter.setFont(QtGui.QFont("Arial", 8))

        # todo: create layout, create text, and dynamically set pixmap w/h based on text length
        rect: QRect = self.pixmap.rect()
        painter.drawText(rect.x(), rect.y() + MARGIN_TOP, rect.width(), rect.height(),
                         QtCore.Qt.AlignHCenter | QtCore.Qt.TextWordWrap, text)
        painter.end()
        self.label.setWordWrap(True)
        self.label.setPixmap(self.pixmap)

    def rotate_tips(self):
        # todo: fix overlapping tips on pixmap
        next_tip = random.choice(self.TIPS)
        self.set_text(next_tip)

    def closeEvent(self, event):
        self.timer.stop()


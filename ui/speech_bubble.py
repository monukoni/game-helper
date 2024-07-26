import random

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QRect, QTimer
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QCheckBox

import psutil
import time
import threading
import ctypes
import multiprocessing
import time
import os
import signal
import sys


from settings import SteppySettings

MARGIN_TOP = 20


class SpeechBubble(QtWidgets.QWidget):
    def __init__(self, parent_app, settings: SteppySettings):
        super().__init__()

        self.parent_app = parent_app
        self.settings: SteppySettings = settings
        
        self.GAMES = ["spotify"]

        self.setFixedSize(200, 200)
        self.move(self.parent_app.pos().x() - int(self.width() / 2),
                  self.parent_app.pos().y() - self.height())
        self.label = QLabel(self)
        self.set_window_flags()

        self.notes_checkbox = QCheckBox('Notes', self)
        self.notes_checkbox.move(self.width() - 80, self.height() - 80)

        # self.pixmap = QPixmap(f'assets/speech_bubble_right.png')
        # self.set_image_background()
        # self.set_text(self.parent_app.TIPS[0])

        
        # self.check_proccess_timer = QTimer()
        # self.check_proccess_timer.setInterval(5000)
        # self.check_proccess_timer.timeout.connect(self.check_proccess)
        # self.check_proccess_timer.start()
        
        # self.check_proccess_thread_stop = False
        # self.check_proccess_thread = threading.Thread(target=self.check_proccess)
        # self.check_proccess_thread.start()
        
        self.set_text("Initialize")
        self.rotate_tips_timer = QTimer()
        self.rotate_tips_timer.setInterval(self.settings.delay * 1000)
        self.rotate_tips_timer.timeout.connect(self.rotate_tips)
        self.rotate_tips_timer.start()

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
        painter.setFont(QtGui.QFont("Arial", self.settings.speech_buble_font_size))

        # todo: create layout, create text, and dynamically set pixmap w/h based on text length
        rect: QRect = self.pixmap.rect()

        # painter.drawText(rect, QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap, text)
        # todo: make normal spawn point
        painter.drawText(rect.x() + 10, rect.y() + MARGIN_TOP, rect.width() - 30, rect.height() - 10,
                         QtCore.Qt.AlignHCenter | QtCore.Qt.TextWordWrap, text)
        painter.end()
        self.label.setWordWrap(True)
        self.label.setPixmap(self.pixmap)

    def rotate_tips(self):
        if self.notes_checkbox.isChecked():
            next_tip = "\n".join(self.parent_app.NOTES)
        else:
            next_tip = random.choice(self.parent_app.TIPS)
        self.set_text(next_tip)

    def check_proccess(self):
        while True:
            processes = psutil.process_iter(['name'])
            for process in processes:
                try:
                    process_info = process.as_dict(attrs=['name'])
                    if process_info["name"] in self.GAMES:
                        print(process_info["name"] )
                except psutil.Error as ex:
                    print(ex)
            
            

    def closeEvent(self, event):
        self.rotate_tips_timer.stop()



    
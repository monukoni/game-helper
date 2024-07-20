from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import (
    QDesktopWidget, QMainWindow, QMenu, QLabel
)
from PyQt5.QtGui import QPixmap, QImage, QMouseEvent, QIcon
from PyQt5.QtCore import Qt

from colors import DEFAULT_MENU_COLOR
from settings import SteppySettings
from ui.actions import (
    make_exit_action,
    make_open_settings_action
)
from ui.settings import SettingsWindow
from ui.speech_bubble import SpeechBubble


class Steppy(QMainWindow):

    def __init__(self, settings: SteppySettings):
        super().__init__()
        self.settings = settings
        self.mascot_size = [128, 128]
        self.taskbar_size = (QDesktopWidget().screenGeometry().height()
                             - QDesktopWidget().availableGeometry().height())
        self.screen_size = QDesktopWidget().screenGeometry()

        self.current_position = QPoint(*[self.screen_size.width() - self.mascot_size[0],
                                         self.screen_size.height() - self.mascot_size[1] - self.taskbar_size])
        self.setGeometry(self.current_position.x(),
                         self.current_position.y(),
                         *self.mascot_size)
        # Налаштування вікна
        self.set_window_flags()
        # Ставимо зображення
        self.set_image_background()
        # Set all UI children windows
        self.add_children_windows()
        self.show()
        self.speech_bubble.show()

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.setStyleSheet(f'background-color: {DEFAULT_MENU_COLOR};')
        exit_action = make_exit_action(self)
        open_settings_action = make_open_settings_action(self)
        menu.addAction(open_settings_action)
        menu.addAction(exit_action)
        menu.exec_(event.globalPos())

    def add_children_windows(self):
        self.settings_window = SettingsWindow(self)
        self.speech_bubble = SpeechBubble(self)

    def set_window_flags(self):
        self.setWindowTitle('Steppy')
        self.setWindowIcon(QIcon('assets/cat256.png'))
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute(0x78))
        self.setAutoFillBackground(True)

    def set_image_background(self):
        self.img = QLabel(self)
        transparent_img = QImage()
        transparent_img.load(f'assets/cat{self.mascot_size[0]}.png')
        self.img.setPixmap(QPixmap.fromImage(transparent_img))
        self.img.resize(self.width(), self.height())

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.current_position)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.current_position = event.globalPos()


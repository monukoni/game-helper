from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QMouseEvent, QIcon
from PyQt5.QtWidgets import (
    QDesktopWidget, QMainWindow, QMenu, QLabel
)

from colors import DEFAULT_MENU_COLOR
from db.database import Database
from settings import SteppySettings
from ui.actions import (
    make_exit_action,
    make_open_notes_action,
    make_open_settings_menu_action
)
from ui.notes import NotesWindow
from ui.speech_bubble import SpeechBubble
from ui.settings_menu import SettingsMenu


class Steppy(QMainWindow):

    def __init__(self, settings: SteppySettings):
        super().__init__()
        self.database = Database()

        self.settings = settings

        self.GAMES = self.database.get_games()
        self.current_game = {'id': self.GAMES[0][0], 'name': self.GAMES[0][1], 'proccess_name': self.GAMES[0][2]}
        self.TIPS = list()
        self.NOTES = list()
        self.initialize_tips()

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

        self.speech_bubble.show()

    def initialize_tips(self):
        self.TIPS = self.database.get_tips(self.current_game["id"])
        self.NOTES = self.database.get_notes(self.current_game["id"])

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.setStyleSheet(f'background-color: {DEFAULT_MENU_COLOR};')
        exit_action = make_exit_action(self)
        open_notes_action = make_open_notes_action(self)
        open_settings_menu_action = make_open_settings_menu_action(self)
        menu.addAction(open_notes_action)
        menu.addAction(open_settings_menu_action)
        menu.addAction(exit_action)
        menu.exec_(event.globalPos())

    def add_children_windows(self):
        self.notes_window = NotesWindow(self)
        self.speech_bubble = SpeechBubble(self, self.settings)
        self.settings_menu_window = SettingsMenu(self.settings)

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

    def mousePressEvent(self, event):
        self.current_position = event.globalPos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            if self.speech_bubble.isVisible():
                self.speech_bubble.move(self.x() - int(self.speech_bubble.width() / 2),
                                        self.y() - self.speech_bubble.height())

            delta = QPoint(event.globalPos() - self.current_position)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.current_position = event.globalPos()

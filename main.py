from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import (
    QDesktopWidget, QMainWindow, QMenu, QLabel, QApplication
)
from PyQt5.QtGui import QPixmap, QImage, QMouseEvent, QIcon
from PyQt5.QtCore import Qt
import sys
from ui.actions import (
    make_exit_action,
    make_open_settings_action
)


class Steppy(QMainWindow):

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        exit_action = make_exit_action(self)
        open_settings_action = make_open_settings_action(self)
        menu.addAction(open_settings_action)
        menu.addAction(exit_action)
        menu.exec(event.globalPos())

    def __init__(self):
        super().__init__()

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
        self.setWindowTitle('Steppy')
        self.setWindowIcon(QIcon('cat256.png'))
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute(0x78))
        self.setAutoFillBackground(True)

        # Ставимо зображення
        self.img = QLabel(self)
        transparent_img = QImage()
        transparent_img.load(f'cat{self.mascot_size[0]}.png')
        self.img.setPixmap(QPixmap.fromImage(transparent_img))
        self.img.resize(self.width(), self.height())

        self.show()

    def mouseMoveEvent(self, event: QMouseEvent):
        delta = QPoint(event.globalPos() - self.current_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.current_position = event.globalPos()


def main():
    app = QApplication(sys.argv)
    steppy = Steppy()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

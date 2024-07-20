from PyQt5.QtWidgets import (
    QMainWindow, QAction, qApp
)


def make_exit_action(app: QMainWindow):
    def _exit(code: int = 0):
        qApp.exit(code)
    exit_action = QAction("Exit", app)
    exit_action.triggered.connect(_exit)
    return exit_action


def make_open_settings_action(app: QMainWindow):
    open_settings_action = QAction("Open settings", app)
    return open_settings_action


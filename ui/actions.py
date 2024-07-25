from PyQt5.QtWidgets import (
    QMainWindow, QAction, qApp
)


def make_exit_action(app: QMainWindow):
    def _exit(code: int = 0):
        qApp.exit(code)

    exit_action = QAction("Exit", app)
    exit_action.triggered.connect(_exit)
    return exit_action


def make_open_notes_action(app: QMainWindow):
    open_notes_action = QAction("Notes")
    open_notes_action.triggered.connect(app.notes_window.show)
    return open_notes_action


def make_open_settings_menu_action(app: QMainWindow):
    open_settings_menu_action = QAction("Settings")
    open_settings_menu_action.triggered.connect(app.settings_menu_window.show)
    return open_settings_menu_action

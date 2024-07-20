from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton
from colors import DEFAULT_MENU_COLOR


class SettingsWindow(QtWidgets.QWidget):

    def __init__(self, app):
        super().__init__()
        # todo: fix layout
        self.app = app
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("New Window")
        # self.setGeometry(0, 0, 500, 500)
        self.setStyleSheet(f'background-color: {DEFAULT_MENU_COLOR};')
        layout = QtWidgets.QVBoxLayout()
        label = QLabel("This is a new window")
        layout.addWidget(label)

        # Add numeric input field
        self.spin_box = QtWidgets.QSpinBox()
        self.spin_box.setPrefix('Speech bubble delay:')
        self.spin_box.setValue(self.app.settings.delay)
        self.spin_box.setRange(0, 100)  # Example range
        self.spin_box.valueChanged.connect(self.on_delay_value_changed)
        layout.addWidget(self.spin_box)

        # Add close button
        close_button_layout = QtWidgets.QHBoxLayout()
        close_button_layout.addStretch()
        close_button = QPushButton('X')
        close_button.setStyleSheet(f'border-radius: 250px; border-color: red;')
        close_button.clicked.connect(self.close)
        close_button_layout.addWidget(close_button)
        layout.addLayout(close_button_layout)

        save_button = QPushButton('Save')
        save_button.clicked.connect(self.save_settings)
        close_button_layout.addWidget(save_button)
        layout.addLayout(close_button_layout)

        self.setLayout(layout)
        # Center the window on the screen
        self.center()

    def on_delay_value_changed(self, e):
        self.app.settings.delay = self.spin_box.value()

    def save_settings(self):
        self.app.settings.save_to_file('conf.json')
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


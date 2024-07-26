from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QSpinBox

from settings import SteppySettings


class SettingsMenu(QWidget):
    def __init__(self, settings: SteppySettings):
        super().__init__()
        self.settings = settings

        layout = QFormLayout()
        delay_line = QSpinBox()
        delay_line.setValue(settings.delay)
        layout.addRow("Bubble delay (in seconds)", delay_line)
        layout.addRow("Hint font size", QLineEdit(str(settings.speech_buble_font_size)))
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.close)
        layout.addRow(save_button)
        self.setLayout(layout)

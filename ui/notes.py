from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox, QTextEdit

from colors import DEFAULT_MENU_COLOR


class NotesWindow(QtWidgets.QWidget):

    def __init__(self, app):
        super().__init__()

        # todo: fix layout
        self.app = app
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Notes")
        self.setGeometry(0, 0, 500, 500)
        self.setStyleSheet(f'background-color: {DEFAULT_MENU_COLOR};')
        layout = QtWidgets.QVBoxLayout()
        label = QLabel("Notes")
        label.setAlignment(Qt.AlignTop)
        layout.addWidget(label)

        self.combo = QComboBox(self)
        self.combo.addItem("Elden Ring", 2)
        self.combo.addItem("Dead by Daylight", 1)
        self.combo.activated.connect(self.onActivated)
        layout.addWidget(self.combo)

        self.note_line_edit = QLineEdit(self)
        self.note_line_edit.setPlaceholderText("Enter your note here")
        layout.addWidget(self.note_line_edit)

        self.save_note_button = QPushButton("Save Note")
        self.save_note_button.pressed.connect(self.save_note)
        layout.addWidget(self.save_note_button)

        self.text_input_layout = QtWidgets.QHBoxLayout()
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter your tip here")
        self.text_input.setAlignment(Qt.AlignLeft)
        self.text_input_layout.addWidget(self.text_input)
        layout.addWidget(self.text_input)

        save_tip_button = QPushButton('Save Tip')
        save_tip_button.clicked.connect(self.save_tip)
        layout.addWidget(save_tip_button)

        # Add numeric input field
        self.spin_box = QtWidgets.QSpinBox()
        self.spin_box.setPrefix('Speech bubble delay:')
        self.spin_box.setValue(self.app.settings.delay)
        self.spin_box.setRange(0, 100)
        self.spin_box.valueChanged.connect(self.on_delay_value_changed)
        layout.addWidget(self.spin_box)

        close_button_layout = QtWidgets.QHBoxLayout()
        close_button_layout.addStretch()
        save_button = QPushButton('Save')
        save_button.clicked.connect(self.save_settings)
        close_button_layout.addWidget(save_button)

        layout.addLayout(close_button_layout)
        close_button = QPushButton('X')
        close_button.clicked.connect(self.close)
        close_button_layout.addWidget(close_button)
        layout.addLayout(close_button_layout)

        self.setLayout(layout)
        # Center the window on the screen
        self.center()

    def onActivated(self, e):
        print(self.combo.currentText())
        print(self.combo.itemData(e))

    def on_delay_value_changed(self, e):
        self.app.settings.delay = self.spin_box.value()

    def save_settings(self):
        self.app.settings.save_to_file('conf.json')
        self.close()

    def save_tip(self):
        text = self.text_input.text()
        self.app.database.insert_tips(text)

    def save_note(self):
        text = self.note_line_edit.text()
        self.app.database.insert_notes(text)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

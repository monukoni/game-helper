import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        example_text = (
            "Did you know you can unhook your teammate?\n"
            "Did you know you can stun killer by dropping palette?\n"
            "Always stay aware of your surroundings to avoid being caught off guard by the killer.\n"

        )

        self.text_edit.setPlainText(example_text)

        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

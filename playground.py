import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget


class ImageWithTextWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image with Text")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel(self)
        layout.addWidget(self.label)

        self.setLayout(layout)

        # Load and display the image with text
        self.loadImageWithText()

    def loadImageWithText(self):
        # Load the image
        pixmap = QtGui.QPixmap("assets/speech_bubble_right.png")

        if pixmap.isNull():
            print("Failed to load image")
            return

        # Create a QPainter to draw text on the image
        painter = QtGui.QPainter(pixmap)
        painter.setPen(QtGui.QPen(QtGui.QColor("black")))
        painter.setFont(QtGui.QFont("Arial", 30))

        # Draw text on the image
        painter.drawText(pixmap.rect(), QtCore.Qt.AlignCenter, "Your Text Here")
        painter.end()

        # Set the modified image to the label
        self.label.setPixmap(pixmap)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 500, 400)

        self.imageWidget = ImageWithTextWidget()
        self.setCentralWidget(self.imageWidget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

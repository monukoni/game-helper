import sys
import signal

from PyQt5.QtWidgets import QApplication

from settings import SteppySettings
from steppy import Steppy


def main():
    app = QApplication(sys.argv)
    settings = SteppySettings.from_file('conf.json')
    steppy = Steppy(settings)
    # trap SIGINT to correctly exit app loop
    signal.signal(signal.SIGINT, lambda *_: app.exit(1))
    steppy.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

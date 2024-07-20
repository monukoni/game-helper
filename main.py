import sys

from PyQt5.QtWidgets import QApplication

from steppy import Steppy
from settings import SteppySettings
from db.database import Database

def main():

    app = QApplication(sys.argv)
    settings = SteppySettings.from_file('conf.json')
    # print(str(settings))
    steppy = Steppy(settings)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

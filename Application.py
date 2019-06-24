# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

class ApplicationHandler():
    def __init__(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    appHandler = ApplicationHandler()
    sys.exit(app.exec())
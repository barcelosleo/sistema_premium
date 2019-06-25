from PyQt5 import QtWidgets

import View.MainWindowView

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = View.MainWindowView()
        self.ui.setupUi(self)

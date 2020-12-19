import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Window import *


class InitWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(InitWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InitWindow()
    window.show()
    sys.exit(app.exec_())

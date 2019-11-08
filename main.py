import sys

from PyQt5.QtWidgets import QApplication

from Classes import *


class Main(MainWindows, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())

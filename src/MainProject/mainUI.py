from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication

import sys


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("Sort Algorithm Visualizer")

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = mainwindow()
    sys.exit(app.exec())
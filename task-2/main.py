from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPen
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from random import randint
import sys


class Ui(QMainWindow, Ui_MainWindow):
    d: int = 0
    x: int = 0
    y: int = 0

    def __init__(self):
        size: QSize
        super().__init__()
        self.setupUi(self)
        self.drawed.clicked.connect(self.run)
        self.do = False
        size = self.size()
        self.x = size.width()
        self.y = size.height()

    def run(self):
        self.d = randint(1, 100)
        self.do = True

    def paintEvent(self, event):
        if self.do:
            self.paint = QPainter(self)
            self.paint.begin(self)
            self.draw()
            self.paint.end()
            self.update()

    def draw(self):
        self.paint.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        self.paint.drawEllipse(self.x // 2 - self.d // 2, self.y // 2 - 20 - self.d // 2, self.d, self.d)


app = QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()

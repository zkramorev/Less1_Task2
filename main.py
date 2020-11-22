import sys
import random
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from okr import Ui_MainWindow


class First(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.do)
        self.f = False

    def paint(self):
        self.repaint()

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.f = False
            qp.setBrush(QColor(255, 255, 0))
            k = random.randint(20, 320)
            qp.drawEllipse(220, 150, k, k)
            qp.end()

    def do(self):
        self.f = True
        self.paint()


app = QApplication(sys.argv)
ex = First()
ex.show()
sys.exit(app.exec())

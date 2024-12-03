import random
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QPushButton, QWidget


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circle_widget = CircleWidget()
        self.setCentralWidget(self.circle_widget)

        self.button = self.findChild(QPushButton, 'Button')
        self.button.clicked.connect(self.circle_widget.add_circle)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

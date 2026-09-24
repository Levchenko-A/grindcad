from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QWidget


class Canvas(QWidget):
    """Main drawing surface for GrindCAD."""

    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)

        pen = QPen()
        pen.setWidth(1)

        painter.setPen(pen)

        width = self.width()
        height = self.height()

        center_x = width // 2
        center_y = height // 2

        # X axis
        painter.drawLine(0, center_y, width, center_y)

        # Y axis
        painter.drawLine(center_x, 0, center_x, height)

        painter.end()

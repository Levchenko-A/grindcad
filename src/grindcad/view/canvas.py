from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QWidget


class Canvas(QWidget):
    """Main drawing surface for GrindCAD."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.scale = 1.0

    def paintEvent(self, event):
        painter = QPainter(self)

        width = self.width()
        height = self.height()

        # Move origin to center of canvas.
        painter.translate(width / 2, height / 2)

        # Flip Y axis so positive Y points upward.
        painter.scale(self.scale, -self.scale)

        self.draw_grid(painter, width, height)
        self.draw_axes(painter, width, height)

        painter.end()

    def draw_grid(self, painter, width, height):
        pen = QPen()
        pen.setWidth(0)
        painter.setPen(pen)

        grid_size = 50

        x_min = -width
        x_max = width

        y_min = -height
        y_max = height

        for x in range(x_min, x_max + 1, grid_size):
            painter.drawLine(x, y_min, x, y_max)

        for y in range(y_min, y_max + 1, grid_size):
            painter.drawLine(x_min, y, x_max, y)

    def draw_axes(self, painter, width, height):
        pen = QPen()
        pen.setWidth(2)
        painter.setPen(pen)

        # X axis
        painter.drawLine(-width, 0, width, 0)

        # Y axis
        painter.drawLine(0, -height, 0, height)
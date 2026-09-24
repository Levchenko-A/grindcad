from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QWidget


class Canvas(QWidget):
    """Main drawing surface for GrindCAD."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.scale = 1.0

    def paintEvent(self, event):
        painter = QPainter(self)

        pen = QPen()
        pen.setWidth(1)
        painter.setPen(pen)

        width = self.width()
        height = self.height()

        # Move the origin to the center of the canvas.
        painter.translate(width / 2, height / 2)

        # Flip the Y axis so positive Y points upward.
        painter.scale(self.scale, -self.scale)

        # Draw X axis.
        painter.drawLine(
            -width,
            0,
            width,
            0,
        )

        # Draw Y axis.
        painter.drawLine(
            0,
            -height,
            0,
            height,
        )

        painter.end()

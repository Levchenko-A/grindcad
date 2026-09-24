from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt


class Canvas(QWidget):
    """Main drawing surface for GrindCAD."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.scale = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.last_mouse_position = None

    def paintEvent(self, event):
        painter = QPainter(self)

        width = self.width()
        height = self.height()

        # Move origin to center of canvas.
        painter.translate(
            width / 2 + self.offset_x,
            height / 2 + self.offset_y,
        )


        # Flip Y axis so positive Y points upward.
        painter.scale(self.scale, -self.scale)

        self.draw_grid(painter, width, height)
        self.draw_axes(painter, width, height)

        painter.end()
        
    def wheelEvent(self, event):
        """Zoom the CAD view using the mouse wheel."""

        if event.angleDelta().y() > 0:
            self.scale *= 1.1
        else:
            self.scale /= 1.1

        self.update()
        
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
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.last_mouse_position = event.position()


    def mouseMoveEvent(self, event):
        if self.last_mouse_position is None:
            return

        if event.buttons() & Qt.MouseButton.MiddleButton:
            current_position = event.position()

            delta = current_position - self.last_mouse_position

            self.offset_x += delta.x()
            self.offset_y += delta.y()

            self.last_mouse_position = current_position

            self.update()


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.last_mouse_position = None

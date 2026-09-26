from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from grindcad.geometry.point import Point

class Canvas(QWidget):
    """Main drawing surface for GrindCAD."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.scale = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.last_mouse_position = None
        self.mouse_world_position = (0.0, 0.0)
        self.entities = []
        self.entities.append(Point(0, 0))
        self.entities.append(Point(100, 100))
        self.entities.append(Point(-150, 50))
    
    def paintEvent(self, event):
        painter = QPainter(self)

        width = self.width()
        height = self.height()

        painter.translate(
            width / 2 + self.offset_x,
            height / 2 + self.offset_y,
        )

        painter.scale(self.scale, -self.scale)

        self.draw_grid(painter, width, height)
        self.draw_axes(painter, width, height)

        self.draw_entities(painter)

        # Return to screen coordinates
        painter.resetTransform()

        x, y = self.mouse_world_position

        painter.drawText(
            10,
            25,
            f"X: {x:.2f}    Y: {y:.2f}",
        )

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
        current_position = event.position()

        self.mouse_world_position = self.screen_to_world(
            current_position
        )

        if self.last_mouse_position is None:
            self.last_mouse_position = current_position

        if event.buttons() & Qt.MouseButton.MiddleButton:
            delta = current_position - self.last_mouse_position

            self.offset_x += delta.x()
            self.offset_y += delta.y()

            self.last_mouse_position = current_position

        self.update()


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.last_mouse_position = None
    
    def screen_to_world(self, position):
        """Convert a screen position to CAD world coordinates."""

        width = self.width()
        height = self.height()

        world_x = (
            position.x() - width / 2 - self.offset_x
        ) / self.scale

        world_y = -(
            position.y() - height / 2 - self.offset_y
        ) / self.scale

        return world_x, world_y
    
    def draw_entities(self, painter):
        """Draw CAD entities."""
        for entity in self.entities:
            if isinstance(entity, Point):
            	painter.drawEllipse(entity.x - 3,entity.y - 3,6,6,)
	

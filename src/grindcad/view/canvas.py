from PySide6.QtWidgets import QWidget


class Canvas(QWidget):
    """Main drawing surface for GrindCAD."""

    def __init__(self, parent=None):
        super().__init__(parent)

import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from grindcad.view.canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GrindCAD")
        self.resize(1000, 700)

        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    main()

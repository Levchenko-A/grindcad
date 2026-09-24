import sys

from PySide6.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("GrindCAD")
    window.resize(1000, 700)
    window.show()

    return app.exec()


if __name__ == "__main__":
    main()


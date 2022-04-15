import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from gui.ui_gui2 import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
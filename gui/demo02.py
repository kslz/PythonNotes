import sys

from PySide6.QtWidgets import QApplication, QLabel

# Hello World
app = QApplication(sys.argv)
label = QLabel("Hello World")
label2 = QLabel("<font color = red size = 40>Hello World</font>")
label.show()
label2.show()
app.exec()


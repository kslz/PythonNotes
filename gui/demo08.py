import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()
    w = QLabel("这是一句文字 This is a text")
    w.setAlignment(Qt.AlignCenter)
    w.setStyleSheet("""
    background-color:#262626;
    color:#FFFFFF;
    font-family: 黑体;
    font-size:58px;
    """)
    w.show()
    sys.exit(app.exec())
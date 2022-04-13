import sys

from PySide6.QtGui import QColor

# 表格
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

colors = [
    ("Red", "#FF0000"),
    ("Green", "#00FF00"),
    ("Blue", "#0000FF"),
    ("Black", "#000000"),
    ("White", "#FFFFFF"),
    ("Yellow", "#F9E56d")
]


def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i + 2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

class color_table(QTableWidget):
    def __init__(self,parent = None):
        super(color_table, self).__init__(parent)
        self.setWindowTitle("我的颜色表")

        self.setRowCount(len(colors))
        self.setColumnCount(len(colors[0]) + 1)
        self.setHorizontalHeaderLabels(["颜色名", "“颜色代码", "颜色"])

        for i, (name, code) in enumerate(colors):
            item_name = QTableWidgetItem(name)
            item_code = QTableWidgetItem(code)
            item_color = QTableWidgetItem()
            item_color.setBackground(get_rgb_from_hex(code))
            self.setItem(i, 0, item_name)
            self.setItem(i, 1, item_code)
            self.setItem(i, 2, item_color)

app = QApplication([])
table = color_table()
table.show()
sys.exit(app.exec())

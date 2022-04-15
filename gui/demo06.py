import os
import sys

from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

data = {
    "dir1": ["file1.py", "file2.jpg"],
    "dir2": ["fileA.txt", "fileB.py"],
    "dir3": []
}

class Tree(QTreeWidget):
    def __init__(self, parent=None):
        super(Tree, self).__init__(parent)
        self.setColumnCount(2)
        self.setHeaderLabels(["文件名","类型"])
        items = []
        for key ,values in data.items():
            item = QTreeWidgetItem([key])
            for value in values:
                ext = value.split(".")[-1].upper()
                child = QTreeWidgetItem([value,ext])
                item.addChild(child)
            items.append(item)
        self.insertTopLevelItems(0,items)






app = QApplication([])
mytree = Tree()
mytree.show()
sys.exit(app.exec())
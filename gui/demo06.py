import os
import sys

from PySide6.QtWidgets import QApplication, QTreeWidget

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






app = QApplication([])
mytree = Tree()
mytree.show()
sys.exit(app.exec())
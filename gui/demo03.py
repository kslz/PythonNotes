from PySide6.QtCore import Slot

from PySide6.QtWidgets import QApplication, QPushButton


# 按钮
@Slot()
# @Slot() 是一个装饰器，用来将一个函数定义为槽函数。
def say_hello():
    print("Button clicked.")


app = QApplication([])
button = QPushButton("点我")
button.clicked.connect(say_hello)
button.show()
app.exec()

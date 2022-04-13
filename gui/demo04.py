import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton, QVBoxLayout


class Form(QDialog):
# 输入框+按钮
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        # 创建组件
        self.edit = QLineEdit("Write my name here..")
        self.button = QPushButton("展示")
        # 创建布局并添加组件
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # 应用布局
        self.setLayout(layout)
        # 连接say_hello槽和按钮单击信号
        self.button.clicked.connect(self.say_hello)

    def say_hello(self):
        print(f"Hello, {self.edit.text()}")



if __name__ == "__main__":
    # 创建Qt应用程序
    app = QApplication([])
    # 创建并显示Form
    form = Form()
    form.show()
    # 运行Qt主循环
    sys.exit(app.exec())

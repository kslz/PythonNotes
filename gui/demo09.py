from PySide6.QtCore import QUrl
from PySide6.QtQuick import QQuickView
from PySide6.QtWidgets import QApplication

app = QApplication([])
view = QQuickView()
url = QUrl("view.qml")

view.setSource(url)
# view.setResizeMode(QQuickView.SizeRootObjectToView)
view.show()
app.exec()
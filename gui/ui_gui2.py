# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 520, 171, 51))
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(590, 520, 171, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(270, 520, 261, 51))
        self.pushButton_3.setFont(font)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(279, 20, 501, 451))
        self.groupBox.setFont(font)
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 481, 411))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.gridLayoutWidget)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)

        self.widget_2 = QWidget(self.gridLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.radioButton = QRadioButton(self.widget_2)
        self.radioButton2 = QRadioButton(self.widget_2)
        self.radioButton.setObjectName(u"radioButton")
        # self.radioButton.setGeometry(QRect(10, 10, 151, 20))

        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)

        self.widget_3 = QWidget(self.gridLayoutWidget)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout.addWidget(self.widget_3, 1, 2, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 2, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u6761", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u6761", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a\u6807\u6ce8", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u6807\u6ce8\u4fe1\u606f", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Project\TP78 Integrated Tools\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 380)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Button_VIA = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_VIA.setStyleSheet("image: url(:/res/via.png);")
        self.Button_VIA.setObjectName("Button_VIA")
        self.gridLayout.addWidget(self.Button_VIA, 0, 1, 1, 1)
        self.Button_TP78 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_TP78.setObjectName("Button_TP78")
        self.gridLayout.addWidget(self.Button_TP78, 0, 0, 1, 1)
        self.Button_TP78FOC = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_TP78FOC.setObjectName("Button_TP78FOC")
        self.gridLayout.addWidget(self.Button_TP78FOC, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.Button_VIA.clicked.connect(Form.hide) # type: ignore
        self.Button_TP78FOC.clicked.connect(Form.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TP78集成工具v1.0"))
        self.Button_VIA.setText(_translate("Form", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"VIA工具"))
        self.Button_TP78.setText(_translate("Form", "TP78主键盘&TP78mini U盘模式配置工具"))
        self.Button_TP78FOC.setText(_translate("Form", "TP78foc固件升级工具"))
import image_rc
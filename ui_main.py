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
        Form.resize(765, 314)
        self.Button_TP78FOC = QtWidgets.QPushButton(Form)
        self.Button_TP78FOC.setGeometry(QtCore.QRect(260, 10, 246, 146))
        font = QtGui.QFont()
        font.setFamily("小赖字体 SC")
        self.Button_TP78FOC.setFont(font)
        self.Button_TP78FOC.setStyleSheet("image: url(:/res/TP78foc.png);")
        self.Button_TP78FOC.setObjectName("Button_TP78FOC")
        self.Button_VIA = QtWidgets.QPushButton(Form)
        self.Button_VIA.setGeometry(QtCore.QRect(10, 160, 246, 146))
        font = QtGui.QFont()
        font.setFamily("小赖字体 SC")
        self.Button_VIA.setFont(font)
        self.Button_VIA.setStyleSheet("image: url(:/res/via.png);")
        self.Button_VIA.setObjectName("Button_VIA")
        self.Button_TP78 = QtWidgets.QPushButton(Form)
        self.Button_TP78.setGeometry(QtCore.QRect(10, 10, 246, 146))
        font = QtGui.QFont()
        font.setFamily("小赖字体 SC")
        self.Button_TP78.setFont(font)
        self.Button_TP78.setStyleSheet("image: url(:/res/TP78.png);")
        self.Button_TP78.setObjectName("Button_TP78")
        self.Button_TP78MINI = QtWidgets.QPushButton(Form)
        self.Button_TP78MINI.setGeometry(QtCore.QRect(510, 10, 246, 146))
        font = QtGui.QFont()
        font.setFamily("小赖字体 SC")
        self.Button_TP78MINI.setFont(font)
        self.Button_TP78MINI.setStyleSheet("image: url(:/res/TP78mini.png);")
        self.Button_TP78MINI.setObjectName("Button_TP78MINI")
        self.Button_MagnetAxis = QtWidgets.QPushButton(Form)
        self.Button_MagnetAxis.setGeometry(QtCore.QRect(260, 160, 246, 146))
        font = QtGui.QFont()
        font.setFamily("小赖字体 SC")
        self.Button_MagnetAxis.setFont(font)
        self.Button_MagnetAxis.setStyleSheet("image: url(:/res/磁轴工具.png);")
        self.Button_MagnetAxis.setObjectName("Button_MagnetAxis")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TP78集成工具v1.0"))
        self.Button_TP78FOC.setText(_translate("Form", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"TP78foc固件升级工具"))
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
        self.Button_TP78.setText(_translate("Form", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"TP78主键盘 U盘模式配置工具"))
        self.Button_TP78MINI.setText(_translate("Form", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"TP78mini U盘模式配置工具"))
        self.Button_MagnetAxis.setText(_translate("Form", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"TP78系列磁轴设置工具"))
import image_rc

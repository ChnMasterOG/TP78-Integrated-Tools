# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Project\TP78 Integrated Tools\tp78foc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 317)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.selected_firmware_path_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("小赖字体 SC")
        font.setPointSize(12)
        self.selected_firmware_path_label.setFont(font)
        self.selected_firmware_path_label.setObjectName("selected_firmware_path_label")
        self.verticalLayout_3.addWidget(self.selected_firmware_path_label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_selectfirmware = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("小赖字体 SC")
        self.Button_selectfirmware.setFont(font)
        self.Button_selectfirmware.setStyleSheet("image: url(:/res/选择固件.png);")
        self.Button_selectfirmware.setObjectName("Button_selectfirmware")
        self.horizontalLayout.addWidget(self.Button_selectfirmware)
        self.Button_update = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("小赖字体 SC")
        self.Button_update.setFont(font)
        self.Button_update.setStyleSheet("image: url(:/res/更新固件.png)")
        self.Button_update.setObjectName("Button_update")
        self.horizontalLayout.addWidget(self.Button_update)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TP78FOC固件升级工具v1.0"))
        self.label.setText(_translate("Form", "**TP78 FOC固件更新**"))
        self.selected_firmware_path_label.setText(_translate("Form", "固件路径："))
        self.Button_selectfirmware.setText(_translate("Form", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"选择固件"))
        self.Button_update.setText(_translate("Form", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"更新固件"))
import image_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Project\TP78 Integrated Tools\news.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 703)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 800, 600))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.note_label = QtWidgets.QLabel(Form)
        self.note_label.setGeometry(QtCore.QRect(10, 610, 801, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.note_label.setFont(font)
        self.note_label.setObjectName("note_label")
        self.close_button = QtWidgets.QPushButton(Form)
        self.close_button.setGeometry(QtCore.QRect(730, 670, 75, 23))
        self.close_button.setObjectName("close_button")
        self.next_button = QtWidgets.QPushButton(Form)
        self.next_button.setGeometry(QtCore.QRect(650, 670, 75, 23))
        self.next_button.setObjectName("next_button")
        self.download_button = QtWidgets.QPushButton(Form)
        self.download_button.setGeometry(QtCore.QRect(570, 670, 75, 23))
        self.download_button.setObjectName("download_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "News"))
        self.note_label.setText(_translate("Form", "Note:"))
        self.close_button.setText(_translate("Form", "我知道了"))
        self.next_button.setText(_translate("Form", "下一条"))
        self.download_button.setText(_translate("Form", "更新版本"))

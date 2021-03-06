# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PerArea(object):
    def setupUi(self, PerArea):
        PerArea.setObjectName("PerArea")
        PerArea.resize(321, 345)
        PerArea.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.pict = QtWidgets.QLabel(PerArea)
        self.pict.setGeometry(QtCore.QRect(120, 10, 81, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.pict.setFont(font)
        self.pict.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.pict.setText("")
        self.pict.setObjectName("pict")
        self.name = QtWidgets.QLabel(PerArea)
        self.name.setGeometry(QtCore.QRect(130, 120, 55, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(255, 255, 255);")
        self.name.setText("")
        self.name.setObjectName("name")
        self.rest_hist = QtWidgets.QPushButton(PerArea)
        self.rest_hist.setGeometry(QtCore.QRect(10, 180, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.rest_hist.setFont(font)
        self.rest_hist.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.373134 rgba(62, 188, 255, 255), stop:0.985075 rgba(0, 0, 255, 255));")
        self.rest_hist.setObjectName("rest_hist")
        self.cin_hist = QtWidgets.QPushButton(PerArea)
        self.cin_hist.setGeometry(QtCore.QRect(10, 230, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.cin_hist.setFont(font)
        self.cin_hist.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.373134 rgba(62, 188, 255, 255), stop:0.985075 rgba(0, 0, 255, 255));")
        self.cin_hist.setObjectName("cin_hist")
        self.edit_profile = QtWidgets.QPushButton(PerArea)
        self.edit_profile.setGeometry(QtCore.QRect(10, 280, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.edit_profile.setFont(font)
        self.edit_profile.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.373134 rgba(62, 188, 255, 255), stop:0.985075 rgba(0, 0, 255, 255));")
        self.edit_profile.setObjectName("edit_profile")

        self.retranslateUi(PerArea)
        QtCore.QMetaObject.connectSlotsByName(PerArea)

    def retranslateUi(self, PerArea):
        _translate = QtCore.QCoreApplication.translate
        PerArea.setWindowTitle(_translate("PerArea", "???????????? ??????????????"))
        self.rest_hist.setText(_translate("PerArea", "?????????????????????? ?????????????? ??????????????"))
        self.cin_hist.setText(_translate("PerArea", "?????????????????????? ?????????????? ??????????????????\n"
"????????"))
        self.edit_profile.setText(_translate("PerArea", "?????????????????????????? ??????????????"))

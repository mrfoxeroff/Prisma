# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'full_rest_hist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FullRestHist(object):
    def setupUi(self, FullRestHist):
        FullRestHist.setObjectName("FullRestHist")
        FullRestHist.resize(547, 530)
        FullRestHist.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.menu = QtWidgets.QTableWidget(FullRestHist)
        self.menu.setGeometry(QtCore.QRect(10, 10, 531, 511))
        self.menu.setMaximumSize(QtCore.QSize(531, 511))
        self.menu.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.menu.setObjectName("menu")
        self.menu.setColumnCount(3)
        self.menu.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        item.setFont(font)
        self.menu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        item.setFont(font)
        self.menu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        item.setFont(font)
        self.menu.setHorizontalHeaderItem(2, item)

        self.retranslateUi(FullRestHist)
        QtCore.QMetaObject.connectSlotsByName(FullRestHist)

    def retranslateUi(self, FullRestHist):
        _translate = QtCore.QCoreApplication.translate
        FullRestHist.setWindowTitle(_translate("FullRestHist", "История заказов"))
        item = self.menu.horizontalHeaderItem(0)
        item.setText(_translate("FullRestHist", "Имя"))
        item = self.menu.horizontalHeaderItem(1)
        item.setText(_translate("FullRestHist", "Заказ"))
        item = self.menu.horizontalHeaderItem(2)
        item.setText(_translate("FullRestHist", "Цена заказа"))

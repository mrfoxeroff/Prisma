# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prisma.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1300, 800)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.prisma_label = QtWidgets.QLabel(self.centralwidget)
        self.prisma_label.setGeometry(QtCore.QRect(210, 30, 891, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.prisma_label.setFont(font)
        self.prisma_label.setStyleSheet("color: rgb(255, 253, 251);")
        self.prisma_label.setObjectName("prisma_label")
        self.per_area = QtWidgets.QRadioButton(self.centralwidget)
        self.per_area.setGeometry(QtCore.QRect(40, 170, 449, 66))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(25)
        self.per_area.setFont(font)
        self.per_area.setStyleSheet("color: rgb(255, 253, 251);")
        self.per_area.setObjectName("per_area")
        self.service = QtWidgets.QRadioButton(self.centralwidget)
        self.service.setGeometry(QtCore.QRect(40, 380, 449, 66))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(30)
        self.service.setFont(font)
        self.service.setStyleSheet("color: rgb(255, 253, 251);")
        self.service.setObjectName("service")
        self.info = QtWidgets.QRadioButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(40, 570, 449, 66))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(30)
        self.info.setFont(font)
        self.info.setStyleSheet("color: rgb(255, 253, 251);")
        self.info.setObjectName("info")
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(570, 150, 771, 121))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(16)
        self.name_2.setFont(font)
        self.name_2.setStyleSheet("color: rgb(255, 253, 251);")
        self.name_2.setObjectName("name_2")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(610, 270, 531, 181))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(255, 253, 251);")
        self.name.setObjectName("name")
        self.target = QtWidgets.QLabel(self.centralwidget)
        self.target.setGeometry(QtCore.QRect(460, 430, 811, 121))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        self.target.setFont(font)
        self.target.setStyleSheet("color: rgb(255, 253, 251);")
        self.target.setObjectName("target")
        self.asking = QtWidgets.QLabel(self.centralwidget)
        self.asking.setGeometry(QtCore.QRect(400, 580, 951, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(13)
        self.asking.setFont(font)
        self.asking.setStyleSheet("color: rgb(255, 253, 251);")
        self.asking.setObjectName("asking")
        self.cinema = QtWidgets.QPushButton(self.centralwidget)
        self.cinema.setGeometry(QtCore.QRect(930, 180, 311, 401))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(20)
        self.cinema.setFont(font)
        self.cinema.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.373134 rgba(62, 188, 255, 255), stop:0.985075 rgba(0, 0, 255, 255));")
        self.cinema.setObjectName("cinema")
        self.registr = QtWidgets.QPushButton(self.centralwidget)
        self.registr.setGeometry(QtCore.QRect(600, 280, 571, 151))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        self.registr.setFont(font)
        self.registr.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.373134 rgba(62, 188, 255, 255), stop:0.985075 rgba(0, 0, 255, 255));")
        self.registr.setObjectName("registr")
        self.restaurant = QtWidgets.QPushButton(self.centralwidget)
        self.restaurant.setGeometry(QtCore.QRect(570, 180, 311, 401))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(20)
        self.restaurant.setFont(font)
        self.restaurant.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.373134 rgba(62, 188, 255, 255), stop:0.985075 rgba(0, 0, 255, 255));")
        self.restaurant.setObjectName("restaurant")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(770, 170, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.373134 rgba(62, 188, 255, 255), stop:0.985075 rgba(0, 0, 255, 255));")
        self.login.setObjectName("login")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(10, 0, 531, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.user_label.setFont(font)
        self.user_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_label.setObjectName("user_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????"))
        self.prisma_label.setText(_translate("MainWindow", "?????????????????? \"????????????\""))
        self.per_area.setText(_translate("MainWindow", "???????????? ??????????????"))
        self.service.setText(_translate("MainWindow", "???????? ????????????"))
        self.info.setText(_translate("MainWindow", "????????"))
        self.name_2.setText(_translate("MainWindow", "?????????????????? ???????????? ?????????????? 9 ?? ????????????\n"
"                                         ??\n"
"               ?????????? ???????????????? ??????????????"))
        self.name.setText(_translate("MainWindow", "???????????????? ????????????"))
        self.target.setText(_translate("MainWindow", "???????????? ?????????????????? ?????????????????????????? ?????? ???????????? ?????? ???? ??????????????????\n"
"              ?? ?????????????? ?????????????? ?? ???????? ?? ???????????????????? \"????????????\""))
        self.asking.setText(_translate("MainWindow", "???? ???????? ???????????? ???????????? ???? ?????????????????????? ??????????: prismacinema33@gmail.com"))
        self.cinema.setText(_translate("MainWindow", "??????????????????"))
        self.registr.setText(_translate("MainWindow", "????????????????????????????????????"))
        self.restaurant.setText(_translate("MainWindow", "????????????????"))
        self.login.setText(_translate("MainWindow", "??????????"))
        self.user_label.setText(_translate("MainWindow", "????????????????????????:"))

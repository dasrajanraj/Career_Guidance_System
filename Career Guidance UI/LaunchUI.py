# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetStarted.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from Instructions import Ui_Instructions
from RegisterUI import Ui_Register
from QuestionsUI import Ui_Questions

class Ui_FirstPage(object):
    def setupUi(self, FirstPage):
        self.run = QTimer()
        self.run.setInterval(200)
        self.run.timeout.connect(self.checkstatus)
        self.run.start()
        FirstPage.setObjectName("FirstPage")
        FirstPage.setEnabled(True)
        FirstPage.resize(1360, 710)
        FirstPage.setStyleSheet("background-color: black")
        #FirstPage.setFixedSize(QtCore.QSize(1360,710))
        layout = QGridLayout()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        FirstPage.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(FirstPage)
        self.label.setGeometry(QtCore.QRect(300, 2, 800, 690))
        self.label.setText("")
        self.mngif=QMovie("Images/Career Guidance3.gif")
        self.label.setMovie(self.mngif)
        self.mngif.start()
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FirstPage)
        self.pushButton.setGeometry(QtCore.QRect(650, 580, 121, 41))
        self.pushButton.setStyleSheet("*{\n"
        "color: rgb(0, 0, 127);\n"
"font: 13pt \"Times New Roman\";\n"
"border-radius: 15px;\n"
"background-color: white;\n"
"}\n"
"*:hover{\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.register)
        self.label_2 = QtWidgets.QLabel(FirstPage)
        self.label_2.setGeometry(QtCore.QRect(458, 10, 461, 51))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        #font.setFamily("MV Boli")
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(FirstPage)
        QtCore.QMetaObject.connectSlotsByName(FirstPage)
        FirstPage.setLayout(layout)
    def checkstatus(self):
        if Ui_Register.Registered==1:
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Instructions()
            self.User_details=[Ui_Register.name_reg,Ui_Register.email_reg]
            self.ui.setupUi(self.window)
            self.window.show()
            Ui_Register.Registered=0
        if Ui_Instructions.taketest==1:
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Questions()
            self.ui.setupUi(self.window,self.User_details)
            self.window.show()
            Ui_Instructions.taketest=0
            
    def register(self):
        print("Button pressed")
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window)
        FirstPage.hide()
        self.window.show()

    def retranslateUi(self, FirstPage):
        _translate = QtCore.QCoreApplication.translate
        FirstPage.setWindowTitle(_translate("FirstPage", "Welcome-CareerGuidance"))
        self.pushButton.setText(_translate("FirstPage", "Get Started"))
        self.label_2.setText(_translate("FirstPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:white;\">Career Analysis and Guidance</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstPage = QtWidgets.QWidget()
    ui = Ui_FirstPage()
    ui.setupUi(FirstPage)
    FirstPage.show()
    sys.exit(app.exec_())


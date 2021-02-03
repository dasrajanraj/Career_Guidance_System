# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox

from Instructions import Ui_Instructions

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(1360,710)
        #Register.setFixedSize(QtCore.QSize(1360,710))
        self.groupBox = QtWidgets.QGroupBox(Register)
        self.groupBox.setGeometry(QtCore.QRect(200, 250, 571, 361))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Register.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:rgb(0, 170, 0);\n"
"border-color: rgb(255, 170, 0);\n"
"font: 11pt \"MV Boli\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(130, 40, 341, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 131, 22))
        self.lineEdit.setToolTip("")
        self.lineEdit.setPlaceholderText("FirstName")
        self.lineEdit.setStyleSheet("font: 8pt \"MV Boli\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 90, 131, 22))
        self.lineEdit_2.setToolTip("")
        self.lineEdit_2.setPlaceholderText("SecondName")
        self.lineEdit_2.setStyleSheet("font: 8pt \"MV Boli\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 150, 181, 22))
        self.lineEdit_3.setToolTip("")
        self.lineEdit_3.setPlaceholderText("Enter Email ID")
        self.lineEdit_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 8pt \"MV Boli\";")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.validate)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 190, 181, 22))
        self.lineEdit_5.setToolTip("")
        self.lineEdit_5.setPlaceholderText("Re-enter Email ID")
        self.lineEdit_5.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 8pt \"MV Boli\";")
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(Register)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 591, 251))
        self.label_5.setText("")
        self.gif2=QMovie("Images/Career Guidance2.gif")
        self.label_5.setMovie(self.gif2)
        self.gif2.start()
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)
    
    def validate(self):
        firstname=self.lineEdit.text()
        secondname=self.lineEdit_2.text()
        email1=self.lineEdit_3.text()
        email2=self.lineEdit_5.text()
        print(firstname,secondname,email1,email2)
        if len(firstname)<1:
            QMessageBox.information(None,'Warning!!','Firstname not entered, Enter FirstName')
        elif (len(secondname)<1):
            QMessageBox.information(None,'Warning!!','Secondname not entered, Enter SecondName')
        elif (len(email1)<1 or len(email2)<1):
            QMessageBox.information(None,'Warning!!','Email ID not entered, Enter Email ID')
        elif not('@' in email1):
            QMessageBox.information(None,'Warning!!','Invalid Email ID')
        elif not(email1 == email2):
            QMessageBox.information(None,'Warning!!','Email IDs not matching, Enter Correct EmailID')
        else:
            QMessageBox.information(None,'Successfully Registered','Lets Proceed with a Test!!')
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Instructions()
            self.ui.setupUi(self.window)
            Register.hide()
            self.window.show()

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.groupBox.setTitle(_translate("Register", "Enter Details"))
        self.label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" color:#00007f;\">First Name:</span></p></body></html>"))
        self.label_2.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" color:#00007f;\">Second Name:</span></p></body></html>"))
        self.label_3.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" color:#00007f;\">Email ID:</span></p></body></html>"))
        self.label_4.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" color:#00007f;\">Email ID:</span></p></body></html>"))
        self.pushButton.setText(_translate("Register", "Proceed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QWidget()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())


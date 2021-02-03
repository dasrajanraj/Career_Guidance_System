# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Instructions.ui'
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

class Ui_Instructions(object):
    taketest=0
    def setupUi(self, Instructions):
        Instructions.setObjectName("Instructions")
        Instructions.resize(1360, 710)
        #Instructions.setStyleSheet("background-image: url(Images/instPic.jpeg);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Instructions.setWindowIcon(icon)
        #self.label = QtWidgets.QLabel(Instructions)
        #self.label.setGeometry(QtCore.QRect(365, 0, 590, 640))
        #self.label.setText("")
        #self.gif3=QMovie("Images/steps3.gif")
        #self.label.setMovie(self.gif3)
        #self.gif3.start()
        #self.label.setScaledContents(True)
        #self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Instructions)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 270, 551, 151))
        self.groupBox_2.setStyleSheet("font: 15pt \"MV Boli\";\n"
"color: rgb(255,255,255);")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 491, 101))
        self.label_4.setStyleSheet("color:rgb(128, 191, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(Instructions)
        self.groupBox.setGeometry(QtCore.QRect(390, 90, 551, 151))
        self.groupBox.setStyleSheet("font: 15pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 491, 101))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(Instructions)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 440, 551, 151))
        self.groupBox_3.setStyleSheet("font: 15pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 491, 101))
        self.label_5.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Instructions)
        self.label_2.setGeometry(QtCore.QRect(400, 30, 551, 51))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Instructions)
        self.pushButton.setGeometry(QtCore.QRect(540, 610, 231, 31))
        self.pushButton.setStyleSheet("color:rgb(0, 255, 0);\n"
"font: 75 10pt \"MV Boli\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.test)

        self.retranslateUi(Instructions)
        QtCore.QMetaObject.connectSlotsByName(Instructions)
    
    def test(self):
        Ui_Instructions.taketest=1


    def retranslateUi(self, Instructions):
        _translate = QtCore.QCoreApplication.translate
        Instructions.setWindowTitle(_translate("Instructions", "Instructions"))
        Instructions.setStyleSheet("background-image: url(Images/instPic.jpeg);")
        self.groupBox_2.setTitle(_translate("Instructions", "Step 2"))
        self.label_4.setText(_translate("Instructions", "<html><head/><body><p align=\"center\"><span style=\"font-weight:bold; color:rgb(128, 191, 255);\">Second round, we would be gathering your interest on various profession based on your social account (Twitter account) </span></p></body></html>"))
        self.groupBox.setTitle(_translate("Instructions", "Step 1"))
        self.label_3.setText(_translate("Instructions", "<html><head/><body><p align=\"center\"><span style=\"font-weight:bold; color:rgb(128, 191, 255);\">First round, we would be gathering the technical knowledge on various fields such as Mathematics, English, Medicine, Aviation, Law, Theater, Politics..etc.</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("Instructions", "Step 3"))
        self.label_5.setText(_translate("Instructions", "<html><head/><body><p align=\"center\"><span style=\"font-weight:bold; color:rgb(128, 191, 255);\">Finally, we would be needing the personality which likely you belong to</span></p></body></html>"))
        self.label_2.setText(_translate("Instructions", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffff00; font-weight:bold;\">Way of Approach</span></p></body></html>"))
        self.pushButton.setText(_translate("Instructions", "Take Test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Instructions = QtWidgets.QWidget()
    ui = Ui_Instructions()
    ui.setupUi(Instructions)
    Instructions.show()
    sys.exit(app.exec_())


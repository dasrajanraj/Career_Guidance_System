# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddonPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(590, 640)
        self.button="Choose"
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 590, 640))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/back.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 50, 151, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Logo_t.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 440, 281, 41))
        self.label_3.setStyleSheet("font: 10pt \"MV Boli\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(260, 490, 73, 31))
        self.comboBox.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color:rgb(235, 235, 235);\n"
"font: 8pt \"MV Boli\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['No','Yes'])
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 580, 71, 31))
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(57, 100, 255);\n"
"font: 10pt \"MV Boli\";\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(180, 190, 261, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.hide()
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(-10, 20, 281, 41))
        self.label_4.setStyleSheet("font: 10pt \"MV Boli\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 231, 41))
        self.lineEdit.setStyleSheet("border-radius:20px;\n"
"color: rgb(55, 15, 255);\n"
"font: 8pt \"MV Boli\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton.clicked.connect(self.check)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def check(self):
        ans=self.comboBox.currentText()
        if self.button=="Choose" and ans=='Yes':
            self.frame.show()
            self.button="Next"
            self.pushButton.setText("Next")
        elif self.button=="Next" and ans=='Yes':
            twitterid=self.lineEdit.text()
            print(twitterid)
            
        elif ans=='No':
            print("Next Page")    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Do you have a twitter account?"))
        self.pushButton.setText(_translate("Form", "Choose"))
        self.label_4.setText(_translate("Form", "Enter Your Twitter ID"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Twitter ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


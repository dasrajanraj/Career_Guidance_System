# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionsUI.ui'
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
from PyQt5.QtGui import QImage, QPalette, QBrush
from selenium import webdriver
import pandas
import numpy as np
from time import sleep
from readcsv import Get_career
import csv

class Ui_Questions(object):
    travel_df = pandas.read_excel('QuestionsDB.xlsx')
    content = travel_df.to_dict()
    #fetch db info
    questcareerlist=list(content['Career'].values())
    questionlist=list(content['Questions'].values())
    optionAlist=list(content['OptionA'].values())
    optionBlist=list(content['OptionB'].values())
    optionClist=list(content['OptionC'].values())
    optionDlist=list(content['OptionD'].values())
    currect_ans_list=list(content['Correct Ans'].values())
    avbl_careers=[]
    for i in questcareerlist:
        if i not in avbl_careers:
            avbl_careers.append(i)
    scores=[0]*len(avbl_careers)
    print(scores)
    print(avbl_careers)
    res={}
    def setupUi(self, Questions,User_details):
        self.User_details=User_details
        self.Questions=Questions
        self.qindex=0
        self.final_result=['Null','Null']
        self.len=len(Ui_Questions.avbl_careers)
        Ui_Questions.res={Ui_Questions.avbl_careers[i]: Ui_Questions.scores[i] for i in range(len(Ui_Questions.avbl_careers))}
        print(Ui_Questions.res)
        self.Questions.setObjectName("Questions")
        self.Questions.resize(1360, 710)
        #self.Questions.setFixedSize(QtCore.QSize(590,640))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Questions.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(self.Questions)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1360, 710))
        #self.label_2.setGeometry(QtCore.QRect(380, 0, 600, 700))
        #self.label_2.setStyleSheet("selection-background-color: rgba(255, 255, 255, 50);")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gif4=QMovie("Images/QuestionBack.jpg")
        self.label_2.setMovie(self.gif4)
        self.gif4.start()
        self.label = QtWidgets.QLabel(self.Questions)
        self.label.setGeometry(QtCore.QRect(400, 28, 551, 61))
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(45)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.Questions)
        self.groupBox.setGeometry(QtCore.QRect(365, 110, 650, 431))
        self.groupBox.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 12pt \"MV Boli\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(75, 40, 471, 161))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: transparent;\n"
"font: 12pt \"MV Boli\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(75, 244, 471, 181))
        self.frame.setStyleSheet("background-color: rgba(239, 239, 239,0.1);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(180, 24, 231, 20))
        self.checkBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75  10pt \"MV Boli\";")
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.onlyA)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 60, 231, 20))
        self.checkBox_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75  10pt \"MV Boli\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.onlyB)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(180, 100, 231, 20))
        self.checkBox_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75  10pt \"MV Boli\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.stateChanged.connect(self.onlyC)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(180, 140, 231, 20))
        self.checkBox_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75  10pt \"MV Boli\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.stateChanged.connect(self.onlyD)
        self.pushButton = QtWidgets.QPushButton(self.Questions)
        self.pushButton.setGeometry(QtCore.QRect(560, 570, 251, 28))
        self.pushButton.setStyleSheet("*{\n"
            "background-color: rgba(24,19,18,0.3);\n"
"color: rgb(247, 247, 247);\n"
"font: 25pt \"MV Boli\";\n"
"}\n"
"*:hover{\n"
"color: rgb(114,19,19);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button)
        
        self.buttonName="Next Question"
        self.retranslateUi(self.Questions)
        QtCore.QMetaObject.connectSlotsByName(self.Questions)
    def button(self):
        optionA=self.checkBox.checkState()
        optionB=self.checkBox_2.checkState()
        optionC=self.checkBox_3.checkState()
        optionD=self.checkBox_4.checkState()
        
        if optionA+optionB+optionC+optionD==2:

            if optionA==2:
                print("A selected")
                selected='A'
            elif optionB==2:
                print("B selected")
                selected='B'
            elif optionC==2:
                print("C selected")
                selected='C'
            elif optionD==2:
                print("D selected")
                selected='D'
            else:
                QMessageBox.information(None,'Warning!!','No Option selected , Select Any One Option')
            #print(Ui_Questions.currect_ans_list[self.qindex])
            #print(selected)
            if(selected==Ui_Questions.currect_ans_list[self.qindex]):
                Ui_Questions.res[Ui_Questions.questcareerlist[self.qindex]]+=1
                #print(Ui_Questions.res)
            print(Ui_Questions.res)
            #print(list(Ui_Questions.res.keys()))
            res_value=list(Ui_Questions.res.values())
            print(res_value)
            res_value=res_value[::-1]
            print(res_value)
            s = np.array(res_value) 
            sort_index = list(s.argsort())[::-1]
            print(sort_index)
            if res_value[sort_index[0]]>3:
                self.final_result[0]=Ui_Questions.avbl_careers[sort_index[0]]
            if res_value[sort_index[1]]>3:
                self.final_result[1]=Ui_Questions.avbl_careers[15-sort_index[1]]

            print(self.final_result)
            if(self.buttonName=='Next Question'):
                self.qindex+=1
            else:
                QMessageBox.information(None,'Results!!',str(self.final_result))
                self.Step2(self.final_result)

            print('No. of questions left:: ',str(len(Ui_Questions.questionlist)-self.qindex))
            if(self.qindex==len(Ui_Questions.questionlist)-1):
                self.buttonName='Get Result'
            #self.retranslateUi(Questions)
            self.label.setText(self._translate("Questions", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:650; color: rgb(102, 255, 179);\">Question Related To-"+str(Ui_Questions.questcareerlist[self.qindex])+"</span></p><p align=\"center\"><br/></p></body></html>"))
            self.groupBox.setTitle(self._translate("Questions", "Question"))
            self.label_3.setText(self._translate("Questions", Ui_Questions.questionlist[self.qindex]))
            self.checkBox.setText(self._translate("Questions", str(Ui_Questions.optionAlist[self.qindex])))
            self.checkBox_2.setText(self._translate("Questions", str(Ui_Questions.optionBlist[self.qindex])))
            self.checkBox_3.setText(self._translate("Questions", str(Ui_Questions.optionClist[self.qindex])))
            self.checkBox_4.setText(self._translate("Questions", str(Ui_Questions.optionDlist[self.qindex])))
            self.pushButton.setText(self._translate("Questions", str(self.buttonName)))
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setChecked(False)

        else:
            QMessageBox.information(None,'Warning!!','No Option selected , Select Any One Option')

        #print(optionA,optionB,optionC,optionD)
        
        
    def Step2(self,Step1_res):
            self.Step2_window = QtWidgets.QWidget()
            self.ui = Step2_Action_Window()
            self.ui.setupUi(self.Step2_window,self.final_result,self.User_details)
            self.Questions.hide()
            self.Step2_window.show()
            self.Questions.close()


    def onlyA(self,state):
        if(state==QtCore.Qt.Checked):
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setChecked(False)
    
    def onlyB(self,state):
        if(state==QtCore.Qt.Checked):
            self.checkBox.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setChecked(False)
    
    def onlyC(self,state):
        if(state==QtCore.Qt.Checked):
            self.checkBox_2.setChecked(False)
            self.checkBox.setChecked(False)
            self.checkBox_4.setChecked(False)
    
    def onlyD(self,state):
        if(state==QtCore.Qt.Checked):
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox.setChecked(False)


    def retranslateUi(self, Questions):
        self._translate = QtCore.QCoreApplication.translate
        Questions.setWindowTitle(self._translate("Questions", "Test"))
        self.label.setText(self._translate("Questions", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:650; color: rgb(102, 255, 179);\">Question Related To-"+str(Ui_Questions.questcareerlist[self.qindex])+"</span></p><p align=\"center\"><br/></p></body></html>"))
        self.groupBox.setTitle(self._translate("Questions", "Question"))
        self.label_3.setText(self._translate("Questions", Ui_Questions.questionlist[self.qindex]))
        self.checkBox.setText(self._translate("Questions", str(Ui_Questions.optionAlist[self.qindex])))
        self.checkBox_2.setText(self._translate("Questions", str(Ui_Questions.optionBlist[self.qindex])))
        self.checkBox_3.setText(self._translate("Questions", str(Ui_Questions.optionClist[self.qindex])))
        self.checkBox_4.setText(self._translate("Questions", str(Ui_Questions.optionDlist[self.qindex])))
        self.pushButton.setText(self._translate("Questions", str(self.buttonName)))


class Step2_Action_Window(object):

    def setupUi(self,Form,final_result_1,User_details):
        self.User_details=User_details
        self.final_result_1=final_result_1
        self.Form=Form
        self.Form.setObjectName("Form")
        self.Form.resize(1360, 710)
        self.button="Choose"
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1360, 715))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/back.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Form)
        self.label_2.setGeometry(QtCore.QRect(600, 50, 151, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Logo_t.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Form)
        self.label_3.setGeometry(QtCore.QRect(550, 440, 281, 41))
        self.label_3.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.Form)
        self.comboBox.setGeometry(QtCore.QRect(640, 490, 73, 31))
        self.comboBox.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color:rgb(235, 235, 235);\n"
"font: 10pt \"MV Boli\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['No','Yes'])
        self.pushButton = QtWidgets.QPushButton(self.Form)
        self.pushButton.setGeometry(QtCore.QRect(640, 580, 71, 31))
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(57, 100, 255);\n"
"font: 10pt \"MV Boli\";\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.Form)
        self.frame.setGeometry(QtCore.QRect(550, 190, 261, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.hide()
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(-10, 20, 281, 41))
        self.label_4.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 231, 41))
        self.lineEdit.setStyleSheet("border-radius:20px;\n"
"color: rgb(55, 15, 255);\n"
"font: 8pt \"MV Boli\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton.clicked.connect(self.check)

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        
    def check(self):
        ans=self.comboBox.currentText()
        if self.button=="Choose" and ans=='Yes':
            self.frame.show()
            self.button="Next"
            self.pushButton.setText("Next")
        
        elif self.button=="Choose" and ans=='No':
            self.nextPage()
        
        elif self.button=="Next" and ans=='Yes':
            twitterid=self.lineEdit.text()
            print(twitterid)
            self.predict_followed_occupation()
            
        elif ans=='No':
            print("Next Page")   

    def nextPage(self):
        self.final_result_2=['Null','Null']
        self.Step3_window = QtWidgets.QWidget()
        self.ui = Step3_Action_Window()
        self.ui.setupUi(self.Step3_window,self.final_result_1,self.final_result_2,self.User_details)
        self.Form.hide()
        self.Step3_window.show()
        self.Form.close()

    def predict_followed_occupation(self):
        self.final_result_2=['sports','actor']
        self.Step3_window = QtWidgets.QWidget()
        self.ui = Step3_Action_Window()
        self.ui.setupUi(self.Step3_window,self.final_result_1,self.final_result_2,self.User_details)
        self.Form.hide()
        self.Step3_window.show()
        self.Form.close()


    def retranslateUi(self,Form):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Do you have a twitter account?"))
        self.pushButton.setText(_translate("Form", "Choose"))
        self.label_4.setText(_translate("Form", "Enter Your Twitter ID"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Eg: narendramodi"))


class Step3_Action_Window(object):

    def setupUi(self, Form,final_result_1,final_result_2,User_details):
        self.User_details=User_details
        self.final_result_1=final_result_1
        self.final_result_2=final_result_2
        self.Form=Form
        self.Form.setObjectName("Form")
        self.Form.resize(1360, 710)
        self.Form.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.button="Choose"
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(0, 140, 1360, 560))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/P_bck.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1360, 300))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Personality.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Form)
        self.label_3.setGeometry(QtCore.QRect(380, 300, 580, 40))
        self.label_3.setStyleSheet("font: 14pt \"MV Boli\";\n"
        "background-color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.Form)
        self.comboBox.setGeometry(QtCore.QRect(625, 400, 85, 31))
        self.comboBox.setStyleSheet("QComboBox::hover"
                                     "{"
                                     "background-color: rgb(126,126,126);\n"
                                     "}") 

        '''
        self.comboBox.setStyleSheet("background-color: rgb(126,126,126);\n"
"color:rgb(17,17,17);\n"
"background-color: transparent;\n"
"font: 8pt \"MV Boli\";")
        '''
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['No','Yes'])

        self.comboBox2 = QtWidgets.QComboBox(self.Form)
        self.comboBox2.setGeometry(QtCore.QRect(625, 400, 100, 31))
        self.comboBox2.setStyleSheet("QComboBox::hover"
                                     "{"
                                     "background-color: rgb(126,126,126);\n"
                                     "}") 

        '''
        self.comboBox.setStyleSheet("background-color: rgb(126,126,126);\n"
"color:rgb(17,17,17);\n"
"background-color: transparent;\n"
"font: 8pt \"MV Boli\";")
        '''
        self.comboBox2.setObjectName("comboBox")
        self.comboBox2.addItems(["ISTJ","ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"])
        self.comboBox2.hide()
        self.pushButton = QtWidgets.QPushButton(self.Form)
        self.pushButton.setGeometry(QtCore.QRect(630, 550, 80, 41))
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(76,76,76);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"MV Boli\";\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")        
        self.pushButton.clicked.connect(self.check)

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        
    def check(self):
        ans=self.comboBox.currentText()
        if self.button=="Choose" and ans=='Yes':
            self.label_3.setText("Please choose your Personality")
            self.comboBox.hide()
            self.comboBox2.show()
            self.button="Next"
            self.pushButton.setText("Get Career!")
        
        elif self.button=="Choose" and ans=='No':
            print("Please take up the test!!")
            self.comboBox.hide()
            self.label_3.setText("Please take up your personlity test and then click on done")
            self.button="Test"
            self.pushButton.setText("Done")
            self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
            self.driver.get('https://www.16personalities.com/free-personality-test')
            self.driver.maximize_window()

        elif self.button=="Test" :
            try:
                self.driver.close()
            except:
                print("already closed")
            self.label_3.setText("Please choose your Personality")
            self.comboBox.hide()
            self.comboBox2.show()
            self.button="Next"
            self.pushButton.setText("Get Career")
            
        elif self.button=="Next" :
            self.final_result_3=self.comboBox2.currentText()
            self.Final_Res=[[self.final_result_1[0],self.final_result_2[0],self.final_result_3],[self.final_result_1[0],self.final_result_2[1],self.final_result_3],[self.final_result_1[1],self.final_result_2[0],self.final_result_3],[self.final_result_1[1],self.final_result_2[1],self.final_result_3]]
            print(self.Final_Res)
            self.Final_result_ui = QtWidgets.QWidget()
            self.ui = Result_Page()
            self.ui.setupUi(self.Final_result_ui,self.Final_Res,self.User_details)
            self.Form.hide()
            self.Final_result_ui.show()
            self.Form.close()
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Have you taken the personality test?"))
        self.pushButton.setText(_translate("Form", "Choose"))

class Result_Page(object):
    def setupUi(self, Result_Page,Result_list,User_details):
        self.User_details=User_details
        self.Result_list=Result_list
        self.Result_Page=Result_Page
        self.Result_Page.setObjectName("Result_Page")
        self.Result_Page.resize(1360, 710)
        self.groupBox = QtWidgets.QGroupBox(self.Result_Page)
        self.groupBox.setGeometry(QtCore.QRect(380, 280, 591, 415))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Result_Page.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:rgb(0,0,0);\n"
"border-color: rgb(255, 170, 0);\n"
"font: 15pt \"MV Boli\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(0, 0, 570, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 40, 570, 30))
        self.label.setText("The Predicted Careers matching your profile is:")
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(0, 90, 570, 100))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label")
        self.Result_career=Get_career(self.Result_list)
        self.User_details.append(self.Result_career)
        print(self.User_details)
        DB_flectched=[self.User_details]
        print(DB_flectched)
        with open('User_DB_Career.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(DB_flectched)
        self.result_string="\n".join(self.Result_career)
        self.label2.setText(self.result_string)
        self.label2.setStyleSheet("\n"
"color: red;")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(225, 290, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close_app)
        self.label_5 = QtWidgets.QLabel(self.Result_Page)
        self.label_5.setGeometry(QtCore.QRect(380, 2, 591, 275))
        self.label_5.setText("")
        self.gif2=QMovie("Images/grad_cap.gif")
        self.label_5.setMovie(self.gif2)
        self.gif2.start()
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.retranslateUi(self.Result_Page)



        QtCore.QMetaObject.connectSlotsByName(self.Result_Page)


    
    def close_app(self):
        self.Result_Page.close()
        
            

    def retranslateUi(self, Result_Page):
        _translate = QtCore.QCoreApplication.translate
        Result_Page.setWindowTitle(_translate("Result_Page", "Result_Page"))
        self.groupBox.setTitle(_translate("Result_Page", "FINAL RESULTS"))
        self.pushButton.setText(_translate("Result_Page", "FINISH"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Questions = QtWidgets.QWidget()
    ui = Ui_Questions()
    ui.setupUi(Questions)
    Questions.show()
    sys.exit(app.exec_())


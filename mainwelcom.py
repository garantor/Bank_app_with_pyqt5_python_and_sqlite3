# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MainLogin import Ui_LoginWindow
from registrationNew import Ui_registrationPage
import sqlite3


#############################################
## Connecting and creating Sqlit database ###
##############################################


dbb = sqlite3.connect('BankNH.db')

def CreateDbb():
    dbb.execute(''' CREATE TABLE IF NOT EXISTS NEWBANK(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME CHAR(20) NOT NULL,
    FIRSTNAME STR NOT NULL,
    LASTNAME STR NOT NULL,
    EMAIL STR NOT NULL,
    PASSWORD STR NOT NULL,
    CONFIRM PASSWORD STR NOT NULL,
    PHONE CHAR(11) NOT NULL,
    SEX STR,
    ADDRESS CHAR(50) NOT NULL);
    ''')
#####################################
##         GUI WELCOME PAGE       ##
#####################################
class Ui_WelcomePage(object):
    def setupUi(self, WelcomePage):
        WelcomePage.setObjectName("WelcomePage")
        WelcomePage.resize(581, 495)
        WelcomePage.setMinimumSize(QtCore.QSize(581, 495))
        self.centralwidget = QtWidgets.QWidget(WelcomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 40, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 100, 241, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_WELCOME_YES = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_WELCOME_YES.setGeometry(QtCore.QRect(170, 190, 93, 28))
        self.pushButton_WELCOME_YES.setObjectName("pushButton_WELCOME_YES")
        self.pushButton_WELCOME_NO = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_WELCOME_NO.setGeometry(QtCore.QRect(300, 190, 93, 28))
        self.pushButton_WELCOME_NO.setObjectName("pushButton_WELCOME_NO")
        self.pushButton_QUIT_WELCOME = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_QUIT_WELCOME.setGeometry(QtCore.QRect(230, 250, 111, 28))
        self.pushButton_QUIT_WELCOME.setStyleSheet("")
        self.pushButton_QUIT_WELCOME.setObjectName("pushButton_QUIT_WELCOME")
        WelcomePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WelcomePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        WelcomePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WelcomePage)
        self.statusbar.setObjectName("statusbar")
        WelcomePage.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(WelcomePage)
        QtCore.QMetaObject.connectSlotsByName(WelcomePage)

        ###################################################
        ####               Connecting buttons          ####
        ###################################################
        self.pushButton_WELCOME_NO.clicked.connect(self.reg)
        self.pushButton_WELCOME_YES.clicked.connect(self.Login)
        self.pushButton_QUIT_WELCOME.clicked.connect(self.Quitprogram)

    def Quitprogram(self):
        exit()


    def Login(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.beginLogin(self.LoginWindow)
        self.LoginWindow.show()
        WelcomePage.close()

    def reg(self):
        self.registrationPage = QtWidgets.QMainWindow()
        self.ui = Ui_registrationPage()
        self.ui.setupUi(self.registrationPage)
        self.registrationPage.show()
        WelcomePage.close()



    def retranslateUi(self, WelcomePage):
        _translate = QtCore.QCoreApplication.translate
        WelcomePage.setWindowTitle(_translate("WelcomePage", "Welcome Page"))
        self.label.setText(_translate("WelcomePage", "WELCOME TO NEW BANK MFB"))
        self.label_2.setText(_translate("WelcomePage", "Do You Have An existing Account? "))
        self.pushButton_WELCOME_YES.setText(_translate("WelcomePage", "YES"))
        self.pushButton_WELCOME_NO.setText(_translate("WelcomePage", "NO"))
        self.pushButton_QUIT_WELCOME.setText(_translate("WelcomePage", "QUIT PROGRAM"))
        self.menuQuit.setTitle(_translate("WelcomePage", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QMainWindow()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())


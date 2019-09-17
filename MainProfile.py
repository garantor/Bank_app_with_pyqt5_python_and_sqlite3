# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_profile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QInputDialog, QLineEdit


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 505)
        MainWindow.setStyleSheet("background-color: rgb(12, 31, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 75 14pt \"Verdana\";\n"
"color: rgb(252, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_coinprice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_coinprice.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_coinprice.setObjectName("pushButton_coinprice")
        self.gridLayout.addWidget(self.pushButton_coinprice, 0, 0, 1, 1)
        self.pushButton_balance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_balance.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_balance.setObjectName("pushButton_balance")
        self.gridLayout.addWidget(self.pushButton_balance, 1, 0, 1, 1)
        self.pushButton_withdrawal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_withdrawal.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_withdrawal.setObjectName("pushButton_withdrawal")
        self.gridLayout.addWidget(self.pushButton_withdrawal, 4, 0, 1, 1)
        self.pushButton_deposit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deposit.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_deposit.setObjectName("pushButton_deposit")
        self.gridLayout.addWidget(self.pushButton_deposit, 3, 0, 1, 1)
        self.pushButton_editprofile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_editprofile.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);\n"
"")
        self.pushButton_editprofile.setObjectName("pushButton_editprofile")
        self.gridLayout.addWidget(self.pushButton_editprofile, 7, 0, 1, 1)
        self.pushButton_deleteAccount = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deleteAccount.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_deleteAccount.setObjectName("pushButton_deleteAccount")
        self.gridLayout.addWidget(self.pushButton_deleteAccount, 9, 0, 1, 1)
        self.pushButton_checkAll = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_checkAll.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_checkAll.setObjectName("pushButton_checkAll")
        self.gridLayout.addWidget(self.pushButton_checkAll, 5, 0, 1, 1)
        self.pushButton_referrals = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_referrals.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_referrals.setObjectName("pushButton_referrals")
        self.gridLayout.addWidget(self.pushButton_referrals, 6, 0, 1, 1)
        self.pushButton_transfer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_transfer.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_transfer.setObjectName("pushButton_transfer")
        self.gridLayout.addWidget(self.pushButton_transfer, 2, 0, 1, 1)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.gridLayout.addWidget(self.pushButton_logout, 10, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #######################################
        #connecting Butttons to the profile functions
        ###############################################

        self.pushButton_balance.clicked.connect(self.CheckBal)
        self.pushButton_transfer.clicked.connect(self.Transfer)
        self.pushButton_deposit.clicked.connect(self.Deposit)
        self.pushButton_withdrawal.clicked.connect(self.Withdrawal)
        self.pushButton_checkAll.clicked.connect(self.CheckAll)
        self.pushButton_referrals.clicked.connect(self.SeeRefferals)
        self.pushButton_editprofile.clicked.connect(self.EditProfile)
        self.pushButton_deleteAccount.clicked.connect(self.DeleteAcc)
        self.pushButton_logout.clicked.connect(self.Logout)

    def CancleNow(self):
        print('working')

# Pop Messages
    def MessagesProfile(self, title, message):
        mssg = QMessageBox()
        mssg.setWindowTitle(title)
        mssg.setIcon(QMessageBox.Warning)
        mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mssg.setText(message)
        mssg.buttonClicked.connect(self.buttonClickeed)
        mssg.exec_()

    def buttonClickeed(self, me):
        if me.text() == QMessageBox.Ok:
            print('quite')
            quit()

    def Logout(self):
        self.MessagesProfile('Quit', 'Will you like to quit?')
        quit()

    def DeleteAcc(self):
        print('DeleteAcc')

    def EditProfile(self):
        print('EditProfile')

    def SeeRefferals(self):
        print('SeeRefferals')

    def CheckAll(self):
        print('CheckAll')

    def Withdrawal(self):
        from withdrawal import Ui_WithdrawalWindow

        self.WithdrawalWindow = QtWidgets.QMainWindow()
        self.ui = Ui_WithdrawalWindow()
        self.ui.setupUi(self.WithdrawalWindow)
        self.WithdrawalWindow.show()

    def Deposit(self):
        from deposit import Ui_DepositWindow
        self.DepositWindow = QtWidgets.QMainWindow()
        self.ui = Ui_DepositWindow()
        self.ui.setupUi(self.DepositWindow)
        self.DepositWindow.show()
    def Transfer(self):
        from Transfer import Ui_TransferWindow
        self.TransferWindow = QtWidgets.QMainWindow()
        self.ui = Ui_TransferWindow()
        self.ui.setupUi(self.TransferWindow)
        self.TransferWindow.show()


    def Passwordmessage(self):
        pmsg = QMessageBox()
        pmsg.setIcon(QMessageBox.Information)
        pmsg.setInformativeText('Please Enter Your Password?')
        pmsg.show()
        pmsg.exec_()

    def initUI(self):
        self.getText()



    def CheckBal(self):
        import sqlite3
        conn = sqlite3.connect('BankNH.db')
        cur = conn.cursor()
        okPressed = QInputDialog.getText(self, "Check Bal", "Please Enter Your Password:", )
        cur.execute("SELECT BAL FROM NEWBANK WHERE USERNAME = ? ", ([str(okPressed)]))
        for d in okPressed:
            print(d, )

        print(okPressed)
        datas = cur.fetchone()
        print(datas)
        if datas == okPressed:
            print('worked')
            # self.Passwordmessage()

        else:
            print('Invalid entry')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOME TO YOUR USER DASHBOARD"))
        self.pushButton_coinprice.setText(_translate("MainWindow", "COIN PRICE TODAY"))
        self.pushButton_balance.setText(_translate("MainWindow", "BALANCE"))
        self.pushButton_withdrawal.setText(_translate("MainWindow", "WITHDRAWAL"))
        self.pushButton_deposit.setText(_translate("MainWindow", "DEPOSIT"))
        self.pushButton_editprofile.setText(_translate("MainWindow", "EDIT PROFILE"))
        self.pushButton_deleteAccount.setText(_translate("MainWindow", "DELETE ACCOUNT"))
        self.pushButton_checkAll.setText(_translate("MainWindow", "CHECK ALL ACCOUNT"))
        self.pushButton_referrals.setText(_translate("MainWindow", "REFERRALS"))
        self.pushButton_transfer.setText(_translate("MainWindow", "TRANSFER"))
        self.pushButton_logout.setText(_translate("MainWindow", "LOG OUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


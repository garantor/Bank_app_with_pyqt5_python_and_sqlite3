# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_profile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QInputDialog, QLineEdit
from MainLogin import Ui_LoginWindow


class Ui_MainWindow(QWidget, Ui_LoginWindow):
    def beginLogin(self, MainWindow):
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

    def DeleteAcc(self):
        print('DeleteAcc')

    def EditProfile(self):
        print('EditProfile')

    def SeeRefferals(self):
        print('SeeRefferals')

    def CheckAll(self):
        print('CheckAll')

    def Withdrawal(self):
        print('Withdrawal')

    def Deposit(self):
        print('Deposit')

    def Transfer(self):
        Ui_TransferWindow.TransferMain(Ui_TransferWindow)


    def Passwordmessage(self):
        pmsg = QMessageBox()
        pmsg.setIcon(QMessageBox.Information)
        pmsg.setInformativeText('Please Enter Your Password?')
        pmsg.show()
        pmsg.exec_()

    def initUI(self):
        self.getText()

    # def CheckBal(self):
    #     import sqlite3
    #     conn = sqlite3.connect('BankNH.db')
    #     cur = conn.cursor()
    #     okPressed = QInputDialog.getText(self, "Check Bal", "Please Enter Your Password:",)
    #     cur.execute("SELECT BAL FROM NEWBANK WHERE USERNAME = ? ", ([str(okPressed)]))
    #     for d in okPressed:
    #         print(d,)
    #
    #     print(okPressed)
    #     datas = cur.fetchone()
    #     print(datas)
    #     if datas == okPressed:
    #         print('worked')
    #         #self.Passwordmessage()
    #
    #     else:
    #         print('Invalid entry')


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



class Ui_TransferWindow(object):
    def setupUi(self, TransferWindow):
        TransferWindow.setObjectName("TransferWindow")
        TransferWindow.resize(567, 352)
        TransferWindow.setStyleSheet("background-color: rgb(12, 31, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(TransferWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 468, 183))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.label_amount2txf = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_amount2txf.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.label_amount2txf.setObjectName("label_amount2txf")
        self.gridLayout.addWidget(self.label_amount2txf, 1, 0, 1, 1)
        self.lineEdit_name2txf = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_name2txf.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_name2txf.setObjectName("lineEdit_name2txf")
        self.gridLayout.addWidget(self.lineEdit_name2txf, 2, 1, 1, 1)
        self.label_name2txf = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_name2txf.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.label_name2txf.setObjectName("label_name2txf")
        self.gridLayout.addWidget(self.label_name2txf, 2, 0, 1, 1)
        self.label_number2txf = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_number2txf.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.label_number2txf.setObjectName("label_number2txf")
        self.gridLayout.addWidget(self.label_number2txf, 3, 0, 1, 1)
        self.comboBox_accountType = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_accountType.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.comboBox_accountType.setObjectName("comboBox_accountType")
        self.comboBox_accountType.addItem("")
        self.comboBox_accountType.addItem("")
        self.comboBox_accountType.addItem("")
        self.gridLayout.addWidget(self.comboBox_accountType, 5, 0, 1, 2)
        self.lineEdit_account2txf = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_account2txf.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_account2txf.setObjectName("lineEdit_account2txf")
        self.gridLayout.addWidget(self.lineEdit_account2txf, 3, 1, 1, 1)
        self.comboBox_bankType = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_bankType.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.comboBox_bankType.setObjectName("comboBox_bankType")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.gridLayout.addWidget(self.comboBox_bankType, 6, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.formLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 1, 1, 1)
        self.lineEdit_amount2txf = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_amount2txf.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_amount2txf.setObjectName("lineEdit_amount2txf")
        self.gridLayout.addWidget(self.lineEdit_amount2txf, 1, 1, 1, 1)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(160, 240, 211, 80))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_transferTransfer = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_transferTransfer.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.pushButton_transferTransfer.setObjectName("pushButton_transferTransfer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_transferTransfer)
        self.pushButton_transferCancle = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_transferCancle.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.pushButton_transferCancle.setObjectName("pushButton_transferCancle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_transferCancle)
        TransferWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TransferWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 26))
        self.menubar.setObjectName("menubar")
        TransferWindow.setMenuBar(self.menubar)

        self.retranslateUi(TransferWindow)
        QtCore.QMetaObject.connectSlotsByName(TransferWindow)
        self.pushButton_transferCancle.clicked.connect(self.CancleTxf)
        self.pushButton_transferTransfer.clicked.connect(self.SendTransfer)



    # def message(self, title, message):
    #     mssg = QMessageBox()
    #     mssg.setWindowTitle(title)
    #     mssg.setIcon(QMessageBox.Warning)
    #     mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     mssg.setText(message)
    #     mssg.exec_()
    #
    #
    # def SendTransfer(self):
    #     import sqlite3
    #     conn = sqlite3.connect("BankNH.db")
    #     cur = conn.cursor()
    #     cur.execute("SELECT FIRSTNAME FROM NEWBANK")
    #     table = cur.fetchall()
    #     print(table)
    #     amount = self.lineEdit_amount2txf.text()
    #     amount2send = int(amount)
    #     name2send = self.lineEdit_name2txf.text()
    #     number2send = self.lineEdit_account2txf.text()
    #     if amount2send != '':
    #         print('amount worked')
    #         if table:
    #             self.message('error sending', 'Please Check the name you are sending to')
    #         else:
    #             print('working')
    #             if number2send !='':
    #                 print('Number fine')
    #     else:
    #         print('Transfer send')
    #
    #
    # def CancleTxf(self):
    #     self.MainWindow = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.beginLogin(MainWindow)
    #     MainWindow.show()
    #     Ui_TransferWindow.TransferWindow.close()


    def TransferMain(self):
        self.TransferWindow = QtWidgets.QMainWindow()
        self.ui = Ui_TransferWindow()
        self.ui.setupUi(self.TransferWindow)
        self.TransferWindow.show()
        MainWindow.close()



    def retranslateUi(self, TransferWindow):
        _translate = QtCore.QCoreApplication.translate
        TransferWindow.setWindowTitle(_translate("TransferWindow", "Transfer"))
        self.label_amount2txf.setText(_translate("TransferWindow", "ENTER AMOUNT TO DEPOSIT"))
        self.label_name2txf.setText(_translate("TransferWindow", "ACCOUNT NAME"))
        self.label_number2txf.setText(_translate("TransferWindow", "ACCOUNT NUMBER"))
        self.comboBox_accountType.setItemText(0, _translate("TransferWindow", "Account Type"))
        self.comboBox_accountType.setItemText(1, _translate("TransferWindow", "SAVINGS"))
        self.comboBox_accountType.setItemText(2, _translate("TransferWindow", "CURRENT"))
        self.comboBox_bankType.setItemText(0, _translate("TransferWindow", "Choose Bank Name Below"))
        self.comboBox_bankType.setItemText(1, _translate("TransferWindow", "FirstBank"))
        self.comboBox_bankType.setItemText(2, _translate("TransferWindow", "GTB"))
        self.comboBox_bankType.setItemText(3, _translate("TransferWindow", "STABIC"))
        self.comboBox_bankType.setItemText(4, _translate("TransferWindow", "POLARIS"))
        self.comboBox_bankType.setItemText(5, _translate("TransferWindow", "FCMB"))
        self.comboBox_bankType.setItemText(6, _translate("TransferWindow", "ACCESS"))
        self.comboBox_bankType.setItemText(7, _translate("TransferWindow", "Others"))
        self.pushButton_transferTransfer.setText(_translate("TransferWindow", "TRANSFER"))
        self.pushButton_transferCancle.setText(_translate("TransferWindow", "CANCLE"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     TransferWindow = QtWidgets.QMainWindow()
#     ui = Ui_TransferWindow()
#     ui.setupUi(TransferWindow)
#     TransferWindow.show()
#     sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.beginLogin(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
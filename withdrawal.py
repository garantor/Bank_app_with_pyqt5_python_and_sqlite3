# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Withdrawal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WithdrawalWindow(object,):
    def setupUi(self, WithdrawalWindow):
        WithdrawalWindow.setObjectName("WithdrawalWindow")
        WithdrawalWindow.resize(480, 368)
        WithdrawalWindow.setStyleSheet("background-color: rgb(12, 31, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WithdrawalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 80, 411, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.label_amountWTD = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_amountWTD.setStyleSheet("font: 75 8pt \"Verdana\";\n"
"color: rgb(252, 255, 255);")
        self.label_amountWTD.setObjectName("label_amountWTD")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_amountWTD)
        self.lineEdit_withdrawaAmt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_withdrawaAmt.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_withdrawaAmt.setObjectName("lineEdit_withdrawaAmt")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_withdrawaAmt)
        self.label_OTPwithdrawal = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_OTPwithdrawal.setStyleSheet("font: 75 8pt \"Verdana\";\n"
"color: rgb(252, 255, 255);")
        self.label_OTPwithdrawal.setObjectName("label_OTPwithdrawal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_OTPwithdrawal)
        self.lineEdit_withdrawalOTP = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_withdrawalOTP.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_withdrawalOTP.setObjectName("lineEdit_withdrawalOTP")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_withdrawalOTP)
        self.comboBox_withdrawalAcctype = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_withdrawalAcctype.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.comboBox_withdrawalAcctype.setObjectName("comboBox_withdrawalAcctype")
        self.comboBox_withdrawalAcctype.addItem("")
        self.comboBox_withdrawalAcctype.addItem("")
        self.comboBox_withdrawalAcctype.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_withdrawalAcctype)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 331, 41))
        self.textEdit.setStyleSheet("font: 75 14pt \"Verdana\";\n"
"color: rgb(252, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-40, 200, 601, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-10, 80, 501, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(130, 260, 213, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.formLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_withdrawlWithdrawbtn = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_withdrawlWithdrawbtn.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_withdrawlWithdrawbtn.setObjectName("pushButton_withdrawlWithdrawbtn")
        self.horizontalLayout.addWidget(self.pushButton_withdrawlWithdrawbtn)
        self.pushButton_withdrawalCancel = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_withdrawalCancel.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_withdrawalCancel.setObjectName("pushButton_withdrawalCancel")
        self.horizontalLayout.addWidget(self.pushButton_withdrawalCancel)
        WithdrawalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WithdrawalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        WithdrawalWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WithdrawalWindow)
        self.statusbar.setObjectName("statusbar")
        WithdrawalWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WithdrawalWindow)
        QtCore.QMetaObject.connectSlotsByName(WithdrawalWindow)
        self.pushButton_withdrawalCancel.clicked.connect(self.WithdrawalCancle)
        self.pushButton_withdrawlWithdrawbtn.clicked.connect(self.WithdrwalButton)

    def getText(self):
        from Qinputdialo import App
        name = App.getText(App)
        print(name)
        # from PyQt5.QtWidgets import QInputDialog, QLineEdit
        # text, okPressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
        # if okPressed and text != '':
        #     print(text)

    def WithdrwalButton(self):
        print('Withdrawal button')
        # import sqlite3
        # self.getText()
        #
        # conn = sqlite3.connect("BankNH.db")
        # okPressed = self.getText()
        # with conn:
        #     cur= conn.cursor()
        #     cur.execute("SELECT BAL FROM NEWBANK WHERE PASSWORD =? ", ([okPressed,]))
        #     data = cur.fetchall()
        #     print(data)
        #     print('WithdrwalButton')


    def WithdrawalCancle(self):
        from MainProfile import Ui_MainWindow
        print('WithdrawalCancle')
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


    def retranslateUi(self, WithdrawalWindow):
        _translate = QtCore.QCoreApplication.translate
        WithdrawalWindow.setWindowTitle(_translate("WithdrawalWindow", "Withdrawal"))
        self.label_amountWTD.setText(_translate("WithdrawalWindow", "AMOUNT"))
        self.label_OTPwithdrawal.setText(_translate("WithdrawalWindow", "OTP"))
        self.comboBox_withdrawalAcctype.setItemText(0, _translate("WithdrawalWindow", "Account Type"))
        self.comboBox_withdrawalAcctype.setItemText(1, _translate("WithdrawalWindow", "Savings"))
        self.comboBox_withdrawalAcctype.setItemText(2, _translate("WithdrawalWindow", "Current"))
        self.textEdit.setHtml(_translate("WithdrawalWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;\">Please Note you need an OTP on your Register Number to use the withdrawal</span></p></body></html>"))
        self.pushButton_withdrawlWithdrawbtn.setText(_translate("WithdrawalWindow", "WITHDRAW"))
        self.pushButton_withdrawalCancel.setText(_translate("WithdrawalWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WithdrawalWindow = QtWidgets.QMainWindow()
    ui = Ui_WithdrawalWindow()
    ui.setupUi(WithdrawalWindow)
    WithdrawalWindow.show()
    sys.exit(app.exec_())


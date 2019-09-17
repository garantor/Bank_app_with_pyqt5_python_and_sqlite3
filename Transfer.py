# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transfer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MainProfile import Ui_MainWindow
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

    def message(self, title, message):
        mssg = QMessageBox()
        mssg.setWindowTitle(title)
        mssg.setIcon(QMessageBox.Warning)
        mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mssg.setText(message)
        mssg.exec_()

    def SendTransfer(self):
        import sqlite3
        conn = sqlite3.connect("BankNH.db")
        cur = conn.cursor()
        cur.execute("SELECT FIRSTNAME FROM NEWBANK")
        table = cur.fetchall()
        print(table)
        amount = self.lineEdit_amount2txf.text()
        amount2send = int(amount)
        name2send = self.lineEdit_name2txf.text()
        number2send = self.lineEdit_account2txf.text()
        if amount2send != '':
            print('amount worked')
            if table:
                self.message('error sending', 'Please Check the name you are sending to')
            else:
                print('working')
                if number2send != '':
                    print('Number fine')
        else:
            print('Transfer send')

    def CancleTxf(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TransferWindow = QtWidgets.QMainWindow()
    ui = Ui_TransferWindow()
    ui.setupUi(TransferWindow)
    TransferWindow.show()
    sys.exit(app.exec_())


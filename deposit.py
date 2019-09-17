# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Deposit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MainProfile import Ui_MainWindow

class Ui_DepositWindow(object):
    def setupUi(self, DepositWindow):
        DepositWindow.setObjectName("DepositWindow")
        DepositWindow.resize(348, 251)
        DepositWindow.setStyleSheet("background-color: rgb(12, 31, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(DepositWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_deposit = QtWidgets.QLabel(self.centralwidget)
        self.label_deposit.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 255, 255);")
        self.label_deposit.setObjectName("label_deposit")
        self.gridLayout.addWidget(self.label_deposit, 0, 0, 1, 1)
        self.lineEdit_depositbox = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_depositbox.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_depositbox.setObjectName("lineEdit_depositbox")
        self.gridLayout.addWidget(self.lineEdit_depositbox, 0, 1, 1, 1)
        self.comboBox_depositCombo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_depositCombo.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.comboBox_depositCombo.setObjectName("comboBox_depositCombo")
        self.comboBox_depositCombo.addItem("")
        self.comboBox_depositCombo.addItem("")
        self.comboBox_depositCombo.addItem("")
        self.gridLayout.addWidget(self.comboBox_depositCombo, 1, 0, 1, 2)
        self.pushButton_depositbtn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_depositbtn.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_depositbtn.setObjectName("pushButton_depositbtn")
        self.gridLayout.addWidget(self.pushButton_depositbtn, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_deposit_cancle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deposit_cancle.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 8pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_deposit_cancle.setObjectName("pushButton_deposit_cancle")
        self.horizontalLayout.addWidget(self.pushButton_deposit_cancle)
        self.pushButton_deposit_transfer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deposit_transfer.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 8pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_deposit_transfer.setObjectName("pushButton_deposit_transfer")
        self.horizontalLayout.addWidget(self.pushButton_deposit_transfer)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        DepositWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DepositWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 26))
        self.menubar.setObjectName("menubar")
        DepositWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DepositWindow)
        self.statusbar.setObjectName("statusbar")
        DepositWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DepositWindow)
        QtCore.QMetaObject.connectSlotsByName(DepositWindow)
        self.pushButton_deposit_cancle.clicked.connect(self.DepositCancled)
        self.pushButton_deposit_transfer.clicked.connect(self.TransferDeposit)

    def TransferDeposit(self):
        print('TransferDeposit')

    def DepositCancled(self):
        print('DepositCancled')
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


    def retranslateUi(self, DepositWindow):
        _translate = QtCore.QCoreApplication.translate
        DepositWindow.setWindowTitle(_translate("DepositWindow", "Deposit"))
        self.label_deposit.setText(_translate("DepositWindow", "AMOUNT"))
        self.comboBox_depositCombo.setItemText(0, _translate("DepositWindow", "Account Type"))
        self.comboBox_depositCombo.setItemText(1, _translate("DepositWindow", "Savings"))
        self.comboBox_depositCombo.setItemText(2, _translate("DepositWindow", "Current"))
        self.pushButton_depositbtn.setText(_translate("DepositWindow", "MAKE DEPOSIT"))
        self.pushButton_deposit_cancle.setText(_translate("DepositWindow", "GO BACK OR CANCLE"))
        self.pushButton_deposit_transfer.setText(_translate("DepositWindow", "TRANSFER INSTEAD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DepositWindow = QtWidgets.QMainWindow()
    ui = Ui_DepositWindow()
    ui.setupUi(DepositWindow)
    DepositWindow.show()
    sys.exit(app.exec_())


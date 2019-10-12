
from PyQt5 import QtCore, QtGui, QtWidgets
from MainProfile import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class Ui_LoginWindow(object):
    def beginLogin(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(453, 466)
        LoginWindow.setStyleSheet("background-color: rgb(12, 31, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgba(240, 240, 240, 240);")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgba(240, 240, 240, 240);")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pushButton_Login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Login.setStyleSheet("color: rgb(240, 240, 240);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(78, 78, 78);")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_Login)
        self.pushButton_Sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sign_up.setStyleSheet("color: rgb(240, 240, 240);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(78, 78, 78);")
        self.pushButton_Sign_up.setObjectName("pushButton_Sign_up")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pushButton_Sign_up)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../Downloads/login_avater_9RD_icon.ico"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        ####################################################
        #         Connecting welcome page button 
        ####################################################

        self.pushButton_Login.clicked.connect(self.loginLogin)
        self.pushButton_Sign_up.clicked.connect(self.reg)

    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()


    def profile(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()



    def loginLogin(self):
        import sqlite3
        dbb = sqlite3.connect('BankNH.db')
        cur = dbb.cursor()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        cur.execute("SELECT * FROM NEWBANK WHERE USERNAME = ? AND PASSWORD = ?", ([(username), (password)]))
        result = cur.fetchall()

        if result:
            self.profile()
        else:
            self.general_message('User Error', 'User does not Exist')
        

    def reg(self):
        from registrationNew import Ui_registrationPage
        self.general_message('Back', 'Will you like to go Back')
        self.registrationPage = QtWidgets.QMainWindow()
        self.ui = Ui_registrationPage()
        self.ui.setupUi(self.registrationPage)
        self.registrationPage.show()
        
        

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login Page"))
        self.label_2.setText(_translate("LoginWindow", "UserName"))
        self.label_3.setText(_translate("LoginWindow", "PassWord"))
        self.pushButton_Login.setText(_translate("LoginWindow", "LOGIN"))
        self.pushButton_Sign_up.setText(_translate("LoginWindow", "BACK TO SIGN-UP PAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.beginLogin(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())


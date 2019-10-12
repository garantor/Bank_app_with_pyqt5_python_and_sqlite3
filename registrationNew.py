# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from MainLogin import Ui_LoginWindow
from PyQt5.QtWidgets import QMessageBox
dbb = sqlite3.connect('BankNH.db')
c = dbb.cursor()

class Ui_registrationPage(object):
    def setupUi(self, registrationPage):
        Ui_LoginWindow.close()
        registrationPage.setObjectName("registrationPage")
        registrationPage.resize(591, 486)
        registrationPage.setStyleSheet("background-color: rgb(12, 31, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(registrationPage)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.label_username.setObjectName("label_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_username)
        self.lineEdit_Username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Username.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Username)
        self.label_fname = QtWidgets.QLabel(self.centralwidget)
        self.label_fname.setStyleSheet("color: rgb(252, 252, 252);font: 75 10pt \"Verdana\";")
        self.label_fname.setObjectName("label_fname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_fname)
        self.lineEdit_Firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Firstname.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_Firstname.setObjectName("lineEdit_Firstname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Firstname)
        self.label_Lname = QtWidgets.QLabel(self.centralwidget)
        self.label_Lname.setStyleSheet("color: rgb(252, 252, 252);font: 75 10pt \"Verdana\";")
        self.label_Lname.setObjectName("label_Lname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_Lname)
        self.lineEdit_Lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Lastname.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_Lastname.setObjectName("lineEdit_Lastname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Lastname)
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setStyleSheet("color: rgb(252, 252, 252);font: 75 10pt \"Verdana\";")
        self.label_email.setObjectName("label_email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_email)
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setStyleSheet("color: rgb(252, 252, 252);font: 75 10pt \"Verdana\";")
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.label_password_confirm = QtWidgets.QLabel(self.centralwidget)
        self.label_password_confirm.setStyleSheet("color: rgb(252, 252, 252);font: 75 10pt \"Verdana\";")
        self.label_password_confirm.setObjectName("label_password_confirm")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_password_confirm)
        self.lineEdit_confirmPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_confirmPassword.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirmPassword.setObjectName("lineEdit_confirmPassword")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_confirmPassword)
        self.label_phone = QtWidgets.QLabel(self.centralwidget)
        self.label_phone.setStyleSheet("color: rgb(252, 252, 252);font: 75 10pt \"Verdana\";")
        self.label_phone.setObjectName("label_phone")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_phone)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_phone.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_phone)
        self.label_sex = QtWidgets.QLabel(self.centralwidget)
        self.label_sex.setStyleSheet("color: rgb(252, 252, 252);font: 75 10pt \"Verdana\";")
        self.label_sex.setObjectName("label_sex")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_sex)
        self.lineEdit_sex = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sex.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_sex.setObjectName("lineEdit_sex")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sex)
        self.label_address = QtWidgets.QLabel(self.centralwidget)
        self.label_address.setStyleSheet("color: rgb(252, 252, 252);font: 75 10pt \"Verdana\";")
        self.label_address.setObjectName("label_address")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_address)
        self.lineEdit_address = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_address.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_address)
        self.pushButton_Register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Register.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(240, 240, 240);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(78, 78, 78);")
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.pushButton_Register)
        self.pushButton_reglogin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reglogin.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(240, 240, 240);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(78, 78, 78);")
        self.pushButton_reglogin.setObjectName("pushButton_reglogin")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.pushButton_reglogin)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.formLayout)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("color: rgb(252, 252, 252);font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_10)
        registrationPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(registrationPage)
        self.statusbar.setObjectName("statusbar")
        registrationPage.setStatusBar(self.statusbar)

        self.retranslateUi(registrationPage)
        QtCore.QMetaObject.connectSlotsByName(registrationPage)
        self.pushButton_Register.clicked.connect(self.CreateDB)
        self.pushButton_reglogin.clicked.connect(self.login)


    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()

    def CreateDB(self):
        c.execute(''' CREATE TABLE IF NOT EXISTS NEWBANK(
           ID INTEGER PRIMARY KEY AUTOINCREMENT,
           USERNAME CHAR(20) NOT NULL,
           FIRSTNAME STR NOT NULL,
           LASTNAME STR NOT NULL,
           EMAIL STR NOT NULL,
           PASSWORD STR NOT NULL,
           CONFIRM STR NOT NULL,
           PHONE CHAR(11) NOT NULL,
           SEX STR,
           ADDRESS CHAR(50) NOT NULL,
           BAL REAL(200) );
           ''')
        self.insertdb()

    def insertdb(self):
        username = self.lineEdit_Username.text()
        firstname = self.lineEdit_Firstname.text()
        lastname = self.lineEdit_Lastname.text()
        email = self.lineEdit_email.text()
        if '@' not in email:
            self.general_message('Invalid Email', 'Please Check your Email again')
            return email
        else:
            password = self.lineEdit_password.text()
            confirmPass = self.lineEdit_confirmPassword.text()
            if password != confirmPass:
                self.general_message('password Error', 'Password Not Match')
                return password and confirmPass
            elif len(password) != len(confirmPass):
                self.general_message('password Error', 'password not Match')
                return password and confirmPass
            else:
                phone = self.lineEdit_phone.text()
                if len(phone) != 11:
                    self.general_message('Invalid Number', 'please Check your Phone number')
                    return phone
                else:
                    sex = self.lineEdit_sex.text()
                    address = self.lineEdit_address.text()
                    c.execute("INSERT INTO NEWBANK(USERNAME, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, CONFIRM, PHONE, SEX ,ADDRESS)VALUES (?,?,?,?,?,?,?,?,?)", (str(username), str(firstname), str(lastname), str(email), str(password), str(confirmPass), str(phone), str(sex), str(address)))
                    print('insert done')
                    dbb.commit()
                    self.login()


    def login(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.beginLogin(self.LoginWindow)
        self.LoginWindow.show()




    def retranslateUi(self, registrationPage):
        _translate = QtCore.QCoreApplication.translate
        registrationPage.setWindowTitle(_translate("registrationPage", "Registration Page"))
        self.label_username.setText(_translate("registrationPage", "Username"))
        self.lineEdit_Username.setPlaceholderText(_translate("registrationPage", "UserName"))
        self.label_fname.setText(_translate("registrationPage", "First Name"))
        self.lineEdit_Firstname.setPlaceholderText(_translate("registrationPage", "First name"))
        self.label_Lname.setText(_translate("registrationPage", "Last name"))
        self.lineEdit_Lastname.setPlaceholderText(_translate("registrationPage", "last name"))
        self.label_email.setText(_translate("registrationPage", "Email"))
        self.lineEdit_email.setPlaceholderText(_translate("registrationPage", "Email"))
        self.label_password.setText(_translate("registrationPage", "Password"))
        self.lineEdit_password.setPlaceholderText(_translate("registrationPage", "password"))
        self.label_password_confirm.setText(_translate("registrationPage", "Confirm"))
        self.lineEdit_confirmPassword.setPlaceholderText(_translate("registrationPage", "Confirm Password"))
        self.label_phone.setText(_translate("registrationPage", "Phone"))
        self.lineEdit_phone.setPlaceholderText(_translate("registrationPage", "phone Number"))
        self.label_sex.setText(_translate("registrationPage", "Sex"))
        self.lineEdit_sex.setPlaceholderText(_translate("registrationPage", "Male or Female"))
        self.label_address.setText(_translate("registrationPage", "Address"))
        self.lineEdit_address.setPlaceholderText(_translate("registrationPage", "address"))
        self.pushButton_Register.setText(_translate("registrationPage", "REGISTER"))
        self.pushButton_reglogin.setText(_translate("registrationPage", "LOGIN"))
        self.label_10.setText(_translate("registrationPage", "REGISTRATION  PAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registrationPage = QtWidgets.QMainWindow()
    ui = Ui_registrationPage()
    ui.setupUi(registrationPage)
    registrationPage.show()
    sys.exit(app.exec_())


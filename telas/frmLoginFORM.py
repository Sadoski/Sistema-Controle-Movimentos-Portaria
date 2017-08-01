# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmLogin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmLogin(object):
    def setupUi(self, frmLogin):
        frmLogin.setObjectName(_fromUtf8("frmLogin"))
        frmLogin.resize(402, 328)
        frmLogin.setMinimumSize(QtCore.QSize(402, 328))
        frmLogin.setMaximumSize(QtCore.QSize(402, 328))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        frmLogin.setFont(font)
        self.centralwidget = QtGui.QWidget(frmLogin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblImagem = QtGui.QLabel(self.centralwidget)
        self.lblImagem.setGeometry(QtCore.QRect(30, 10, 341, 71))
        self.lblImagem.setText(_fromUtf8(""))
        self.lblImagem.setObjectName(_fromUtf8("lblImagem"))
        self.lblSenha = QtGui.QLabel(self.centralwidget)
        self.lblSenha.setGeometry(QtCore.QRect(70, 160, 66, 19))
        self.lblSenha.setObjectName(_fromUtf8("lblSenha"))
        self.lblUsuario = QtGui.QLabel(self.centralwidget)
        self.lblUsuario.setGeometry(QtCore.QRect(70, 90, 66, 19))
        self.lblUsuario.setObjectName(_fromUtf8("lblUsuario"))
        self.txtSenha = QtGui.QLineEdit(self.centralwidget)
        self.txtSenha.setGeometry(QtCore.QRect(70, 180, 251, 25))
        self.txtSenha.setEchoMode(QtGui.QLineEdit.Password)
        self.txtSenha.setObjectName(_fromUtf8("txtSenha"))
        self.txtUsuario = QtGui.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(70, 110, 251, 25))
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))
        self.btnSair = QtGui.QPushButton(self.centralwidget)
        self.btnSair.setGeometry(QtCore.QRect(260, 240, 61, 27))
        self.btnSair.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSair.setObjectName(_fromUtf8("btnSair"))
        self.btnEsqueciSenha = QtGui.QPushButton(self.centralwidget)
        self.btnEsqueciSenha.setGeometry(QtCore.QRect(120, 300, 151, 26))
        self.btnEsqueciSenha.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnEsqueciSenha.setFlat(True)
        self.btnEsqueciSenha.setObjectName(_fromUtf8("btnEsqueciSenha"))
        self.btnLogin = QtGui.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(180, 240, 61, 27))
        self.btnLogin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        frmLogin.setCentralWidget(self.centralwidget)
        self.lblSenha.setBuddy(self.txtSenha)
        self.lblUsuario.setBuddy(self.txtUsuario)

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)
        frmLogin.setTabOrder(self.txtUsuario, self.txtSenha)
        frmLogin.setTabOrder(self.txtSenha, self.btnLogin)
        frmLogin.setTabOrder(self.btnLogin, self.btnSair)

    def retranslateUi(self, frmLogin):
        frmLogin.setWindowTitle(_translate("frmLogin", "Log-in", None))
        self.lblSenha.setText(_translate("frmLogin", "Senha :", None))
        self.lblUsuario.setText(_translate("frmLogin", "Usuario :", None))
        self.btnSair.setText(_translate("frmLogin", "Sair", None))
        self.btnEsqueciSenha.setText(_translate("frmLogin", "Esqueci minha senha", None))
        self.btnLogin.setText(_translate("frmLogin", "Log-in", None))


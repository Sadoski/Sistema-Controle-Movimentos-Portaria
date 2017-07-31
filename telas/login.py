# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        frmLogin.resize(397, 325)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        frmLogin.setFont(font)
        self.centralwidget = QtGui.QWidget(frmLogin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.txtSenha = QtGui.QLineEdit(self.centralwidget)
        self.txtSenha.setGeometry(QtCore.QRect(60, 180, 251, 25))
        self.txtSenha.setObjectName(_fromUtf8("txtSenha"))
        self.btnLogin = QtGui.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(170, 240, 61, 27))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.lblUsuario = QtGui.QLabel(self.centralwidget)
        self.lblUsuario.setGeometry(QtCore.QRect(60, 90, 66, 19))
        self.lblUsuario.setObjectName(_fromUtf8("lblUsuario"))
        self.txtUsuario = QtGui.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(60, 110, 251, 25))
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))
        self.lblImagem = QtGui.QLabel(self.centralwidget)
        self.lblImagem.setGeometry(QtCore.QRect(20, 10, 341, 71))
        self.lblImagem.setText(_fromUtf8(""))
        self.lblImagem.setObjectName(_fromUtf8("lblImagem"))
        self.lblSenha = QtGui.QLabel(self.centralwidget)
        self.lblSenha.setGeometry(QtCore.QRect(60, 160, 66, 19))
        self.lblSenha.setObjectName(_fromUtf8("lblSenha"))
        self.btnSair = QtGui.QPushButton(self.centralwidget)
        self.btnSair.setGeometry(QtCore.QRect(250, 240, 61, 27))
        self.btnSair.setObjectName(_fromUtf8("btnSair"))
        self.btnEsqueciSenha = QtGui.QPushButton(self.centralwidget)
        self.btnEsqueciSenha.setGeometry(QtCore.QRect(110, 300, 151, 21))
        self.btnEsqueciSenha.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnEsqueciSenha.setFlat(True)
        self.btnEsqueciSenha.setObjectName(_fromUtf8("btnEsqueciSenha"))
        frmLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)

    def retranslateUi(self, frmLogin):
        frmLogin.setWindowTitle(_translate("frmLogin", "Log-in", None))
        self.btnLogin.setText(_translate("frmLogin", "Log-in", None))
        self.lblUsuario.setText(_translate("frmLogin", "Usuario :", None))
        self.lblSenha.setText(_translate("frmLogin", "Senha :", None))
        self.btnSair.setText(_translate("frmLogin", "Sair", None))
        self.btnEsqueciSenha.setText(_translate("frmLogin", "Esqueci minha senha", None))


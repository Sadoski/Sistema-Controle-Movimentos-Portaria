# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmLogin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
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
        frmLogin.setWindowModality(QtCore.Qt.WindowModal)
        frmLogin.resize(400, 326)
        frmLogin.setMinimumSize(QtCore.QSize(400, 326))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        frmLogin.setFont(font)
        frmLogin.setModal(True)
        
        self.txtUsuario = QtGui.QLineEdit(frmLogin)
        self.txtUsuario.setGeometry(QtCore.QRect(70, 110, 251, 25))
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))

        
        self.txtSenha = QtGui.QLineEdit(frmLogin)
        self.txtSenha.setGeometry(QtCore.QRect(70, 180, 251, 25))
        self.txtSenha.setObjectName(_fromUtf8("txtSenha"))
        self.txtSenha.setEchoMode(QtGui.QLineEdit.Password)
        
        self.lblUsuario = QtGui.QLabel(frmLogin)
        self.lblUsuario.setGeometry(QtCore.QRect(70, 90, 66, 19))
        self.lblUsuario.setObjectName(_fromUtf8("lblUsuario"))
        
        self.lblSenha = QtGui.QLabel(frmLogin)
        self.lblSenha.setGeometry(QtCore.QRect(70, 160, 66, 19))
        self.lblSenha.setObjectName(_fromUtf8("lblSenha"))
        
        self.btnLogin = QtGui.QPushButton(frmLogin)
        self.btnLogin.setGeometry(QtCore.QRect(180, 240, 61, 27))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        
        self.btnSair = QtGui.QPushButton(frmLogin)
        self.btnSair.setGeometry(QtCore.QRect(260, 240, 61, 27))
        self.btnSair.setObjectName(_fromUtf8("btnSair"))
        
        self.lblImagem = QtGui.QLabel(frmLogin)
        self.lblImagem.setGeometry(QtCore.QRect(30, 10, 341, 71))
        self.lblImagem.setText(_fromUtf8(""))
        self.lblImagem.setObjectName(_fromUtf8("lblImagem"))
        
        self.btnEsqueciSenha = QtGui.QPushButton(frmLogin)
        self.btnEsqueciSenha.setGeometry(QtCore.QRect(120, 300, 151, 21))
        self.btnEsqueciSenha.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnEsqueciSenha.setFlat(True)
        self.btnEsqueciSenha.setObjectName(_fromUtf8("btnEsqueciSenha"))

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)

    def retranslateUi(self, frmLogin):
        frmLogin.setWindowTitle(_translate("frmLogin", "Log-in", None))

        self.lblUsuario.setText(_translate("frmLogin", "Usuario :", None))
        self.lblSenha.setText(_translate("frmLogin", "Senha :", None))
        self.btnLogin.setText(_translate("frmLogin", "Log-in", None))
        self.btnSair.setText(_translate("frmLogin", "Sair", None))
        self.btnEsqueciSenha.setText(_translate("frmLogin", "Esqueci minha senha", None))
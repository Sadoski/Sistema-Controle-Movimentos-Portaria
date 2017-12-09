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
        frmLogin.setWindowModality(QtCore.Qt.ApplicationModal)
        frmLogin.resize(400, 300)
        frmLogin.setMinimumSize(QtCore.QSize(400, 300))
        frmLogin.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/scmp.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmLogin.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(11)
        frmLogin.setFont(font)
        
        self.txtUsuario = QtGui.QLineEdit(frmLogin)
        self.txtUsuario.setGeometry(QtCore.QRect(90, 110, 251, 25))
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))
        
        self.txtSenha = QtGui.QLineEdit(frmLogin)
        self.txtSenha.setGeometry(QtCore.QRect(90, 180, 251, 25))
        self.txtSenha.setEchoMode(QtGui.QLineEdit.Password)
        self.txtSenha.setObjectName(_fromUtf8("txtSenha"))
        
        self.btnLogin = QtGui.QPushButton(frmLogin)
        self.btnLogin.setGeometry(QtCore.QRect(200, 240, 61, 27))
        self.btnLogin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        
        self.btnSair = QtGui.QPushButton(frmLogin)
        self.btnSair.setGeometry(QtCore.QRect(280, 240, 61, 27))
        self.btnSair.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSair.setObjectName(_fromUtf8("btnSair"))
        
        self.lblImagem = QtGui.QLabel(frmLogin)
        self.lblImagem.setGeometry(QtCore.QRect(30, 10, 341, 71))
        self.lblImagem.setText(_fromUtf8(""))
        self.lblImagem.setPixmap(QtGui.QPixmap(_fromUtf8("./imagens/scmp-login.jpg")))
        self.lblImagem.setObjectName(_fromUtf8("lblImagem"))
        
        self.lblImagemUsuario = QtGui.QLabel(frmLogin)
        self.lblImagemUsuario.setGeometry(QtCore.QRect(50, 100, 31, 41))
        self.lblImagemUsuario.setText(_fromUtf8(""))
        self.lblImagemUsuario.setPixmap(QtGui.QPixmap(_fromUtf8("./imagens/User.png")))
        self.lblImagemUsuario.setObjectName(_fromUtf8("lblImagemUsuario"))
        
        self.lblImagemSenha = QtGui.QLabel(frmLogin)
        self.lblImagemSenha.setGeometry(QtCore.QRect(50, 167, 34, 41))
        self.lblImagemSenha.setText(_fromUtf8(""))
        self.lblImagemSenha.setPixmap(QtGui.QPixmap(_fromUtf8("./imagens/password.png")))
        self.lblImagemSenha.setObjectName(_fromUtf8("lblImagemSenha"))

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)

    def retranslateUi(self, frmLogin):
        frmLogin.setWindowTitle(_translate("frmLogin", "Log-in", None))
        self.txtUsuario.setPlaceholderText(_translate("frmLogin", "Usuário", None))
        self.txtSenha.setPlaceholderText(_translate("frmLogin", "Senha", None))
        self.btnLogin.setText(_translate("frmLogin", "Log-in", None))
        self.btnSair.setText(_translate("frmLogin", "Sair", None))


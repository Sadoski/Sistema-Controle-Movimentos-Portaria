# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email.ui'
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

class Ui_Email(object):
    def setupUi(self, Email):
        Email.setObjectName(_fromUtf8("Email"))
        Email.resize(662, 433)
        font = QtGui.QFont()
        font.setPointSize(12)
        Email.setFont(font)
        self.txtNome = QtGui.QComboBox(Email)
        self.txtNome.setGeometry(QtCore.QRect(20, 30, 181, 22))
        self.txtNome.setObjectName(_fromUtf8("txtNome"))
        self.txtNome.addItem(_fromUtf8(""))
        self.txtNome.addItem(_fromUtf8(""))
        self.txtNome.addItem(_fromUtf8(""))
        self.txtNome.addItem(_fromUtf8(""))
        self.txtNome.addItem(_fromUtf8(""))
        self.txtNome.addItem(_fromUtf8(""))
        self.txtNome.addItem(_fromUtf8(""))
        self.txtNome.addItem(_fromUtf8(""))
        
        self.lblNome = QtGui.QLabel(Email)
        self.lblNome.setGeometry(QtCore.QRect(20, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName(_fromUtf8("lblNome"))
        
        self.txtServidor = QtGui.QLineEdit(Email)
        self.txtServidor.setEnabled(False)
        self.txtServidor.setGeometry(QtCore.QRect(210, 30, 181, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtServidor.setPalette(palette)
        self.txtServidor.setObjectName(_fromUtf8("txtServidor"))
        
        self.txtRemetente = QtGui.QLineEdit(Email)
        self.txtRemetente.setGeometry(QtCore.QRect(110, 80, 531, 20))
        self.txtRemetente.setObjectName(_fromUtf8("txtRemetente"))
        
        self.lblPorta = QtGui.QLabel(Email)
        self.lblPorta.setGeometry(QtCore.QRect(210, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblPorta.setFont(font)
        self.lblPorta.setObjectName(_fromUtf8("lblPorta"))
        
        self.lblRemetente = QtGui.QLabel(Email)
        self.lblRemetente.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.lblRemetente.setObjectName(_fromUtf8("lblRemetente"))
        
        self.lblSenhaRemetente = QtGui.QLabel(Email)
        self.lblSenhaRemetente.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.lblSenhaRemetente.setObjectName(_fromUtf8("lblSenhaRemetente"))
        
        self.txtSenhaRemetente = QtGui.QLineEdit(Email)
        self.txtSenhaRemetente.setGeometry(QtCore.QRect(110, 110, 531, 20))
        self.txtSenhaRemetente.setEchoMode(QtGui.QLineEdit.Password)
        self.txtSenhaRemetente.setObjectName(_fromUtf8("txtSenhaRemetente"))
        
        self.lblDestinatario = QtGui.QLabel(Email)
        self.lblDestinatario.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.lblDestinatario.setObjectName(_fromUtf8("lblDestinatario"))
        
        self.txtDestinatario = QtGui.QLineEdit(Email)
        self.txtDestinatario.setGeometry(QtCore.QRect(110, 140, 531, 20))
        self.txtDestinatario.setObjectName(_fromUtf8("txtDestinatario"))
        
        self.txtAssunto = QtGui.QLineEdit(Email)
        self.txtAssunto.setGeometry(QtCore.QRect(110, 180, 531, 20))
        self.txtAssunto.setObjectName(_fromUtf8("txtAssunto"))
        
        self.lblAssunto = QtGui.QLabel(Email)
        self.lblAssunto.setGeometry(QtCore.QRect(20, 180, 91, 16))
        self.lblAssunto.setObjectName(_fromUtf8("lblAssunto"))
        
        self.txtTexto = QtGui.QTextEdit(Email)
        self.txtTexto.setGeometry(QtCore.QRect(20, 240, 621, 141))
        self.txtTexto.setObjectName(_fromUtf8("txtTexto"))
        
        self.btnCancelar = QtGui.QPushButton(Email)
        self.btnCancelar.setGeometry(QtCore.QRect(490, 380, 71, 51))
        self.btnCancelar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/email-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon)
        self.btnCancelar.setIconSize(QtCore.QSize(64, 64))
        self.btnCancelar.setFlat(True)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        
        self.btnEnviar = QtGui.QPushButton(Email)
        self.btnEnviar.setGeometry(QtCore.QRect(570, 380, 71, 51))
        self.btnEnviar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/email-send.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnviar.setIcon(icon1)
        self.btnEnviar.setIconSize(QtCore.QSize(64, 64))
        self.btnEnviar.setFlat(True)
        self.btnEnviar.setObjectName(_fromUtf8("btnEnviar"))
        
        self.btnAnexo = QtGui.QPushButton(Email)
        self.btnAnexo.setGeometry(QtCore.QRect(606, 205, 31, 31))
        self.btnAnexo.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/attachment.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAnexo.setIcon(icon2)
        self.btnAnexo.setIconSize(QtCore.QSize(25, 25))
        self.btnAnexo.setFlat(True)
        self.btnAnexo.setObjectName(_fromUtf8("btnAnexo"))
        
        self.txtPorta = QtGui.QLineEdit(Email)
        self.txtPorta.setEnabled(False)
        self.txtPorta.setGeometry(QtCore.QRect(530, 30, 111, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtPorta.setPalette(palette)
        self.txtPorta.setObjectName(_fromUtf8("txtPorta"))
        
        self.lblPorta_2 = QtGui.QLabel(Email)
        self.lblPorta_2.setGeometry(QtCore.QRect(530, 10, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblPorta_2.setFont(font)
        self.lblPorta_2.setObjectName(_fromUtf8("lblPorta_2"))
        
        self.lblAutenticacao = QtGui.QLabel(Email)
        self.lblAutenticacao.setGeometry(QtCore.QRect(400, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblAutenticacao.setFont(font)
        self.lblAutenticacao.setObjectName(_fromUtf8("lblAutenticacao"))
        
        self.txtAutenticacao = QtGui.QLineEdit(Email)
        self.txtAutenticacao.setEnabled(False)
        self.txtAutenticacao.setGeometry(QtCore.QRect(400, 30, 121, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtAutenticacao.setPalette(palette)
        self.txtAutenticacao.setObjectName(_fromUtf8("txtAutenticacao"))
        
        self.lblNome.setBuddy(self.txtNome)
        self.lblPorta.setBuddy(self.txtServidor)
        self.lblRemetente.setBuddy(self.txtRemetente)
        self.lblSenhaRemetente.setBuddy(self.txtSenhaRemetente)
        self.lblDestinatario.setBuddy(self.txtDestinatario)
        self.lblAssunto.setBuddy(self.txtAssunto)
        self.lblPorta_2.setBuddy(self.txtPorta)
        self.lblAutenticacao.setBuddy(self.txtAutenticacao)

        self.retranslateUi(Email)
        QtCore.QMetaObject.connectSlotsByName(Email)
        Email.setTabOrder(self.txtNome, self.txtServidor)
        Email.setTabOrder(self.txtServidor, self.txtAutenticacao)
        Email.setTabOrder(self.txtAutenticacao, self.txtPorta)
        Email.setTabOrder(self.txtPorta, self.txtRemetente)
        Email.setTabOrder(self.txtRemetente, self.txtSenhaRemetente)
        Email.setTabOrder(self.txtSenhaRemetente, self.txtDestinatario)
        Email.setTabOrder(self.txtDestinatario, self.txtAssunto)
        Email.setTabOrder(self.txtAssunto, self.btnAnexo)
        Email.setTabOrder(self.btnAnexo, self.txtTexto)
        Email.setTabOrder(self.txtTexto, self.btnCancelar)
        Email.setTabOrder(self.btnCancelar, self.btnEnviar)

    def retranslateUi(self, Email):
        Email.setWindowTitle(_translate("Email", "E-mail", None))
        self.txtNome.setItemText(0, _translate("Email", "Gmail", None))
        self.txtServidor.setText("smtp.gmail.com")
        self.txtAutenticacao.setText("SSL")
        self.txtPorta.setText("465")
        self.txtNome.setItemText(1, _translate("Email", "Gmail", None))
        self.txtNome.setItemText(2, _translate("Email", "Hotmail", None))
        self.txtNome.setItemText(3, _translate("Email", "Mail.com", None))
        self.txtNome.setItemText(4, _translate("Email", "Outlook.com", None))
        self.txtNome.setItemText(5, _translate("Email", "Office365.com", None))
        self.txtNome.setItemText(6, _translate("Email", "Yahoo Mail", None))
        self.txtNome.setItemText(7, _translate("Email", "Outros", None))
        self.lblNome.setText(_translate("Email", "Nome", None))
        self.lblPorta.setText(_translate("Email", "Servidor", None))
        self.lblRemetente.setText(_translate("Email", "Remetente", None))
        self.lblSenhaRemetente.setText(_translate("Email", "Senha Rem.", None))
        self.lblDestinatario.setText(_translate("Email", "Destinatario", None))
        self.lblAssunto.setText(_translate("Email", "Assunto", None))
        self.lblPorta_2.setText(_translate("Email", "Porta", None))
        self.lblAutenticacao.setText(_translate("Email", "Autenticação", None))


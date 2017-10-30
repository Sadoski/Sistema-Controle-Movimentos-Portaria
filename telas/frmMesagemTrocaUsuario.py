# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMesagemTrocaUsuario.ui'
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

class Ui_frmMensagemTrocaUsuario(object):
    def setupUi(self, frmMensagemTrocaUsuario):
        frmMensagemTrocaUsuario.setObjectName(_fromUtf8("frmMensagemTrocaUsuario"))
        frmMensagemTrocaUsuario.resize(344, 95)
        frmMensagemTrocaUsuario.setMinimumSize(QtCore.QSize(344, 95))
        frmMensagemTrocaUsuario.setMaximumSize(QtCore.QSize(344, 95))
        font = QtGui.QFont()
        font.setPointSize(10)
        frmMensagemTrocaUsuario.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/question.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmMensagemTrocaUsuario.setWindowIcon(icon)

        self.btnSim = QtGui.QPushButton(frmMensagemTrocaUsuario)
        self.btnSim.setGeometry(QtCore.QRect(100, 59, 75, 23))
        self.btnSim.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSim.setObjectName(_fromUtf8("btnSim"))

        self.btnNao = QtGui.QPushButton(frmMensagemTrocaUsuario)
        self.btnNao.setGeometry(QtCore.QRect(180, 59, 75, 23))
        self.btnNao.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btnNao.setObjectName(_fromUtf8("btnNao"))

        self.lblIconQuestion = QtGui.QLabel(frmMensagemTrocaUsuario)
        self.lblIconQuestion.setGeometry(QtCore.QRect(3, 10, 51, 41))
        self.lblIconQuestion.setText(_fromUtf8(""))
        self.lblIconQuestion.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-question.png")))
        self.lblIconQuestion.setObjectName(_fromUtf8("lblIconQuestion"))

        self.lblTexto = QtGui.QLabel(frmMensagemTrocaUsuario)
        self.lblTexto.setGeometry(QtCore.QRect(60, 13, 281, 16))
        self.lblTexto.setObjectName(_fromUtf8("lblTexto"))

        self.retranslateUi(frmMensagemTrocaUsuario)
        QtCore.QMetaObject.connectSlotsByName(frmMensagemTrocaUsuario)

    def retranslateUi(self, frmMensagemTrocaUsuario):
        frmMensagemTrocaUsuario.setWindowTitle(_translate("frmMensagemTrocaUsuario", "Mensagem", None))
        self.btnSim.setText(_translate("frmMensagemTrocaUsuario", "Sim", None))
        self.btnNao.setText(_translate("frmMensagemTrocaUsuario", "Não", None))
        self.lblTexto.setText(_translate("frmMensagemTrocaUsuario", "Você tem certeza que deseja trocar de usuário?", None))


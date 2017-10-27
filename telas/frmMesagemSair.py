# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMesagemSair.ui'
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

class Ui_frmMensagemSair(object):
    def setupUi(self, frmMensagemSair):
        frmMensagemSair.setObjectName(_fromUtf8("frmMensagemSair"))
        frmMensagemSair.resize(218, 95)
        frmMensagemSair.setMinimumSize(QtCore.QSize(218, 95))
        frmMensagemSair.setMaximumSize(QtCore.QSize(218, 95))
        font = QtGui.QFont()
        font.setPointSize(10)
        frmMensagemSair.setFont(font)

        self.btnSim = QtGui.QPushButton(frmMensagemSair)
        self.btnSim.setGeometry(QtCore.QRect(33, 59, 75, 23))
        self.btnSim.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSim.setObjectName(_fromUtf8("btnSim"))

        self.btnNao = QtGui.QPushButton(frmMensagemSair)
        self.btnNao.setGeometry(QtCore.QRect(113, 59, 75, 23))
        self.btnNao.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btnNao.setObjectName(_fromUtf8("btnNao"))

        self.lblIconQuestion = QtGui.QLabel(frmMensagemSair)
        self.lblIconQuestion.setGeometry(QtCore.QRect(3, 10, 51, 41))
        self.lblIconQuestion.setText(_fromUtf8(""))
        self.lblIconQuestion.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-question.png")))
        self.lblIconQuestion.setObjectName(_fromUtf8("lblIconQuestion"))

        self.lblTexto = QtGui.QLabel(frmMensagemSair)
        self.lblTexto.setGeometry(QtCore.QRect(60, 13, 151, 16))
        self.lblTexto.setObjectName(_fromUtf8("lblTexto"))

        self.retranslateUi(frmMensagemSair)
        QtCore.QMetaObject.connectSlotsByName(frmMensagemSair)

    def retranslateUi(self, frmMensagemSair):
        frmMensagemSair.setWindowTitle(_translate("frmMensagemSair", "Atenção", None))
        self.btnSim.setText(_translate("frmMensagemSair", "Sim", None))
        self.btnNao.setText(_translate("frmMensagemSair", "Não", None))
        self.lblTexto.setText(_translate("frmMensagemSair", "Deseja sair do Programa?", None))


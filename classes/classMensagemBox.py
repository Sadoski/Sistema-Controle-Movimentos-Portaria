from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MensagemBox():


    def critico(self, titulo, texto):
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle(titulo)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/critical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-critical.png")))
        self.msgBox.setText(texto)
        btnOk = QtGui.QPushButton('Ok')
        self.msgBox.addButton(btnOk, QtGui.QMessageBox.YesRole)
        btnOk.clicked.connect(self.fechar)
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def informacao(self, titulo, texto):
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle(titulo)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/information.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-informatio.png")))
        self.msgBox.setText(texto)
        btnSim = QtGui.QPushButton('Sim')
        self.msgBox.addButton(btnSim, QtGui.QMessageBox.YesRole)
        btnNao = QtGui.QPushButton('Não')
        self.msgBox.addButton(btnNao, QtGui.QMessageBox.NoRole)
        btnNao.clicked.connect(self.fechar)
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def warning(self, titulo, texto):
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle(titulo)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/warning.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-warning.png")))
        self.msgBox.setText(texto)
        btnOk = QtGui.QPushButton('Ok')
        self.msgBox.addButton(btnOk, QtGui.QMessageBox.YesRole)
        btnOk.clicked.connect(self.fechar)
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def fechar(self):
        self.msgBox.close()
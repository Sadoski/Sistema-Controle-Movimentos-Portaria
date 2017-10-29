import mysql.connector
from mysql.connector import errorcode
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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

class ConexaoDb(object):

    def __init__(self):
        try:

            self.conn = mysql.connector.connect(user='root', password='',
                                                host='127.1.1.1',
                                                database='sistemasportaria')
        except mysql.connector.Error as e:

            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.erroDBUsuarioSenha()
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                self.erroDBInexistente()
            else:
                self.erroFatal()


            self.conn.close()

    def erroDBUsuarioSenha(self):
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle('Erro')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/critical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-critical.png")))
        self.msgBox.setText('Usuário/Senha do banco MySql errado(s)')
        btnQS = QtGui.QPushButton('Ok')
        self.msgBox.addButton(btnQS, QtGui.QMessageBox.YesRole)
        btnQS.clicked.connect(self.fechar)
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def erroDBInexistente(self):
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle('Erro')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/critical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-critical.png")))
        self.msgBox.setText('Banco de Dados inexistente!')
        btnQS = QtGui.QPushButton('Ok')
        self.msgBox.addButton(btnQS, QtGui.QMessageBox.YesRole)
        btnQS.clicked.connect(self.fechar)
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def erroDBInexistente(self):
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle('Erro')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/critical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-critical.png")))
        self.msgBox.setText('Banco de Dados inexistente!')
        btnQS = QtGui.QPushButton('Ok')
        self.msgBox.addButton(btnQS, QtGui.QMessageBox.YesRole)
        btnQS.clicked.connect(self.fechar)
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def erroFatal(self):
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle('Erro')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/critical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-critical.png")))
        self.msgBox.setText('Erro fatal no banco de dados')
        btnQS = QtGui.QPushButton('Ok')
        self.msgBox.addButton(btnQS, QtGui.QMessageBox.YesRole)
        btnQS.clicked.connect(self.fechar)
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def fechar(self):
        self.msgBox.close()
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mysql.connector import Error
from conexao.conexao import ConexaoDb, mysql
from classes.classUsuario import Usuario

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

class LogarDao(object):


    def __init__(self):
        self.__conexao = ConexaoDb()
        self.__cursor = self.__conexao.conn.cursor()

    def salto(self, usuario):
        sql = "select salto from usuarios where login = '" + usuario + "'"
        self.__cursor.execute(sql)
        salto = self.__cursor.fetchone()[0]
        return salto

    def login(self, pUsuario, pSenha):
        __usuario = Usuario()
        __salto = self.salto(pUsuario)
        __senhaCripto = __usuario.criptografar(pSenha, __salto)


        __sql = "select * from usuarios where login= '"+pUsuario+"' and senha = '"+__senhaCripto+"'"
        self.__cursor.execute(__sql)

        result = self.__cursor.fetchall()
        self.__conexao.conn.commit()
        try:
            if result:
                for i in result:
                    return result
                self.__cursor.close()

            else:
                self.erroUsuario()

        except mysql.connector.Error as e:
            self.erroFatal()


    def fechar(self):
        self.msgBox.close()

    def erroUsuario(self):
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle('Atenção')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/warning.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("imagens/icon-warning.png")))
        self.msgBox.setText('Usuário ou Senha incorreto!')
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
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("icon-critical.png")))
        self.msgBox.setText('Erro fatal no banco de dados')
        btnQS = QtGui.QPushButton('Ok')
        self.msgBox.addButton(btnQS, QtGui.QMessageBox.YesRole)
        btnQS.clicked.connect(self.fechar)
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()


import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmLogin import Ui_frmLogin
from dao.loginDao import LogarDao


class Login(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.__ui = Ui_frmLogin()
        self.__ui.setupUi(self)
        self.__logarDao = LogarDao()


        self.__ui.btnLogin.clicked.connect(self.__login)
        self.__ui.btnSair.clicked.connect(self.__sair)
        self.__ui.btnEsqueciSenha.clicked.connect(self.__esqueciSenha)

    def __login(self):
        self.__login = self.__ui.txtUsuario.text()
        self.__senha = self.__ui.txtSenha.text()

        self.__logarDao.login(self.__login, self.__senha)

    def __sair(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja sair do Programa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            sys.exit(None)
            
    def __esqueciSenha(self):
        pass



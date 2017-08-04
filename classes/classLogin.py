import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmLogin import Ui_frmLogin
from dao.loginDao import LogarDao
from classes.classPrincipal import Principal


class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.__ui = Ui_frmLogin()
        self.__ui.setupUi(self)
        self.__logarDao = LogarDao()


        self.__ui.btnLogin.clicked.connect(self.__login)
        self.__ui.btnSair.clicked.connect(self.__sair)
        self.__ui.btnEsqueciSenha.clicked.connect(self.__esqueciSenha)

    def focusOutEvent(self, *args, **kwargs):
        text = self.text()
        self.setText(text.__str__().upper())
        return QtGui.QLineEdit.focusOutEvent(self, *args, **kwargs)

    def __login(self):
        __login = self.__ui.txtUsuario.text()
        __senha = self.__ui.txtSenha.text()

        __empresa = self.__logarDao.login(__login, __senha)

        if __empresa:
            for log in __empresa:
                principal.show()
                self.close()


    def __sair(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja sair do Programa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            sys.exit(0)

            
    def __esqueciSenha(self):
        pass


#if __name__ == '__main__':
app = QtGui.QApplication(sys.argv)
principal = Principal()
login = Login()
login.show()
sys.exit(app.exec_())
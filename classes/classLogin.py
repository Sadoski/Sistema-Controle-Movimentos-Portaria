import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetDadosUsuarios import DadosUsuario
from telas.frmLogin import Ui_frmLogin
from dao.loginDao import LogarDao
from classes.classPrincipal import Principal


class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self._ui = Ui_frmLogin()
        self._ui.setupUi(self)
        self._logarDao = LogarDao()

        self._ui.txtUsuario.textChanged.connect(self.upperCaseUsuario)
        self._ui.txtSenha.textChanged.connect(self.upperCaseSenha)

        self._ui.btnLogin.clicked.connect(self._login)
        self._ui.btnSair.clicked.connect(self._sair)
        self._ui.btnEsqueciSenha.clicked.connect(self._esqueciSenha)

        self._ui.txtUsuario.returnPressed.connect(self.focusSenha)

    def upperCaseUsuario(self):
        text = self._ui.txtUsuario.text()
        self._ui.txtUsuario.setText(text.upper())

    def upperCaseSenha(self):
        text = self._ui.txtSenha.text()
        self._ui.txtSenha.setText(text.upper())

    def focusSenha(self):
        self._ui.txtSenha.setFocus()

    def focusBotaoLogar(self):
        self._ui.btnLogin.setFocus()

    def _login(self):
        _login = self._ui.txtUsuario.text()
        _senha = self._ui.txtSenha.text()

        _empresa = self._logarDao.login(_login, _senha)

        if _empresa:
            for log in _empresa:
                id = int(log[0])
                nome = str(log[1])
                DadosUsuario(id, nome)
                principal.status(nome)
                principal.show()
                self.close()


    def _sair(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja sair do Programa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            sys.exit(0)

            
    def _esqueciSenha(self):
        pass


app = QtGui.QApplication(sys.argv)
principal = Principal()
login = Login()
login.show()
sys.exit(app.exec_())
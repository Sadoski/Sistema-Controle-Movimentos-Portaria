import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetDadosUsuarios import DadosUsuario
from telas.frmLogin import Ui_frmLogin
from dao.loginDao import LogarDao
from classes.classPrincipal import Principal
from telas.frmMesagemSair import Ui_frmMensagemSair


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
        #self._ui.btnEsqueciSenha.clicked.connect(self._esqueciSenha)

        self._ui.txtUsuario.returnPressed.connect(self.focusSenha)
        self._ui.txtSenha.returnPressed.connect(self._login)

    def upperCaseUsuario(self):
        self._ui.txtUsuario.setText(self._ui.txtUsuario.text().upper())

    def upperCaseSenha(self):
        self._ui.txtSenha.setText(self._ui.txtSenha.text().upper())

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
        self.dialogMensagem = QDialog(self, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.dialogMensagem.setWindowModality(Qt.NonModal)
        self.__mesagem = Ui_frmMensagemSair()
        self.__mesagem.setupUi(self.dialogMensagem)

        self.__mesagem.btnSim.clicked.connect(self.fechar)
        self.__mesagem.btnNao.clicked.connect(self.closeMesagem)


        self.dialogMensagem.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogMensagem.exec_()

    def fechar(self):
        sys.exit(0)

    def closeMesagem(self):
        self.dialogMensagem.close()

    def _esqueciSenha(self):
        pass


app = QtGui.QApplication(sys.argv)
principal = Principal()
login = Login()
login.show()
sys.exit(app.exec_())
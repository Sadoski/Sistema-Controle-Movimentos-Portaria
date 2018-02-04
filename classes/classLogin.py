import sys, time
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classUsuario import Usuario
from .classValidator import Validator
from controller.getSetDadosUsuarios import DadosUsuario
from telas.frmLogin import Ui_frmLogin
from dao.loginDao import LogarDao
from .classPrincipal import Principal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
app = QApplication(sys.argv)


class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self._ui = Ui_frmLogin()
        self._ui.setupUi(self)
        self.validator = Validator()
        self._ui.lblImagem.setFocus()
        self._logarDao = LogarDao()

        self._ui.txtUsuario.setValidator(self.validator)
        self._ui.txtSenha.setValidator(self.validator)

        self._ui.btnLogin.clicked.connect(self._login)
        self._ui.btnSair.clicked.connect(self._sair)
        #self._ui.btnEsqueciSenha.clicked.connect(self._esqueciSenha)

        self._ui.txtUsuario.returnPressed.connect(self.focusSenha)
        self._ui.txtSenha.returnPressed.connect(self._login)


    def focusSenha(self):
        self._ui.txtSenha.setFocus()

    def focusBotaoLogar(self):
        self._ui.btnLogin.setFocus()

    def focusBotaoSair(self):
        self._ui.btnSair.setFocus()

    def _login(self):
        _login = self._ui.txtUsuario.text()
        _senha = self._ui.txtSenha.text()

        __usuario = Usuario()
        __salto = self._logarDao.salto(_login)
        if __salto != False:
            __senhaCripto = __usuario.criptografar(_senha, __salto)
            _empresa = self._logarDao.login(_login, __senhaCripto)

            if _empresa:
                for log in _empresa:
                    id = int(log[0])
                    nome = str(log[1])
                    DadosUsuario(id, nome)
                    principal.status(nome)
                    principal.show()
                    self.close()
        else:
            MensagemBox().warning('Mensagem', "Usuário incorreto ou inexistente!")


    def _sair(self):
        try:
            _fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            def _fromUtf8(s):
                return s
        self.msgBox = QtGui.QMessageBox()
        self.msgBox.setWindowTitle("Mensagem")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/question.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBox.setWindowIcon(icon)
        self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("./imagens/icon-question.png")))
        self.msgBox.setText("Deseja sair do Programa?")
        btnSim = QtGui.QPushButton('Sim')
        self.msgBox.addButton(btnSim, QtGui.QMessageBox.YesRole)
        btnSim.clicked.connect(self.fechar)
        btnNao = QtGui.QPushButton('Não')
        self.msgBox.addButton(btnNao, QtGui.QMessageBox.YesRole)
        btnNao.clicked.connect(self.closeMesagem)
        btnNao.setFocus()
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()


    def fechar(self):
        sys.exit(0)

    def closeMesagem(self):
        self.msgBox.close()

    def _esqueciSenha(self):
        pass


principal = Principal()
login = Login()
login.show()
sys.exit(app.exec_())

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from telas.frmCadastroUsuarios import Ui_frmCadastroUsuarios


class UsuarioPermissao(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroUsuarios()
        self.ui.setupUi(self)

        # inicio botoes usuario
        self.ui.btnNovo.clicked.connect(self.ativarPesquisaUsuario)

        # fim botoes usuario

        # inicio botoes permissão
        self.ui.btnPermissoesNovo.clicked.connect(self.ativarPesquisaPermissao)
        # fim botoes permissão

    def ativarPesquisaUsuario(self):
        self.ui.grbDadosPesquisaFuncionario.setEnabled(True)
        self.ui.txtNomeFuncionarioUsuario.setEnabled(True)
        self.ui.btnCadPermiPesquisarFuncionario.setEnabled(True)
        self.ui.tabFuncioariosUsuario.setEnabled(True)

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)

    def ativarPesquisaPermissao(self):
        self.ui.grbDadosPesquisa.setEnabled(True)
        self.ui.txtNomeFuncionarioPermissoes.setEnabled(True)
        self.ui.btnCadPermiPesquisar.setEnabled(True)
        self.ui.tabFuncioariosPermissoes.setEnabled(True)

        self.ui.btnPermissoesNovo.setEnabled(False)
        self.ui.btnPermissoesSalvar.setEnabled(True)
        self.ui.btnPermissoesCancelar.setEnabled(True)
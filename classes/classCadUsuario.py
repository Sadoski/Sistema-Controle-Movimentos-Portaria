import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmCadUsuarios import Ui_frmCadastroUsuarios

class CadastroUsuarios(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroUsuarios()
        self.ui.setupUi(self)

        self.ui.btnNovo.clicked.connect(self.ativarPesquisaUsuario)
        #self.ui.btnCancelar.clicked.connect(self.cancelarUsuario)

        self.ui.btnAvacarPg1.clicked.connect(self.avancarVoltarPg2)
        self.ui.btnVoltarPg1.clicked.connect(self.avancarVoltarPg2)
        self.ui.btnAvacarPg2.clicked.connect(self.avancarVoltarPg1)
        self.ui.btnVoltarPg2.clicked.connect(self.avancarVoltarPg1)

    def avancarVoltarPg1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def avancarVoltarPg2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def ativarPesquisaUsuario(self):
        self.ui.grbFuncionarioPesquisa.setEnabled(True)
        self.ui.tabwCadPermUsuario.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)



    def limparCamposCheckBox(self):


        self.ui.cheBoxEntradaVeiculosCarregamentoAtivar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoCadastro.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoCancelar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoDeletar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosCarregamentoEditar.setChecked(False)

        self.ui.cheBoxEntradaVeiculosDescarregamentoAtivar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoCadastro.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoCancelar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoDeletar.setChecked(False)
        self.ui.cheBoxEntradaVeiculosDescarregamentoEditar.setChecked(False)

        self.ui.cheBoxEntrdaFuncionarioAtivar.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioCadastro.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioCancelar.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioDeletar.setChecked(False)
        self.ui.cheBoxEntrdaFuncionarioEditar.setChecked(False)

        self.ui.cheBoxEntrdaMaquinaAtivar.setChecked(False)
        self.ui.cheBoxEntrdaMaquinaCadastro.setChecked(False)
        self.ui.cheBoxEntrdaMaquinaCancelar.setChecked(False)
        self.ui.cheBoxEntrdaMaquinaDeletar.setChecked(False)
        self.ui.cheBoxEntrdaMaquinaEditar.setChecked(False)

        self.ui.cheBoxSaidaFuncionarioAtivar.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioCadastro.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioCancelar.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioDeletar.setChecked(False)
        self.ui.cheBoxSaidaFuncionarioEditar.setChecked(False)

        self.ui.cheBoxSaidaMaquinaAtivar.setChecked(False)
        self.ui.cheBoxSaidaMaquinaCadastro.setChecked(False)
        self.ui.cheBoxSaidaMaquinaCancelar.setChecked(False)
        self.ui.cheBoxSaidaMaquinaDeletar.setChecked(False)
        self.ui.cheBoxSaidaMaquinaEditar.setChecked(False)

        self.ui.cheBoxSaidaVeiculosDescarregamentoAtivar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoCadastro.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoCancelar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoDeletar.setChecked(False)
        self.ui.cheBoxSaidaVeiculosDescarregamentoEditar.setChecked(False)


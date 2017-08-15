import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmCadastroMotorista import Ui_frmCadastroMotorista

class CadastroMotoristas(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroMotorista()
        self.ui.setupUi(self)

        self.ui.txtNomeMotorista.returnPressed.connect(self.focusDataNacimento)
        self.ui.txtRg.returnPressed.connect(self.focusExpeditor)
        self.ui.txtExpeditor.returnPressed.connect(self.focusCpf)
        self.ui.txtCpf.returnPressed.connect(self.focusPis)
        self.ui.txtPis.returnPressed.connect(self.focusCnh)
        self.ui.txtCnh.returnPressed.connect(self.focusEndereco)
        self.ui.txtEndereco.returnPressed.connect(self.focusNumero)
        self.ui.txtNumero.returnPressed.connect(self.focusComplemento)
        self.ui.txtComplemento.returnPressed.connect(self.focusBairro)
        self.ui.txtBairro.returnPressed.connect(self.focusCep)
        self.ui.txtCep.returnPressed.connect(self.focusTelefone)
        self.ui.txtTelefone.returnPressed.connect(self.focusCelular)
        self.ui.txtCelular.returnPressed.connect(self.focusMarca)
        self.ui.txtMarca.returnPressed.connect(self.focusModelo)
        self.ui.txtModelo.returnPressed.connect(self.focusPlaca)

        self.ui.btnCadNovo.clicked.connect(self.botaoNovoCad)

    def focusDataNacimento(self):
        self.ui.txtDataNascimento.setFocus()

    def focusRg(self):
        self.ui.txtRg.setFocus()

    def focusExpeditor(self):
        self.ui.txtExpeditor.setFocus()

    def focusCpf(self):
        self.ui.txtCpf.setFocus()

    def focusPis(self):
        self.ui.txtPis.setFocus()

    def focusCnh(self):
        self.ui.txtCnh.setFocus()

    def focusCategoriaCnh(self):
        self.ui.txtCategoriaCnh.setFocus()

    def focusEndereco(self):
        self.ui.txtEndereco.setFocus()

    def focusNumero(self):
        self.ui.txtNumero.setFocus()

    def focusComplemento(self):
        self.ui.txtComplemento.setFocus()

    def focusBairro(self):
        self.ui.txtBairro.setFocus()

    def focusCep(self):
        self.ui.txtCep.setFocus()

    def focusTelefone(self):
        self.ui.txtTelefone.setFocus()

    def focusCelular(self):
        self.ui.txtCelular.setFocus()

    def focusTipoVeiculo(self):
        self.ui.txtTipoVeiculo.setFocus()

    def focusMarca(self):
        self.ui.txtMarca.setFocus()

    def focusModelo(self):
        self.ui.txtModelo.setFocus()

    def focusPlaca(self):
        self.ui.txtPlaca.setFocus()

    def botaoNovoCad(self):
        self.ui.btnCadNovo.setEnabled(False)
        self.ui.btnCadSalvar.setEnabled(True)
        self.ui.btnCadCancelar.setEnabled(True)

        self.ui.grbMotorista.setEnabled(True)
        self.ui.grbVeiculo.setEnabled(True)
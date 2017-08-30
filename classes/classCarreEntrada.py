import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.carregamentoEntradaDao import CarregamentoEntradaDao
from telas.frmEntradaVeiculosCarregamentos import Ui_frmEntradaVeiculosCarregamento

class CarregamentoEntrada(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaVeiculosCarregamento()
        self.ui.setupUi(self)

        self.ui.btnNovo.clicked.connect(self.botoesNovoCadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelarCadastro)

        self.ui.txtTipoCarga.currentIndexChanged.connect(self.pesquisaProduto)

    def pesquisarTiposCarga(self):
        __carrEntrada = CarregamentoEntradaDao()
        __carga = __carrEntrada.pesquisarTipoCarga()
        for i in __carga:
            self.ui.txtTipoCarga.addItem(i[0])

    def pesquisaProduto(self):
        __carrEntrada = CarregamentoEntradaDao()
        __produto = __carrEntrada.pesquisarProduto(str(self.ui.txtTipoCarga.currentText()))
        self.ui.txtProduto.clear()
        for i in __produto:
            self.ui.txtProduto.addItem(i[0])

    def botoesNovoCadastro(self):

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)

        self.ui.grbDadosMotorista.setEnabled(True)
        self.ui.grbDadosClienteDestinatario.setEnabled(True)
        self.ui.grbDadosEmpresaOrigem.setEnabled(True)
        self.ui.txtData.setEnabled(True)
        self.ui.txtHora.setEnabled(True)
        self.ui.txtTipoCarga.setEnabled(True)
        self.ui.txtProduto.setEnabled(True)
        self.pesquisarTiposCarga()

    def botoesCancelarCadastro(self):

        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)

        self.ui.grbDadosMotorista.setEnabled(False)
        self.ui.grbDadosClienteDestinatario.setEnabled(False)
        self.ui.grbDadosEmpresaOrigem.setEnabled(False)
        self.ui.txtData.setEnabled(False)
        self.ui.txtHora.setEnabled(False)
        self.ui.txtTipoCarga.setEnabled(False)
        self.ui.txtProduto.setEnabled(False)

    def limparCampos(self):
        self.ui.txtData.setDate(QDate.currentDate())
        self.ui.txtHora.setTime(QTime.currentTime())
        self.ui.txtTipoCarga.clear()
        self.ui.txtProduto.clear()

        self.ui.txtidFuncionario.clear()
        self.ui.txtNomeMotorista.clear()
        self.ui.txtModeloMotorista.clear()
        self.ui.txtMarcaMotorista.clear()
        self.ui.txtPlacaMotorista.clear()

        self.ui.txtIdClienteDestinatario.clear()
        self.ui.txtNomeClienteDestinatario.clear()
        self.ui.txtRazaoSocialClienteDestinatario.clear()
        self.ui.txtInscricaoEstaduaClienteDestinatario.clear()

        self.ui.txtIdEmpresaOrigem.clear()
        self.ui.txtNomeEmpresaOrigem.clear()
        self.ui.txtRazaoSocialEmpresaOrigem.clear()
        self.ui.txtInscricaoEstaduaEmpresaOrigem.clear()

    def cancelarCadastro(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja cancelar essa operação?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botoesCancelarCadastro()
            self.limparCampos()
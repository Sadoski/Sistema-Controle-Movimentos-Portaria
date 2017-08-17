import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo
from telas.frmEntradaNotasRomaneios import Ui_frmEntradaNotaRomaneios

class CadastroEmpresa(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaNotaRomaneios()
        self.ui.setupUi(self)

        self.unidadeMedida()
        self.pesquisarTiposCarga()

        self.ui.txtNomeEmitente.returnPressed.connect(self.pesquisarFornecedor)
        self.ui.txtFantasiaDestinatario.returnPressed.connect(self.pesquisarEmpresa)
        self.ui.txtNomeMotorista.returnPressed.connect(self.pesquisarMotorista)

        self.ui.txtNomeEmitente.returnPressed.connect(self.focusEmpresa)
        self.ui.txtFantasiaDestinatario.returnPressed.connect(self.focusMotorista)
        self.ui.txtNomeMotorista.returnPressed.connect(self.focusNumNota)
        self.ui.txtNumeroNotaFiscal.returnPressed.connect(self.focusDataEmissao)
        self.ui.txtValorTotal.returnPressed.connect(self.focusNumRomaneio)
        self.ui.txtNumeroRomaneio.returnPressed.connect(self.focusMetragem)
        self.ui.txtQuantidade.returnPressed.connect(self.focusValorUnitario)


        self.ui.txtTipoCargaServico.currentIndexChanged.connect(self.pesquisaProduto)

    def focusEmpresa(self):
        self.ui.txtFantasiaDestinatario.setFocus()

    def focusMotorista(self):
        self.ui.txtNomeMotorista.setFocus()

    def focusNumNota(self):
        self.ui.txtNumeroNotaFiscal.setFocus()

    def focusDataEmissao(self):
        self.ui.txtDataEmissao.setFocus()

    def focusValorTotal(self):
        self.ui.txtValorTotal.setFocus()

    def focusNumRomaneio(self):
        self.ui.txtNumeroRomaneio.setFocus()

    def focusMetragem(self):
        self.ui.txtMetragemMadeira.setFocus()

    def focusQuantidade(self):
        self.ui.txtQuantidade.setFocus()

    def focusValorUnitario(self):
        self.ui.txtValorUnitario.setFocus()


    def unidadeMedida(self):
        lista = ["UN", "KM", "HM", "DAM", "M", "DM", "CM", "MM", "KM²", "HM²", "DAM²", "M²", "DM²", "CM²", "MM²", "KM³", "HM³", "DAM³", "M³", "DM³", "CM³", "MM³", "T", "KG", "HG", "DAG", "G", "DG", "CG", "MG", "KL", "HL", "DAL", "L", "DL", "CL", "ML"]
        for i in lista:
            self.ui.txtUn.addItem(i)

    def pesquisarTiposCarga(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __cargo = __notaRomaneio.pesquisarTipoCarga()
        for i in __cargo:
            self.ui.txtTipoCargaServico.addItem(i[0])

    def pesquisaProduto(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __produto = __notaRomaneio.pesquisarProduto(str(self.ui.txtTipoCargaServico.currentText()))
        self.ui.txtTipoProdutoServico.clear()
        for i in __produto:
            self.ui.txtTipoProdutoServico.addItem(i[0])

    def limparCamposEmitente(self):
        self.ui.txtIdEmitente.clear()
        self.ui.txtRazaoSocialEmitente.clear()
        self.ui.txtCnpjEmitente.clear()
        self.ui.txtInscricaoEstaduaEmitente.clear()

    def pesquisarFornecedor(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __fornecedor = __notaRomaneio.pesquisarFornecedor(str(self.ui.txtNomeEmitente.text()))
        if __fornecedor == False:
            self.limparCamposEmitente()
        else:
            self.limparCamposEmitente()
            for i in __fornecedor:
                self.ui.txtIdEmitente.setText(str(i[0]))
                self.ui.txtRazaoSocialEmitente.setText(i[1])
                self.ui.txtCnpjEmitente.setText(i[2])
                self.ui.txtInscricaoEstaduaEmitente.setText(i[3])

    def limparCamposDestinatario(self):
        self.ui.txtIdDestinatario.clear()
        self.ui.txtRazaoSocialDestinatario.clear()
        self.ui.txtCnpjDestinatario.clear()
        self.ui.txtInscricaoEstaduaDestinatario.clear()

    def pesquisarEmpresa(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __fornecedor = __notaRomaneio.pesquisarEmpresa(str(self.ui.txtFantasiaDestinatario.text()))
        if __fornecedor == False:
            self.limparCamposDestinatario()
        else:
            self.limparCamposDestinatario()
            for i in __fornecedor:
                self.ui.txtIdDestinatario.setText(str(i[0]))
                self.ui.txtRazaoSocialDestinatario.setText(i[1])
                self.ui.txtCnpjDestinatario.setText(i[2])
                self.ui.txtInscricaoEstaduaDestinatario.setText(i[3])

    def limparCamposMotorista(self):
        self.ui.txtidMotorista.clear()
        self.ui.txtRg.clear()
        self.ui.txtCpf.clear()
        self.ui.txtMarca.clear()
        self.ui.txtModelo.clear()
        self.ui.txtPlaca.clear()


    def pesquisarMotorista(self):
        __notaRomaneio = NotaFiscalRomanieo()
        __motorista = __notaRomaneio.pesquisarMotorista(str(self.ui.txtNomeMotorista.text()))
        if __motorista == False:
            self.limparCamposMotorista()
        else:
            self.limparCamposMotorista()
            for i in __motorista:
                self.ui.txtidMotorista.setText(str(i[0]))
                self.ui.txtRg.setText(i[1])
                self.ui.txtCpf.setText(i[2])
                self.ui.txtMarca.setText(i[3])
                self.ui.txtModelo.setText(i[4])
                self.ui.txtPlaca.setText(i[5])
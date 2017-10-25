import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.descarregamentoEntradaDao import DescarreEntradaDao
from telas.frmEntradaVeiculosDescarregamento import Ui_frmEntradaVeiculosDescarregamento

class DescaEntrada(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmEntradaVeiculosDescarregamento()
        self.ui.setupUi(self)

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.radbtnDescarregamentoComNotaFiscal.clicked.connect(self.pesquisarNota)
        self.ui.radbtnDescarregamentoSemNotaFiscal.clicked.connect(self.ativarCampos)
        self.ui.radbtnNumeroNota.clicked.connect(self.ativarPesquisa)
        self.ui.radbtnNumeroRomaneio.clicked.connect(self.ativarPesquisa)
        self.ui.radbtnEmitente.clicked.connect(self.ativarPesquisa)
        self.ui.radbtnDstinatario.clicked.connect(self.ativarPesquisa)
        self.ui.radbtnMotorista.clicked.connect(self.ativarPesquisa)

        self.ui.txtPesquisar.returnPressed.connect(self.pesquisar)

    def novo(self):
        self.ui.grbTipoOperacao.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)

    def cancelar(self):
        self.ui.grbTipoOperacao.setEnabled(False)
        self.ui.grbTipoPesquisa.setEnabled(False)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)

        self.desativarCampos()

    def pesquisarNota(self):
        self.ui.grbTipoPesquisa.setEnabled(True)
        self.desativarCampos()

    def ativarPesquisa(self):
        self.ui.txtPesquisar.setEnabled(True)
        self.ui.btnPesquisarNotaFiscal.setEnabled(True)
        self.ui.tabPesquisar.setEnabled(True)

        self.ui.txtPesquisar.setFocus()

    def desativarCampos(self):
        self.ui.txtPesquisar.setEnabled(False)
        self.ui.btnPesquisarNotaFiscal.setEnabled(False)
        self.ui.tabPesquisar.setEnabled(False)

        self.ui.txtData.setEnabled(False)
        self.ui.txtHora.setEnabled(False)

        self.ui.grbNotaFiscal.setEnabled(False)
        self.ui.grbDadosEmitente.setEnabled(False)
        self.ui.grbDadosDestinatario.setEnabled(False)
        self.ui.grbDadosMotorista.setEnabled(False)

        self.limparNotasFiscal()
        self.limparEmitente()
        self.limparDestinatario()
        self.limparMotorista()

    def ativarCampos(self):
        self.limparPesquisa()
        self.ui.grbTipoPesquisa.setEnabled(False)
        self.ui.txtPesquisar.setEnabled(False)
        self.ui.btnPesquisarNotaFiscal.setEnabled(False)
        self.ui.tabPesquisar.setEnabled(False)


        self.limparNotasFiscal()

        self.ui.txtData.setEnabled(True)
        self.ui.txtHora.setEnabled(True)

        self.ui.grbNotaFiscal.setEnabled(False)
        self.ui.grbDadosEmitente.setEnabled(True)
        self.ui.grbDadosDestinatario.setEnabled(True)
        self.ui.grbDadosMotorista.setEnabled(True)

    def limparTabelaPesquisa(self):
        for i in reversed(range(self.ui.tabPesquisar.rowCount())):
            self.ui.tabPesquisar.removeRow(i)

    def limparPesquisa(self):
        self.ui.txtPesquisar.clear()
        self.limparTabelaPesquisa()

    def limparNotasFiscal(self):
        self.ui.txtNumeroNotaFiscal.clear()
        self.ui.txtTipoProduto.clear()
        self.ui.txtCertificada.clear()
        self.ui.txtNumeroRomaneio.clear()
        self.ui.txtMetragemMadeira.clear()

    def limparEmitente(self):
        self.ui.txtIdEmitente.clear()
        self.ui.txtNomeEmitente.clear()
        self.ui.txtRazaoSocialEmitente.clear()
        self.ui.txtCnpjEmitente.clear()
        self.ui.txtInscricaoEstaduaEmitente.clear()
        self.ui.txtEnderecoEmitente.clear()
        self.ui.txtNumeroEmitente.clear()
        self.ui.txtComplementoEmitente.clear()
        self.ui.txtBairroEmitente.clear()
        self.ui.txtCidadeEmitente.clear()
        self.ui.txtEstadoEmitente.clear()
        self.ui.txtCepEmitente.clear()

    def limparDestinatario(self):
        self.ui.txtIdDestinatario.clear()
        self.ui.txtFantasiaDestinatario.clear()
        self.ui.txtRazaoSocialDestinatario.clear()
        self.ui.txtCnpjDestinatario.clear()
        self.ui.txtInscricaoEstaduaDestinatario.clear()
        self.ui.txtEnderecoDestinatario.clear()
        self.ui.txtNumeroDestinatario.clear()
        self.ui.txtComplementoDestinatario.clear()
        self.ui.txtBairroDestinatario.clear()
        self.ui.txtCidadeDestinatario.clear()
        self.ui.txtEstadoDestinatario.clear()
        self.ui.txtCepDestinatario.clear()

    def limparMotorista(self):
        self.ui.txtidFuncionario.clear()
        self.ui.txtNomeFuncionario.clear()
        self.ui.txtModelo.clear()
        self.ui.txtMarca.clear()
        self.ui.txtPlaca.clear()

    def pesquisar(self):
        des = DescarreEntradaDao()
        if self.ui.radbtnNumeroNota.isChecked():
            pesquisarCod = des.pesquisarNumeroNota(self.ui.txtPesquisar.text())

            qtde_registros = len(pesquisarCod)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in pesquisarCod:
                # capturando os dados da tupla

                numNota = pesqui[0]
                numRomaneio = pesqui[1]
                if pesqui[2] == 1:
                    certificada = 'Certificada'

                else:
                    certificada = 'Não Certificada'
                metragem = pesqui[3]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(numNota)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(numRomaneio)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(certificada)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(metragem)))

                linha += 1

        elif self.ui.radbtnNumeroRomaneio.isChecked():
            pesquisarCod = des.pesquisarNumeroRomaneio(self.ui.txtPesquisar.text())

            qtde_registros = len(pesquisarCod)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in pesquisarCod:
                # capturando os dados da tupla

                numNota = pesqui[0]
                numRomaneio = pesqui[1]
                if pesqui[2] == 1:
                    certificada = 'Certificada'

                else:
                    certificada = 'Não Certificada'
                metragem = pesqui[3]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(numNota)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(numRomaneio)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(certificada)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(metragem)))

                linha += 1

        elif self.ui.radbtnEmitente.isChecked():
            pass
        elif self.ui.radbtnDstinatario.isChecked():
            pass
        elif self.ui.radbtnMotorista.isChecked():
            pass



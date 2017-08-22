import sys
from PyQt4 import QtGui, QtCore

from dao.pesquisarNotaFiscalRomaneioDao import PesquisarNotaFiscalRomaneioDao
from telas.frmPesquisarNotasFiscais import Ui_frmConsultarNotasFiscais

class PesquisarNotaFiscal(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmConsultarNotasFiscais()
        self.ui.setupUi(self)

        self.ui.txtPesquisar.returnPressed.connect(self.pesquisar)

    def pesquisar(self):
        if self.ui.radBtnNumNotaFiscal.isChecked():
            __nunNota = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarNumeroNota(__nunNota)

            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                numNotaFiscal = pesqui[1]
                data = pesqui[2]
                valorTotal = pesqui[3]
                codFornecedor = pesqui[4]
                forneFantasia = pesqui[5]
                forneRazaoSocial = pesqui[6]
                forneCnpj = pesqui[7]
                forneInsEstadual = pesqui[8]
                codEmpresa = pesqui[9]
                emprFantasia = pesqui[10]
                emprRazaoSocial = pesqui[11]
                emprCnpj = pesqui[12]
                emprInsEstadual = pesqui[13]
                codMotorista = pesqui[14]
                nomeMotorista = pesqui[15]
                rg = pesqui[16]
                cpf = pesqui[17]
                codRomaneio = pesqui[18]
                numRomaneio = pesqui[19]
                if pesqui[20] == 1:
                    certificada = "Certificada"
                else:
                    certificada = "Não Certificada"
                metragem = pesqui[21]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(numNotaFiscal)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(valorTotal)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(codFornecedor)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(forneFantasia)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(forneRazaoSocial)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(forneCnpj)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(forneInsEstadual)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(codEmpresa)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(emprFantasia)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(emprRazaoSocial)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(emprCnpj)))
                self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(emprInsEstadual)))
                self.ui.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(codMotorista)))
                self.ui.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(nomeMotorista)))
                self.ui.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(codRomaneio)))
                self.ui.tabPesquisar.setItem(linha, 19, QtGui.QTableWidgetItem(str(numRomaneio)))
                self.ui.tabPesquisar.setItem(linha, 20, QtGui.QTableWidgetItem(str(certificada)))
                self.ui.tabPesquisar.setItem(linha, 21, QtGui.QTableWidgetItem(str(metragem)))

                linha += 1

        elif self.ui.radBtnRomaneio.isChecked():
            __numRomaneio = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarNumeroRomaneio(__numRomaneio)

            qtde_registros = len(__retorno)
            self.ui.tabPesquisar.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __retorno:
                # capturando os dados da tupla

                codigo = pesqui[0]
                numNotaFiscal = pesqui[1]
                data = pesqui[2]
                valorTotal = pesqui[3]
                codFornecedor = pesqui[4]
                forneFantasia = pesqui[5]
                forneRazaoSocial = pesqui[6]
                forneCnpj = pesqui[7]
                forneInsEstadual = pesqui[8]
                codEmpresa = pesqui[9]
                emprFantasia = pesqui[10]
                emprRazaoSocial = pesqui[11]
                emprCnpj = pesqui[12]
                emprInsEstadual = pesqui[13]
                codMotorista = pesqui[14]
                nomeMotorista = pesqui[15]
                rg = pesqui[16]
                cpf = pesqui[17]
                codRomaneio = pesqui[18]
                numRomaneio = pesqui[19]
                if pesqui[20] == 1:
                    certificada = "Certificada"
                else:
                    certificada = "Não Certificada"
                metragem = pesqui[21]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(numNotaFiscal)))
                self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(valorTotal)))
                self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(codFornecedor)))
                self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(forneFantasia)))
                self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(forneRazaoSocial)))
                self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(forneCnpj)))
                self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(forneInsEstadual)))
                self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(codEmpresa)))
                self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(emprFantasia)))
                self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(emprRazaoSocial)))
                self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(emprCnpj)))
                self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(emprInsEstadual)))
                self.ui.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(codMotorista)))
                self.ui.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(nomeMotorista)))
                self.ui.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(codRomaneio)))
                self.ui.tabPesquisar.setItem(linha, 19, QtGui.QTableWidgetItem(str(numRomaneio)))
                self.ui.tabPesquisar.setItem(linha, 20, QtGui.QTableWidgetItem(str(certificada)))
                self.ui.tabPesquisar.setItem(linha, 21, QtGui.QTableWidgetItem(str(metragem)))

                linha += 1
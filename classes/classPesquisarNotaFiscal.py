from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *

from controller.getSetPesquisaNotaFiscal import PesquisaNotaFiscal
from dao.pesquisarNotaFiscalRomaneioDao import PesquisarNotaFiscalRomaneioDao
from telas.frmPesquisarNotasFiscais import Ui_frmConsultarNotasFiscais


class PesquisarNotaFiscal(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmConsultarNotasFiscais()
        self.ui.setupUi(self)

        self.ui.txtPesquisar.returnPressed.connect(self.pesquisar)
        self.ui.radBtnDataLanamento.clicked.connect(self.ativarDataLancamento)
        self.ui.radBtnDataPeriodos.clicked.connect(self.ativarData)
        self.ui.radBtnFantasiaEmitente.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnRazaoSocialEmitente.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnCnpjEmitente.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnIncrisaoEstadualEmitente.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnFantasiaDestinatario.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnRazaoSocialDestinatario.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnCnpjDestinatario.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnIncrisaoEstadualDestinatario.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnNumNotaFiscal.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnRomaneio.clicked.connect(self.ativarPesquisa)

        self.ui.btnPesquisar.clicked.connect(self.pesquisar)

        self.ui.tabPesquisar.doubleClicked.connect(self.setarCampos)

    def ativarDataLancamento(self):
        self.ui.txtDataInicial.setEnabled(True)
        self.ui.txtDataFinal.setEnabled(False)

        self.ui.txtPesquisar.setEnabled(False)
        self.ui.btnPesquisar.setEnabled(True)

    def ativarData(self):
        self.ui.txtDataInicial.setEnabled(True)
        self.ui.txtDataFinal.setEnabled(True)

        self.ui.txtPesquisar.setEnabled(False)

        self.ui.btnPesquisar.setEnabled(True)

    def ativarPesquisa(self):
        self.ui.txtDataInicial.setEnabled(False)
        self.ui.txtDataFinal.setEnabled(False)

        self.ui.txtPesquisar.setEnabled(True)

        self.ui.btnPesquisar.setEnabled(True)

    def formatarData(self, data):
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:8]

        return ("%s%s%s" % (ano, mes, dia))

    def removerCaracter(self, i):
        i = str(i)
        i = i.replace('.', '')
        i = i.replace(',', '')
        i = i.replace('/', '')
        i = i.replace('-', '')
        i = i.replace('(', '')
        i = i.replace(')', '')
        i = i.replace('\\', '')
        return i

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

        elif self.ui.radBtnFantasiaDestinatario.isChecked():
            __fantasiaDestinatario = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarFantasiaDest(__fantasiaDestinatario)

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

        elif self.ui.radBtnRazaoSocialDestinatario.isChecked():
            __razaoSocialDestinatario = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarRozaoSocialDest(__razaoSocialDestinatario)

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

        elif self.ui.radBtnCnpjDestinatario.isChecked():
            __cnpjDestinatario = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarCnpjDest(__cnpjDestinatario)

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

        elif self.ui.radBtnIncrisaoEstadualDestinatario.isChecked():
            __insDestinatario = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarInsEstadualDest(__insDestinatario)

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

        elif self.ui.radBtnFantasiaEmitente.isChecked():
            __fantasiaEmitente = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarFantasiaEmit(__fantasiaEmitente)

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

        elif self.ui.radBtnRazaoSocialEmitente.isChecked():
            __razaoSocialEmitente = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarRozaoSocialEmit(__razaoSocialEmitente)

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

        elif self.ui.radBtnCnpjEmitente.isChecked():
            __cnpjEmitente = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarCnpjEmit(__cnpjEmitente)

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

        elif self.ui.radBtnIncrisaoEstadualEmitente.isChecked():
            __insEmitente = self.ui.txtPesquisar.text()
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarInsEstadualEmit(__insEmitente)

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

        elif self.ui.radBtnDataLanamento.isChecked():
            __dataLancamento = self.formatarData(self.removerCaracter(self.ui.txtDataInicial.text()))
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarDataLancamento(__dataLancamento)

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

        elif self.ui.radBtnDataPeriodos.isChecked():
            __dataIni = self.formatarData(self.removerCaracter(self.ui.txtDataInicial.text()))
            __dataFim = self.formatarData(self.removerCaracter(self.ui.txtDataFinal.text()))
            __pesDao = PesquisarNotaFiscalRomaneioDao()
            __retorno = __pesDao.pesquisarDataPeriodo(__dataIni, __dataFim)

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
        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Selecione uma das opções de pesquisa")

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def setarCampos(self, dados):

            itens = []

            for item in self.ui.tabPesquisar.selectedItems():
                itens.append(item.text())

            codNotaFiscal = str(itens[0])
            print(codNotaFiscal)
            numeroNotaFiscal = str(itens[1])
            print(numeroNotaFiscal)
            dataNota = self.formatarDataRetorno(itens[2])
            print(dataNota)
            valorTotl = str(itens[3])
            print(valorTotl)
            codEmitente = str(itens[4])
            print(codEmitente)
            fantasiaEmitente = itens[5]
            print(fantasiaEmitente)
            razaoSocialEmitente = itens[6]
            print(razaoSocialEmitente)
            cnpjEmitente = str(itens[7])
            print(cnpjEmitente)
            insEstadualEmitente = str(itens[8])
            print(insEstadualEmitente)
            codDestinatario = str(itens[9])
            print(codDestinatario)
            fantasiaDestinatario = itens[10]
            print(fantasiaDestinatario)
            razaoSocialDestinatario = itens[11]
            print(razaoSocialDestinatario)
            cnpjDestinatario = str(itens[12])
            print(cnpjDestinatario)
            insEstadualDestinatario = str(itens[13])
            print(insEstadualDestinatario)
            codMotorista = str(itens[14])
            print(codMotorista)
            nomeMotorista = itens[15]
            print(nomeMotorista)
            rg = str(itens[16])
            print(rg)
            cpf = str(itens[17])
            print(cpf)
            codRomaneio = str(itens[18])
            print(codRomaneio)
            numRomaneio = str(itens[19])
            print(numRomaneio)
            if itens[20] == 'Certificada':
                certificada = True
            elif itens[20] == 'Não Certificada':
                certificada = False
            else:
                return None
            print(certificada)
            metragem = itens[21]
            print(metragem)

            from .classNotasFiscal import CadastroNotaFiscal
            __dados = PesquisaNotaFiscal(codNotaFiscal, numeroNotaFiscal, dataNota, valorTotl, codEmitente, fantasiaEmitente, razaoSocialEmitente, cnpjEmitente, insEstadualEmitente, codDestinatario, fantasiaDestinatario, razaoSocialDestinatario, cnpjDestinatario, insEstadualDestinatario, codMotorista, nomeMotorista, rg, cpf, codRomaneio, numRomaneio, certificada, metragem)

            __ca = CadastroNotaFiscal()
            __ca.setCampos(__dados)
            __ca.ui.txtFantasiaDestinatario.setText(str(numeroNotaFiscal))
            __ca.window()
            self.close()



import sys
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.CSV import RelatorioPessoaFisicaCSV
from classes.HTML import TAG
from classes.classValidator import Validator
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from telas.frmRelatorio import Ui_frmRelatorio


class Relatorio(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmRelatorio()
        self.ui.setupUi(self)
        self.validator = Validator()

        self.ui.radBtnPessoaFisica.clicked.connect(self.ativarTab)
        self.ui.radBtnPessoaJuridica.clicked.connect(self.ativarTab)

        self.ui.txtPesquisar.returnPressed.connect(self.pesquisar)
        self.ui.btnPesquisar.clicked.connect(self.pesquisar)

        self.ui.btnGerarCsv.clicked.connect(self.gerarCsv)
        self.ui.btnGerarHtml.clicked.connect(self.gerarHtml)

    def removerColuna(self):
        self.ui.tabPesquisar.horizontalHeader().hide()
        self.ui.tabPesquisar.verticalHeader().hide()


    def rowTab(self):
        if self.ui.radBtnPessoaFisica.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(18)
            self.ui.tabPesquisar.setRowCount(0)
            self.ui.tabPesquisar.setHorizontalHeaderLabels(['Codigo', 'Nome', 'Sobrenome', 'CPF', 'RG', 'Expeditor', 'UF', 'Aniversario', 'Gênero', 'Mãe', 'Pai', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP'])
        elif self.ui.radBtnPessoaJuridica.isChecked():
            self.removerColuna()
            self.ui.tabPesquisar.setColumnCount(13)
            self.ui.tabPesquisar.setRowCount(0)
            self.ui.tabPesquisar.setHorizontalHeaderLabels(["Cod.", "Razão Social", "Fantasia", "CNPJ", "Ins. Estadual", "Site", "Endereço", "Número", "Complemento", "Bairro", "Cidade", "Estado", "CEP"])

    def limparRad(self):
        self.ui.radBtn1.setText("")
        self.ui.radBtn2.setText("")
        self.ui.radBtn3.setText("")
        self.ui.radBtn4.setText("")
        self.ui.radBtn5.setText("")
        self.ui.radBtn6.setText("")

    def ativarTab(self):
        if self.ui.radBtnPessoaFisica.isChecked():
            self.ui.grbPesquisaRelatorio.setEnabled(True)
            self.ui.txtPesquisar.setEnabled(True)
            self.ui.btnPesquisar.setEnabled(True)
            self.ui.btnGerarCsv.setEnabled(True)
            self.ui.btnGerarHtml.setEnabled(True)
            self.ui.tabPesquisar.setEnabled(True)
            self.limparRad()
            self.ui.radBtn1.setText("Codigo")
            self.ui.radBtn2.setText("Nome")
            self.ui.radBtn3.setText("Sobrenome")
            self.ui.radBtn4.setText("CPF")
            self.ui.radBtn5.setText("RG")
            self.ui.radBtn6.setEnabled(False)
            self.rowTab()


    def pesquisar(self):
        if self.ui.radBtnPessoaFisica.isChecked():

            fisicaDao = PesquisarPessoaFisicaDao()

            if self.ui.radBtn1.isChecked():
                dados = fisicaDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn2.isChecked():
                dados = fisicaDao.pesquisaNome(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn3.isChecked():
                dados = fisicaDao.pesquisaApelido(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn4.isChecked():
                dados = fisicaDao.pesquisaCpf(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn5.isChecked():
                dados = fisicaDao.pesquisaRg(self.ui.txtPesquisar.text())
                self.setarTabelaPesquisa(dados)
            elif self.ui.radBtn6.isChecked():
                pass

    def setarTabelaPesquisa(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            sobrenome = pesqui[2]
            cpf = pesqui[3]
            rg = pesqui[4]
            expeditor = pesqui[5]
            uf = pesqui[6]
            data = pesqui[7]
            sexo = pesqui[8]
            mae = pesqui[9]
            pai = pesqui[10]
            endereco = pesqui[11]
            numero = pesqui[12]
            complemento = pesqui[13]
            bairro = pesqui[14]
            cidade = pesqui[15]
            estado = pesqui[16]
            cep = pesqui[17]


            # preenchendo o grid de pesquisa
            self.ui.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.ui.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.ui.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(sobrenome)))
            self.ui.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
            self.ui.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
            self.ui.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
            self.ui.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
            self.ui.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(data)))
            self.ui.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(sexo)))
            self.ui.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(mae)))
            self.ui.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(pai)))
            self.ui.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(endereco)))
            self.ui.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(numero)))
            self.ui.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(complemento)))
            self.ui.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(bairro)))
            self.ui.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cidade)))
            self.ui.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(estado)))
            self.ui.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cep)))

            linha += 1

    def gerarCsv(self):
        if self.ui.radBtnPessoaFisica.isChecked():

            fisicaDao = PesquisarPessoaFisicaDao()

            if self.ui.radBtn1.isChecked():
                dados = fisicaDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = fisicaDao.pesquisaNome(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = fisicaDao.pesquisaApelido(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = fisicaDao.pesquisaCpf(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = fisicaDao.pesquisaRg(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass

    def gerarHtml(self):
        if self.ui.radBtnPessoaFisica.isChecked():

            fisicaDao = PesquisarPessoaFisicaDao()

            if self.ui.radBtn1.isChecked():
                dados = fisicaDao.pesquisaCodigo(self.ui.txtPesquisar.text())
                if dados != "":
                    html = TAG
                    html.gerar(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn2.isChecked():
                dados = fisicaDao.pesquisaNome(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn3.isChecked():
                dados = fisicaDao.pesquisaApelido(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn4.isChecked():
                dados = fisicaDao.pesquisaCpf(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn5.isChecked():
                dados = fisicaDao.pesquisaRg(self.ui.txtPesquisar.text())
                if dados != "":
                    RelatorioPessoaFisicaCSV(dados)
                else:
                    QMessageBox.warning(QWidget(), 'Atenção', "Não à dados de pesquisa para gerar o arquivo")
            elif self.ui.radBtn6.isChecked():
                pass
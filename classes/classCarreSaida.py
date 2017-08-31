import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.carregamentoSaidaDao import CarregamentoSaidaDao
from telas.frmSaidaVeiculosCarregamentos import Ui_frmSaidaVeiculosCarregamento

class CarregamentoSaida(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaVeiculosCarregamento()
        self.ui.setupUi(self)
        self.idEntrada = None

        self.ui.btnNovo.clicked.connect(self.botoesNovoCadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelarCadastro)

        self.ui.radbtnEntrouVazio.clicked.connect(self.operacao)
        self.ui.radbtnEntrouCarregado.clicked.connect(self.operacao)

        self.ui.radbtnMotorista.clicked.connect(self.ativarPesquisa)
        self.ui.radbtnMarcaVeiculo.clicked.connect(self.ativarPesquisa)
        self.ui.radbtnModeloVeiculo.clicked.connect(self.ativarPesquisa)
        self.ui.radbtnPlacaVeiculo.clicked.connect(self.ativarPesquisa)

        self.ui.txtTipoCarga.currentIndexChanged.connect(self.pesquisaProduto)

        self.ui.txtPesquisar.returnPressed.connect(self.pesquisarEntrada)

        self.ui.tabPesquisa.doubleClicked.connect(self.tablePesquisa)

    def pesquisarTiposCarga(self):
        __carrSaida= CarregamentoSaidaDao()
        __carga = __carrSaida.pesquisarTipoCarga()
        for i in __carga:
            self.ui.txtTipoCarga.addItem(i[0])

    def pesquisaProduto(self):
        __carrSaida = CarregamentoSaidaDao()
        __produto = __carrSaida.pesquisarProduto(str(self.ui.txtTipoCarga.currentText()))
        self.ui.txtProduto.clear()
        for i in __produto:
            self.ui.txtProduto.addItem(i[0])

    def botoesNovoCadastro(self):

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)

        self.ui.grbTipoOperacao.setEnabled(True)

    def botaoEditarCadastro(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)

        self.ui.grbDadosMotorista.setEnabled(True)
        self.ui.grbDadosEmpresaOrigem.setEnabled(True)
        self.ui.grbDadosEmpresaOrigem.setEnabled(True)

    def botoesCancelarCadastro(self):

        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)

        self.ui.grbTipoOperacao.setEnabled(False)
        self.ui.grbTipoPesquisa.setEnabled(False)
        self.ui.grbDadosMotorista.setEnabled(False)
        self.ui.grbDadosClienteDestinatario.setEnabled(False)
        self.ui.grbDadosEmpresaOrigem.setEnabled(False)
        self.ui.txtPesquisar.setEnabled(False)
        self.ui.btnPesquisar.setEnabled(False)
        self.ui.txtData.setEnabled(False)
        self.ui.txtHora.setEnabled(False)
        self.ui.txtTipoCarga.setEnabled(False)
        self.ui.txtProduto.setEnabled(False)
        self.idEntrada = None

    def operacao(self):
        self.ui.grbTipoPesquisa.setEnabled(True)

    def ativarPesquisa(self):
        self.ui.txtPesquisar.setEnabled(True)
        self.ui.btnPesquisar.setEnabled(True)

    def pesquisarEntrada(self):
        self.ui.tabPesquisa.setEnabled(True)
        if self.ui.radbtnMotorista.isChecked():
            __carrSaida = CarregamentoSaidaDao()
            _pesquisar = __carrSaida.pesquisarNomeMotorista(self.ui.txtPesquisar.text())
            print(_pesquisar)
            qtde_registros = len(_pesquisar)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                idEntrada = str(pesqui[0])
                codMotorista = str(pesqui[1])
                nomeMotorista = pesqui[2]
                marcaVeiculo = pesqui[3]
                modeloVeiculo = pesqui[4]
                placaVeiculo = pesqui[5]
                data = str(pesqui[6])
                hora = str(pesqui[7])
                carga = pesqui[8]
                produto = pesqui[9]
                codDestinatario = str(pesqui[10])
                nomeDestinatario = pesqui[11]
                razaoDestinatario = pesqui[12]
                cnpjDestinatario = str(pesqui[13])
                insEstaDestinatario = str(pesqui[14])
                codEmpresa = str(pesqui[15])
                nomeEmpresa = pesqui[16]
                razaoEmpresa = pesqui[17]
                cnpjEmpresa = str(pesqui[18])
                insEstaEmpresa = str(pesqui[19])

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idEntrada)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codMotorista)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nomeMotorista)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(marcaVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(modeloVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(placaVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tabPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(carga)))
                self.ui.tabPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(produto)))
                self.ui.tabPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(codDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(nomeDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(razaoDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cnpjDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(insEstaDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(codEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(nomeEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEstaEmpresa)))


                linha += 1

        elif self.ui.radbtnMarcaVeiculo.isChecked():
            __carrSaida = CarregamentoSaidaDao()
            _pesquisar = __carrSaida.pesquisarNomeMotorista(self.ui.txtPesquisar.text())

            qtde_registros = len(_pesquisar)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:

                # capturando os dados da tupla

                idEntrada = str(pesqui[0])
                codMotorista = str(pesqui[1])
                nomeMotorista = pesqui[2]
                marcaVeiculo = pesqui[3]
                modeloVeiculo = pesqui[4]
                placaVeiculo = pesqui[5]
                data = str(pesqui[6])
                hora = str(pesqui[7])
                carga = pesqui[8]
                produto = pesqui[9]
                codDestinatario = str(pesqui[10])
                nomeDestinatario = pesqui[11]
                razaoDestinatario = pesqui[12]
                cnpjDestinatario = str(pesqui[13])
                insEstaDestinatario = str(pesqui[14])
                codEmpresa = str(pesqui[15])
                nomeEmpresa = pesqui[16]
                razaoEmpresa = pesqui[17]
                cnpjEmpresa = str(pesqui[18])
                insEstaEmpresa = str(pesqui[19])

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idEntrada)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codMotorista)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nomeMotorista)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(marcaVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(modeloVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(placaVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tabPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(carga)))
                self.ui.tabPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(produto)))
                self.ui.tabPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(codDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(nomeDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(razaoDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cnpjDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(insEstaDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(codEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(nomeEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEstaEmpresa)))

                linha += 1

        elif self.ui.radbtnModeloVeiculo.isChecked():
            __carrSaida = CarregamentoSaidaDao()
            _pesquisar = __carrSaida.pesquisarNomeMotorista(self.ui.txtPesquisar.text())

            qtde_registros = len(_pesquisar)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:

                # capturando os dados da tupla

                idEntrada = str(pesqui[0])
                codMotorista = str(pesqui[1])
                nomeMotorista = pesqui[2]
                marcaVeiculo = pesqui[3]
                modeloVeiculo = pesqui[4]
                placaVeiculo = pesqui[5]
                data = str(pesqui[6])
                hora = str(pesqui[7])
                carga = pesqui[8]
                produto = pesqui[9]
                codDestinatario = str(pesqui[10])
                nomeDestinatario = pesqui[11]
                razaoDestinatario = pesqui[12]
                cnpjDestinatario = str(pesqui[13])
                insEstaDestinatario = str(pesqui[14])
                codEmpresa = str(pesqui[15])
                nomeEmpresa = pesqui[16]
                razaoEmpresa = pesqui[17]
                cnpjEmpresa = str(pesqui[18])
                insEstaEmpresa = str(pesqui[19])

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idEntrada)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codMotorista)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nomeMotorista)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(marcaVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(modeloVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(placaVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tabPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(carga)))
                self.ui.tabPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(produto)))
                self.ui.tabPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(codDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(nomeDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(razaoDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cnpjDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(insEstaDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(codEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(nomeEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEstaEmpresa)))

                linha += 1

        elif self.ui.radbtnPlacaVeiculo.isChecked():
            __carrSaida = CarregamentoSaidaDao()
            _pesquisar = __carrSaida.pesquisarNomeMotorista(self.ui.txtPesquisar.text())

            qtde_registros = len(_pesquisar)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:

                # capturando os dados da tupla

                idEntrada = str(pesqui[0])
                codMotorista = str(pesqui[1])
                nomeMotorista = pesqui[2]
                marcaVeiculo = pesqui[3]
                modeloVeiculo = pesqui[4]
                placaVeiculo = pesqui[5]
                data = str(pesqui[6])
                hora = str(pesqui[7])
                carga = pesqui[8]
                produto = pesqui[9]
                codDestinatario = str(pesqui[10])
                nomeDestinatario = pesqui[11]
                razaoDestinatario = pesqui[12]
                cnpjDestinatario = str(pesqui[13])
                insEstaDestinatario = str(pesqui[14])
                codEmpresa = str(pesqui[15])
                nomeEmpresa = pesqui[16]
                razaoEmpresa = pesqui[17]
                cnpjEmpresa = str(pesqui[18])
                insEstaEmpresa = str(pesqui[19])

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idEntrada)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codMotorista)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nomeMotorista)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(marcaVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(modeloVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(placaVeiculo)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tabPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(carga)))
                self.ui.tabPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(produto)))
                self.ui.tabPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(codDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(nomeDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(razaoDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cnpjDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(insEstaDestinatario)))
                self.ui.tabPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(codEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(nomeEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmpresa)))
                self.ui.tabPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEstaEmpresa)))

                linha += 1




    def habilitarCampos(self):
        self.ui.grbDadosMotorista.setEnabled(True)
        self.ui.grbDadosClienteDestinatario.setEnabled(True)
        self.ui.grbDadosEmpresaOrigem.setEnabled(True)
        self.ui.txtData.setEnabled(True)
        self.ui.txtHora.setEnabled(True)
        self.ui.txtTipoCarga.setEnabled(True)
        self.ui.txtProduto.setEnabled(True)

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
        result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja cancelar essa operação?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botoesCancelarCadastro()
            self.limparCampos()

    def tablePesquisa(self, pesquisa):
        if self.ui.txtidMotorista.text() and self.ui.txtNomeMotorista.text() and self.ui.txtMarcaMotorista.text() and self.ui.txtModeloMotorista.text() and self.ui.txtIdClienteDestinatario.text() and self.ui.txtNomeClienteDestinatario.text() and self.ui.txtRazaoSocialClienteDestinatario.text() and self.ui.txtInscricaoEstaduaClienteDestinatario and self.ui.txtIdEmpresaOrigem.text() and self.ui.txtNomeEmpresaOrigem.text() and self.ui.txtRazaoSocialEmpresaOrigem.text() and self.ui.txtInscricaoEstaduaEmpresaOrigem.text() == "":
                self.setarCampos()
                self.botaoEditarCadastro()
        else:
                w = QWidget()
                result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.setarCampos()
                    self.botaoEditarCadastro()

    def setarCampos(self):

        itens = []
        for item in self.ui.tabPesquisa.selectedItems():
            itens.append(item.text())

        if len(itens) == 20:
            self.idEntrada = itens[0]
            self.ui.txtidMotorista.setText(itens[1])
            self.ui.txtNomeMotorista.setText(itens[2])
            self.ui.txtModeloMotorista.setText(itens[3])
            self.ui.txtMarcaMotorista.setText(itens[4])
            self.ui.txtPlacaMotorista.setText(itens[5])
            self.ui.txtData.setEnabled(True)
            self.ui.txtHora.setEnabled(True)
            tipoCarga = str(itens[8])
            self.ui.txtTipoCarga.addItem(tipoCarga)
            self.addtTipoCargaAtualizacao(tipoCarga)
            self.ui.txtTipoCarga.setEnabled(True)
            produto = str(itens[9])
            self.ui.txtProduto.addItem(produto)
            self.addtProdutoAtualizacao(produto)
            self.ui.txtProduto.setEnabled(True)
            self.ui.txtIdClienteDestinatario.setText(itens[10])
            self.ui.txtNomeClienteDestinatario.setText(itens[11])
            self.ui.txtRazaoSocialClienteDestinatario.setText(itens[12])
            self.ui.txtCnpjClienteDestinatario.setText(itens[13])
            self.ui.txtInscricaoEstaduaClienteDestinatario.setText(itens[14])
            self.ui.txtIdEmpresaOrigem.setText(itens[15])
            self.ui.txtNomeEmpresaOrigem.setText(itens[16])
            self.ui.txtRazaoSocialEmpresaOrigem.setText(itens[17])
            self.ui.txtCnpjEmpresaOrigem.setText(itens[18])
            self.ui.txtInscricaoEstaduaEmpresaOrigem.setText(itens[19])

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def formatarHoraRetorno(self, hora):
        horas = int(hora[:2])
        minuto = int(hora[3:5])
        segundo = int(hora[6:8])


        return QtCore.QTime(horas, minuto, segundo)

    def removerCaracter(self, i):
        i = str(i)
        i = i.replace('.', '')
        i = i.replace(',', '')
        i = i.replace('/', '')
        i = i.replace('-', '')
        i = i.replace('(', '')
        i = i.replace(')', '')
        i = i.replace(':', '')
        return i

    def addtTipoCargaAtualizacao(self, dados):
        __carrSaida = CarregamentoSaidaDao()
        __tipoCarga = __carrSaida.pesquisarTipoCarga()
        for tipo in __tipoCarga:
            if tipo[0] != dados:
                self.ui.txtTipoCarga.addItem(tipo[0])

    def addtProdutoAtualizacao(self, dados):
        __carrSaida = CarregamentoSaidaDao()
        __produto = __carrSaida.pesquisarProduto(str(self.ui.txtTipoCarga.currentText()))
        for produto in __produto:
            if produto[0] != dados:
                self.ui.txtProduto.addItem(produto[0])
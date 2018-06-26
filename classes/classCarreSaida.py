import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetSaidaCarre import SaidaCarre
from dao.carregamentoSaidaDao import CarregamentoSaidaDao
from telas.frmSaidaVeiculosCarregamentos import Ui_frmSaidaVeiculosCarregamento

class CarregamentoSaida(QtGui.QDialog):
    def __init__(self, cadatra, cancela ):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaVeiculosCarregamento()
        self.ui.setupUi(self)
        self.idEntrada = int()
        self.cada = cadatra
        self.canc = cancela

        self.ui.btnNovo.setEnabled(self.cada)

        self.ui.btnNovo.clicked.connect(self.botoesNovoCadastro)
        self.ui.btnSalvar.clicked.connect(self.cadastrosEntradaVazio)
        self.ui.btnCancelar.clicked.connect(self.cancelarCadastro)

        self.ui.tabPesquisa.doubleClicked.connect(self.tablePesquisa)


    def botoesNovoCadastro(self):

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(self.cada)
        self.ui.btnCancelar.setEnabled(self.canc)

        self.ui.tabPesquisa.setEnabled(self.cada)
        self.dados()


    def botoesCancelarCadastro(self):

        self.ui.btnNovo.setEnabled(self.cada)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)

        self.ui.grbDadosMotorista.setEnabled(False)
        self.ui.grbDadosClienteDestinatario.setEnabled(False)
        self.ui.txtData.setEnabled(False)
        self.ui.txtHora.setEnabled(False)
        self.ui.txtTipoCarga.setEnabled(False)
        self.ui.txtProduto.setEnabled(False)

        self.deletarDescricaoProduto()
        self.ui.tabPesquisa.setEnabled(False)


    def dados(self):
        saiDao = CarregamentoSaidaDao()
        pesquisa = saiDao.pesquisarEntradaCarregamento()

        qtde_registros = len(pesquisa)
        self.ui.tabPesquisa.setRowCount(qtde_registros)
        linha = 0
        for pesqui in pesquisa:

            # capturando os dados da tupla

            idEntrada = str(pesqui[0])
            data = str(pesqui[1])
            hora = str(pesqui[2])
            carga = pesqui[3]
            produto = pesqui[4]
            codMotorista = str(pesqui[5])
            marcaVeiculo = pesqui[6]
            modeloVeiculo = pesqui[7]
            placaVeiculo = pesqui[8]
            codDestinatario = str(pesqui[9])


            motorista = saiDao.pesquisaCodigoMotorista(codMotorista)
            cliente = saiDao.pesquisaCodigoCliente(codDestinatario)

            for mot in motorista:
                nome = mot[1]
                sobrenome = mot[2]

                for cli in cliente:
                    razao = cli[1]
                    fantazia = cli[2]
                    cnpj = cli[3]
                    inscr = cli[4]
                    endereco = cli[8]
                    numero = cli[9]
                    complemento = cli[10]
                    bairro = cli[11]
                    cidade = cli[12]
                    estado = cli[13]
                    cep = cli[14]

                    # preenchendo o grid de pesquisa
                    self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idEntrada)))
                    self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(data)))
                    self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(hora)))
                    self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(carga)))
                    self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(produto)))
                    self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(nome + ' ' + sobrenome)))
                    self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(marcaVeiculo)))
                    self.ui.tabPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(modeloVeiculo)))
                    self.ui.tabPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(placaVeiculo)))
                    self.ui.tabPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(razao)))
                    self.ui.tabPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(fantazia)))
                    self.ui.tabPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(cnpj)))
                    self.ui.tabPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(inscr)))
                    self.ui.tabPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(endereco)))
                    self.ui.tabPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(numero)))
                    self.ui.tabPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(complemento)))
                    self.ui.tabPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(bairro)))
                    self.ui.tabPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
                    self.ui.tabPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
                    self.ui.tabPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(cep)))

                    linha += 1


    def habilitarCampos(self):
        self.ui.grbDadosMotorista.setEnabled(self.cada)
        self.ui.grbDadosClienteDestinatario.setEnabled(self.cada)
        self.ui.txtData.setEnabled(self.cada)
        self.ui.txtHora.setEnabled(self.cada)
        self.ui.txtTipoCarga.setEnabled(self.cada)
        self.ui.txtProduto.setEnabled(self.cada)

    def limparCampos(self):
        self.idEntrada = int()
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
        self.ui.txtCnpjClienteDestinatario.clear()
        self.ui.txtEndereco.clear()
        self.ui.txtNumero.clear()
        self.ui.txtComplemento.clear()
        self.ui.txtBairro.clear()
        self.ui.txtCidade.clear()
        self.ui.txtEstado.clear()
        self.ui.txtCep.clear()



    def cancelarCadastro(self):
        self.botoesCancelarCadastro()
        self.limparCampos()

    def tablePesquisa(self):
        if self.ui.txtidFuncionario.text() != "" and self.ui.txtNomeMotorista.text() != "" and self.ui.txtMarcaMotorista.text() != "" and self.ui.txtModeloMotorista.text() != "" and self.ui.txtIdClienteDestinatario.text() != "" and self.ui.txtNomeClienteDestinatario.text() != "" and self.ui.txtRazaoSocialClienteDestinatario.text() != "" and self.ui.txtInscricaoEstaduaClienteDestinatario != "":
            result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.setarCampos()
        else:
            self.setarCampos()


    def setarCampos(self):
        saiDao = CarregamentoSaidaDao()
        itens = []
        for item in self.ui.tabPesquisa.selectedItems():
            itens.append(item.text())

        idMot = saiDao.pesquisarIdMotorista(itens[0])
        idCli = saiDao.pesquisarIdCliente(itens[0])
        if len(itens) == 20:
            self.ui.txtData.setEnabled(True)
            self.ui.txtHora.setEnabled(True)
            self.idEntrada = itens[0]
            self.ui.txtTipoCarga.setText(itens[3])
            self.ui.txtProduto.setText(itens[4])
            self.ui.txtidFuncionario.setText(str(idMot))
            self.ui.txtNomeMotorista.setText(itens[5])
            self.ui.txtModeloMotorista.setText(itens[6])
            self.ui.txtMarcaMotorista.setText(itens[7])
            self.ui.txtPlacaMotorista.setText(itens[8])
            self.ui.txtIdClienteDestinatario.setText(str(idCli))
            self.ui.txtNomeClienteDestinatario.setText(itens[9])
            self.ui.txtRazaoSocialClienteDestinatario.setText(itens[10])
            self.ui.txtCnpjClienteDestinatario.setText(itens[11])
            self.ui.txtInscricaoEstaduaClienteDestinatario.setText(itens[12])
            self.ui.txtEndereco.setText(itens[13])
            self.ui.txtNumero.setText(itens[14])
            self.ui.txtComplemento.setText(itens[15])
            self.ui.txtBairro.setText(itens[16])
            self.ui.txtCidade.setText(itens[17])
            self.ui.txtEstado.setText(itens[18])
            self.ui.txtCep.setText(itens[19])


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

    def formatarData(self, data):
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:8]

        return ("%s-%s-%s" % (ano, mes, dia))


    def cadastrosEntradaVazio(self):
        if self.ui.txtidFuncionario.text() != "" and self.ui.txtNomeMotorista.text() != "" and self.ui.txtMarcaMotorista.text() != "" and self.ui.txtModeloMotorista.text() != "" and self.ui.txtIdClienteDestinatario.text() != "" and self.ui.txtNomeClienteDestinatario.text() != "" and self.ui.txtRazaoSocialClienteDestinatario.text() != "" and self.ui.txtInscricaoEstaduaClienteDestinatario != "":

                __idEntrada = self.idEntrada
                __data = self.formatarData(self.removerCaracter(self.ui.txtData.text()))
                __hora = self.ui.txtHora.text()

                __dados = SaidaCarre(__idEntrada, __data, __hora)

                __carrSaida = CarregamentoSaidaDao()
                __cad = __carrSaida.cadastrar(__dados)

                self.limparCampos()
                self.botoesCancelarCadastro()
                self.deletarDescricaoProduto()

    def deletarDescricaoProduto(self):
        for i in reversed(range(self.ui.tabPesquisa.rowCount())):
            self.ui.tabPesquisa.removeRow(i)
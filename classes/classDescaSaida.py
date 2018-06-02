import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetSaidaDesca import SaidaDesca
from dao.descarregamentoSaidaDao import DescarreSaidaDao
from telas.frmSaidaVeiculoDescarregamento import Ui_frmSaidaVeiculoDescarregamento

class DescaSaida(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaVeiculoDescarregamento()
        self.ui.setupUi(self)
        self.idSaida = int()

        self.ui.btnNovo.clicked.connect(self.botoesNovoCadastro)
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelarCadastro)

        self.ui.tabPesquisa.doubleClicked.connect(self.tablePesquisa)

    def botoesNovoCadastro(self):

        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)

        self.ui.tabPesquisa.setEnabled(True)
        self.pesquisarEntradaDescarre()

    def botoesCancelarCadastro(self):

        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)

        self.ui.grbDadosMotorista.setEnabled(False)
        self.ui.txtData.setEnabled(False)
        self.ui.txtHora.setEnabled(False)

        self.deletarPesquisa()
        self.ui.tabPesquisa.setEnabled(False)

    def deletarPesquisa(self):
        for i in reversed(range(self.ui.tabPesquisa.rowCount())):
            self.ui.tabPesquisa.removeRow(i)

    def limparCampos(self):
        self.ui.txtData.setDate(QtCore.QDate.currentDate())
        self.ui.txtHora.setTime(QtCore.QTime.currentTime())
        self.ui.txtidFuncionario.clear()
        self.ui.txtNomeMotorista.clear()
        self.ui.txtModeloMotorista.clear()
        self.ui.txtMarcaMotorista.clear()
        self.ui.txtPlacaMotorista.clear()

    def formatarHoraRetorno(self, hora):
        horas = int(hora[:2])
        minuto = int(hora[3:5])
        segundo = int(hora[6:8])


        return QtCore.QTime(horas, minuto, segundo)

    def pesquisarEntradaDescarre(self):
        entDao = DescarreSaidaDao()
        __retorno = entDao.pesquisarEntrada()
        qtde_registros = len(__retorno)
        self.ui.tabPesquisa.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            data = pesqui[1]
            hora = pesqui[2]
            funcionario= pesqui[3]
            sobrenome = pesqui[4]
            marca = pesqui[5]
            modelo = pesqui[6]
            placa = pesqui[7]


            # preenchendo o grid de pesquisa
            self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(data)))
            self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(hora)))
            self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(funcionario + ' ' +sobrenome)))
            self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(marca)))
            self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(modelo)))
            self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(placa)))



            linha += 1

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

    def cancelarCadastro(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja cancelar essa operação?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botoesCancelarCadastro()
            self.limparCampos()

    def tablePesquisa(self):
        if self.ui.txtidFuncionario.text() != "" and self.ui.txtNomeMotorista.text() != "" and self.ui.txtMarcaMotorista.text() != "" and self.ui.txtModeloMotorista.text() != "" :
            result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.setarCampos()
        else:
            self.setarCampos()


    def setarCampos(self):
        saiDao = DescarreSaidaDao()
        itens = []
        for item in self.ui.tabPesquisa.selectedItems():
            itens.append(item.text())

        idMot = saiDao.pesquisarIdMotorista(itens[0])
        if len(itens) == 7:
            self.ui.txtData.setEnabled(True)
            self.ui.txtHora.setEnabled(True)
            self.idSaida = itens[0]
            self.ui.txtidFuncionario.setText(str(idMot))
            self.ui.txtNomeMotorista.setText(itens[3])
            self.ui.txtModeloMotorista.setText(itens[5])
            self.ui.txtMarcaMotorista.setText(itens[4])
            self.ui.txtPlacaMotorista.setText(itens[6])

    def cadastro(self):
        if self.ui.txtidFuncionario.text() != "" and self.ui.txtNomeMotorista.text() != "" and self.ui.txtMarcaMotorista.text() != "" and self.ui.txtModeloMotorista.text() != "":
            __data = self.formatarData(self.removerCaracter(self.ui.txtData.text()))
            __hora = self.ui.txtHora.text()
            __id = str(self.idSaida)

            __dados = SaidaDesca(__id, __data, __hora)
            __entFunci = DescarreSaidaDao()
            __entFunci.cadastrar(__dados)


            self.limparCampos()
            self.botoesCancelarCadastro()
            self.deletarPesquisa()

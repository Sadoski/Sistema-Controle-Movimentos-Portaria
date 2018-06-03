import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetEntradaFuncionario import EntradaFuncionario
from dao.entradaFuncionarioDao import EntradaFuncionarioDao
from telas.frmEntradaFuncionario import Ui_frmCadastroEntradaFuncionario

class EntradaFuncionarios(QtGui.QDialog):
    def __init__(self, cadatra, cancela):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroEntradaFuncionario()
        self.ui.setupUi(self)
        self.idSaida = int()
        self.cada = cadatra
        self.canc = cancela

        self.ui.btnNovo.setEnabled(self.cada)

        self.ui.tabPesquisa.doubleClicked.connect(self.tablePesquisa)

        self.ui.btnNovo.clicked.connect(self.botaoNovoCadastro)
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

    def ativarPesquisa(self):
        self.ui.tabPesquisa.setEnabled(True)


    def cancelarCad(self):
        self.botaoCancelarCadastro()
        self.limparCamposCad()


    def botaoNovoCadastro(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(self.cada)
        self.ui.btnCancelar.setEnabled(self.canc)

        self.ui.tabPesquisa.setEnabled(self.cada)
        self.ui.grbDadosSaidaFuncionario.setEnabled(self.cada)
        self.pesquisarSaidaFuncionario()

    def botaoCancelarCadastro(self):
        self.ui.btnNovo.setEnabled(self.cada)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)

        self.ui.tabPesquisa.setEnabled(False)
        self.ui.grbDadosSaidaFuncionario.setEnabled(False)

    def pesquisarSaidaFuncionario(self):
        entDao = EntradaFuncionarioDao()
        __retorno = entDao.pesquisarSaida()
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
            setor = pesqui[5]
            cargo = pesqui[6]


            # preenchendo o grid de pesquisa
            self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(data)))
            self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(hora)))
            self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(funcionario + ' ' +sobrenome)))
            self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(setor)))
            self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cargo)))


            linha += 1


    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def formatarHorasRetorno(self, hora):
        horas = hora[0:2]
        minutos = hora[3:5]
        segundos = hora[6:8]

        return QtCore.QTime(int(horas), int(minutos), int(segundos))

    def tablePesquisa(self):
        if self.ui.txtidFuncionario.text() == "" and self.ui.txtNomeFuncionario.text() == "" and self.ui.txtCargos.text() == "" and self.ui.txtSetor.text() == "":
                self.setarCampos()
        else:
                result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.setarCampos()

    def setarCampos(self):

        itens = []
        for item in self.ui.tabPesquisa.selectedItems():
            itens.append(item.text())

        entDao = EntradaFuncionarioDao()
        idFuncionario = entDao.pesquisarIdFuncionario(itens[0])

        self.idSaida = itens[0]
        self.ui.txtidFuncionario.setText(str(idFuncionario))
        self.ui.txtNomeFuncionario.setText(str(itens[3]))
        self.ui.txtSetor.setText(str(itens[4]))
        self.ui.txtCargos.setText(str(itens[5]))

    def formatarData(self, data):
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:8]

        return ("%s-%s-%s" % (ano, mes, dia))

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

    def cadastro(self):
        if self.ui.txtidFuncionario.text() != "" and self.ui.txtNomeFuncionario.text() != "" and self.ui.txtCargos.text() != "" and self.ui.txtSetor.text() != "":
            __data = self.formatarData(self.removerCaracter(self.ui.txtDataEntrada.text()))
            __hora = self.ui.txtHoraEntrada.text()
            __id = str(self.idSaida)

            __dados = EntradaFuncionario(__id, __data, __hora)
            __entFunci = EntradaFuncionarioDao()
            __entFunci.cadastro(__dados)
            __entFunci.updateSaidaFuncionario()

            self.limparCampos()
            self.botaoCancelarCadastro()
            self.deletarPesquisa()

    def deletarPesquisa(self):
        for i in reversed(range(self.ui.tabPesquisa.rowCount())):
            self.ui.tabPesquisa.removeRow(i)

    def limparCampos(self):
        self.ui.txtidFuncionario.clear()
        self.ui.txtNomeFuncionario.clear()
        self.ui.txtSetor.clear()
        self.ui.txtCargos.clear()
        self.ui.txtDataEntrada.setDate(QDate.currentDate())
        self.ui.txtHoraEntrada.setTime(QTime.currentTime())

    def cancelar(self):
        if self.ui.txtidFuncionario.text() != "" and self.ui.txtNomeFuncionario.text() != "" and self.ui.txtCargos.text() != "" and self.ui.txtSetor.text() != "":
            result = QMessageBox.question(QWidget(), 'Menssagem',"Tem certeza que deseja cancelar essa operação ", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.botaoCancelarCadastro()
                self.limparCampos()
                self.deletarPesquisa()
        else:
            self.botaoCancelarCadastro()
            self.limparCampos()
            self.deletarPesquisa()
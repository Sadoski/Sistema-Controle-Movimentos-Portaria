import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.entradaFuncionario import EntradaFuncionario
from dao.entradaFuncionarioDao import EntradaFuncionarioDao
from telas.frmEntradaFuncionario import Ui_frmCadastroEntradaFuncionario

class EntradaFuncionarios(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroEntradaFuncionario()
        self.ui.setupUi(self)
        self.idSaida = None

        self.ui.txtPesquisaNomeFuncionario.returnPressed.connect(self.pesquisar)

        self.ui.btnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tabPesquisa.doubleClicked.connect(self.tablePesquisa)

        self.ui.radBtnNome.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnCpf.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnRg.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnSetor.clicked.connect(self.ativarPesquisa)
        self.ui.radBtnCargo.clicked.connect(self.ativarPesquisa)

        self.ui.btnNovo.clicked.connect(self.botaoNovoCadastro)
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

    def ativarPesquisa(self):
        self.ui.txtPesquisaNomeFuncionario.setEnabled(True)
        self.ui.tabPesquisa.setEnabled(True)
        self.ui.btnPesquisar.setEnabled(True)
        self.ui.txtPesquisaNomeFuncionario.setFocus()

    def pesquisar(self):
        if self.ui.radBtnNome.isChecked():
            __pesquisar = self.ui.txtPesquisaNomeFuncionario.text()
            __entFunci = EntradaFuncionarioDao()
            __resultado = __entFunci.pesquisarNome(__pesquisar)

            qtde_registros = len(__resultado)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __resultado:
                # capturando os dados da tupla

                idSaida = pesqui[0]
                codigo = pesqui[1]
                nome = pesqui[2]
                setor = pesqui[3]
                cargo = pesqui[4]
                data = pesqui[5]
                hora = pesqui[6]


                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idSaida)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cargo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(hora)))


                linha += 1

        elif self.ui.radBtnCpf.isChecked():
            __pesquisar = self.ui.txtPesquisaNomeFuncionario.text()
            __entFunci = EntradaFuncionarioDao()
            __resultado = __entFunci.pesquisarCpf(__pesquisar)

            qtde_registros = len(__resultado)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __resultado:
                # capturando os dados da tupla

                idSaida = pesqui[0]
                codigo = pesqui[1]
                nome = pesqui[2]
                setor = pesqui[3]
                cargo = pesqui[4]
                data = pesqui[5]
                hora = pesqui[6]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idSaida)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cargo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(hora)))


                linha += 1

        elif self.ui.radBtnRg.isChecked():
            __pesquisar = self.ui.txtPesquisaNomeFuncionario.text()
            __entFunci = EntradaFuncionarioDao()
            __resultado = __entFunci.pesquisarRg(__pesquisar)

            qtde_registros = len(__resultado)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __resultado:
                # capturando os dados da tupla

                idSaida = pesqui[0]
                codigo = pesqui[1]
                nome = pesqui[2]
                setor = pesqui[3]
                cargo = pesqui[4]
                data = pesqui[5]
                hora = pesqui[6]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idSaida)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cargo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(hora)))

                linha += 1

        elif self.ui.radBtnSetor.isChecked():
            __pesquisar = self.ui.txtPesquisaNomeFuncionario.text()
            __entFunci = EntradaFuncionarioDao()
            __resultado = __entFunci.pesquisarSetor(__pesquisar)

            qtde_registros = len(__resultado)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __resultado:
                # capturando os dados da tupla

                idSaida = pesqui[0]
                codigo = pesqui[1]
                nome = pesqui[2]
                setor = pesqui[3]
                cargo = pesqui[4]
                data = pesqui[5]
                hora = pesqui[6]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idSaida)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cargo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(hora)))

                linha += 1

        elif self.ui.radBtnCargo.isChecked():
            __pesquisar = self.ui.txtPesquisaNomeFuncionario.text()
            __entFunci = EntradaFuncionarioDao()
            __resultado = __entFunci.pesquisarCargo(__pesquisar)

            qtde_registros = len(__resultado)
            self.ui.tabPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in __resultado:
                # capturando os dados da tupla

                idSaida = pesqui[0]
                codigo = pesqui[1]
                nome = pesqui[2]
                setor = pesqui[3]
                cargo = pesqui[4]
                data = pesqui[5]
                hora = pesqui[6]

                # preenchendo o grid de pesquisa
                self.ui.tabPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(idSaida)))
                self.ui.tabPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tabPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tabPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tabPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cargo)))
                self.ui.tabPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(data)))
                self.ui.tabPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(hora)))

                linha += 1

    def cancelarCad(self):
        self.botaoCancelarCadastro()
        self.limparCamposCad()

    def botaoEditarCadastro(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)

        self.ui.grbDadosSaidaFuncionario.setEnabled(True)

    def botaoNovoCadastro(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

        self.ui.grbTipoPesquisa.setEnabled(True)
        self.ui.grbDadosSaidaFuncionario.setEnabled(True)

    def botaoCancelarCadastro(self):
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

        self.ui.grbTipoPesquisa.setEnabled(False)
        self.ui.txtPesquisaNomeFuncionario.setEnabled(False)
        self.ui.txtPesquisaNomeFuncionario.clear()
        self.ui.tabPesquisa.setEnabled(False)
        self.ui.btnPesquisar.setEnabled(False)
        self.ui.grbDadosSaidaFuncionario.setEnabled(False)


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

        if len(itens) == 7:
            self.idSaida = itens[0]
            self.ui.txtidFuncionario.setText(str(itens[1]))
            self.ui.txtNomeFuncionario.setText(str(itens[2]))
            self.ui.txtSetor.setText(str(itens[3]))
            self.ui.txtCargos.setText(str(itens[4]))

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
            __data = self.formatarData(self.removerCaracter(self.ui.txtData.text()))
            __hora = self.ui.txtHoraEntrda.text()
            __id = self.idSaida
            print(__id)
            __dados = EntradaFuncionario(__id, __data, __hora)
            __entFunci = EntradaFuncionarioDao()
            __result = __entFunci.cadastro(__dados)
            if __result == True:
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
        self.ui.txtData.setDate(QDate.currentDate())
        self.ui.txtHoraEntrda.setTime(QTime.currentTime())

    def cancelar(self):
        if self.ui.txtidFuncionario.text() != "" and self.ui.txtNomeFuncionario.text() != "" and self.ui.txtCargos.text() != "" and self.ui.txtSetor.text() != "":
            result = QMessageBox.question(QWidget(), 'Menssagem',"Tem certeza que deseja cancelar essa operação ", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.botaoCancelarCadastro()
                self.limparCampos()
                self.deletarPesquisa()
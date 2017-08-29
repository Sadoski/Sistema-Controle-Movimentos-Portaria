import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetPesquisaNotaFiscal import PesquisaNotaFiscal
from controller.saidaFuncionario import FuncionarioSaida
from dao.pesquisarNotaFiscalRomaneioDao import PesquisarNotaFiscalRomaneioDao
from dao.saidaFuncionarioDao import SaidaFuncionarioDao
from telas.frmPesquisarNotasFiscais import Ui_frmConsultarNotasFiscais
from telas.frmSaidaFuncionario import Ui_frmSaidaFuncionario

class SaidaFuncionario(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaFuncionario()
        self.ui.setupUi(self)
        self.idFuncao = None

        self.ui.txtNomeFuncionario.editingFinished.connect(self.pesquisarFuncionario)

        self.ui.txtNomeFuncionario.returnPressed.connect(self.focusData)

        self.ui.btnNovo.clicked.connect(self.botaoNovoCadastro)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnEditar.clicked.connect(self.editar)
        self.ui.btnPesquisarFuncionario.clicked.connect(self.pesquisarFuncionario)
        self.ui.btnCancelar.clicked.connect(self.cancelarCad)
        self.ui.btnDeletar.clicked.connect(self.deletar)

        self.ui.txtPesquisaFuncionario.returnPressed.connect(self.pesquisarSaidaFuncionario)

        self.ui.tbPesquisaFuncionario.doubleClicked.connect(self.tablePesquisa)

        self.ui.btnPesquisar.clicked.connect(self.pesquisarFuncionario)


    def focusData(self):
        self.ui.txtDataSaida.setFocus()

    def limparCampos(self):
        #self.ui.txtNomeFuncionario.clear()
        self.ui.txtidFuncionario.clear()
        self.ui.txtSetor.clear()
        self.ui.txtCargos.clear()

    def pesquisarFuncionario(self):
        __nome = self.ui.txtNomeFuncionario.text()
        __funDao = SaidaFuncionarioDao()
        __resultada = __funDao.pesquisarFuncionario(__nome)
        if __resultada == False:
            self.limparCampos()
        else:
            self.limparCampos()
            for non in __resultada:
                self.ui.txtidFuncionario.setText(str(non[0]))
                self.idFuncao = non[1]
                self.ui.txtSetor.setText(non[2])
                self.ui.txtCargos.setText(non[3])

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

    def formatarData(self, data):
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:8]

        return ("%s-%s-%s" % (ano, mes, dia))

    def limparCamposCad(self):
        self.ui.txtidFuncionario.clear()
        self.ui.txtNomeFuncionario.clear()
        self.idFuncao = None
        self.ui.txtDataSaida.setDate(QDate.currentDate())
        self.ui.txtHoraSaida.setTime(QTime.currentTime())
        self.ui.txtSetor.clear()
        self.ui.txtCargos.clear()


    def cadastrar(self):
        __idFuncionario = self.ui.txtidFuncionario.text()
        __idFuncao = self.idFuncao
        __data = self.formatarData(self.removerCaracter(self.ui.txtDataSaida.text()))
        __hora = self.ui.txtHoraSaida.text()

        __funcionario = FuncionarioSaida(None, __idFuncionario, __idFuncao, __data, __hora)
        __funDao = SaidaFuncionarioDao()
        __funDao.cadastro(__funcionario)
        self.botaoCancelarCadastro()
        self.limparCamposCad()

    def editar(self):
        __funDao = SaidaFuncionarioDao()
        __idFuncionario = self.ui.txtidFuncionario.text()
        __idSaidaFuncionario = __funDao.pesquisarIdSaidaFuncionario(__idFuncionario)
        __idFuncao = __funDao.pesquisarIdFuncao(__idFuncionario)
        __data = self.formatarData(self.removerCaracter(self.ui.txtDataSaida.text()))
        __hora = self.ui.txtHoraSaida.text()

        __funcionario = FuncionarioSaida(__idSaidaFuncionario, __idFuncionario, __idFuncao, __data, __hora)

        __funDao.editar(__funcionario)
        self.botaoCancelarCadastro()
        self.limparCamposCad()

    def pesquisarSaidaFuncionario(self):
        if self.ui.radBtnCodigoFuncionario.isChecked():
            _funId = SaidaFuncionarioDao()
            _pesquisar = _funId.pesquisarCodigoFuncionario(self.ui.txtPesquisaFuncionario.text())

            qtde_registros = len(_pesquisar)
            self.ui.tbPesquisaFuncionario.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                data = pesqui[2]
                hora = pesqui[3]
                self.idFuncao = pesqui[4]
                setor = pesqui[5]
                cargo = pesqui[6]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisaFuncionario.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 2, QtGui.QTableWidgetItem(str(data)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 3, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 4, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 5, QtGui.QTableWidgetItem(str(cargo)))

                linha += 1

        elif self.ui.radBtnNomeFuncionario.isChecked():
            _funNome = SaidaFuncionarioDao()
            _pesquisar = _funNome.pesquisarNomeFuncionario(self.ui.txtPesquisaFuncionario.text())

            qtde_registros = len(_pesquisar)
            self.ui.tbPesquisaFuncionario.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                data = pesqui[2]
                hora = pesqui[3]
                self.idFuncao = pesqui[4]
                setor = pesqui[5]
                cargo = pesqui[6]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisaFuncionario.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 2, QtGui.QTableWidgetItem(str(data)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 3, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 4, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 5, QtGui.QTableWidgetItem(str(cargo)))

                linha += 1

        elif self.ui.radBtnRg.isChecked():
            _funRg = SaidaFuncionarioDao()
            _pesquisar = _funRg.pesquisarRgFuncionario(self.ui.txtPesquisaFuncionario.text())

            print(_pesquisar)
            qtde_registros = len(_pesquisar)
            self.ui.tbPesquisaFuncionario.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                data = pesqui[2]
                hora = pesqui[3]
                self.idFuncao = pesqui[4]
                setor = pesqui[5]
                cargo = pesqui[6]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisaFuncionario.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 2, QtGui.QTableWidgetItem(str(data)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 3, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 4, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 5, QtGui.QTableWidgetItem(str(cargo)))

                linha += 1

        elif self.ui.radBtnCpf.isChecked():
            _funCpf = SaidaFuncionarioDao()
            _pesquisar = _funCpf.pesquisarCpfFuncionario(self.ui.txtPesquisaFuncionario.text())

            qtde_registros = len(_pesquisar)
            self.ui.tbPesquisaFuncionario.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                data = pesqui[2]
                hora = pesqui[3]
                self.idFuncao = pesqui[4]
                setor = pesqui[5]
                cargo = pesqui[6]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisaFuncionario.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 2, QtGui.QTableWidgetItem(str(data)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 3, QtGui.QTableWidgetItem(str(hora)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 4, QtGui.QTableWidgetItem(str(setor)))
                self.ui.tbPesquisaFuncionario.setItem(linha, 5, QtGui.QTableWidgetItem(str(cargo)))

                linha += 1

        else:
            QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")

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

        self.ui.grbDadosSaidaFuncionario.setEnabled(True)

    def botaoCancelarCadastro(self):
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

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
                self.botaoEditarCadastro()
        else:
                result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.setarCampos()
                    self.botaoEditarCadastro()

    def setarCampos(self):

        itens = []
        for item in self.ui.tbPesquisaFuncionario.selectedItems():
            itens.append(item.text())

        if len(itens) == 6:
            self.ui.txtidFuncionario.setText(str(itens[0]))
            self.ui.txtNomeFuncionario.setText(str(itens[1]))
            self.ui.txtDataSaida.setDate(self.formatarDataRetorno(itens[2]))
            self.ui.txtHoraSaida.setTime(self.formatarHorasRetorno(itens[3]))
            self.ui.txtSetor.setText(str(itens[4]))
            self.ui.txtCargos.setText(str(itens[5]))

    def deletar(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja excluir esse funcionario", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            __funDao = SaidaFuncionarioDao()
            __funDao.deletar(self.ui.txtidFuncionario.text())
            self.botaoCancelarCadastro()
            self.limparCamposCad()

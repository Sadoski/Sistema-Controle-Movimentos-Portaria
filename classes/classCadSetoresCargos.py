
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.setGetConfimarEmpresa import ConfirmarEmpresa
from controller.setGetSetoresCargos import Setor, Cargo, Relacao
from dao.empresaDao import EmpresaDao
from dao.setoresCargosDao import SetoresCargosDao
from telas.frmCadastroSetoresCargos import Ui_frmCadastroSetoresCargos


class SetoresCargos(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.__ui = Ui_frmCadastroSetoresCargos()
        self.__ui.setupUi(self)
        self._setoresCargos = SetoresCargosDao()

        self.__ui.txtCadSetoresNomeFantasia.returnPressed.connect(self.focusSetor)
        self.__ui.txtCadSetoresSetor.returnPressed.connect(self.focusBotaoSetorSslvar)
        self.__ui.txtCadCargoNomeFantasia.returnPressed.connect(self.focusCargo)
        self.__ui.txtCadCargoCargo.returnPressed.connect(self.focusBotaoCargoSalvar)
        self.__ui.txtRelacaoNomeFantasia.returnPressed.connect(self.focusComboSetor)

        self.__ui.txtCadSetoresNomeFantasia.editingFinished.connect(self.pesquisarSetorEmpresa)
        self.__ui.txtCadCargoNomeFantasia.editingFinished.connect(self.pesquisarCargoEmpresa)
        self.__ui.txtRelacaoNomeFantasia.editingFinished.connect(self.pesquisarRelacaoEmpresa)

        self.__ui.btnCadSetoresNovo.clicked.connect(self.novoCadSetor)
        self.__ui.btnCadSetoresSalvar.clicked.connect(self.cadastrarSetor)
        self.__ui.btnCadSetoresCancelar.clicked.connect(self.cancelarSetor)

        self.__ui.btnCadCargoNovo.clicked.connect(self.novoCadCargo)
        self.__ui.btnCadCargoSalvar.clicked.connect(self.cadastrarCargo)
        self.__ui.btnCadCargoCancelar.clicked.connect(self.cancelarCargo)

        self.__ui.btnRelacaoNovo.clicked.connect(self.novoCadRelacao)
        self.__ui.btnRelacaoSalvar.clicked.connect(self.cadastrarRelacao)
        self.__ui.btnRelacaoCancelar.clicked.connect(self.cancelarRelacao)

        self.__ui.txtSetorPesquisa.returnPressed.connect(self.pesquisarSetores)

    def focusSetor(self):
        self.__ui.txtCadSetoresSetor.setFocus()

    def focusBotaoSetorSslvar(self):
        self.__ui.btnCadSetoresSalvar.setFocus()

    def focusCargo(self):
        self.__ui.txtCadCargoCargo.setFocus()

    def focusBotaoCargoSalvar(self):
        self.__ui.btnCadCargoSalvar.setFocus()

    def focusComboSetor(self):
        self.__ui.txtRelacaoSetor.setFocus()

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

    def limparSetorCampos(self):
        self.__ui.txtCadSetoresCodigo.clear()
        self.__ui.txtCadSetoresRazaoSocial.clear()
        self.__ui.txtCadSetoresTipoEmpresa.clear()
        self.__ui.txtCadSetoresCnpj.clear()
        self.__ui.txtCadSetoresInscricaoEstadual.clear()

    def pesquisarSetorEmpresa(self):

        _empresaDao = EmpresaDao()

        _empresa = _empresaDao.pesquisaEmpresaSetCar(str(self.__ui.txtCadSetoresNomeFantasia.text()))
        if _empresa == False:

            self.limparSetorCampos()
        else:
            self.limparSetorCampos()
            for empe in _empresa:
                self.__ui.txtCadSetoresCodigo.setText(str(empe[0]))
                self.__ui.txtCadSetoresRazaoSocial.setText(empe[1])
                self.__ui.txtCadSetoresTipoEmpresa.setText(empe[2])
                self.__ui.txtCadSetoresCnpj.setText(empe[3])
                self.__ui.txtCadSetoresInscricaoEstadual.setText(empe[4])

    def limparCargoCampos(self):
        self.__ui.txtCadCargoCodigo.clear()
        self.__ui.txtCadCargoRazaoSocial.clear()
        self.__ui.txtCadCargoTipoEmpresa.clear()
        self.__ui.txtCadCargoCnpj.clear()
        self.__ui.txtCadCargoInscricaoEstadual.clear()

    def pesquisarCargoEmpresa(self):

        _empresaDao = EmpresaDao()

        _empresa = _empresaDao.pesquisaEmpresaSetCar(str(self.__ui.txtCadCargoNomeFantasia.text()))
        if _empresa == False:

            self.limparCargoCampos()
        else:
            self.limparCargoCampos()
            for empe in _empresa:
                self.__ui.txtCadCargoCodigo.setText(str(empe[0]))
                self.__ui.txtCadCargoRazaoSocial.setText(empe[1])
                self.__ui.txtCadCargoTipoEmpresa.setText(empe[2])
                self.__ui.txtCadCargoCnpj.setText(empe[3])
                self.__ui.txtCadCargoInscricaoEstadual.setText(empe[4])

    def limparRelacaoCampos(self):
        self.__ui.txtRelacaoCodigo.clear()
        self.__ui.txtRelacaoRazaoSocial.clear()
        self.__ui.txtRelacaoTipoEmpresa.clear()
        self.__ui.txtRelacaoCnpj.clear()
        self.__ui.txtRelacaoInscricaoEstadual.clear()

    def pesquisarRelacaoEmpresa(self):

        _empresaDao = EmpresaDao()

        _empresa = _empresaDao.pesquisaEmpresaSetCar(str(self.__ui.txtRelacaoNomeFantasia.text()))
        if _empresa == False:

            self.limparRelacaoCampos()
        else:
            self.limparRelacaoCampos()
            for empe in _empresa:
                self.__ui.txtRelacaoCodigo.setText(str(empe[0]))
                self.__ui.txtRelacaoRazaoSocial.setText(empe[1])
                self.__ui.txtRelacaoTipoEmpresa.setText(empe[2])
                self.__ui.txtRelacaoCnpj.setText(empe[3])
                self.__ui.txtRelacaoInscricaoEstadual.setText(empe[4])

    def limparSetorCampostTodos(self):
        self.__ui.txtCadSetoresCodigo.clear()
        self.__ui.txtCadSetoresNomeFantasia.clear()
        self.__ui.txtCadSetoresRazaoSocial.clear()
        self.__ui.txtCadSetoresTipoEmpresa.clear()
        self.__ui.txtCadSetoresCnpj.clear()
        self.__ui.txtCadSetoresInscricaoEstadual.clear()
        self.__ui.txtCadSetoresCodigo.clear()
        self.__ui.txtCadSetoresSetor.clear()

    def novoCadSetor(self):
        self.limparSetorCampostTodos()

        self.__ui.btnCadSetoresNovo.setEnabled(False)
        self.__ui.btnCadSetoresSalvar.setEnabled(True)
        self.__ui.btnCadSetoresCancelar.setEnabled(True)
        self.__ui.btnCadSetoresPesquisar.setEnabled(True)

        self.__ui.txtCadSetoresNomeFantasia.setEnabled(True)
        self.__ui.txtCadSetoresSetor.setEnabled(True)

        self.__ui.txtCadSetoresNomeFantasia.setFocus()

    def cadastrarSetor(self):
        if  self.__ui.txtCadSetoresCodigo and self.__ui.txtCadSetoresNomeFantasia and self.__ui.txtCadSetoresRazaoSocial and self.__ui.txtCadSetoresTipoEmpresa and self.__ui.txtCadSetoresCnpj and self.__ui.txtCadSetoresInscricaoEstadual == "":
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")
        else:
            _codigo = int(self.__ui.txtCadSetoresCodigo.text())
            _fantasia = self.__ui.txtCadSetoresNomeFantasia.text()
            _razaoSocial = self.__ui.txtCadSetoresRazaoSocial.text()
            _cnpj = self.removerCaracter(self.__ui.txtCadSetoresCnpj.text())
            _incricao = self.__ui.txtCadSetoresInscricaoEstadual.text()
            _setores = str(self.__ui.txtCadSetoresSetor.text())
            __confiEmp = ConfirmarEmpresa(_codigo, _fantasia, _razaoSocial, _cnpj, _incricao)

            __empDao = EmpresaDao()

            __validar = __empDao.confirmarEmpresa(__confiEmp)

            if __validar == _codigo:

                __setor = Setor(_codigo, _setores)

                __cadSetor = SetoresCargosDao()
                __cadSetor.cadastrarSetor(__setor)
                self.limparSetorCampostTodos()

    def cancelarSetor(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Tenceteza que quer Cancelar a operação", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.limparSetorCampostTodos()
            self.botoesDesativarSetor()

    def botoesDesativarSetor(self):
        self.__ui.btnCadSetoresNovo.setEnabled(True)
        self.__ui.btnCadSetoresSalvar.setEnabled(False)
        self.__ui.btnCadSetoresCancelar.setEnabled(False)
        self.__ui.btnCadSetoresPesquisar.setEnabled(False)

        self.__ui.txtCadSetoresNomeFantasia.setEnabled(False)
        self.__ui.txtCadSetoresSetor.setEnabled(False)

    def limparCargoCampostTodos(self):
        self.__ui.txtCadCargoCodigo.clear()
        self.__ui.txtCadCargoNomeFantasia.clear()
        self.__ui.txtCadCargoRazaoSocial.clear()
        self.__ui.txtCadCargoTipoEmpresa.clear()
        self.__ui.txtCadCargoCnpj.clear()
        self.__ui.txtCadCargoInscricaoEstadual.clear()
        self.__ui.txtCadCargoCodigo.clear()
        self.__ui.txtCadCargoCargo.clear()

    def novoCadCargo(self):
        self.limparSetorCampostTodos()

        self.__ui.btnCadCargoNovo.setEnabled(False)
        self.__ui.btnCadCargoSalvar.setEnabled(True)
        self.__ui.btnCadCargoCancelar.setEnabled(True)
        self.__ui.btnCadCargoPesquisar.setEnabled(True)

        self.__ui.txtCadCargoNomeFantasia.setEnabled(True)
        self.__ui.txtCadCargoCargo.setEnabled(True)

        self.__ui.txtCadCargoNomeFantasia.setFocus()

    def cadastrarCargo(self):
        if  self.__ui.txtCadCargoCodigo and self.__ui.txtCadCargoNomeFantasia and self.__ui.txtCadCargoRazaoSocial and self.__ui.txtCadCargoTipoEmpresa and self.__ui.txtCadCargoCnpj and self.__ui.txtCadCargoInscricaoEstadual == "":
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")
        else:
            _codigo = int(self.__ui.txtCadCargoCodigo.text())
            _fantasia = self.__ui.txtCadCargoNomeFantasia.text()
            _razaoSocial = self.__ui.txtCadCargoRazaoSocial.text()
            _cnpj = self.removerCaracter(self.__ui.txtCadCargoCnpj.text())
            _incricao = self.__ui.txtCadCargoInscricaoEstadual.text()
            _setores = str(self.__ui.txtCadCargoCargo.text())
            __confiEmp = ConfirmarEmpresa(_codigo, _fantasia, _razaoSocial, _cnpj, _incricao)

            __empDao = EmpresaDao()

            __validar = __empDao.confirmarEmpresa(__confiEmp)

            if __validar == _codigo:

                __cargo = Cargo(_codigo, _setores)

                __cadCargo = SetoresCargosDao()
                __cadCargo.cadastrarCargo(__cargo)
                self.limparCargoCampostTodos()

    def cancelarCargo(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Tenceteza que quer Cancelar a operação", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.limparCargoCampostTodos()
            self.botoesDesativarCargo()

    def botoesDesativarCargo(self):
        self.limparCargoCampostTodos()

        self.__ui.btnCadCargoNovo.setEnabled(True)
        self.__ui.btnCadCargoSalvar.setEnabled(False)
        self.__ui.btnCadCargoCancelar.setEnabled(False)
        self.__ui.btnCadCargoPesquisar.setEnabled(False)

        self.__ui.txtCadCargoNomeFantasia.setEnabled(False)
        self.__ui.txtCadCargoCargo.setEnabled(False)

    def limparRelacaoCampostTodos(self):
        self.__ui.txtRelacaoCodigo.clear()
        self.__ui.txtRelacaoNomeFantasia.clear()
        self.__ui.txtRelacaoRazaoSocial.clear()
        self.__ui.txtRelacaoTipoEmpresa.clear()
        self.__ui.txtRelacaoCnpj.clear()
        self.__ui.txtRelacaoInscricaoEstadual.clear()
        self.__ui.txtRelacaoCodigo.clear()
        self.__ui.txtRelacaoSetor.clear()
        self.__ui.txtRelacaoCargo.clear()

    def novoCadRelacao(self):
        self.limparRelacaoCampostTodos()

        self.__ui.btnRelacaoNovo.setEnabled(False)
        self.__ui.btnRelacaoSalvar.setEnabled(True)
        self.__ui.btnRelacaoCancelar.setEnabled(True)
        self.__ui.btnRelacaoPesquisar.setEnabled(True)

        self.__ui.txtRelacaoNomeFantasia.setEnabled(True)
        self.__ui.txtRelacaoSetor.setEnabled(True)
        self.__ui.txtRelacaoCargo.setEnabled(True)
        self.setRelacaoSetor()
        self.setRelacaoCargo()

        self.__ui.txtRelacaoNomeFantasia.setFocus()

    def cadastrarRelacao(self):
        if  self.__ui.txtCadSetoresCodigo and self.__ui.txtCadSetoresNomeFantasia and self.__ui.txtCadSetoresRazaoSocial and self.__ui.txtCadSetoresTipoEmpresa and self.__ui.txtCadSetoresCnpj and self.__ui.txtCadSetoresInscricaoEstadual == "":
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")
        else:
            __cadRelacao = SetoresCargosDao()
            _codigo = int(self.__ui.txtRelacaoCodigo.text())
            _fantasia = self.__ui.txtRelacaoNomeFantasia.text()
            _razaoSocial = self.__ui.txtRelacaoRazaoSocial.text()
            _cnpj = self.removerCaracter(self.__ui.txtRelacaoCnpj.text())
            _incricao = self.__ui.txtRelacaoInscricaoEstadual.text()
            _setores = __cadRelacao.verificarSetor(str(self.__ui.txtRelacaoSetor.currentText()))
            _cargo = __cadRelacao.verificarCargo(str(self.__ui.txtRelacaoCargo.currentText()))
            __confiEmp = ConfirmarEmpresa(_codigo, _fantasia, _razaoSocial, _cnpj, _incricao)

            __empDao = EmpresaDao()

            __validar = __empDao.confirmarEmpresa(__confiEmp)

            if __validar == _codigo:

                __relacao = Relacao(_codigo, _setores, _cargo)


                __cadRelacao.cadastrarRelacao(__relacao)
                self.limparRelacaoCampostTodos()
                self.botoesDesativarRelacao()

    def cancelarRelacao(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Tenceteza que quer Cancelar a operação", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.limparRelacaoCampostTodos()
            self.botoesDesativarRelacao()

    def botoesDesativarRelacao(self):
        self.__ui.btnRelacaoNovo.setEnabled(True)
        self.__ui.btnRelacaoSalvar.setEnabled(False)
        self.__ui.btnRelacaoCancelar.setEnabled(False)
        self.__ui.btnRelacaoPesquisar.setEnabled(False)

        self.__ui.txtRelacaoNomeFantasia.setEnabled(False)
        self.__ui.txtRelacaoSetor.setEnabled(False)
        self.__ui.txtRelacaoCargo.setEnabled(False)

    def setRelacaoSetor(self):
        _setor = SetoresCargosDao()
        lista = _setor.pesquisaSetor()

        for setores in lista:
            self.__ui.txtRelacaoSetor.addItem(setores[0])

    def setRelacaoCargo(self):
        _cargo = SetoresCargosDao()
        lista = _cargo.pesquisaCargo()

        for cargos in lista:
            self.__ui.txtRelacaoCargo.addItem(cargos[0])

    def pesquisarSetores(self):
        if self.__ui.radSetorBtnCodigo.isChecked():
            _setor = SetoresCargosDao()
            _pesquisar = _setor.pesquisarSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]


                # preenchendo o grid de pesquisa
                self.__ui.tbSetorPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str( tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorBtnFantasia.isChecked():
            _setor = SetoresCargosDao()
            _pesquisar = _setor.pesquisarSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorBtnRazaoSocial.isChecked():
            _setor = SetoresCargosDao()
            _pesquisar = _setor.pesquisarSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorBtnCnpj.isChecked():
            _setor = SetoresCargosDao()
            _pesquisar = _setor.pesquisarSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

            qtde_registros = len(_pesquisar)
            self._ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorBtnInsEstadual.isChecked():
            _setor = SetoresCargosDao()
            _pesquisar = _setor.pesquisarSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

            qtde_registros = len(_pesquisar)
            self._ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorBtnSetor.isChecked():
            _setor = SetoresCargosDao()
            _pesquisar = _setor.pesquisarSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        else:
            result = QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")
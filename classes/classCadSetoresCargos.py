
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.setGetConfimarEmpresa import ConfirmarEmpresa
from controller.setGetSetor import Setor, Cargo, Relacao
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
        self.__ui.txtCargoPesquisa.returnPressed.connect(self.pesquisarCargos)
        self.__ui.txtSetorCargoPesquisa.returnPressed.connect(self.pesquisarRelacao)

        self.__ui.tbSetorPesquisa.doubleClicked.connect(self.tablePesquisaSetor)

        self.__ui.tbCargoPesquisa.doubleClicked.connect(self.tablePesquisaCargo)

        self.__ui.tbSetorCargoPesquisa.doubleClicked.connect(self.tablePesquisaRelacao)

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
        self.__ui.btnCadSetoresEditar.setEnabled(False)
        self.__ui.btnCadSetoresCancelar.setEnabled(False)
        self.__ui.btnCadSetoresDeletar.setEnabled(False)
        #self.__ui.btnCadSetoresPesquisar.setEnabled(False)

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
        self.__ui.btnCadCargoEditar.setEnabled(False)
        self.__ui.btnCadCargoCancelar.setEnabled(False)
        self.__ui.btnCadCargoDeletar.setEnabled(False)
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
        self.__ui.btnRelacaoEditar.setEnabled(False)
        self.__ui.btnRelacaoCancelar.setEnabled(False)
        self.__ui.btnRelacaoDeletar.setEnabled(False)
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
            _setorId = SetoresCargosDao()
            _pesquisar = _setorId.pesquisarIdSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

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

        elif self.__ui.radSetorBtnFantasia.isChecked():
            _setorFantasia = SetoresCargosDao()
            _pesquisar = _setorFantasia.pesquisarFantasiaSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

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
            _setorRazaoSocial = SetoresCargosDao()
            _pesquisar = _setorRazaoSocial.pesquisarRazaoSocialSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

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
            _setorCnpj = SetoresCargosDao()
            _pesquisar = _setorCnpj.pesquisarCnpjSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

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

        elif self.__ui.radSetorBtnInsEstadual.isChecked():
            _setorInsEstdual = SetoresCargosDao()
            _pesquisar = _setorInsEstdual.pesquisarInscEstadualSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

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

        elif self.__ui.radSetorBtnSetor.isChecked():
            _setorSetor = SetoresCargosDao()
            _pesquisar = _setorSetor.pesquisarSetoresEmpresa(self.__ui.txtSetorPesquisa.text())

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

    def pesquisarCargos(self):
        if self.__ui.radCargoBtnCodigo.isChecked():
            _cargoId = SetoresCargosDao()
            _pesquisar = _cargoId.pesquisarIdCargoEmpresa(self.__ui.txtCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                cargo = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]


                # preenchendo o grid de pesquisa
                self.__ui.tbCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(cargo)))
                self.__ui.tbCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radCargoBtnFantasia.isChecked():
            _cargoFantasia = SetoresCargosDao()
            _pesquisar = _cargoFantasia.pesquisarFantasiaCargoEmpresa(self.__ui.txtCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                carga = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(carga)))
                self.__ui.tbCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radCargoBtnRazaoSocial.isChecked():
            _cargoRazaoSocial = SetoresCargosDao()
            _pesquisar = _cargoRazaoSocial.pesquisarRazaoSocialCargoEmpresa(self.__ui.txtCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                carga = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(carga)))
                self.__ui.tbCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radCargoBtnCnpj.isChecked():
            _cargoCnpj = SetoresCargosDao()
            _pesquisar = _cargoCnpj.pesquisarCnpjCargoEmpresa(self.__ui.txtCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                carga = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(carga)))
                self.__ui.tbCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radCargoBtnInsEstadual.isChecked():
            _cargoInsEstdual = SetoresCargosDao()
            _pesquisar = _cargoInsEstdual.pesquisarInscEstadualCargoEmpresa(self.__ui.txtCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                carga = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(carga)))
                self.__ui.tbCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radCargoBtnSetor.isChecked():
            _cargoSetor = SetoresCargosDao()
            _pesquisar = _cargoSetor.pesquisarCargoEmpresa(self.__ui.txtCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                carga = pesqui[1]
                fantasia = pesqui[2]
                razaoSocial = pesqui[3]
                cnpj = pesqui[4]
                inscrEstadual = pesqui[5]
                tipoEmpresa = pesqui[6]

                # preenchendo o grid de pesquisa
                self.__ui.tbCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(carga)))
                self.__ui.tbCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        else:
            result = QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")

    def pesquisarRelacao(self):
        if self.__ui.radSetorCargoBtnCodigo.isChecked():
            _relacaoId = SetoresCargosDao()
            _pesquisar = _relacaoId.pesquisarIdRelacaoEmpresa(self.__ui.txtSetorCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                cargo = pesqui[2]
                fantasia = pesqui[3]
                razaoSocial = pesqui[4]
                cnpj = pesqui[5]
                inscrEstadual = pesqui[6]
                tipoEmpresa = pesqui[7]


                # preenchendo o grid de pesquisa
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cargo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorCargoBtnFantasia.isChecked():
            _relacaoFantasia = SetoresCargosDao()
            _pesquisar = _relacaoFantasia.pesquisarFantasiaRelacaoEmpresa(self.__ui.txtSetorCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                cargo = pesqui[2]
                fantasia = pesqui[3]
                razaoSocial = pesqui[4]
                cnpj = pesqui[5]
                inscrEstadual = pesqui[6]
                tipoEmpresa = pesqui[7]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cargo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorCargoBtnRazaoSocial.isChecked():
            _relacaoRazaoSocial = SetoresCargosDao()
            _pesquisar = _relacaoRazaoSocial.pesquisarRazaoSocialRelacaoEmpresa(self.__ui.txtSetorCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                cargo = pesqui[2]
                fantasia = pesqui[3]
                razaoSocial = pesqui[4]
                cnpj = pesqui[5]
                inscrEstadual = pesqui[6]
                tipoEmpresa = pesqui[7]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cargo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorCargoBtnCnpj.isChecked():
            _relacaoCnpj = SetoresCargosDao()
            _pesquisar = _relacaoCnpj.pesquisarCnpjRelacaoEmpresa(self.__ui.txtSetorCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                cargo = pesqui[2]
                fantasia = pesqui[3]
                razaoSocial = pesqui[4]
                cnpj = pesqui[5]
                inscrEstadual = pesqui[6]
                tipoEmpresa = pesqui[7]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cargo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorCargoBtnSetor.isChecked():
            _relacaoSetor = SetoresCargosDao()
            _pesquisar = _relacaoSetor.pesquisarSetorRelacaoEmpresa(self.__ui.txtSetorCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                cargo = pesqui[2]
                fantasia = pesqui[3]
                razaoSocial = pesqui[4]
                cnpj = pesqui[5]
                inscrEstadual = pesqui[6]
                tipoEmpresa = pesqui[7]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cargo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        elif self.__ui.radSetorCargoBtnCargo.isChecked():
            _relacaoCargo = SetoresCargosDao()
            _pesquisar = _relacaoCargo.pesquisarCargoRelacaoEmpresa(self.__ui.txtSetorCargoPesquisa.text())

            qtde_registros = len(_pesquisar)
            self.__ui.tbSetorCargoPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                setor = pesqui[1]
                cargo = pesqui[2]
                fantasia = pesqui[3]
                razaoSocial = pesqui[4]
                cnpj = pesqui[5]
                inscrEstadual = pesqui[6]
                tipoEmpresa = pesqui[7]

                # preenchendo o grid de pesquisa
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(setor)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cargo)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(fantasia)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cnpj)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.__ui.tbSetorCargoPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(tipoEmpresa)))

                linha += 1

        else:
            result = QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")


    def tablePesquisaSetor(self, pesquisa):
        if self.__ui.txtCadSetoresCodigo.text() == '' and self.__ui.txtCadSetoresNomeFantasia.text() == '' and self.__ui.txtCadSetoresRazaoSocial.text() == '' and self.__ui.txtCadSetoresTipoEmpresa.text() == '' and self.__ui.txtCadSetoresInscricaoEstadual.text() == '' :
            self.setarCamposSetor()
            self.__ui.txtCadSetoresNomeFantasia.setEnabled(True)
            self.__ui.txtCadSetoresSetor.setEnabled(True)


        else:
            w = QWidget()
            result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.setarCamposSetor()
                self.__ui.txtCadSetoresNomeFantasia.setEnabled(True)
                self.__ui.txtCadSetoresSetor.setEnabled(True)

    def setarCamposSetor(self):

        itens = []
        for item in self.__ui.tbSetorPesquisa.selectedItems():
            itens.append(item.text())
        if len(itens) == 7:
            self.__botoesSetor()
            self.__botoesEditarSetor()
            self.__ui.txtCadSetoresCodigo.setText(str(itens[0]))
            self.__ui.txtCadSetoresSetor.setText(str(itens[1]))
            self.__ui.txtCadSetoresNomeFantasia.setText(str(itens[2]))
            self.__ui.txtCadSetoresRazaoSocial.setText(str(itens[3]))
            self.__ui.txtCadSetoresCnpj.setText(str(itens[4]))
            self.__ui.txtCadSetoresInscricaoEstadual.setText(str(itens[5]))
            self.__ui.txtCadSetoresTipoEmpresa.setText(str(itens[6]))


    def __botoesSetor(self):
        self.__ui.btnCadSetoresNovo.setEnabled(True)

        self.__ui.btnCadSetoresSalvar.setEnabled(False)
        self.__ui.btnCadSetoresEditar.setEnabled(False)
        self.__ui.btnCadSetoresCancelar.setEnabled(False)
        self.__ui.btnCadSetoresDeletar.setEnabled(False)

    def __botoesEditarSetor(self):
        self.__ui.btnCadSetoresNovo.setEnabled(False)

        self.__ui.btnCadSetoresSalvar.setEnabled(False)
        self.__ui.btnCadSetoresEditar.setEnabled(True)
        self.__ui.btnCadSetoresCancelar.setEnabled(True)
        self.__ui.btnCadSetoresDeletar.setEnabled(True)

    def tablePesquisaCargo(self, pesquisa):
        _cnpj = self.removerCaracter(self.__ui.txtCadCargoCnpj.text())
        if self.__ui.txtCadCargoCodigo.text() == '' and self.__ui.txtCadCargoNomeFantasia.text() == '' and self.__ui.txtCadCargoRazaoSocial.text() == '' and self.__ui.txtCadCargoTipoEmpresa.text() == '' and self.__ui.txtCadCargoInscricaoEstadual.text() == '' :
                self.setarCamposCargo()
                self.__ui.txtCadCargoNomeFantasia.setEnabled(True)
                self.__ui.txtCadCargoCargo.setEnabled(True)

        else:
                w = QWidget()
                result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.setarCamposCargo()
                    self.__ui.txtCadCargoNomeFantasia.setEnabled(True)
                    self.__ui.txtCadCargoCargo.setEnabled(True)

    def setarCamposCargo(self):

        itens = []
        for item in self.__ui.tbCargoPesquisa.selectedItems():
            itens.append(item.text())
        if len(itens) == 7:
            self.__botoesCargo()
            self.__botoesEditarCargo()
            self.__ui.txtCadCargoCodigo.setText(str(itens[0]))
            self.__ui.txtCadCargoCargo.setText(str(itens[1]))
            self.__ui.txtCadCargoNomeFantasia.setText(str(itens[2]))
            self.__ui.txtCadCargoRazaoSocial.setText(str(itens[3]))
            self.__ui.txtCadCargoCnpj.setText(str(itens[4]))
            self.__ui.txtCadCargoInscricaoEstadual.setText(str(itens[5]))
            self.__ui.txtCadCargoTipoEmpresa.setText(str(itens[6]))


    def __botoesCargo(self):
        self.__ui.btnCadCargoNovo.setEnabled(True)

        self.__ui.btnCadCargoSalvar.setEnabled(False)
        self.__ui.btnCadCargoEditar.setEnabled(False)
        self.__ui.btnCadCargoCancelar.setEnabled(False)
        self.__ui.btnCadCargoDeletar.setEnabled(False)

    def __botoesEditarCargo(self):
        self.__ui.btnCadCargoNovo.setEnabled(False)

        self.__ui.btnCadCargoSalvar.setEnabled(False)
        self.__ui.btnCadCargoEditar.setEnabled(True)
        self.__ui.btnCadCargoCancelar.setEnabled(True)
        self.__ui.btnCadCargoDeletar.setEnabled(True)

    def tablePesquisaRelacao(self, pesquisa):
        if self.__ui.txtRelacaoCodigo.text() == '' and self.__ui.txtRelacaoNomeFantasia.text() == '' and self.__ui.txtRelacaoRazaoSocial.text() == '' and self.__ui.txtRelacaoTipoEmpresa.text() == '' and self.__ui.txtRelacaoInscricaoEstadual.text() == '' :
            self.__ui.txtRelacaoSetor.clear()
            self.__ui.txtRelacaoCargo.clear()
            self.setarCamposRelacao()
            self.__ui.txtRelacaoNomeFantasia.setEnabled(True)
            self.__ui.txtRelacaoSetor.setEnabled(True)
            self.__ui.txtRelacaoCargo.setEnabled(True)


        else:
            w = QWidget()
            result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.__ui.txtRelacaoSetor.clear()
                self.__ui.txtRelacaoCargo.clear()
                self.setarCamposRelacao()
                self.__ui.txtRelacaoNomeFantasia.setEnabled(True)
                self.__ui.txtRelacaoSetor.setEnabled(True)
                self.__ui.txtRelacaoCargo.setEnabled(True)


    def setRelacaoSetorAtualizacao(self, dados):
        _setor = SetoresCargosDao()
        lista = _setor.pesquisaSetor()

        for setores in lista:
            if setores[0] != dados:
                self.__ui.txtRelacaoSetor.addItem(setores[0])

    def setRelacaoCargoAtualizacao(self, dados):
        _cargo = SetoresCargosDao()
        lista = _cargo.pesquisaCargo()

        for cargos in lista:
            if cargos[0] != dados:
                self.__ui.txtRelacaoCargo.addItem(cargos[0])


    def setarCamposRelacao(self):

        itens = []
        for item in self.__ui.tbSetorCargoPesquisa.selectedItems():
            itens.append(item.text())
        if len(itens) == 8:
            self.__botoesRelacao()
            self.__botoesEditarRelacao()
            self.__ui.txtRelacaoCodigo.setText(str(itens[0]))
            setor = str(itens[1])
            self.__ui.txtRelacaoSetor.addItem(setor)
            self.setRelacaoSetorAtualizacao(setor)
            cargo = str(itens[2])
            self.__ui.txtRelacaoCargo.addItem(cargo)
            self.setRelacaoCargoAtualizacao(cargo)
            self.__ui.txtRelacaoNomeFantasia.setText(str(itens[3]))
            self.__ui.txtRelacaoRazaoSocial.setText(str(itens[4]))
            self.__ui.txtRelacaoCnpj.setText(str(itens[5]))
            self.__ui.txtRelacaoInscricaoEstadual.setText(str(itens[6]))
            self.__ui.txtRelacaoTipoEmpresa.setText(str(itens[7]))


    def __botoesRelacao(self):
        self.__ui.btnRelacaoNovo.setEnabled(True)

        self.__ui.btnRelacaoSalvar.setEnabled(False)
        self.__ui.btnRelacaoEditar.setEnabled(False)
        self.__ui.btnRelacaoCancelar.setEnabled(False)
        self.__ui.btnRelacaoDeletar.setEnabled(False)

    def __botoesEditarRelacao(self):
        self.__ui.btnRelacaoNovo.setEnabled(False)

        self.__ui.btnRelacaoSalvar.setEnabled(False)
        self.__ui.btnRelacaoEditar.setEnabled(True)
        self.__ui.btnRelacaoCancelar.setEnabled(True)
        self.__ui.btnRelacaoDeletar.setEnabled(True)
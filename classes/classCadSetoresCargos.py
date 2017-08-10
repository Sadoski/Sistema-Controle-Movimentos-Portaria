
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.setGetConfimarEmpresa import ConfirmarEmpresa
from controller.setGetSetoresCargos import Setor
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
        self.__ui.txtRelacaooCnpj.clear()
        self.__ui.txtRelacaoInscricaoEstadual.clear()

    def pesquisarRelacaoEmpresa(self):

        _empresaDao = EmpresaDao()

        _empresa = _empresaDao.pesquisaEmpresaSetCar(str(self.__ui.txtCadCargoNomeFantasia.text()))
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

    def cadastrarSetor(self):
        if  self.__ui.CadSetoresCodigo and self.__ui.txtCadSetoresNomeFantasia and self.__ui.txtCadSetoresRazaoSocial and self.__ui.txtCadSetoresTipoEmpresa and self.__ui.txtCadSetoresCnpj and self.__ui.txtCadSetoresInscricaoEstadual == "":
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")
        else:
            _codigo = self.__ui.txtCadSetoresCodigo.text()
            _fantasia = self.__ui.txtCadSetoresNomeFantasia.text()
            _razaoSocial = self.__ui.txtCadSetoresRazaoSocial.text()
            _cnpj = self.__ui.txtCadSetoresCnpj.text()
            _incricao = self.__ui.txtCadSetoresInscricaoEstadual.text()
            _setor = self.__ui.txtCadSetoresSetor.text()

            __confiEmp = ConfirmarEmpresa(_codigo, _fantasia, _razaoSocial, _cnpj, _incricao)

            __empDao = EmpresaDao()

            __validar = __empDao.confirmarEmpresa(__confiEmp)

            if __validar == _codigo:
                __setor = Setor(_codigo, _setor)
                __cadSetor = SetoresCargosDao()
                __cadSetor.cadastrar(__setor)

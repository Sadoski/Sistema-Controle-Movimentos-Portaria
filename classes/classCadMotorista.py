import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetMotorista import Motorista
from controller.getSetVeiculoMotorista import VeiculoMotorista
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.motoristaDao import MotoristaDao
from telas.frmCadastroMotorista import Ui_frmCadastroMotorista

class CadastroMotoristas(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroMotorista()
        self.ui.setupUi(self)

        self.ui.txtNomeMotorista.returnPressed.connect(self.focusDataNacimento)
        self.ui.txtRg.returnPressed.connect(self.focusExpeditor)
        self.ui.txtExpeditor.returnPressed.connect(self.focusCpf)
        self.ui.txtCpf.returnPressed.connect(self.focusPis)
        self.ui.txtPis.returnPressed.connect(self.focusCnh)
        self.ui.txtCnh.returnPressed.connect(self.focusEndereco)
        self.ui.txtEndereco.returnPressed.connect(self.focusNumero)
        self.ui.txtNumero.returnPressed.connect(self.focusComplemento)
        self.ui.txtComplemento.returnPressed.connect(self.focusBairro)
        self.ui.txtBairro.returnPressed.connect(self.focusCep)
        self.ui.txtCep.returnPressed.connect(self.focusTelefone)
        self.ui.txtTelefone.returnPressed.connect(self.focusCelular)
        self.ui.txtCelular.returnPressed.connect(self.focusMarca)
        self.ui.txtMarca.returnPressed.connect(self.focusModelo)
        self.ui.txtModelo.returnPressed.connect(self.focusPlaca)

        self.ui.btnCadNovo.clicked.connect(self.botaoNovoCad)
        self.ui.btnCadSalvar.clicked.connect(self.cadastrarCadastro)
        self.ui.btnCadCancelar.clicked.connect(self.cancelarCadastro)

    def focusDataNacimento(self):
        self.ui.txtDataNascimento.setFocus()

    def focusRg(self):
        self.ui.txtRg.setFocus()

    def focusExpeditor(self):
        self.ui.txtExpeditor.setFocus()

    def focusCpf(self):
        self.ui.txtCpf.setFocus()

    def focusPis(self):
        self.ui.txtPis.setFocus()

    def focusCnh(self):
        self.ui.txtCnh.setFocus()

    def focusCategoriaCnh(self):
        self.ui.txtCategoriaCnh.setFocus()

    def focusEndereco(self):
        self.ui.txtEndereco.setFocus()

    def focusNumero(self):
        self.ui.txtNumero.setFocus()

    def focusComplemento(self):
        self.ui.txtComplemento.setFocus()

    def focusBairro(self):
        self.ui.txtBairro.setFocus()

    def focusCep(self):
        self.ui.txtCep.setFocus()

    def focusTelefone(self):
        self.ui.txtTelefone.setFocus()

    def focusCelular(self):
        self.ui.txtCelular.setFocus()

    def focusTipoVeiculo(self):
        self.ui.txtTipoVeiculo.setFocus()

    def focusMarca(self):
        self.ui.txtMarca.setFocus()

    def focusModelo(self):
        self.ui.txtModelo.setFocus()

    def focusPlaca(self):
        self.ui.txtPlaca.setFocus()

    def botaoNovoCad(self):
        self.ui.btnCadNovo.setEnabled(False)
        self.ui.btnCadSalvar.setEnabled(True)
        self.ui.btnCadCancelar.setEnabled(True)

        self.ui.grbMotorista.setEnabled(True)
        self.ui.grbVeiculo.setEnabled(True)

        self.addCategoria()
        self.addTipoVeiculo()

    def botaoCancelar(self):
        self.ui.btnCadNovo.setEnabled(True)
        self.ui.btnCadSalvar.setEnabled(False)
        self.ui.btnCadEditar.setEnabled(False)
        self.ui.btnCadCancelar.setEnabled(False)
        self.ui.btnCadDeletar.setEnabled(False)

        self.ui.grbMotorista.setEnabled(False)
        self.ui.grbVeiculo.setEnabled(False)

    def limparCampos(self):
        self.ui.txtidMotorista.clear()
        self.ui.txtNomeMotorista.clear()
        self.ui.txtRg.clear()
        self.ui.txtExpeditor.clear()
        self.ui.txtCpf.clear()
        self.ui.txtPis.clear()
        self.ui.txtCnh.clear()
        self.ui.txtCategoriaCnh.clear()
        self.ui.txtEndereco.clear()
        self.ui.txtCep.clear()
        self.ui.txtCidades.clear()
        self.ui.txtEstados.clear()
        self.ui.txtTelefone.clear()
        self.ui.txtCelular.clear()
        self.ui.txtTipoVeiculo.clear()
        self.ui.txtMarca.clear()
        self.ui.txtModelo.clear()
        self.ui.txtPlaca.clear()

    def addCategoria(self):
        __motoDao = MotoristaDao()
        __categoria = __motoDao.pesquisarCategoria()
        for cate in __categoria:
            self.ui.txtCategoriaCnh.addItem(cate[0])

    def addTipoVeiculo(self):
        __motoDao = MotoristaDao()
        __tipo = __motoDao.pesquisarTipoVeiculo()
        for cate in __tipo:
            self.ui.txtTipoVeiculo.addItem(cate[0])

    def cancelarCadastro(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja realmente cancelar a operação",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botaoCancelar()
            self.limparCampos()

    def cadastrarCadastro(self):
        _cidade = CidadesEstadosDao()
        __motoDao = MotoristaDao()

        nome = self.ui.txtNomeMotorista.text()
        nascimento = self.formatarData(self.ui.txtDataNascimento.text())
        rg = self.ui.txtRg.text()
        expeditor = self.ui.txtExpeditor.text()
        cpf = self.removerCaracter(self.ui.txtCpf.text())
        pis = self.ui.txtPis.text()
        cnh = self.ui.txtCnh.text()
        categoria = self.ui.txtCategoriaCnh.currentText()
        endereco = self.ui.txtEndereco.text()
        numero = self.ui.txtNumero.text()
        complemento = self.ui.txtComplemento.text()
        bairro = self.ui.txtBairro.text()
        _cep = self.removerCaracter(self.__ui.txtCep.text())
        if len(_cep) == 8:
            _cida = _cidade.idCidade(_cep, self.__ui.txtCidades.text(), self.__ui.txtEstados.text())
        else:
            return False
        telefone = self.ui.txtTelefone.text()
        celular = self.ui.txtCelular.text()

        if self.ui.radBtnMasculino.isChecked():
            sexo = 'MASCULINO'
        elif self.ui.radBtnFeminino.isChecked():
            sexo = 'FEMININO'
        else:
            return None
        __motorista = Motorista(None, nome, nascimento, rg, expeditor, cpf, pis, cnh, categoria, endereco, numero, complemento, bairro, _cida, telefone, celular, sexo)
        __mot = __motoDao.cadastrarMotorista(__motorista)

        if __mot != False:

            __idMotorista = __motoDao.pesquisarIdMotorista(__motorista)
            tipoVei = __motoDao.pesquisarIdTipoVeiculo(self.ui.txtTipoVeiculo.currentText())
            marca = self.ui.txtMarca.text()
            modelo = self.ui.txtModelo.text()
            placa = self.removerCaracter(self.ui.txtPlaca.text())

            __veiculo = VeiculoMotorista(__idMotorista, tipoVei, marca, modelo, placa)
            __motoDao.cadastrarVeiculoMotorista(__veiculo)

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
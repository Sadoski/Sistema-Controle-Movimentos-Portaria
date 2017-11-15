import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.cidadesEstadosDao import CidadesEstadosDao
from telas.frmCadastroPessoaJuridica import Ui_frmCadastroPessoaJuridica


class CadastroPessoaJuridica(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroPessoaJuridica()
        self.ui.setupUi(self)
        self.idCidade = ''

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

        self.ui.txtRazaoSocial.textChanged.connect(self.upperRazaoSocial)
        self.ui.txtFantasia.textChanged.connect(self.upperFantasia)
        self.ui.txtEndereco.textChanged.connect(self.upperEndereco)
        self.ui.txtNumero.textChanged.connect(self.upperNumero)
        self.ui.txtComplemento.textChanged.connect(self.upperComplemento)
        self.ui.txtBairro.textChanged.connect(self.upperBairro)
        self.ui.txtSite.textChanged.connect(self.upperSite)

        self.ui.txtCep.returnPressed.connect(self.pesquisarCidade)
        self.ui.txtCep.editingFinished.connect(self.pesquisarCidade)

        self.ui.txtCep.cursorPositionChanged.connect(self.positionCursorCep)
        self.ui.txtCnpj.cursorPositionChanged.connect(self.positionCursorCnpj)

    def upperRazaoSocial(self):
        self.ui.txtRazaoSocial.setText(self.ui.txtRazaoSocial.text().upper())

    def upperFantasia(self):
        self.ui.txtFantasia.setText(self.ui.txtFantasia.text().upper())

    def upperEndereco(self):
        self.ui.txtEndereco.setText(self.ui.txtEndereco.text().upper())

    def upperNumero(self):
        self.ui.txtNumero.setText(self.ui.txtNumero.text().upper())

    def upperComplemento(self):
        self.ui.txtComplemento.setText(self.ui.txtComplemento.text().upper())

    def upperBairro(self):
        self.ui.txtBairro.setText(self.ui.txtBairro.text().upper())

    def upperSite(self):
        self.ui.txtSite.setText(self.ui.txtSite.text().upper())

    def pesquisarCidade(self):
        _cep = self.removerCaracter(self.ui.txtCep.text())
        if len(_cep) < 8:
            self.idCidade = ''
            self.ui.txtCidade.clear()
            self.ui.txtEstado.clear()
        else:
            cidades = CidadesEstadosDao()
            cid = cidades.cidade(_cep)

            for cidade in cid:
                self.ui.txtCidade.setText(cidade[0])
                self.ui.txtEstado.setText(cidade[1])
            if cid == []:
                self.idCidade = ''
                self.ui.txtCidade.clear()
                self.ui.txtEstado.clear()

    def positionCursorCnpj(self):
        texto = self.removerCaracter(self.ui.txtCnpj.text())

        if len(texto) == 0:
            self.ui.txtCnpj.setCursorPosition(0)
        elif len(texto) <= 1:
            b = len(texto)
            self.ui.txtCnpj.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) <5:
            b = len(texto)+1
            self.ui.txtCnpj.setCursorPosition(b)
        elif len(texto) >= 5 and len(texto) <8:
            b = len(texto)+2
            self.ui.txtCnpj.setCursorPosition(b)
        elif len(texto) >= 8 and len(texto) <12:
            b = len(texto)+3
            self.ui.txtCnpj.setCursorPosition(b)
        elif len(texto) >= 12 :
            b = len(texto)+4
            self.ui.txtCnpj.setCursorPosition(b)

    def positionCursorCep(self):
        texto = self.removerCaracter(self.ui.txtCep.text())
        if len(texto) == 0:
            self.ui.txtCep.setCursorPosition(0)
        elif len(texto) <= 4:
            b = len(texto)
            self.ui.txtCep.setCursorPosition(b)
        elif len(texto) >= 5 and len(texto) <9:
            b = len(texto)+1
            self.ui.txtCep.setCursorPosition(b)

    def novo(self):
        self.limparCampos()
        self.ui.grbDados.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

    def cancelar(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Deseja realmente cancelar a operação", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.limparCampos()
            self.ui.grbDados.setEnabled(False)
            self.ui.btnNovo.setEnabled(True)
            self.ui.btnSalvar.setEnabled(False)
            self.ui.btnEditar.setEnabled(False)
            self.ui.btnCancelar.setEnabled(False)
            self.ui.btnDeletar.setEnabled(False)

    def limparCampos(self):
       self.ui.txtRazaoSocial.clear()
       self.ui.txtFantasia.clear()
       self.ui.txtCnpj.clear()
       self.ui.txtInsEstadual.clear()
       self.ui.txtEndereco.clear()
       self.ui.txtNumero.clear()
       self.ui.txtComplemento.clear()
       self.ui.txtBairro.clear()
       self.ui.txtCep.clear()
       self.ui.txtCidade.clear()
       self.ui.txtEstado.clear()
       self.ui.txtSite.clear()
       self.idCidade = ''

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

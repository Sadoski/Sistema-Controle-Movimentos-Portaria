import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetPessoaJuridica import PessoaJuridica
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.pesquisarPessoaJuridicaDao import PesquisarPessoaJuridicaDao
from dao.pessoaJuridicaDao import PessoaJuridicaDao
from telas.frmCadastroPessoaJuridica import Ui_frmCadastroPessoaJuridica
from telas.frmPesquisarPessoaFisica import Ui_frmPesquisarPessoaFisica
from telas.frmPesquisarPessoaJuridica import Ui_frmPesquisarPessoaJuridica


class CadastroPessoaJuridica(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroPessoaJuridica()
        self.ui.setupUi(self)
        self.pessoa = ''
        self.idCidade = ''

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnEditar.clicked.connect(self.editar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnDeletar.clicked.connect(self.deletar)

        self.ui.txtRazaoSocial.textChanged.connect(self.upperRazaoSocial)
        self.ui.txtFantasia.textChanged.connect(self.upperFantasia)
        self.ui.txtEndereco.textChanged.connect(self.upperEndereco)
        self.ui.txtNumero.textChanged.connect(self.upperNumero)
        self.ui.txtComplemento.textChanged.connect(self.upperComplemento)
        self.ui.txtBairro.textChanged.connect(self.upperBairro)
        self.ui.txtSite.textChanged.connect(self.upperSite)

        self.ui.txtCnpj.editingFinished.connect(self.validacaoCnpj)

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
                self.idCidade = cidade[0]
                self.ui.txtCidade.setText(cidade[1])
                self.ui.txtEstado.setText(cidade[2])
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

    def desativarCampos(self):
        self.limparCampos()
        self.ui.grbDados.setEnabled(False)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def cancelar(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Deseja realmente cancelar a operação", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.limparCampos()
            self.desativarCampos()

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
       self.pessoa = ''
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

    def validacaoCnpj(self):
        _cnpj = self.removerCaracter(self.ui.txtCnpj.text())
        if len(_cnpj) == 14:
            _val = self.validaCnpj(_cnpj)
            if _val == False:
                w = QWidget()
                result = QMessageBox.critical(w, 'Atenção', "CNPJ Invalido, por favor insira um CNPJ Valido")
                return False


    def validaCnpj(self,cnpj):
        #Recebe um CNPJ e retorna True se formato válido ou False se inválido

        cnpj = self.removerCaracter(cnpj)

        if len(cnpj) != 14 or not cnpj.isnumeric():
            w = QWidget()
            result = QMessageBox.critical(w, 'Atenção', "CNPJ Invalido, por favor insira um CNPJ Valido")
            return False

        verificadores = cnpj[-2:]
        lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        #Calcular o primeiro digito verificador'
        soma = 0
        for numero, ind in zip(cnpj[:-1], range(len(cnpj[:-2]))):
            soma += int(numero) * int(lista_validacao_um[ind])

        soma = soma % 11
        digito_um = 0 if soma < 2 else 11 - soma

        #Calcular o segundo digito verificador
        soma = 0
        for numero, ind in zip(cnpj[:-1], range(len(cnpj[:-1]))):
            soma += int(numero) * int(lista_validacao_dois[ind])

        soma = soma % 11
        digito_dois = 0 if soma < 2 else 11 - soma

        return verificadores == str(digito_um) + str(digito_dois)

    def cadastrar(self):
        if self.ui.txtRazaoSocial.text() != '' and self.ui.txtFantasia.text() != '' and self.removerCaracter(self.ui.txtCnpj.text()) != '' and self.ui.txtInsEstadual.text() != '' and self.ui.txtEndereco.text() != '' and self.ui.txtNumero.text() != '' and  self.ui.txtComplemento.text() != '' and  self.ui.txtBairro.text() != '' and self.ui.txtCidade.text() != '' and self.ui.txtCep.text() != '' and self.ui.txtSite.text() != '':

            razao = self.ui.txtRazaoSocial.text()
            fantasia = self.ui.txtFantasia.text()
            cnpj = self.removerCaracter(self.ui.txtCnpj.text())
            inscricao = self.ui.txtInsEstadual.text()
            endereco = self.ui.txtEndereco.text()
            numero = self.ui.txtNumero.text()
            complemento = self.ui.txtComplemento.text()
            bairro = self.ui.txtBairro.text()
            site = self.ui.txtSite.text()
            cidade = self.idCidade

            pessoaJuridica = PessoaJuridica(None, razao, fantasia, cnpj, inscricao, endereco, numero, complemento, bairro, cidade,  None, None, None, site)
            __dao = PessoaJuridicaDao()
            __dao.pesquisarPessoaJuridica(pessoaJuridica)
            __dao.cadastrarPessoaJuridica(pessoaJuridica)
            self.desativarCampos()
        else:
            QMessageBox.critical(QWidget(), 'Atenção', "Por Favor, preencham os campos obrigtorios ")


    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialog = QDialog(self)
            self.__pesquisar =  Ui_frmPesquisarPessoaJuridica()
            self.__pesquisar.setupUi(self.dialog)

            self.__pesquisar.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisar.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisar.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        if self.__pesquisar.radBtnCodigo.isChecked():
            __codigo= self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaCodigo(__codigo)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnRazaoSocial.isChecked():
            __razao = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaRazaoSocial(__razao)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnFantasia.isChecked():
            __fantasia = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaFantasia(__fantasia)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnCnpj.isChecked():
            __cnpj = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaCnpj(__cnpj)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisar.radBtnInsEstadual.isChecked():
            __inscricao = self.__pesquisar.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaInsEstadual(__inscricao)

            self.setarTabelaPesquisa(__retorno)

        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisa(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisar.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            razao = pesqui[1]
            fantasia = pesqui[2]
            cnpj = pesqui[3]
            inscricao = pesqui[4]
            endereco = pesqui[5]
            numero = pesqui[6]
            complemento = pesqui[7]
            bairro = pesqui[8]
            cidade = pesqui[9]
            estado = pesqui[10]
            cep = pesqui[11]
            site = pesqui[12]


            # preenchendo o grid de pesquisa
            self.__pesquisar.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisar.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(razao)))
            self.__pesquisar.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
            self.__pesquisar.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
            self.__pesquisar.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscricao)))
            self.__pesquisar.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisar.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisar.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisar.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisar.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisar.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisar.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisar.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(site)))


            linha += 1

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def setarCampos(self):
        itens = []

        for item in self.__pesquisar.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = str(itens[0])
        razao = str(itens[1])
        fantasia = str(itens[2])
        cnpj = str(itens[3])
        inscricao = str(itens[4])
        endereco = str(itens[5])
        numero = str(itens[6])
        complemento = str(itens[7])
        bairro = str(itens[8])
        cidade = str(itens[9])
        estado = str(itens[10])
        cep = str(itens[11])
        site = str(itens[12])


        __dados = PessoaJuridica(codigo, razao, fantasia, cnpj, inscricao, endereco, numero, complemento, bairro, None, cidade, estado, cep, site)
        self.setCampos(__dados)
        self.botoesEditar()
        self.dialog.close()

    def setCampos(self, campos):
        self.pessoa = campos.getIdPesJuridica
        self.ui.txtRazaoSocial.setText(campos.getRazao)
        self.ui.txtFantasia.setText(campos.getFantasia)
        self.ui.txtCnpj.setText(campos.getCnpj)
        self.ui.txtInsEstadual.setText(campos.getInscricao)
        self.ui.txtEndereco.setText(campos.getEndereco)
        self.ui.txtNumero.setText(campos.getNumero)
        self.ui.txtComplemento.setText(campos.getComplemento)
        self.ui.txtBairro.setText(campos.getBairro)
        self.ui.txtCep.setText(campos.getCep)
        self.ui.txtCidade.setText(campos.getCidade)
        self.ui.txtEstado.setText(campos.getEstado)
        self.ui.txtSite.setText(campos.getSite)


    def botoesEditar(self):
        self.ui.grbDados.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)

    def editar(self):
        if self.ui.txtRazaoSocial.text() != '' and self.ui.txtFantasia.text() != '' and self.removerCaracter(self.ui.txtCnpj.text()) != '' and self.ui.txtInsEstadual.text() != '' and self.ui.txtEndereco.text() != '' and self.ui.txtNumero.text() != '' and  self.ui.txtComplemento.text() != '' and  self.ui.txtBairro.text() != '' and self.ui.txtCidade.text() != '' and self.ui.txtCep.text() != '' and self.ui.txtSite.text() != '':
            codigo = self.pessoa
            razao = self.ui.txtRazaoSocial.text()
            fantasia = self.ui.txtFantasia.text()
            cnpj = self.removerCaracter(self.ui.txtCnpj.text())
            inscricao = self.ui.txtInsEstadual.text()
            endereco = self.ui.txtEndereco.text()
            numero = self.ui.txtNumero.text()
            complemento = self.ui.txtComplemento.text()
            bairro = self.ui.txtBairro.text()
            site = self.ui.txtSite.text()
            cid = CidadesEstadosDao()
            cidade = cid.idCidade(self.removerCaracter(self.ui.txtCep.text()), self.ui.txtCidade.text(), self.ui.txtEstado.text())

            pessoaJuridica = PessoaJuridica(codigo, razao, fantasia, cnpj, inscricao, endereco, numero, complemento, bairro, cidade, None, None, None, site)
            __dao = PessoaJuridicaDao()
            __dao.atualizarPessoaJuridica(pessoaJuridica)
            self.desativarCampos()
        else:
            QMessageBox.critical(QWidget(), 'Atenção', "Por Favor, preencham os campos obrigtorios ")

    def deletar(self):
        result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja excluir esse registro", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            fisicaDao = PessoaJuridicaDao()
            fisicaDao.deletarPessoaJuridica(self.pessoa)
            self.desativarCampos()
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetCliente import Cliente
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.clienteDao import ClienteDao
from dao.empresaDao import EmpresaDao
from telas.frmCadastroClientes import Ui_frmCadastroClientes

class CadastroClientes(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroClientes()
        self.ui.setupUi(self)

        self.ui.txtFantasiaEmpresa.returnPressed.connect(self.focusCnpjFornecedor)
        self.ui.txtCnpjCliente.returnPressed.connect(self.focusInscricaoEstadualFornecedor)
        self.ui.txtInscricaoEstadualCliente.returnPressed.connect(self.focustxtFantasiaFornecedor)
        self.ui.txtFantasiaCliente.returnPressed.connect(self.focusRazaoSocialFornecedor)
        self.ui.txtRazaoSocialCliente.returnPressed.connect(self.focusEnderecoFornecedor)
        self.ui.txtEnderecoCliente.returnPressed.connect(self.focustNumeroFornecedor)
        self.ui.txtNumeroCliente.returnPressed.connect(self.focusComplementoFornecedor)
        self.ui.txtComplementoCliente.returnPressed.connect(self.focusBairroFornecedor)
        self.ui.txtBairroCliente.returnPressed.connect(self.focusCepFornecedor)
        self.ui.txtCepCliente.returnPressed.connect(self.focusTelefoneFornecedor)
        self.ui.txtTelefoneCliente.returnPressed.connect(self.focusSiteFornecedor)
        self.ui.txtSiteCliente.returnPressed.connect(self.focusEmailFornecedor)

        self.ui.txtPesquisa.returnPressed.connect(self.pesquisar)

        self.ui.txtFantasiaEmpresa.editingFinished.connect(self.pesquisarEmpresa)
        self.ui.txtCepCliente.editingFinished.connect(self.pesquisarCidade)
        self.ui.txtCnpjCliente.editingFinished.connect(self.validacaoCnpj)

        self.ui.btnNovo.clicked.connect(self.botaoNovoCad)
        self.ui.btnSalvar.clicked.connect(self.cadastroFornecedor)
        self.ui.btnEditar.clicked.connect(self.atualizarFornecedor)
        self.ui.btnCancelar.clicked.connect(self.cancelarCadastro)
        self.ui.btnDeletar.clicked.connect(self.deletarEmpresa)

        self.ui.tbPesquisa.doubleClicked.connect(self.tablePesquisa)

    def focusCnpjFornecedor(self):
        self.ui.txtCnpjCliente.setFocus()

    def focusInscricaoEstadualFornecedor(self):
        self.ui.txtInscricaoEstadualCliente.setFocus()

    def focustxtFantasiaFornecedor(self):
        self.ui.txtFantasiaCliente.setFocus()

    def focusRazaoSocialFornecedor(self):
        self.ui.txtRazaoSocialCliente.setFocus()

    def focusEnderecoFornecedor(self):
        self.ui.txtEnderecoCliente.setFocus()

    def focustNumeroFornecedor(self):
        self.ui.txtNumeroCliente.setFocus()

    def focusComplementoFornecedor(self):
        self.ui.txtComplementoCliente.setFocus()

    def focusBairroFornecedor(self):
        self.ui.txtBairroCliente.setFocus()

    def focusCepFornecedor(self):
        self.ui.txtCepCliente.setFocus()

    def focusTelefoneFornecedor(self):
        self.ui.txtTelefoneCliente.setFocus()

    def focusSiteFornecedor(self):
        self.ui.txtSiteCliente.setFocus()

    def focusEmailFornecedor(self):
        self.ui.txtEmailCliente.setFocus()

    def limparCamposEmp(self):
        self.ui.txtIdEmpresa.clear()
        self.ui.txtRazaoSocialEmpresa.clear()
        self.ui.txtCnpjEmpresa.clear()
        self.ui.txtInscricaoEstaduaEmpresa.clear()

    def pesquisarEmpresa(self):
        _empresaDao = EmpresaDao()

        _empresa = _empresaDao.pesquisaEmpresa(str(self.ui.txtFantasiaEmpresa.text()))
        if _empresa == False:
            self.limparCamposEmp()
        else:
            self.limparCamposEmp()
            for empe in _empresa:
                self.ui.txtIdEmpresa.setText(str(empe[0]))
                self.ui.txtRazaoSocialEmpresa.setText(empe[1])
                self.ui.txtCnpjEmpresa.setText(empe[2])
                self.ui.txtInscricaoEstaduaEmpresa.setText(empe[3])

    def pesquisarCidade(self):
        _cep = self.removerCaracter(self.ui.txtCepCliente.text())
        if len(_cep) < 8:
            self.ui.txtCidadesCliente.clear()
            self.ui.txtEstadosCliente.clear()
        else:
            cidades = CidadesEstadosDao()
            cid = cidades.cidade(_cep)

            for cidade in cid:
                self.ui.txtCidadesCliente.setText(cidade[0])
                self.ui.txtEstadosCliente.setText(cidade[1])
            if cid == []:
                self.ui.txtCidadesCliente.clear()
                self.ui.txtEstadosCliente.clear()

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
        _cnpj = self.removerCaracter(self.ui.txtCnpjCliente.text())
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

    def botaoNovoCad(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)

        self.ui.btnPesquisar.setEnabled(True)
        self.ui.txtFantasiaEmpresa.setEnabled(True)
        self.ui.grbDadosCliente.setEnabled(True)

        self.ui.txtFantasiaEmpresa.setFocus()

    def botaoCancelar(self):
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

        self.ui.btnPesquisar.setEnabled(False)
        self.ui.txtFantasiaEmpresa.setEnabled(False)
        self.ui.grbDadosCliente.setEnabled(False)

    def limparCampos(self):
        self.ui.txtIdEmpresa.clear()
        self.ui.txtFantasiaEmpresa.clear()
        self.ui.txtRazaoSocialEmpresa.clear()
        self.ui.txtCnpjEmpresa.clear()
        self.ui.txtInscricaoEstaduaEmpresa.clear()

        self.ui.txtIdCliente.clear()
        self.ui.txtCnpjCliente.clear()
        self.ui.txtInscricaoEstadualCliente.clear()
        self.ui.txtFantasiaCliente.clear()
        self.ui.txtRazaoSocialCliente.clear()
        self.ui.txtEnderecoCliente.clear()
        self.ui.txtNumeroCliente.clear()
        self.ui.txtComplementoCliente.clear()
        self.ui.txtBairroCliente.clear()
        self.ui.txtTelefoneCliente.clear()
        self.ui.txtSiteCliente.clear()
        self.ui.txtEmailCliente.clear()
        self.ui.txtCepCliente.clear()
        self.ui.txtCidadesCliente.clear()
        self.ui.txtEstadosCliente.clear()

    def cadastroFornecedor(self):

        if self.ui.txtIdEmpresa.text() != "" and self.ui.txtFantasiaEmpresa.text() != "" and self.ui.txtRazaoSocialEmpresa.text() != "" and self.ui.txtInscricaoEstadualCliente.text() != "" and self.ui.txtFantasiaCliente.text() != "" and self.ui.txtRazaoSocialCliente.text() != "" and self.ui.txtEnderecoCliente.text() != "" and self.ui.txtNumeroCliente.text() != "" and self.ui.txtBairroCliente.text() != "" and self.ui.txtCidadesCliente.text() != "" and self.ui.txtEstadosCliente.text() != "":
            _cidade = CidadesEstadosDao()

            idEmpresa = self.ui.txtIdEmpresa.text()
            fanEmp = self.ui.txtFantasiaEmpresa.text()
            razaoEmp = self.ui.txtRazaoSocialEmpresa.text()
            cnpjEmp = self.ui.txtCnpjEmpresa.text()

            cnpjFor = self.removerCaracter(self.ui.txtCnpjCliente.text())
            inscFor = self.ui.txtInscricaoEstadualCliente.text()
            fantasia = self.ui.txtFantasiaCliente.text()
            razaoFor = self.ui.txtRazaoSocialCliente.text()
            endereco = self.ui.txtEnderecoCliente.text()
            numero = self.ui.txtNumeroCliente.text()
            complemeto = self.ui.txtComplementoCliente.text()
            bairro = self.ui.txtBairroCliente.text()
            telefone = self.removerCaracter(self.ui.txtTelefoneCliente.text())
            site = self.ui.txtSiteCliente.text()
            email = self.ui.txtEmailCliente.text()

            _cep = self.removerCaracter(self.ui.txtCepCliente.text())
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self.ui.txtCidadesCliente.text(), self.ui.txtEstadosCliente.text())
            else:
                return False
            __cliente = Cliente(None, cnpjFor, inscFor, fantasia, razaoFor, endereco, numero, complemeto, bairro, telefone, site, email, _cida, idEmpresa)
            __forDao = ClienteDao()
            __dao = __forDao.cadastrarCliente(__cliente)
            if __dao != False:
                self.limparCampos()
                self.botaoCancelar()

        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")

    def atualizarFornecedor(self):

        if self.ui.txtIdEmpresa.text() != "" and self.ui.txtFantasiaEmpresa.text() != "" and self.ui.txtRazaoSocialEmpresa.text() != "" and self.ui.txtCnpjCliente.text() != "" and self.ui.txtInscricaoEstadualCliente.text() != "" and self.ui.txtFantasiaCliente.text() != "" and self.ui.txtRazaoSocialCliente.text() != "" and self.ui.txtEnderecoCliente.text() != "" and self.ui.txtNumeroCliente.text() != "" and self.ui.txtBairroCliente.text() != "" and self.ui.txtTelefoneCliente.text() != "" and self.ui.txtCidadesCliente.text() != "" and self.ui.txtEstadosCliente.text() != "":
            _cidade = CidadesEstadosDao()

            idEmpresa = self.ui.txtIdEmpresa.text()
            fanEmp = self.ui.txtFantasiaEmpresa.text()
            razaoEmp = self.ui.txtRazaoSocialEmpresa.text()
            cnpjEmp = self.ui.txtCnpjEmpresa.text()

            idfor = self.ui.txtIdCliente.text()
            cnpjFor = self.removerCaracter(self.ui.txtCnpjCliente.text())
            inscFor = self.ui.txtInscricaoEstadualCliente.text()
            fantasia = self.ui.txtFantasiaCliente.text()
            razaoFor = self.ui.txtRazaoSocialCliente.text()
            endereco = self.ui.txtEnderecoCliente.text()
            numero = self.ui.txtNumeroCliente.text()
            complemeto = self.ui.txtComplementoCliente.text()
            bairro = self.ui.txtBairroCliente.text()
            telefone = self.removerCaracter(self.ui.txtTelefoneCliente.text())
            site = self.ui.txtSiteCliente.text()
            email = self.ui.txtEmailCliente.text()

            _cep = self.removerCaracter(self.ui.txtCepCliente.text())
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self.ui.txtCidadesCliente.text(), self.ui.txtEstadosCliente.text())
            else:
                return False
            __cliente = Cliente(idfor, cnpjFor, inscFor, fantasia, razaoFor, endereco, numero, complemeto, bairro, telefone, site, email, _cida, idEmpresa)
            __cliDao = ClienteDao()
            __dao = __cliDao.atualizarCliente(__cliente)
            if __dao != False:
                self.limparCampos()
                self.botaoCancelar()

        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")

    def cancelarCadastro(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja realmente cancelar a operação",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botaoCancelar()
            self.limparCampos()

    def deletarEmpresa(self):

        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja excluir essa empresa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            __cliDao = ClienteDao()
            __dao = __cliDao.deletarFornecedor(self.ui.txtIdCliente.text())
            if __dao != False:
                self.limparCampos()
                self.botaoCancelar()

    def pesquisar(self):
        __cliDao = ClienteDao()
        if self.ui.radBtnCodigo.isChecked():
            _pesquisarCod = __cliDao.pesquisaCodigo(self.ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarCod)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarCod:
                # capturando os dados da tupla

                codigo = pesqui[0]
                fantasia = pesqui[1]
                razaoSocial = pesqui[2]
                cnpj = pesqui[3]
                inscrEstadual = pesqui[4]
                endereco = pesqui[5]
                numero = pesqui[6]
                complemento = pesqui[7]
                bairro = pesqui[8]
                telefone = pesqui[9]
                site = pesqui[10]
                email = pesqui[11]
                cep = pesqui[12]
                cidade = pesqui[13]
                estado = pesqui[14]
                idEmpresa = pesqui[15]
                fanEmp = pesqui[16]
                razaoEmp = pesqui[17]
                cnpjEmp = pesqui[18]
                insEmp = pesqui[19]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(fantasia)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(site)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(email)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(idEmpresa)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(fanEmp)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmp)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmp)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEmp)))

                linha += 1

        elif self.ui.radBtnFantasia.isChecked():
            _pesquisarFantasia = __cliDao.pesquisaFantasia(str(self.ui.txtPesquisa.text()))

            qtde_registros = len(_pesquisarFantasia)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarFantasia:
                # capturando os dados da tupla

                codigo = pesqui[0]
                fantasia = pesqui[1]
                razaoSocial = pesqui[2]
                cnpj = pesqui[3]
                inscrEstadual = pesqui[4]
                endereco = pesqui[5]
                numero = pesqui[6]
                complemento = pesqui[7]
                bairro = pesqui[8]
                telefone = pesqui[9]
                site = pesqui[10]
                email = pesqui[11]
                cep = pesqui[12]
                cidade = pesqui[13]
                estado = pesqui[14]
                idEmpresa = pesqui[15]
                fanEmp = pesqui[16]
                razaoEmp = pesqui[17]
                cnpjEmp = pesqui[18]
                insEmp = pesqui[19]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(fantasia)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(site)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(email)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(idEmpresa)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(fanEmp)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmp)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmp)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEmp)))

                linha += 1

        elif self.ui.radBtnRazaoSocial.isChecked():
            _pesquisarRazaoSocial = __cliDao.pesquisaRazaoSocial(str(self.ui.txtPesquisa.text()))

            qtde_registros = len(_pesquisarRazaoSocial)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarRazaoSocial:
                # capturando os dados da tupla

                codigo = pesqui[0]
                fantasia = pesqui[1]
                razaoSocial = pesqui[2]
                cnpj = pesqui[3]
                inscrEstadual = pesqui[4]
                endereco = pesqui[5]
                numero = pesqui[6]
                complemento = pesqui[7]
                bairro = pesqui[8]
                telefone = pesqui[9]
                site = pesqui[10]
                email = pesqui[11]
                cep = pesqui[12]
                cidade = pesqui[13]
                estado = pesqui[14]
                idEmpresa = pesqui[15]
                fanEmp = pesqui[16]
                razaoEmp = pesqui[17]
                cnpjEmp = pesqui[18]
                insEmp = pesqui[19]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(fantasia)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(site)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(email)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(idEmpresa)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(fanEmp)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmp)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmp)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEmp)))

                linha += 1

        elif self.ui.radBtnCnpj.isChecked():
            _pesquisarCnpj = __cliDao.pesquisaCnpj(self.ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarCnpj)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarCnpj:
                # capturando os dados da tupla

                codigo = pesqui[0]
                fantasia = pesqui[1]
                razaoSocial = pesqui[2]
                cnpj = pesqui[3]
                inscrEstadual = pesqui[4]
                endereco = pesqui[5]
                numero = pesqui[6]
                complemento = pesqui[7]
                bairro = pesqui[8]
                telefone = pesqui[9]
                site = pesqui[10]
                email = pesqui[11]
                cep = pesqui[12]
                cidade = pesqui[13]
                estado = pesqui[14]
                idEmpresa = pesqui[15]
                fanEmp = pesqui[16]
                razaoEmp = pesqui[17]
                cnpjEmp = pesqui[18]
                insEmp = pesqui[19]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(fantasia)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(site)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(email)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(idEmpresa)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(fanEmp)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmp)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmp)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEmp)))

                linha += 1

        elif self.ui.radBtnInsEstadual.isChecked():
            _pesquisarInsEstadual = __cliDao.pesquisaInscEstadual(self.ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarInsEstadual)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarInsEstadual:
                # capturando os dados da tupla

                codigo = pesqui[0]
                fantasia = pesqui[1]
                razaoSocial = pesqui[2]
                cnpj = pesqui[3]
                inscrEstadual = pesqui[4]
                endereco = pesqui[5]
                numero = pesqui[6]
                complemento = pesqui[7]
                bairro = pesqui[8]
                telefone = pesqui[9]
                site = pesqui[10]
                email = pesqui[11]
                cep = pesqui[12]
                cidade = pesqui[13]
                estado = pesqui[14]
                idEmpresa = pesqui[15]
                fanEmp = pesqui[16]
                razaoEmp = pesqui[17]
                cnpjEmp = pesqui[18]
                insEmp = pesqui[19]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(fantasia)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(razaoSocial)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(site)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(email)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(idEmpresa)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(fanEmp)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(razaoEmp)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(cnpjEmp)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(insEmp)))

                linha += 1

        else:
            result = QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")

    def botaoEditar(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)

        self.ui.txtFantasiaEmpresa.setEnabled(True)
        self.ui.grbDadosCliente.setEnabled(True)

    def tablePesquisa(self, pesquisa):
        if self.ui.txtIdEmpresa.text() != "" and self.ui.txtFantasiaEmpresa.text() != "" and self.ui.txtRazaoSocialEmpresa.text() != "" and self.ui.txtInscricaoEstaduaEmpresa.text() != "" and self.ui.txtInscricaoEstadualFornecedor.text() != "" and self.ui.txtFantasiaFornecedor.text() != "" and self.ui.txtRazaoSocialFornecedor.text() != "" and self.ui.txtEnderecoFornecedor.text() != "" and self.ui.txtNumeroFornecedor.text() != "" and self.ui.txtBairroFornecedor.text() != "" and self.ui.txtTelefoneFornecedor.text() != "" and self.ui.txtCidadesFornecedor.text() != "" and self.ui.txtEstadosFornecedor.text() != "":
                self.setarCampos()
        else:
                w = QWidget()
                result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.setarCampos()

    def setarCampos(self):

        itens = []
        for item in self.ui.tbPesquisa.selectedItems():
            itens.append(item.text())
        if len(itens) == 20:
            self.botaoNovoCad()
            self.botaoEditar()
            self.ui.txtIdCliente.setText(str(itens[0]))
            self.ui.txtFantasiaCliente.setText(str(itens[1]))
            self.ui.txtRazaoSocialCliente.setText(str(itens[2]))
            self.ui.txtCnpjCliente.setText(str(itens[3]))
            self.ui.txtInscricaoEstadualCliente.setText(str(itens[4]))
            self.ui.txtEnderecoCliente.setText(str(itens[5]))
            self.ui.txtNumeroCliente.setText(str(itens[6]))
            self.ui.txtComplementoCliente.setText(str(itens[7]))
            self.ui.txtBairroCliente.setText(str(itens[8]))
            self.ui.txtTelefoneCliente.setText(str(itens[9]))
            self.ui.txtSiteCliente.setText(str(itens[10]))
            self.ui.txtEmailCliente.setText(str(itens[11]))
            self.ui.txtCepCliente.setText(str(itens[12]))
            self.ui.txtCidadesCliente.setText(str(itens[13]))
            self.ui.txtEstadosCliente.setText(str(itens[14]))
            self.ui.txtIdEmpresa.setText(str(itens[15]))
            self.ui.txtFantasiaEmpresa.setText(str(itens[16]))
            self.ui.txtRazaoSocialEmpresa.setText(str(itens[17]))
            self.ui.txtCnpjEmpresa.setText(str(itens[18]))
            self.ui.txtInscricaoEstaduaEmpresa.setText(str(itens[19]))
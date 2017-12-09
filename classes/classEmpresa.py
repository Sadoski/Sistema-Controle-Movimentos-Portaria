from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classValidator import Validator
from controller.getSetContatoEmail import ContatoEmail
from controller.getSetContatoTelefone import ContatoTelefone
from controller.getSetCargo import Cargo
from controller.getSetPessoaJuridica import PessoaJuridica
from controller.setGetSetor import Setor
from dao.pesquisarPessoaJuridicaDao import PesquisarPessoaJuridicaDao
from dao.tipoEmpresaDao import TipoEmpresaDao
from telas.frmCadEmpresa import Ui_frmCadastroEmpresa
from dao.empresaDao import EmpresaDao
from controller.getSetEmpresa import Empresas
from telas.frmPesquisarEmpresa import Ui_frmConsultarEmpresa
from telas.frmPesquisarPessoaJuridica import Ui_frmPesquisarPessoaJuridica

class Empresa(QtGui.QDialog):


    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroEmpresa()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.idEmpresa = int()
        self.idTipoEmpresa = int()
        self.contatoAdd = []
        self.contatoRemove = []
        self.emailAdd = []
        self.emailRemove = []
        self.setoresAdd = []
        self.setoresRemove = []
        self.cargoAdd = []
        self.cargoRemove = []

        self.ui.txtContatoEmail.setValidator(self.validator)
        self.ui.txtContatoTelefone.setValidator(self.validator)
        self.ui.txtCadSetoresSetor.setValidator(self.validator)
        self.ui.txtCadCargoCargo.setValidator(self.validator)


        self.ui.cBoxTipoEmpresa.currentIndexChanged.connect(self.pesquisarTipoEmpresa)


        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnPesquisarEmpresa.clicked.connect(self.pesquisarPessoaJuridica)


        self.ui.btnAddTelefone.clicked.connect(self.addContatoTelefone)
        self.ui.btnRemoverTelefone.clicked.connect(self.delContatoTelefone)

        self.ui.btnAddEmail.clicked.connect(self.addContatoEmail)
        self.ui.btnRemoverEmail.clicked.connect(self.delContatoEmail)

        self.ui.btnAddSetor.clicked.connect(self.addContatoSetor)
        self.ui.btnRemoverSetor.clicked.connect(self.delContatoSetor)

        self.ui.btnAddCargos.clicked.connect(self.addContatoCargo)
        self.ui.btnRemoverCargos.clicked.connect(self.delContatoCargo)

        self.ui.txtCodigo.returnPressed.connect(self.setEmpresa)

        self.ui.txtCodigo.textChanged.connect(self.numberCodigo)
        self.ui.txtNumeroTelefone.textChanged.connect(self.numberTelefone)
        self.ui.txtInscricaoMunicipal.textChanged.connect(self.numberInscricaoMunicipal)


    def numberCodigo(self):
        if self.ui.txtCodigo.text().isnumeric() == False:
            self.ui.txtCodigo.backspace()

    def numberTelefone(self):
        if self.ui.txtNumeroTelefone.text().isnumeric() == False:
            self.ui.txtNumeroTelefone.backspace()

    def numberInscricaoMunicipal(self):
        if self.ui.txtInscricaoMunicipal.text().isnumeric() == False:
            self.ui.txtInscricaoMunicipal.backspace()

    def pesquisarTipoEmpresa(self):
        if self.ui.cBoxTipoEmpresa.currentText() != '':
            tipoEmpresa = TipoEmpresaDao()
            self.idTipoEmpresa = tipoEmpresa.idTipoEmpresa(self.ui.cBoxTipoEmpresa.currentText())


    def novo(self):
        self.limparCampos()
        self.ui.grbDadosPessoaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

        self.setTipoEmpresa()

    def cancelar(self):
        self.limparCampos()
        self.deletarContatoTelefone()
        self.deletarContatoEmail()
        self.deletarSetor()
        self.deletarCargo()
        self.desativarCampos()


    def botoesEditar(self):
        self.ui.grbDadosPessoaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.radBtnAtivo.setCheckable(True)
        self.ui.radBtnDesativo.setCheckable(True)
        self.ui.grbAtivo.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)


    def limparCampos(self):
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtRazaoSocial.clear()
        self.ui.txtFantasia.clear()
        self.ui.cBoxTipoEmpresa.clear()
        self.ui.txtInscricaoMunicipal.clear()

        self.ui.txtContatoTelefone.clear()
        self.ui.txtNumeroTelefone.clear()
        self.ui.txtEnderecoEmail.clear()
        self.ui.txtContatoEmail.clear()

        self.ui.txtCadSetoresSetor.clear()
        self.ui.txtCadCargoCargo.clear()

        self.idEmpresa = int()
        self.contatoAdd.clear()
        self.contatoRemove.clear()
        self.emailAdd.clear()
        self.emailRemove.clear()


        self.deletarContatoTelefone()
        self.deletarContatoEmail()
        self.deletarSetor()
        self.deletarCargo()

        self.ui.radBtnAtivo.setCheckable(False)
        self.ui.radBtnDesativo.setCheckable(False)

    def deletarContatoTelefone(self):
        for i in reversed(range(self.ui.tabContatoTelefone.rowCount())):
            self.ui.tabContatoTelefone.removeRow(i)

    def deletarContatoEmail(self):
        for i in reversed(range(self.ui.tabContatoEmail.rowCount())):
            self.ui.tabContatoEmail.removeRow(i)

    def deletarSetor(self):
        for i in reversed(range(self.ui.tabSetores.rowCount())):
            self.ui.tabSetores.removeRow(i)

    def deletarCargo(self):
        for i in reversed(range(self.ui.tabCargos.rowCount())):
            self.ui.tabCargos.removeRow(i)


    def desativarCampos(self):
        self.ui.grbDadosPessoaJuridica.setEnabled(False)
        self.ui.tabWiAdicionais.setEnabled(False)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def ativarCampos(self):
        self.ui.grbDadosPessoaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

    def setTipoEmpresa(self):
        empresa = EmpresaDao()
        lista = empresa.tipoEmpresa()

        for tipo in lista:
            self.ui.cBoxTipoEmpresa.addItem(tipo[0])

    def setEmpresa(self):
        empresa = EmpresaDao()
        em = empresa.pesquisarEmpresaId(self.ui.txtCodigo.text())

        if em == []:
            emp = empresa.pesquisarPessoaJuridica(self.ui.txtCodigo.text())
            if emp == []:
                QMessageBox.warning(QWidget(), 'Mensagem', "Atenção não existe nenhum cadastro neste codigo")
                self.ui.txtCnpj.clear()
                self.ui.txtInscricaoEstadua.clear()
                self.ui.txtRazaoSocial.clear()
                self.ui.txtFantasia.clear()
            else:
                for empres in emp:
                    self.ui.txtCnpj.setText(str(empres[0]))
                    self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                    self.ui.txtRazaoSocial.setText(str(empres[2]))
                    self.ui.txtFantasia.setText(str(empres[3]))
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Atenção já tem um cadastro desta empresa")

    def addContatoTelefone(self):
        if self.ui.txtContatoTelefone.text() != "" and self.ui.txtNumeroTelefone.text() != "":
            if len(self.ui.txtNumeroTelefone.text()) == 10 or len(self.ui.txtNumeroTelefone.text()) == 11:
                __contato = str(self.ui.txtContatoTelefone.text())
                __telefone = str(self.ui.txtNumeroTelefone.text())

                add = [(__contato, __telefone)]
                self.contatoAdd.append([__contato, __telefone])
                self.inserirTabelaTelefone(add)

                self.ui.txtContatoTelefone.clear()
                self.ui.txtNumeroTelefone.clear()

                self.ui.txtContatoTelefone.setFocus()
            elif len(self.ui.txtNumeroTelefone.text()) >11:
                QMessageBox.warning(QWidget(), 'Mensagem', "Atenção contem digitos do telefone a mais")
            else:
                QMessageBox.warning(QWidget(), 'Mensagem', "Atenção esta faltando digitos do telefone")
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def inserirTabelaTelefone(self, dado):

        linha = self.ui.tabContatoTelefone.rowCount()
        for info in dado:
            self.ui.tabContatoTelefone.insertRow(linha)
            __contato = info[0]
            __telefone = info[1]


            self.ui.tabContatoTelefone.setItem(linha, 0, QtGui.QTableWidgetItem(str(__contato)))
            self.ui.tabContatoTelefone.setItem(linha, 1, QtGui.QTableWidgetItem(str(__telefone)))


            linha += 1


    def contatoRemovidoTelefone(self):
        itens = []
        for item in self.ui.tabContatoTelefone.selectedItems():
            itens.append(item.text())
        self.contatoRemove.append(itens)


    def delContatoTelefone(self):
        self.contatoRemovidoTelefone()
        index = self.ui.tabContatoTelefone.currentRow()
        self.ui.tabContatoTelefone.removeRow(index)
        print(index)
        if index >= 0:
            del self.contatoAdd[index]
        else:
            QMessageBox.warning(QWidget(), 'Mensagem',"Impossivel realizar essa ação, por favor selecione um item da lista para excluir")

    def inserirTabelaEmail(self, dado):

        linha = self.ui.tabContatoEmail.rowCount()
        for info in dado:
            self.ui.tabContatoEmail.insertRow(linha)
            __contato = info[0]
            __email = info[1]

            self.ui.tabContatoEmail.setItem(linha, 0, QtGui.QTableWidgetItem(str(__contato)))
            self.ui.tabContatoEmail.setItem(linha, 1, QtGui.QTableWidgetItem(str(__email)))

            linha += 1

    def addContatoEmail(self):
        if self.ui.txtContatoEmail.text() != "" and self.ui.txtEnderecoEmail.text() != "":
                __contato = str(self.ui.txtContatoEmail.text())
                __email = str(self.ui.txtEnderecoEmail.text())

                add = [(__contato, __email)]
                self.emailAdd.append([__contato, __email])
                self.inserirTabelaEmail(add)

                self.ui.txtContatoEmail.clear()
                self.ui.txtEnderecoEmail.clear()

                self.ui.txtContatoEmail.setFocus()
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def contatoRemovidoEmail(self):
        itens = []
        for item in self.ui.tabContatoEmail.selectedItems():
            itens.append(item.text())
        self.emailRemove.append(itens)

    def delContatoEmail(self):
        self.contatoRemovidoEmail()
        index = self.ui.tabContatoEmail.currentRow()
        self.ui.tabContatoEmail.removeRow(index)

        if index >= 0:
            del self.emailAdd[index]
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")

    def inserirTabelaSetor(self, dado):

        linha = self.ui.tabSetores.rowCount()
        for info in dado:
            self.ui.tabSetores.insertRow(linha)
            __setor = info


            self.ui.tabSetores.setItem(linha, 0, QtGui.QTableWidgetItem(str(__setor)))

            linha += 1

    def addContatoSetor(self):
        if self.ui.txtCadSetoresSetor.text() != "" :
                __setor = str(self.ui.txtCadSetoresSetor.text())

                add = [(__setor)]
                self.setoresAdd.append([__setor])
                self.inserirTabelaSetor(add)

                self.ui.txtCadSetoresSetor.clear()

                self.ui.txtCadSetoresSetor.setFocus()
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def contatoRemovidoSetor(self):
        itens = []
        for item in self.ui.tabSetores.selectedItems():
            itens.append(item.text())
        self.setoresRemove.append(itens)

    def delContatoSetor(self):
        self.contatoRemovidoSetor()
        index = self.ui.tabSetores.currentRow()
        self.ui.tabSetores.removeRow(index)

        if index >= 0:
            del self.setoresAdd[index]
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")

    def inserirTabelaCargo(self, dado):

        linha = self.ui.tabCargos.rowCount()
        for info in dado:
            self.ui.tabCargos.insertRow(linha)
            __cargo = info

            self.ui.tabCargos.setItem(linha, 0, QtGui.QTableWidgetItem(str(__cargo)))

            linha += 1

    def addContatoCargo(self):
        if self.ui.txtCadCargoCargo.text() != "":
            __cargo = str(self.ui.txtCadCargoCargo.text())

            add = [(__cargo)]
            self.cargoAdd.append([__cargo])
            self.inserirTabelaCargo(add)

            self.ui.txtCadCargoCargo.clear()

            self.ui.txtCadCargoCargo.setFocus()
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def contatoRemovidoCargo(self):
        itens = []
        for item in self.ui.tabCargos.selectedItems():
            itens.append(item.text())
        self.cargoRemove.append(itens)

    def delContatoCargo(self):
        self.contatoRemovidoCargo()
        index = self.ui.tabCargos.currentRow()
        self.ui.tabCargos.removeRow(index)

        if index >= 0:
            del self.cargoAdd[index]
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")

    def cadastrarTelefone(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.contatoAdd:
            a = self.contatoAdd[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, self.idEmpresa)
            emp.cadastrarTelefone(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarTelefoneEmpresa(id, self.idEmpresa)

            i += 1

    def cadastrarEmail(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idEmpresa)
            emp.cadastrarEmail(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarEmailEmpresa(id, self.idEmpresa)

            i += 1

    def cadastrarSetores(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.setoresAdd:
            a = self.setoresAdd[i]

            setor = a[0]

            __descricao = Setor(None, setor, self.idEmpresa)
            emp.cadastrarSetor(__descricao)

            i += 1

    def cadastrarCargo(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.cargoAdd:
            a = self.cargoAdd[i]

            cargo = a[0]

            __descricao = Cargo(None, cargo, self.idEmpresa)
            emp.cadastrarCargo(__descricao)

            i += 1

    def cadastro(self):
        if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtFantasia.text() != '' and self.ui.txtRazaoSocial.text() != '':
            empresaDao = EmpresaDao()
            empresa = Empresas(None, self.ui.txtCodigo.text(), self.idTipoEmpresa, None, None, self.ui.txtInscricaoMunicipal.text(), None, None, None, None, None, None, None, None, None, None, 1)
            empresaDao.cadastroEmpresa(empresa)
            self.idEmpresa = empresaDao.ultimoRegistro()


            if self.contatoAdd != []:
                self.cadastrarTelefone()

            if self.emailAdd != []:
                self.cadastrarEmail()

            if self.setoresAdd != []:
                self.cadastrarSetores()

            if self.cargoAdd != []:
                self.cadastrarCargo()

            self.cancelar()
        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Preencha os campos obrigatorio")

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialog = QDialog(self)
            self.__pesquisarEmpresa = Ui_frmConsultarEmpresa()
            self.__pesquisarEmpresa.setupUi(self.dialog)

            self.__pesquisarEmpresa.txtPesquisar.setValidator(self.validator)

            self.__pesquisarEmpresa.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisarEmpresa.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisarEmpresa.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        if self.__pesquisarEmpresa.radBtnCodigo.isChecked():
            __codigo = self.__pesquisarEmpresa.txtPesquisar.text()
            __pesDao = EmpresaDao()
            __retorno = __pesDao.pesquisaCodigo(__codigo)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarEmpresa.radBtnFantasia.isChecked():
            __fantasia = self.__pesquisarEmpresa.txtPesquisar.text()
            __pesDao = EmpresaDao()
            __retorno = __pesDao.pesquisaFantasia(__fantasia)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarEmpresa.radBtnRazaoSocial.isChecked():
            __razao = self.__pesquisarEmpresa.txtPesquisar.text()
            __pesDao = EmpresaDao()
            __retorno = __pesDao.pesquisaRazaoSocial(__razao)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarEmpresa.radBtnCnpj.isChecked():
            __cnpj = self.__pesquisarEmpresa.txtPesquisar.text()
            __pesDao = EmpresaDao()
            __retorno = __pesDao.pesquisaCnpj(__cnpj)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarEmpresa.radBtnIncrisaoEstadual.isChecked():
            __insEstadual = self.__pesquisarEmpresa.txtPesquisar.text()
            __pesDao = EmpresaDao()
            __retorno = __pesDao.pesquisaInscEstadual(__insEstadual)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarEmpresa.radBtnIncrisaoMunicipal.isChecked():
            __insMunicipal = self.__pesquisarEmpresa.txtPesquisar.text()
            __pesDao = EmpresaDao()
            __retorno = __pesDao.pesquisaInscMunicipal(__insMunicipal)

            self.setarTabelaPesquisa(__retorno)

        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisa(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarEmpresa.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            fantsia = pesqui[1]
            razao = pesqui[2]
            cnpj = pesqui[3]
            insEstadual = pesqui[4]
            insMunicipal = pesqui[5]
            tipoEmpresa = pesqui[6]
            endereco = pesqui[7]
            numero = pesqui[8]
            complemento = pesqui[9]
            bairro = pesqui[10]
            cidade = pesqui[11]
            estado = pesqui[12]
            cep = pesqui[13]
            if pesqui[14] == 1:
                situacao = 'ATIVA'
            else:
                situacao = 'Desativa'

            # preenchendo o grid de pesquisa
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(fantsia)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(razao)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(insEstadual)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(insMunicipal)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(tipoEmpresa)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(situacao)))


            linha += 1

    def setarCampos(self):
        itens = []

        for item in self.__pesquisarEmpresa.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = str(itens[0])
        fantasia = str(itens[1])
        razao = str(itens[2])
        cnpj = str(itens[3])
        insEstadual = str(itens[4])
        insMunicipal = str(itens[5])
        tipoEmpresa = str(itens[6])
        endereco = str(itens[7])
        numero = str(itens[8])
        complemento = str(itens[9])
        bairro = str(itens[10])
        cidade = str(itens[11])
        estado = str(itens[12])
        cep = str(itens[13])
        if itens[14] == 'ATIVA':
            situacao = True
        else:
            situacao = False
        empresaDao = EmpresaDao()
        idPessoa = empresaDao.pesquisarPessoaJuridicaId(codigo)


        __dados = Empresas(codigo, idPessoa, tipoEmpresa, cnpj, insEstadual, insMunicipal, fantasia, razao, endereco, numero, complemento, bairro, None, cidade, estado, cep, situacao)
        self.botoesEditar()
        self.setCampos(__dados)
        self.pesquisarTelefone(codigo)
        self.pesquisaEmail(codigo)
        self.pesquisaSetor(codigo)
        self.pesquisaCargo(codigo)
        self.dialog.close()

    def setCampos(self, campos):
        self.idEmpresa = campos.getIdEmpresa
        self.ui.txtCodigo.setText(str(campos.getIdPessoaJuridica))
        self.ui.txtCnpj.setText(campos.getCnpj)
        self.ui.txtInscricaoEstadua.setText(campos.getInscricaoEstadual)
        self.ui.txtInscricaoMunicipal.setText(campos.getInscricaoMunicipal)
        self.ui.txtFantasia.setText(campos.getFantasia)
        self.ui.txtRazaoSocial.setText(campos.getRazaoSocial)
        tipo = campos.getTipoEmpresa
        self.ui.cBoxTipoEmpresa.addItem(tipo)
        self.setTipoEmpresaAtualizado(tipo)
        if campos.getSituacao == True:
            self.ui.radBtnAtivo.setChecked(True)
        else:
            self.ui.radBtnDesativo.setChecked(False)

    def setTipoEmpresaAtualizado(self, dados):
        empresa = EmpresaDao()
        lista = empresa.tipoEmpresa()

        for tipo in lista:
            if tipo[0] != dados:

                self.ui.cBoxTipoEmpresa.addItem(tipo[0])

    def pesquisarPessoaJuridica(self):
        self.dialogJuridico = QDialog(self)
        self.__pesquisarJuridica = Ui_frmPesquisarPessoaJuridica()
        self.__pesquisarJuridica.setupUi(self.dialogJuridico)

        self.__pesquisarJuridica.txtPesquisar.setValidator(self.validator)

        self.__pesquisarJuridica.txtPesquisar.returnPressed.connect(self.pesquisarJuridico)

        self.__pesquisarJuridica.btnPesquisar.clicked.connect(self.pesquisarJuridico)

        self.__pesquisarJuridica.tabPesquisar.doubleClicked.connect(self.setarCamposJuridico)

        self.dialogJuridico.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogJuridico.exec_()


    def pesquisarJuridico(self):
        if self.__pesquisarJuridica.radBtnCodigo.isChecked():
            __codigo = self.__pesquisarJuridica.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaCodigo(__codigo)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarJuridica.radBtnRazaoSocial.isChecked():
            __razao = self.__pesquisarJuridica.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaRazaoSocial(__razao)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarJuridica.radBtnFantasia.isChecked():
            __fantasia = self.__pesquisarJuridica.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaFantasia(__fantasia)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarJuridica.radBtnCnpj.isChecked():
            __cnpj = self.__pesquisarJuridica.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaCnpj(__cnpj)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarJuridica.radBtnInsEstadual.isChecked():
            __inscricao = self.__pesquisarJuridica.txtPesquisar.text()
            __pesDao = PesquisarPessoaJuridicaDao()
            __retorno = __pesDao.pesquisaInsEstadual(__inscricao)

            self.setarTabelaPesquisaJuridico(__retorno)

        else:
            QMessageBox.warning(QWidget(), 'Atenção', "Selecione uma das opções de pesquisa")


    def setarTabelaPesquisaJuridico(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarJuridica.tabPesquisar.setRowCount(qtde_registros)

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
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(razao)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscricao)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarJuridica.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(site)))

            linha += 1


    def setarCamposJuridico(self):
        itens = []

        for item in self.__pesquisarJuridica.tabPesquisar.selectedItems():
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
        self.setCamposJuridico(__dados)
        self.ativarCampos()
        self.dialogJuridico.close()

    def pesquisarTelefone(self, campos):
        empresaDao = EmpresaDao()
        id = empresaDao.pesquisaTelefone(campos)
        if id != []:
            self.contatoAdd.append(id)
            self.setTabelaTelefone(id)

    def setTabelaTelefone(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabContatoTelefone.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            contato = pesqui[1]
            telefone = pesqui[2]


            self.ui.tabContatoTelefone.setItem(linha, 0, QtGui.QTableWidgetItem(str(contato)))
            self.ui.tabContatoTelefone.setItem(linha, 1, QtGui.QTableWidgetItem(str(telefone)))


    def setCamposJuridico(self, campos):
        self.ui.txtCodigo.setText(campos.getIdPesJuridica)
        self.ui.txtCnpj.setText(campos.getCnpj)
        self.ui.txtInscricaoEstadua.setText(campos.setInscricao)
        self.ui.txtFantasia.setText(campos.getFantasia)
        self.ui.txtRazaoSocial.setText(campos.getRazao)

    def pesquisaEmail(self, campos):
        empresaDao = EmpresaDao()
        id = empresaDao.pesquisaEmail(campos)
        if id != []:
            self.emailAdd.append(id)
            self.setTabelaEmail(id)

    def setTabelaEmail(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabContatoEmail.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            contato = pesqui[1]
            email = pesqui[2]

            self.ui.tabContatoEmail.setItem(linha, 0, QtGui.QTableWidgetItem(str(contato)))
            self.ui.tabContatoEmail.setItem(linha, 1, QtGui.QTableWidgetItem(str(email)))

    def pesquisaSetor(self, campos):
        empresaDao = EmpresaDao()
        id = empresaDao.pesquisaSetor(campos)

        if id != []:
            self.setoresAdd.append(id)
            self.setTabelaSetores(id)

    def setTabelaSetores(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabSetores.setRowCount(qtde_registros)
        linha = 0
        for pesqui in __retorno:
            setor = pesqui[1]
            self.ui.tabSetores.setItem(linha, 0, QtGui.QTableWidgetItem(str(setor)))
            linha += 1

    def pesquisaCargo(self, campos):
        empresaDao = EmpresaDao()
        id = empresaDao.pesquisaCargo(campos)

        if id != []:
            self.cargoAdd.append(id)
            self.setTabelaCargo(id)

    def setTabelaCargo(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabCargos.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            cargos = pesqui[1]
            self.ui.tabCargos.setItem(linha, 0, QtGui.QTableWidgetItem(str(cargos)))

            linha += 1

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetContatoEmail import ContatoEmail
from controller.getSetContatoTelefone import ContatoTelefone
from controller.getSetFornecedor import Fornecedor
from controller.getSetPessoaFisica import PessoaFisica
from controller.getSetPessoaJuridica import PessoaJuridica
from dao.fornecedorDao import FornecedorDao
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from dao.pesquisarPessoaJuridicaDao import PesquisarPessoaJuridicaDao
from telas.frmCadFornecedor import Ui_frmCadastroFornecedor
from telas.frmPesquisarFornecedor import Ui_frmPesquisarFornecedor
from telas.frmPesquisarPessoaFisicaJuridica import Ui_frmPesquisarPessoaFisicaJuridica


class CadastroFornecedores(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroFornecedor()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.idFornecedor = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.idPessoaJurirdica = int()
        self.editar = False
        self.contatoAdd = []
        self.contatoRemove = []
        self.contatoAtualizar = []
        self.emailAdd = []
        self.emailRemove = []
        self.emailAtualizar = []

        self.ui.txtContatoEmail.setValidator(self.validator)
        self.ui.txtContatoTelefone.setValidator(self.validator)

        self.ui.btnNovo.clicked.connect(self.novo)
        #self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        #self.ui.btnEditar.clicked.connect(self.atualizar)
        self.ui.btnPesquisarEmpresa.clicked.connect(self.pesquisarPessoaFisicaJuridica)


        self.ui.txtCodigo.textChanged.connect(self.numberCodigo)
        self.ui.txtNumeroTelefone.textChanged.connect(self.numberTelefone)
        self.ui.txtObservacao.textChanged.connect(self.textEdite)

        self.ui.radBtnPessoaFisica.clicked.connect(self.botaoNovo)
        self.ui.radBtnPessoaJuridica.clicked.connect(self.botaoNovo)

        self.ui.btnAddTelefone.clicked.connect(self.addContatoTelefone)
        self.ui.btnRemoverTelefone.clicked.connect(self.delContatoTelefone)

        self.ui.btnAddEmail.clicked.connect(self.addContatoEmail)
        self.ui.btnRemoverEmail.clicked.connect(self.delContatoEmail)

        self.ui.txtCodigo.returnPressed.connect(self.setCliente)

        self.ui.txtCodigo.editingFinished.connect(self.setClienteEditFinish)


    def numberCodigo(self):
        if self.ui.txtCodigo.text().isnumeric() == False:
            self.ui.txtCodigo.backspace()

    def numberTelefone(self):
        if self.ui.txtNumeroTelefone.text().isnumeric() == False:
            self.ui.txtNumeroTelefone.backspace()

    def textEdite(self):
        if (len(self.ui.txtObservacao.toPlainText()) > 255):
            self.ui.txtObservacao.textCursor().deletePreviousChar()

    def novo(self):
        self.limparCampos()
        self.ui.grbTipoPessoa.setEnabled(True)
        self.ui.radBtnPessoaFisica.setCheckable(True)
        self.ui.radBtnPessoaJuridica.setCheckable(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

    def botaoNovo(self):
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtRazaoSocial.clear()
        self.ui.txtFantasia.clear()

        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)

        self.deletarContatoTelefone()
        self.deletarContatoEmail()


    def cancelar(self):
        self.limparCampos()
        self.deletarContatoTelefone()
        self.deletarContatoEmail()
        self.desativarCampos()

    def desativarCampos(self):
        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(False)
        self.ui.tabWiAdicionais.setEnabled(False)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def botoesEditar(self):
        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(False)
        self.limparCampos()
        self.ui.grbTipoPessoa.setEnabled(False)
        self.ui.radBtnPessoaFisica.setCheckable(True)
        self.ui.radBtnPessoaJuridica.setCheckable(True)
        self.ui.grbAtivo.setEnabled(True)
        self.ui.radBtnAtivo.setCheckable(True)
        self.ui.radBtnDesativo.setCheckable(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)

    def ativarCampos(self):
        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)


    def limparCampos(self):
        self.idFornecedor = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.idPessoaJurirdica = int()
        self.ui.grbTipoPessoa.setEnabled(True)
        self.ui.radBtnPessoaFisica.setCheckable(False)
        self.ui.radBtnPessoaJuridica.setCheckable(False)
        self.ui.grbTipoPessoa.setEnabled(False)
        self.ui.txtCodigo.setEnabled(True)
        self.ui.btnPesquisarEmpresa.setEnabled(True)
        self.editar = False
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtRazaoSocial.clear()
        self.ui.txtFantasia.clear()

        self.ui.txtObservacao.clear()

        self.ui.txtContatoTelefone.clear()
        self.ui.txtNumeroTelefone.clear()
        self.ui.txtEnderecoEmail.clear()
        self.ui.txtContatoEmail.clear()


        self.contatoAdd.clear()
        self.contatoRemove.clear()
        self.contatoAtualizar.clear()
        self.emailAdd.clear()
        self.emailRemove.clear()
        self.emailAtualizar.clear()

        self.deletarContatoTelefone()
        self.deletarContatoEmail()

        self.ui.radBtnAtivo.setCheckable(False)
        self.ui.radBtnDesativo.setCheckable(False)

    def deletarContatoTelefone(self):
        for i in reversed(range(self.ui.tabContatoTelefone.rowCount())):
            self.ui.tabContatoTelefone.removeRow(i)

    def deletarContatoEmail(self):
        for i in reversed(range(self.ui.tabContatoEmail.rowCount())):
            self.ui.tabContatoEmail.removeRow(i)

    def addContatoTelefone(self):

        if self.ui.txtContatoTelefone.text() != "" and self.ui.txtNumeroTelefone.text() != "":
            if len(self.ui.txtNumeroTelefone.text()) == 10 or len(self.ui.txtNumeroTelefone.text()) == 11:
                __contato = str(self.ui.txtContatoTelefone.text())
                __telefone = str(self.ui.txtNumeroTelefone.text())
                if self.editar == False:
                    add = [(__contato, __telefone)]
                    self.contatoAdd.append([__contato, __telefone])
                    self.inserirTabelaTelefone(add)

                elif self.editar == True:
                    add = [(__contato, __telefone)]
                    self.contatoAtualizar.append([__contato, __telefone])
                    self.inserirTabelaTelefone(add)

                self.ui.txtContatoTelefone.clear()
                self.ui.txtNumeroTelefone.clear()

                self.ui.txtContatoTelefone.setFocus()
            elif len(self.ui.txtNumeroTelefone.text()) >11:
                self.mensagem.warning( 'Mensagem', "Atenção contem digitos do telefone a mais")
            else:
                self.mensagem.warning( 'Mensagem', "Atenção esta faltando digitos do telefone")
        else:
            self.mensagem.warning( 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def inserirTabelaTelefone(self, dado):

        linha = self.ui.tabContatoTelefone.rowCount()
        for info in dado:
            self.ui.tabContatoTelefone.insertRow(linha)
            __contato = info[0]
            __telefone = info[1]


            self.ui.tabContatoTelefone.setItem(linha, 0, QtGui.QTableWidgetItem(str(__contato)))
            self.ui.tabContatoTelefone.setItem(linha, 1, QtGui.QTableWidgetItem(str(__telefone)))


            linha += 1

    def cellClickTelefone(self):
        index = self.ui.tabContatoTelefone.currentRow()
        list=[]
        columcount = self.ui.tabContatoTelefone.columnCount()
        row = self.ui.tabContatoTelefone.currentItem().row()
        for x in range(0, columcount, 1):
            cell =self.ui.tabContatoTelefone.item(row, x).text()
            list.append(cell)

        if list in self.contatoAtualizar:
            self.contatoAtualizar.remove(list)
            self.ui.tabContatoTelefone.removeRow(index)
        else:
            self.ui.tabContatoTelefone.removeRow(index)
            if index >= 0:
                self.contatoRemove.append(self.contatoAdd[index])
                del self.contatoAdd[index]
            else:
                MensagemBox().warning( 'Mensagem',"Impossivel realizar essa ação, por favor selecione um item da lista para excluir")

    def delContatoTelefone(self):
        index = self.ui.tabContatoTelefone.currentRow()

        if self.editar == False:
            self.ui.tabContatoTelefone.removeRow(index)
            if index >= 0:
                del self.contatoAdd[index]
            else:
                MensagemBox().warning('Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickTelefone()

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
                if self.editar == False:
                    add = [(__contato, __email)]
                    self.emailAdd.append([__contato, __email])
                    self.inserirTabelaEmail(add)

                elif self.editar == True:
                    add = [(__contato, __email)]
                    self.emailAtualizar.append([__contato, __email])
                    self.inserirTabelaEmail(add)

                self.ui.txtContatoEmail.clear()
                self.ui.txtEnderecoEmail.clear()

                self.ui.txtContatoEmail.setFocus()
        else:
            self.mensagem.warning( 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def cellClickEmail(self):
        index = self.ui.tabContatoEmail.currentRow()
        list = []
        columcount = self.ui.tabContatoEmail.columnCount()
        row = self.ui.tabContatoEmail.currentItem().row()
        for x in range(0, columcount, 1):
            cell = self.ui.tabContatoEmail.item(row, x).text()
            list.append(cell)

        if list in self.emailAtualizar:
            self.emailAtualizar.remove(list)
            self.ui.tabContatoEmail.removeRow(index)
        else:
            self.ui.tabContatoEmail.removeRow(index)
            if index >= 0:
                self.emailRemove.append(self.emailAdd[index])
                del self.emailAdd[index]
            else:
                MensagemBox().warning('Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")


    def delContatoEmail(self):
        index = self.ui.tabContatoEmail.currentRow()

        if self.editar == False:
            self.ui.tabContatoEmail.removeRow(index)
            if index >= 0:
                del self.emailAdd[index]
            else:
                MensagemBox().warning('Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickEmail()

    def setCliente(self):
        cliente = FornecedorDao()
        if self.ui.radBtnPessoaFisica.isChecked():
            cli = cliente.pesquisarFornecedorIdFisico(self.ui.txtCodigo.text())

            if cli == []:
                clien = cliente.pesquisarPessoaFisica(self.ui.txtCodigo.text())
                if clien == []:
                    self.mensagem.warning('Mensagem', "Atenção não existe nenhum cadastro neste codigo")
                    self.ui.txtCnpj.clear()
                    self.ui.txtInscricaoEstadua.clear()
                    self.ui.txtRazaoSocial.clear()
                    self.ui.txtFantasia.clear()
                else:
                    for empres in clien:
                        self.ui.txtCnpj.setText(str(empres[0]))
                        self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                        self.ui.txtRazaoSocial.setText(str(empres[2]))
                        self.ui.txtFantasia.setText(str(empres[3]))
            else:
                self.mensagem.warning( 'Mensagem', "Atenção já tem um cadastro deste cliente")

        elif self.ui.radBtnPessoaJuridica.isChecked():
            cli = cliente.pesquisarFornecedorIdJuridico(self.ui.txtCodigo.text())

            if cli == []:
                clien = cliente.pesquisarPessoaJuridica(self.ui.txtCodigo.text())
                if clien == []:
                    self.mensagem.warning('Mensagem', "Atenção não existe nenhum cadastro neste codigo")
                    self.ui.txtCnpj.clear()
                    self.ui.txtInscricaoEstadua.clear()
                    self.ui.txtRazaoSocial.clear()
                    self.ui.txtFantasia.clear()
                else:
                    for empres in clien:
                        self.ui.txtCnpj.setText(str(empres[0]))
                        self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                        self.ui.txtRazaoSocial.setText(str(empres[2]))
                        self.ui.txtFantasia.setText(str(empres[3]))
            else:
                self.mensagem.warning( 'Mensagem', "Atenção já tem um cadastro deste cliente")

    def setClienteEditFinish(self):
        cliente = FornecedorDao()
        if self.ui.radBtnPessoaFisica.isChecked():
            cli = cliente.pesquisarFornecedorIdFisico(self.ui.txtCodigo.text())

            if cli == []:
                clien = cliente.pesquisarPessoaFisica(self.ui.txtCodigo.text())
                if clien == []:
                    self.ui.txtCnpj.clear()
                    self.ui.txtInscricaoEstadua.clear()
                    self.ui.txtRazaoSocial.clear()
                    self.ui.txtFantasia.clear()
                else:
                    for empres in clien:
                        self.ui.txtCnpj.setText(str(empres[0]))
                        self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                        self.ui.txtRazaoSocial.setText(str(empres[2]))
                        self.ui.txtFantasia.setText(str(empres[3]))

        elif self.ui.radBtnPessoaJuridica.isChecked():
            cli = cliente.pesquisarFornecedorIdJuridico(self.ui.txtCodigo.text())

            if cli == []:
                clien = cliente.pesquisarPessoaJuridica(self.ui.txtCodigo.text())
                if clien == []:
                    self.ui.txtCnpj.clear()
                    self.ui.txtInscricaoEstadua.clear()
                    self.ui.txtRazaoSocial.clear()
                    self.ui.txtFantasia.clear()
                else:
                    for empres in clien:
                        self.ui.txtCnpj.setText(str(empres[0]))
                        self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                        self.ui.txtRazaoSocial.setText(str(empres[2]))
                        self.ui.txtFantasia.setText(str(empres[3]))

    def pesquisarPessoaFisicaJuridica(self):
        self.dialogFisicoJuridico = QDialog(self)
        self.__pesquisarFisicaJuridica = Ui_frmPesquisarPessoaFisicaJuridica()
        self.__pesquisarFisicaJuridica.setupUi(self.dialogFisicoJuridico)
        self.colunasTabela()
        self.__pesquisarFisicaJuridica.txtPesquisar.setValidator(self.validator)

        self.__pesquisarFisicaJuridica.txtPesquisar.returnPressed.connect(self.pesquisarFisicoJuridico)

        self.__pesquisarFisicaJuridica.btnPesquisar.clicked.connect(self.pesquisarFisicoJuridico)

        self.__pesquisarFisicaJuridica.tabPesquisar.doubleClicked.connect(self.setarCamposFisicoJuridico)

        self.dialogFisicoJuridico.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogFisicoJuridico.exec_()

    def colunasTabela(self):
        if self.ui.radBtnPessoaFisica.isChecked():
            self.__pesquisarFisicaJuridica.tabPesquisar.setColumnCount(18)
            self.__pesquisarFisicaJuridica.tabPesquisar.setRowCount(0)
            self.__pesquisarFisicaJuridica.tabPesquisar.setHorizontalHeaderLabels(["Cod.", "Nome", "Apelido", "CPF", "RG", "Expeditor", "UF", "Aniversario", "Sexo", "Mãe", "Pai", "Endereço", "Número", "Complemento", "Bairro", "Cidade", "Estado", "CEP"])
        elif self.ui.radBtnPessoaJuridica.isChecked():
            self.__pesquisarFisicaJuridica.tabPesquisar.setColumnCount(12)
            self.__pesquisarFisicaJuridica.tabPesquisar.setRowCount(0)
            self.__pesquisarFisicaJuridica.tabPesquisar.setHorizontalHeaderLabels(["Cod.", "Razão Social", "Fantasia", "CNPJ", "Ins. Estadual", "Endereço", "Número", "Complemento", "Bairro", "Cidade" , "Estado", "CEP"])


    def pesquisarFisicoJuridico(self):
        if self.__pesquisarFisicaJuridica.radBtnCodigo.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __codigo = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaCodigo(__codigo)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __codigo = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaCodigo(__codigo)
                self.setarTabelaPesquisaJuridico(__retorno)
        elif self.__pesquisarFisicaJuridica.radBtnRazaoSocial.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __razao = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaNome(__razao)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __razao = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaRazaoSocial(__razao)
                self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisicaJuridica.radBtnFantasia.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __fantasia = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaApelido(__fantasia)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __fantasia = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaFantasia(__fantasia)
                self.setarTabelaPesquisaJuridico(__retorno)
        elif self.__pesquisarFisicaJuridica.radBtnCnpj.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __cnpj = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaCpf(__cnpj)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __cnpj = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaCnpj(__cnpj)
                self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisicaJuridica.radBtnInsEstadual.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __inscricao = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaRg(__inscricao)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __inscricao = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaInsEstadual(__inscricao)
                self.setarTabelaPesquisaJuridico(__retorno)

        else:
            self.mensagem.warning( 'Atenção', "Selecione uma das opções de pesquisa")


    def setarTabelaPesquisaFisica(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarFisicaJuridica.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            apelido = pesqui[2]
            cpf = pesqui[3]
            rg = pesqui[4]
            expeditor = pesqui[5]
            uf = pesqui[6]
            aniversario = pesqui[7]
            sexo = pesqui[8]
            mae = pesqui[9]
            pai = pesqui[10]
            endereco = pesqui[11]
            numero = pesqui[12]
            complemento = pesqui[13]
            bairro = pesqui[14]
            cidade = pesqui[15]
            estado = pesqui[16]
            cep = pesqui[17]


            # preenchendo o grid de pesquisa
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(apelido)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(aniversario)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(sexo)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(mae)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(pai)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cep)))

            linha += 1

    def setarTabelaPesquisaJuridico(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarFisicaJuridica.tabPesquisar.setRowCount(qtde_registros)

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


            # preenchendo o grid de pesquisa
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(razao)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscricao)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cep)))

            linha += 1



    def setarCamposFisicoJuridico(self):
        if self.ui.radBtnPessoaFisica.isChecked():
            itens = []

            for item in self.__pesquisarFisicaJuridica.tabPesquisar.selectedItems():
                itens.append(item.text())

            codigo = str(itens[0])
            nome = str(itens[1])
            apelido = str(itens[2])
            cpf = str(itens[3])
            rg = str(itens[4])
            expeditor = str(itens[5])
            uf = str(itens[6])
            aniversario = str(itens[7])
            sexo = str(itens[8])
            endereco = str(itens[9])
            numero = str(itens[10])
            complemento = str(itens[11])
            bairro = str(itens[12])
            cidade = str(itens[13])
            estado = str(itens[14])
            cep = str(itens[15])

            __dados = PessoaFisica(None, codigo, None, nome, apelido, cpf, rg, expeditor, uf, aniversario, sexo, endereco, numero, complemento, bairro, None, None, None, cidade, estado, cep)
            self.setCamposFisicoJuridico(__dados)
            self.dialogFisicoJuridico.close()

        elif self.ui.radBtnPessoaJuridica.isChecked():
            itens = []

            for item in self.__pesquisarFisicaJuridica.tabPesquisar.selectedItems():
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

            __dados = PessoaJuridica(None, codigo, None, razao, fantasia, cnpj, inscricao, endereco, numero, complemento, bairro, None, cidade, estado, cep, None)
            self.setCamposFisicoJuridico(__dados)
            self.dialogFisicoJuridico.close()

    def setCamposFisicoJuridico(self, campos):
        if self.ui.radBtnPessoaFisica.isChecked():
            self.ui.txtCodigo.setText(campos.getIdPesFisica)
            self.ui.txtCnpj.setText(campos.getCpf)
            self.ui.txtInscricaoEstadua.setText(campos.setRg)
            self.ui.txtFantasia.setText(campos.getApelido)
            self.ui.txtRazaoSocial.setText(campos.getNome)
        elif self.ui.radBtnPessoaJuridica.isChecked():
            self.ui.txtCodigo.setText(campos.getIdPesJuridica)
            self.ui.txtCnpj.setText(campos.getCnpj)
            self.ui.txtInscricaoEstadua.setText(campos.setInscricao)
            self.ui.txtFantasia.setText(campos.getFantasia)
            self.ui.txtRazaoSocial.setText(campos.getRazao)

    def cadastrarTelefone(self):
        cli = FornecedorDao()
        i = 0
        for lista in self.contatoAdd:
            a = self.contatoAdd[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, self.idCliente)
            cli.cadastrarTelefone(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarTelefoneCliente(id, self.idCliente)

            i += 1

    def cadastrarEmail(self):
        cli = FornecedorDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idCliente)
            cli.cadastrarEmail(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarEmailCliente(id, self.idCliente)

            i += 1

    def cadastro(self):
        if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtFantasia.text() != '' and self.ui.txtRazaoSocial.text() != '':
            fornecedorDao = FornecedorDao()
            if self.ui.radBtnPessoaFisica.isChecked():
                idPessoa = fornecedorDao.pesquisarPessoaFis(self.ui.txtCodigo.text())
                fornecedor = Fornecedor(None, idPessoa, self.ui.txtCodigo.text(), None, None, None, None, None, self.ui.txtObservacao.toPlainText(), 1, None)
                fornecedorDao.cadastrarFornecedorFisico(fornecedor)
                self.idFornecedor = fornecedorDao.ultimoRegistro()


                if self.contatoAdd != []:
                    self.cadastrarTelefone()

                if self.emailAdd != []:
                    self.cadastrarEmail()

                self.cancelar()

            elif self.ui.radBtnPessoaJuridica.isChecked():
                idPessoa = fornecedorDao.pesquisarPessoaJur(self.ui.txtCodigo.text())
                fornecedor = Fornecedor(None, idPessoa, None, self.ui.txtCodigo.text(), None, None, None, None, self.ui.txtObservacao.toPlainText(), 1, None)
                fornecedorDao.cadastrarFornecedorJuridica(fornecedor)
                self.idFornecedor = fornecedorDao.ultimoRegistro()

                if self.contatoAdd != []:
                    self.cadastrarTelefone()

                if self.emailAdd != []:
                    self.cadastrarEmail()

                self.cancelar()

        else:
            self.mensagem.warning( 'Atenção', "Preencha os campos obrigatorio")

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialog = QDialog(self)
            self.__pesquisarFornecedor = Ui_frmPesquisarFornecedor()
            self.__pesquisarFornecedor.setupUi(self.dialog)

            self.__pesquisarFornecedor.txtPesquisar.setValidator(self.validator)

            self.__pesquisarFornecedor.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisarFornecedor.btnPesquisar.clicked.connect(self.pesquisar)

            #self.__pesquisarFornecedor.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        __pesDao = FornecedorDao()
        if self.__pesquisarFornecedor.radBtnCodigo.isChecked():
            __codigo = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaCodigoFisica(__codigo)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnRazaoSocial.isChecked():
            __razao = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisarNomeFisica(__razao)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnFantasia.isChecked():
            __fantasia = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaApelidoFisica(__fantasia)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnCnpj.isChecked():
            __cnpj = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaCpfFisica(__cnpj)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnInsEstadual.isChecked():
            __inscricao = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaRgFisica(__inscricao)
            self.setarTabelaPesquisaEditar(__retorno)

        else:
            self.mensagem.warning('Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaEditar(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarFornecedor.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            tipo = pesqui[1]
            nome = pesqui[2]
            apelido = pesqui[3]
            cpf = pesqui[4]
            rg = pesqui[5]
            expeditor = pesqui[6]
            uf = pesqui[7]
            aniversario = pesqui[8]
            endereco = pesqui[9]
            numero = pesqui[10]
            complemento = pesqui[11]
            bairro = pesqui[12]
            cidade = pesqui[13]
            estado = pesqui[14]
            cep = pesqui[15]
            site = pesqui[16]
            obs = pesqui[17]
            if pesqui[18] == 1:
                situacao = "Ativo"
            else:
                situacao = "Inativo"


            # preenchendo o grid de pesquisa
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipo)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(apelido)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(aniversario)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(site)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(obs)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(situacao)))

            linha += 1

    def setarCampos(self):
        clienteDao = FornecedorDao()
        itens = []

        for item in self.__pesquisarFornecedor.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = str(itens[0])
        tipo = str(itens[1])
        razao = str(itens[2])
        fantasia = str(itens[3])
        cnpj = str(itens[4])
        insEstadual = str(itens[5])
        expeditor = str(itens[6])
        uf = str(itens[7])
        aniversario = str(itens[8])
        endereco = str(itens[9])
        numero = str(itens[10])
        complemento = str(itens[11])
        bairro = str(itens[12])
        cidade = str(itens[13])
        estado = str(itens[14])
        cep = str(itens[15])
        site = str(itens[16])
        obs = str(itens[17])
        if itens[18] == 'Ativo':
            situacao = True
        else:
            situacao = False

        idPessoa = clienteDao.pesquisarPessoaCodigo(codigo)
        idPessoaFisico = clienteDao.pesquisarPessoaFisicaId(idPessoa)
        idPessoaJuridica = clienteDao.pesquisarPessoaJuridicaId(idPessoa)

        __dados = Fornecedor(codigo, idPessoa, idPessoaFisico, idPessoaJuridica, cnpj, insEstadual, fantasia, razao, obs, situacao, tipo)
        self.botoesEditar()
        self.setCampos(__dados)
        #self.pesquisarTelefone(codigo)
        #self.pesquisaEmail(codigo)
        self.dialog.close()

    def setCampos(self, campos):
        self.ui.txtCodigo.setEnabled(False)
        self.ui.btnPesquisarEmpresa.setEnabled(False)

        if campos.getTipo == "PESSOA FÍSICA":
            self.ui.radBtnPessoaFisica.setChecked(True)
            self.idPessoaFisica = campos.getIdPessoaFisica
        elif campos.getTipo == "PESSOA JURÍDICA":
            self.idPessoaJurirdica = campos.getIdPessoaJuridica
            self.ui.radBtnPessoaJuridica.setChecked(True)

        self.idCliente= int(campos.getIdCliente)
        self.idPessoa = int(campos.getIdPessoa)
        self.ui.txtCodigo.setText(str(campos.getIdPessoa))
        self.ui.txtCnpj.setText(campos.getCnpj)
        self.ui.txtInscricaoEstadua.setText(campos.getInscricaoEstadual)
        self.ui.txtFantasia.setText(campos.getFantasia)
        self.ui.txtRazaoSocial.setText(campos.getRazaoSocial)

        if campos.getSituacao == True:
            self.ui.radBtnAtivo.setChecked(True)
        else:
            self.ui.radBtnDesativo.setChecked(True)

        self.ui.txtObservacao.setText(str(campos.getObservacao))
        self.editar = True

"""
        self.ui.txtFantasiaEmpresa.returnPressed.connect(self.focusCnpjFornecedor)
        self.ui.txtCnpjFornecedor.returnPressed.connect(self.focusInscricaoEstadualFornecedor)
        self.ui.txtInscricaoEstadualFornecedor.returnPressed.connect(self.focustxtFantasiaFornecedor)
        self.ui.txtFantasiaFornecedor.returnPressed.connect(self.focusRazaoSocialFornecedor)
        self.ui.txtRazaoSocialFornecedor.returnPressed.connect(self.focusEnderecoFornecedor)
        self.ui.txtEnderecoFornecedor.returnPressed.connect(self.focustNumeroFornecedor)
        self.ui.txtNumeroFornecedor.returnPressed.connect(self.focusComplementoFornecedor)
        self.ui.txtComplementoFornecedor.returnPressed.connect(self.focusBairroFornecedor)
        self.ui.txtBairroFornecedor.returnPressed.connect(self.focusCepFornecedor)
        self.ui.txtCepFornecedor.returnPressed.connect(self.focusTelefoneFornecedor)
        self.ui.txtTelefoneFornecedor.returnPressed.connect(self.focusSiteFornecedor)
        self.ui.txtSiteFornecedor.returnPressed.connect(self.focusEmailFornecedor)

        self.ui.txtPesquisa.returnPressed.connect(self.pesquisar)

        self.ui.txtFantasiaEmpresa.editingFinished.connect(self.pesquisarEmpresa)
        self.ui.txtCepFornecedor.editingFinished.connect(self.pesquisarCidade)
        self.ui.txtCnpjFornecedor.editingFinished.connect(self.validacaoCnpj)

        self.ui.btnNovo.clicked.connect(self.botaoNovoCad)
        self.ui.btnSalvar.clicked.connect(self.cadastroFornecedor)
        self.ui.btnEditar.clicked.connect(self.atualizarFornecedor)
        self.ui.btnCancelar.clicked.connect(self.cancelarCadastro)
        self.ui.btnDeletar.clicked.connect(self.deletarEmpresa)

        self.ui.tbPesquisa.doubleClicked.connect(self.tablePesquisa)

        self.ui.txtFantasiaFornecedor.textChanged.connect(self.upperFantasia)
        self.ui.txtRazaoSocialFornecedor.textChanged.connect(self.upperRazao)
        self.ui.txtEnderecoFornecedor.textChanged.connect(self.upperEndereco)
        self.ui.txtNumeroFornecedor.textChanged.connect(self.upperNumero)
        self.ui.txtComplementoFornecedor.textChanged.connect(self.upperComplemento)
        self.ui.txtBairroFornecedor.textChanged.connect(self.upperBairro)

        self.ui.txtCepFornecedor.cursorPositionChanged.connect(self.positionCursorCep)
        self.ui.txtTelefoneFornecedor.cursorPositionChanged.connect(self.positionCursorTelefone)
        self.ui.txtCnpjFornecedor.cursorPositionChanged.connect(self.positionCursorCnpj)

    def upperFantasia(self):
        self.ui.txtFantasiaFornecedor.setText(self.ui.txtFantasiaFornecedor.text().upper())

    def upperRazao(self):
        self.ui.txtRazaoSocialFornecedor.setText(self.ui.txtRazaoSocialFornecedor.text().upper())

    def upperEndereco(self):
        self.ui.txtEnderecoFornecedor.setText(self.ui.txtEnderecoFornecedor.text().upper())

    def upperNumero(self):
        self.ui.txtNumeroFornecedor.setText(self.ui.txtNumeroFornecedor.text().upper())

    def upperComplemento(self):
        self.ui.txtComplementoFornecedor.setText(self.ui.txtComplementoFornecedor.text().upper())

    def upperBairro(self):
        self.ui.txtBairroFornecedor.setText(self.ui.txtBairroFornecedor.text().upper())

    def positionCursorCnpj(self):
        texto = self.removerCaracter(self.ui.txtCnpjFornecedor.text())

        if len(texto) == 0:
            self.ui.txtCnpjFornecedor.setCursorPosition(0)
        elif len(texto) <= 1:
            b = len(texto)
            self.ui.txtCnpjFornecedor.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) <5:
            b = len(texto)+1
            self.ui.txtCnpjFornecedor.setCursorPosition(b)
        elif len(texto) >= 5 and len(texto) <8:
            b = len(texto)+2
            self.ui.txtCnpjFornecedor.setCursorPosition(b)
        elif len(texto) >= 8 and len(texto) <12:
            b = len(texto)+3
            self.ui.txtCnpjFornecedor.setCursorPosition(b)
        elif len(texto) >= 12 :
            b = len(texto)+4
            self.ui.txtCnpjFornecedor.setCursorPosition(b)


    def positionCursorCep(self):
        texto = self.removerCaracter(self.ui.txtCepFornecedor.text())
        if len(texto) == 0:
            self.ui.txtCepFornecedor.setCursorPosition(0)
        elif len(texto) <= 4:
            b = len(texto)
            self.ui.txtCepFornecedor.setCursorPosition(b)
        elif len(texto) >= 5 and len(texto) <9:
            b = len(texto)+1
            self.ui.txtCepFornecedor.setCursorPosition(b)


    def positionCursorTelefone(self):
        texto = self.removerCaracter(self.ui.txtTelefoneFornecedor.text())
        if len(texto) == 0:
            self.ui.txtTelefoneFornecedor.setCursorPosition(1)
        elif len(texto) <= 1:
            b = len(texto)+1
            self.ui.txtTelefoneFornecedor.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) <7:
            b = len(texto)+2
            self.ui.txtTelefoneFornecedor.setCursorPosition(b)
        elif len(texto) >= 7 and len(texto) <12:
            b = len(texto)+3
            self.ui.txtTelefoneFornecedor.setCursorPosition(b)

    def focusCnpjFornecedor(self):
        self.ui.txtCnpjFornecedor.setFocus()

    def focusInscricaoEstadualFornecedor(self):
        self.ui.txtInscricaoEstadualFornecedor.setFocus()

    def focustxtFantasiaFornecedor(self):
        self.ui.txtFantasiaFornecedor.setFocus()

    def focusRazaoSocialFornecedor(self):
        self.ui.txtRazaoSocialFornecedor.setFocus()

    def focusEnderecoFornecedor(self):
        self.ui.txtEnderecoFornecedor.setFocus()

    def focustNumeroFornecedor(self):
        self.ui.txtNumeroFornecedor.setFocus()

    def focusComplementoFornecedor(self):
        self.ui.txtComplementoFornecedor.setFocus()

    def focusBairroFornecedor(self):
        self.ui.txtBairroFornecedor.setFocus()

    def focusCepFornecedor(self):
        self.ui.txtCepFornecedor.setFocus()

    def focusTelefoneFornecedor(self):
        self.ui.txtTelefoneFornecedor.setFocus()

    def focusSiteFornecedor(self):
        self.ui.txtSiteFornecedor.setFocus()

    def focusEmailFornecedor(self):
        self.ui.txtEmailFornecedor.setFocus()

    def focusBotaoSalvar(self):
        self.ui.btnSalvar.setFocus()

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
        _cep = self.removerCaracter(self.ui.txtCepFornecedor.text())
        if len(_cep) < 8:
            self.ui.txtCidadesFornecedor.clear()
            self.ui.txtEstadosFornecedor.clear()
        else:
            cidades = CidadesEstadosDao()
            cid = cidades.cidade(_cep)

            for cidade in cid:
                self.ui.txtCidadesFornecedor.setText(cidade[0])
                self.ui.txtEstadosFornecedor.setText(cidade[1])
            if cid == []:
                self.ui.txtCidadesFornecedor.clear()
                self.ui.txtEstadosFornecedor.clear()

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
        _cnpj = self.removerCaracter(self.ui.txtCnpjFornecedor.text())
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
        self.ui.grbDadosFornecedor.setEnabled(True)

        self.ui.txtFantasiaEmpresa.setFocus()

    def botaoCancelar(self):
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

        self.ui.btnPesquisar.setEnabled(False)
        self.ui.txtFantasiaEmpresa.setEnabled(False)
        self.ui.grbDadosFornecedor.setEnabled(False)

    def limparCampos(self):
        self.ui.txtIdEmpresa.clear()
        self.ui.txtFantasiaEmpresa.clear()
        self.ui.txtRazaoSocialEmpresa.clear()
        self.ui.txtCnpjEmpresa.clear()
        self.ui.txtInscricaoEstaduaEmpresa.clear()

        self.ui.txtIdFornecedor.clear()
        self.ui.txtCnpjFornecedor.clear()
        self.ui.txtInscricaoEstadualFornecedor.clear()
        self.ui.txtFantasiaFornecedor.clear()
        self.ui.txtRazaoSocialFornecedor.clear()
        self.ui.txtEnderecoFornecedor.clear()
        self.ui.txtNumeroFornecedor.clear()
        self.ui.txtComplementoFornecedor.clear()
        self.ui.txtBairroFornecedor.clear()
        self.ui.txtTelefoneFornecedor.clear()
        self.ui.txtSiteFornecedor.clear()
        self.ui.txtEmailFornecedor.clear()
        self.ui.txtCepFornecedor.clear()
        self.ui.txtCidadesFornecedor.clear()
        self.ui.txtEstadosFornecedor.clear()

    def cadastroFornecedor(self):

        if self.ui.txtIdEmpresa.text() != "" and self.ui.txtFantasiaEmpresa.text() != "" and self.ui.txtRazaoSocialEmpresa.text() != "" and self.ui.txtInscricaoEstadualFornecedor.text() != "" and self.ui.txtFantasiaFornecedor.text() != "" and self.ui.txtRazaoSocialFornecedor.text() != "" and self.ui.txtEnderecoFornecedor.text() != "" and self.ui.txtNumeroFornecedor.text() != "" and self.ui.txtBairroFornecedor.text() != "" and self.ui.txtCidadesFornecedor.text() != "" and self.ui.txtEstadosFornecedor.text() != "":
            _cidade = CidadesEstadosDao()

            idEmpresa = self.ui.txtIdEmpresa.text()
            fanEmp = self.ui.txtFantasiaEmpresa.text()
            razaoEmp = self.ui.txtRazaoSocialEmpresa.text()
            cnpjEmp = self.ui.txtCnpjEmpresa.text()

            cnpjFor = self.removerCaracter(self.ui.txtCnpjFornecedor.text())
            inscFor = self.ui.txtInscricaoEstadualFornecedor.text()
            fantasia = self.ui.txtFantasiaFornecedor.text()
            razaoFor = self.ui.txtRazaoSocialFornecedor.text()
            endereco = self.ui.txtEnderecoFornecedor.text()
            numero = self.ui.txtNumeroFornecedor.text()
            complemeto = self.ui.txtComplementoFornecedor.text()
            bairro = self.ui.txtBairroFornecedor.text()
            telefone = self.removerCaracter(self.ui.txtTelefoneFornecedor.text())
            site = self.ui.txtSiteFornecedor.text()
            email = self.ui.txtEmailFornecedor.text()

            _cep = self.removerCaracter(self.ui.txtCepFornecedor.text())
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self.ui.txtCidadesFornecedor.text(), self.ui.txtEstadosFornecedor.text())
            else:
                return False
            __fornecedor = Fornecedor(None, cnpjFor, inscFor, fantasia, razaoFor, endereco, numero, complemeto, bairro, telefone, site, email, _cida, idEmpresa)
            __forDao = FornecedorDao()
            __dao = __forDao.cadastrarFornecedor(__fornecedor)
            if __dao != False:
                self.limparCampos()
                self.botaoCancelar()

        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")

    def atualizarFornecedor(self):

        if self.ui.txtIdEmpresa.text() != "" and self.ui.txtFantasiaEmpresa.text() != "" and self.ui.txtRazaoSocialEmpresa.text() != "" and self.ui.txtCnpjEmpresa.text() != "" and self.ui.txtCnpjFornecedor.text() != "" and self.ui.txtInscricaoEstadualFornecedor.text() != "" and self.ui.txtFantasiaFornecedor.text() != "" and self.ui.txtRazaoSocialFornecedor.text() != "" and self.ui.txtEnderecoFornecedor.text() != "" and self.ui.txtNumeroFornecedor.text() != "" and self.ui.txtBairroFornecedor.text() != "" and self.ui.txtTelefoneFornecedor.text() != "" and self.ui.txtCidadesFornecedor.text() != "" and self.ui.txtEstadosFornecedor.text() != "":
            _cidade = CidadesEstadosDao()

            idEmpresa = self.ui.txtIdEmpresa.text()
            fanEmp = self.ui.txtFantasiaEmpresa.text()
            razaoEmp = self.ui.txtRazaoSocialEmpresa.text()
            cnpjEmp = self.ui.txtCnpjEmpresa.text()

            idfor = self.ui.txtIdFornecedor.text()
            cnpjFor = self.removerCaracter(self.ui.txtCnpjFornecedor.text())
            inscFor = self.ui.txtInscricaoEstadualFornecedor.text()
            fantasia = self.ui.txtFantasiaFornecedor.text()
            razaoFor = self.ui.txtRazaoSocialFornecedor.text()
            endereco = self.ui.txtEnderecoFornecedor.text()
            numero = self.ui.txtNumeroFornecedor.text()
            complemeto = self.ui.txtComplementoFornecedor.text()
            bairro = self.ui.txtBairroFornecedor.text()
            telefone = self.removerCaracter(self.ui.txtTelefoneFornecedor.text())
            site = self.ui.txtSiteFornecedor.text()
            email = self.ui.txtEmailFornecedor.text()

            _cep = self.removerCaracter(self.ui.txtCepFornecedor.text())
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self.ui.txtCidadesFornecedor.text(), self.ui.txtEstadosFornecedor.text())
            else:
                return False
            __fornecedor = Fornecedor(idfor, cnpjFor, inscFor, fantasia, razaoFor, endereco, numero, complemeto, bairro, telefone, site, email, _cida, idEmpresa)
            __forDao = FornecedorDao()
            __dao = __forDao.atualizarFornecedor(__fornecedor)
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

        result = QMessageBox.question(QWidget(), 'Menssagem', "Tem certeza que deseja excluir essa empresa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            __forDao = FornecedorDao()
            __dao = __forDao.deletarFornecedor(self.ui.txtIdFornecedor.text())
            if __dao != False:
                self.limparCampos()
                self.botaoCancelar()

    def pesquisar(self):
        __forDao = FornecedorDao()
        if self.ui.radBtnCodigo.isChecked():
            _pesquisarCod = __forDao.pesquisaCodigo(self.ui.txtPesquisa.text())

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
            _pesquisarFantasia = __forDao.pesquisaFantasia(str(self.ui.txtPesquisa.text()))

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
            _pesquisarRazaoSocial = __forDao.pesquisaRazaoSocial(str(self.ui.txtPesquisa.text()))

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
            _pesquisarCnpj = __forDao.pesquisaCnpj(self.ui.txtPesquisa.text())

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
            _pesquisarInsEstadual = __forDao.pesquisaInscEstadual(self.ui.txtPesquisa.text())

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
        self.ui.grbDadosFornecedor.setEnabled(True)

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
            self.ui.txtIdFornecedor.setText(str(itens[0]))
            self.ui.txtFantasiaFornecedor.setText(str(itens[1]))
            self.ui.txtRazaoSocialFornecedor.setText(str(itens[2]))
            self.ui.txtCnpjFornecedor.setText(str(itens[3]))
            self.ui.txtInscricaoEstadualFornecedor.setText(str(itens[4]))
            self.ui.txtEnderecoFornecedor.setText(str(itens[5]))
            self.ui.txtNumeroFornecedor.setText(str(itens[6]))
            self.ui.txtComplementoFornecedor.setText(str(itens[7]))
            self.ui.txtBairroFornecedor.setText(str(itens[8]))
            self.ui.txtTelefoneFornecedor.setText(str(itens[9]))
            self.ui.txtSiteFornecedor.setText(str(itens[10]))
            self.ui.txtEmailFornecedor.setText(str(itens[11]))
            self.ui.txtCepFornecedor.setText(str(itens[12]))
            self.ui.txtCidadesFornecedor.setText(str(itens[13]))
            self.ui.txtEstadosFornecedor.setText(str(itens[14]))
            self.ui.txtIdEmpresa.setText(str(itens[15]))
            self.ui.txtFantasiaEmpresa.setText(str(itens[16]))
            self.ui.txtRazaoSocialEmpresa.setText(str(itens[17]))
            self.ui.txtCnpjEmpresa.setText(str(itens[18]))
            self.ui.txtInscricaoEstaduaEmpresa.setText(str(itens[19]))
"""
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetCliente import Cliente
from controller.getSetContatoEmail import ContatoEmail
from controller.getSetContatoTelefone import ContatoTelefone
from controller.getSetPessoaFisica import PessoaFisica
from controller.getSetPessoaJuridica import PessoaJuridica
from dao.clienteDao import ClienteDao
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from dao.pesquisarPessoaJuridicaDao import PesquisarPessoaJuridicaDao
from telas.frmCadCliente import Ui_frmCadastroCliente
from telas.frmPesquisarClientes import Ui_frmPesquisarCliente
from telas.frmPesquisarPessoaFisicaJuridica import Ui_frmPesquisarPessoaFisicaJuridica


class CadastroClientes(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroCliente()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.idCliente = int()
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
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnPesquisarEmpresa.clicked.connect(self.pesquisarPessoaFisicaJuridica)

        self.ui.radBtnPessoaFisica.clicked.connect(self.botaoNovo)
        self.ui.radBtnPessoaJuridica.clicked.connect(self.botaoNovo)

        self.ui.txtCodigo.textChanged.connect(self.numberCodigo)
        self.ui.txtNumeroTelefone.textChanged.connect(self.numberTelefone)

        self.ui.txtCodigo.returnPressed.connect(self.setCliente)

        self.ui.btnAddTelefone.clicked.connect(self.addContatoTelefone)
        self.ui.btnRemoverTelefone.clicked.connect(self.delContatoTelefone)

        self.ui.btnAddEmail.clicked.connect(self.addContatoEmail)
        self.ui.btnRemoverEmail.clicked.connect(self.delContatoEmail)

    def numberCodigo(self):
        if self.ui.txtCodigo.text().isnumeric() == False:
            self.ui.txtCodigo.backspace()

    def numberTelefone(self):
        if self.ui.txtNumeroTelefone.text().isnumeric() == False:
            self.ui.txtNumeroTelefone.backspace()

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

    def ativarCampos(self):
        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

    def limparCampos(self):
        self.ui.grbTipoPessoa.setEnabled(False)
        self.ui.radBtnPessoaFisica.setCheckable(False)
        self.ui.radBtnPessoaJuridica.setCheckable(False)
        self.ui.txtCodigo.setEnabled(True)
        self.ui.btnPesquisarEmpresa.setEnabled(True)
        self.editar = False
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtRazaoSocial.clear()
        self.ui.txtFantasia.clear()

        self.ui.txtContatoTelefone.clear()
        self.ui.txtNumeroTelefone.clear()
        self.ui.txtEnderecoEmail.clear()
        self.ui.txtContatoEmail.clear()


        self.contatoAdd.clear()
        self.contatoRemove.clear()
        self.emailAdd.clear()
        self.emailRemove.clear()

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
        cliente = ClienteDao()
        if self.ui.radBtnPessoaFisica.isChecked():
            cli = cliente.pesquisarClienteIdFisico(self.ui.txtCodigo.text())

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
            cli = cliente.pesquisarClienteIdJuridico(self.ui.txtCodigo.text())

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

    def cadastrarTelefone(self):
        cli = ClienteDao()
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
        cli = ClienteDao()
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
            clienteDao = ClienteDao()
            cliente = Cliente(None, self.ui.txtCodigo.text(), None, None, None, None, None, 1)
            clienteDao.cadastrarCliente(cliente)
            self.idCliente = clienteDao.ultimoRegistro()


            if self.contatoAdd != []:
                self.cadastrarTelefone()

            if self.emailAdd != []:
                self.cadastrarEmail()

            self.cancelar()
        else:
            self.mensagem.warning( 'Atenção', "Preencha os campos obrigatorio")


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

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialog = QDialog(self)
            self.__pesquisarCliente = Ui_frmPesquisarCliente()
            self.__pesquisarCliente.setupUi(self.dialog)

            self.__pesquisarCliente.txtPesquisar.setValidator(self.validator)

            #self.__pesquisarCliente.txtPesquisar.returnPressed.connect(self.pesquisar)

            #self.__pesquisarCliente.btnPesquisar.clicked.connect(self.pesquisar)

            #self.__pesquisarCliente.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        __pesDao = ClienteDao()
        if self.__pesquisarCliente.radBtnCodigo.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __codigo = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCodigoFisica(__codigo)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __codigo = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCodigoJuridica(__codigo)
                self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarCliente.radBtnRazaoSocial.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __razao = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisarNomeFisica(__razao)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __razao = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaRazaoSocialJuridica(__razao)
                self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarCliente.radBtnFantasia.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __fantasia = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaApelidoFisica(__fantasia)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __fantasia = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaFantasiaJuridica(__fantasia)
                self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarCliente.radBtnCnpj.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __cnpj = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCpfFisica(__cnpj)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __cnpj = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCnpjJuridica(__cnpj)
                self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarCliente.radBtnInsEstadual.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __inscricao = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaRgFisica(__inscricao)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __inscricao = self.__pesquisarCliente.txtPesquisar.text()
                __retorno = __pesDao.pesquisaInscEstadualJuridica(__inscricao)
                self.setarTabelaPesquisaJuridico(__retorno)

        else:
            self.mensagem.warning( 'Atenção', "Selecione uma das opções de pesquisa")

    '''
      
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
        result = QMessageBox.question(QWidget(), 'Menssagem', "Deseja realmente cancelar a operação",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
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
'''
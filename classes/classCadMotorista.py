import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetContatoEmail import ContatoEmail
from controller.getSetContatoTelefone import ContatoTelefone
from controller.getSetMotorista import Motorista
from controller.getSetPessoaFisica import PessoaFisica
from dao.motoristaDao import MotoristaDao
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from telas.frmCadMotorista import Ui_frmCadastroMotorista
from telas.frmPesquisarMotorista import Ui_frmConsultarMotoristas
from telas.frmPesquisarPessoaFisica import Ui_frmPesquisarPessoaFisica


class CadastroMotoristas(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroMotorista()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.idMotorista = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.IdVeiculo = int()
        self.editar = False
        self.novoVei = False
        self.contatoAdd = []
        self.contatoRemove = []
        self.contatoAtualizar = []
        self.emailAdd = []
        self.emailRemove = []
        self.emailAtualizar = []
        self.categoriaCnh = []

        self.ui.txtMarca.setValidator(self.validator)
        self.ui.txtModelo.setValidator(self.validator)
        self.ui.txtPlaca.setValidator(self.validator)
        self.ui.txtContatoTelefone.setValidator(self.validator)
        self.ui.txtContatoEmail.setValidator(self.validator)

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnEditar.clicked.connect(self.atualizar)
        self.ui.btnDeletar.clicked.connect(self.deletar)
        self.ui.btnPesquisarEmpresa.clicked.connect(self.pesquisarPessoaFisica)

        self.ui.txtCodigo.textChanged.connect(self.numberCodigo)
        self.ui.txtNumeroTelefone.textChanged.connect(self.numberTelefone)
        self.ui.txtCnh.textChanged.connect(self.numberCnh)
        self.ui.txtPis.textChanged.connect(self.numberPis)
        self.ui.txtPlaca.cursorPositionChanged.connect(self.positionCursorPlaca)
        self.ui.txtObservacao.textChanged.connect(self.textEdite)

        self.ui.txtCodigo.returnPressed.connect(self.setMotorista)

        self.ui.txtCodigo.editingFinished.connect(self.setMotoristaEditFinish)

        self.ui.btnAddTelefone.clicked.connect(self.addContatoTelefone)
        self.ui.btnRemoverTelefone.clicked.connect(self.delContatoTelefone)

        self.ui.btnAddEmail.clicked.connect(self.addContatoEmail)
        self.ui.btnRemoverEmail.clicked.connect(self.delContatoEmail)

        self.ui.btnAddNovoVeiculo.clicked.connect(self.novoVeiculo)

    def numberCodigo(self):
        if self.ui.txtCodigo.text().isnumeric() == False:
            self.ui.txtCodigo.backspace()

    def numberTelefone(self):
        if self.ui.txtNumeroTelefone.text().isnumeric() == False:
            self.ui.txtNumeroTelefone.backspace()

    def numberCnh(self):
        if self.ui.txtCnh.text().isnumeric() == False:
            self.ui.txtCnh.backspace()

    def numberPis(self):
        if self.ui.txtPis.text().isnumeric() == False:
            self.ui.txtPis.backspace()

    def addCategoria(self):
        __motoDao = MotoristaDao()
        __categoria = __motoDao.pesquisarCategoria()

        self.categoriaCnh.append(__categoria)
        for cate in __categoria:
            self.ui.txtCategoriaCnh.addItem(cate[1])

    def textEdite(self):
        if (len(self.ui.txtObservacao.toPlainText()) > 255):
            self.ui.txtObservacao.textCursor().deletePreviousChar()

    def positionCursorPlaca(self):
        texto = self.removerCaracter(self.ui.txtPlaca.text())

        if len(texto) == 0:
            self.ui.txtPlaca.setCursorPosition(0)
        elif len(texto) <= 2:
            b = len(texto)
            self.ui.txtPlaca.setCursorPosition(b)
        elif len(texto) >= 3 and len(texto) < 9:
            b = len(texto) + 1
            self.ui.txtPlaca.setCursorPosition(b)

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

    def setMotorista(self):
        motorista = MotoristaDao()

        mot = motorista.pesquisarMotoristaIdFisico(self.ui.txtCodigo.text())

        if mot == []:
            moto = motorista.pesquisarPessoaFisica(self.ui.txtCodigo.text())
            if moto  == []:
                self.mensagem.warning('Mensagem', "Atenção não existe nenhum cadastro neste codigo")
                self.ui.txtCnpj.clear()
                self.ui.txtInscricaoEstadua.clear()
                self.ui.txtNome.clear()
                self.ui.txtSobrenome.clear()
            else:
                for empres in moto:
                    self.ui.txtCnpj.setText(str(empres[0]))
                    self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                    self.ui.txtNome.setText(str(empres[2]))
                    self.ui.txtSobrenome.setText(str(empres[3]))
        else:
            self.mensagem.warning( 'Mensagem', "Atenção já tem um cadastro deste motorista")

    def setMotoristaEditFinish(self):
        motorista = MotoristaDao()

        mot = motorista.pesquisarMotoristaIdFisico(self.ui.txtCodigo.text())

        if mot == []:
            moto = motorista.pesquisarPessoaFisica(self.ui.txtCodigo.text())
            if moto == []:
                self.ui.txtCnpj.clear()
                self.ui.txtInscricaoEstadua.clear()
                self.ui.txtNome.clear()
                self.ui.txtSobrenome.clear()
            else:
                for empres in moto:
                    self.ui.txtCnpj.setText(str(empres[0]))
                    self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                    self.ui.txtNome.setText(str(empres[2]))
                    self.ui.txtSobrenome.setText(str(empres[3]))

    def novo(self):
        self.limparCampos()
        self.ui.grbDadosPessoaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

        self.addCategoria()

    def botaoNovo(self):
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtNome.clear()
        self.ui.txtSobrenome.clear()

        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.txtModelo.setEnabled(True)
        self.ui.txtMarca.setEnabled(True)
        self.ui.txtPlaca.setEnabled(True)

        self.deletarContatoTelefone()
        self.deletarContatoEmail()

    def cancelar(self):
        self.limparCampos()
        self.deletarContatoTelefone()
        self.deletarContatoEmail()
        self.desativarCampos()

    def desativarCampos(self):
        self.ui.grbDadosPessoaJuridica.setEnabled(False)
        self.ui.tabWiAdicionais.setEnabled(False)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def botoesEditar(self):
        self.limparCampos()
        self.ui.grbAtivo.setEnabled(True)
        self.ui.radBtnAtivo.setCheckable(True)
        self.ui.radBtnDesativo.setCheckable(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)

        self.addCategoria()

    def ativarCampos(self):
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

    def limparCampos(self):
        self.idMotorista = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.IdVeiculo = int()
        self.ui.txtCodigo.setEnabled(True)
        self.ui.btnPesquisarEmpresa.setEnabled(True)
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtNome.clear()
        self.ui.txtSobrenome.clear()

        self.ui.txtCnh.clear()
        self.ui.txtPis.clear()
        self.ui.txtCategoriaCnh.clear()
        self.ui.txtObservacao.clear()
        self.ui.txtModelo.clear()
        self.ui.txtMarca.clear()
        self.ui.txtPlaca.clear()

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
        self.categoriaCnh.clear()

        self.deletarContatoTelefone()
        self.deletarContatoEmail()

        self.ui.tabWiAdicionais.setCurrentIndex(0)

        self.ui.radBtnAtivo.setCheckable(False)
        self.ui.radBtnDesativo.setCheckable(False)
        self.ui.btnAddNovoVeiculo.setEnabled(False)
        self.novoVei = False
        self.editar = False

    def novoVeiculo(self):
        self.ui.txtModelo.clear()
        self.ui.txtMarca.clear()
        self.ui.txtPlaca.clear()
        self.ui.txtModelo.setEnabled(True)
        self.ui.txtMarca.setEnabled(True)
        self.ui.txtPlaca.setEnabled(True)
        self.novoVei = True

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

    def pesquisarPessoaFisica(self):
        self.dialogFisicoJuridico = QDialog(self)
        self.__pesquisarFisica = Ui_frmPesquisarPessoaFisica()
        self.__pesquisarFisica.setupUi(self.dialogFisicoJuridico)
        self.__pesquisarFisica.txtPesquisar.setValidator(self.validator)

        self.__pesquisarFisica.txtPesquisar.returnPressed.connect(self.pesquisarFisico)

        self.__pesquisarFisica.btnPesquisar.clicked.connect(self.pesquisarFisico)

        self.__pesquisarFisica.tabPesquisar.doubleClicked.connect(self.setarCamposFisicoJuridico)

        self.dialogFisicoJuridico.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogFisicoJuridico.exec_()

    def pesquisarFisico(self):
        if self.__pesquisarFisica.radBtnCodigo.isChecked():
            __codigo = self.__pesquisarFisica.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaCodigo(__codigo)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisica.radBtnNome.isChecked():
            __nome = self.__pesquisarFisica.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaNome(__nome)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisica.radBtncPF.isChecked():
            __cpf = self.__pesquisarFisica.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaCpf(__cpf)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisica.radBtnRg.isChecked():
            __rg = self.__pesquisarFisica.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaRg(__rg)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisica.radBtnMae.isChecked():
            __mae = self.__pesquisarFisica.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaMae(__mae)

            self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisica.radBtnPai.isChecked():
            __pai = self.__pesquisarFisica.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaPai(__pai)

            self.setarTabelaPesquisaJuridico(__retorno)

        else:
            MensagemBox().warning( 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaJuridico(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarFisica.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            sobrenome = pesqui[2]
            cpf = pesqui[3]
            rg = pesqui[4]
            expeditor = pesqui[5]
            uf = pesqui[6]
            data = pesqui[7]
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
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(sobrenome)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(data)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(sexo)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(mae)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(pai)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarFisica.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cep)))

            linha += 1

    def setarCamposFisicoJuridico(self):
        motorista = MotoristaDao()
        itens = []

        for item in self.__pesquisarFisica.tabPesquisar.selectedItems():
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

        fun = motorista.pesquisarMotoristaFisico(codigo)
        if fun == []:
            __dados = PessoaFisica(None, codigo, None, nome, apelido, cpf, rg, expeditor, uf, aniversario, sexo, endereco, numero, complemento, bairro, None, None, None, cidade, estado, cep)
            self.setCamposFisicoJuridico(__dados)
            self.dialogFisicoJuridico.close()
        else:
            MensagemBox().warning('Mensagem', "Atenção já tem um cadastro desta pessoa")

    def setCamposFisicoJuridico(self, campos):
        self.ui.txtCodigo.setText(campos.getIdPesFisica)
        self.ui.txtCnpj.setText(campos.getCpf)
        self.ui.txtInscricaoEstadua.setText(campos.setRg)
        self.ui.txtSobrenome.setText(campos.getApelido)
        self.ui.txtNome.setText(campos.getNome)

    def cadastrarTelefone(self):
        cli = MotoristaDao()
        i = 0
        for lista in self.contatoAdd:
            a = self.contatoAdd[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, self.idMotorista)
            cli.cadastrarTelefone(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarTelefoneMotorista(id, self.idMotorista)

            i += 1

    def cadastrarEmail(self):
        cli = MotoristaDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idMotorista)
            cli.cadastrarEmail(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarEmailMotorista(id, self.idMotorista)

            i += 1

    def getIndexCategoria(self):
        index = self.ui.txtCategoriaCnh.currentIndex()

        for lista in self.categoriaCnh:
            a = lista[index]
        categoria = int(a[0])

        return categoria

    def cadastrar(self):

        if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtNome.text() != '' and self.ui.txtSobrenome.text() != '' and self.ui.txtCnh.text() != '' and self.ui.txtPis.text() != '' and self.ui.txtMarca.text() != '' and self.ui.txtModelo.text() != '' and self.removerCaracter(self.ui.txtPlaca.text()) != '':
            motoDao = MotoristaDao()
            idPessoa = motoDao.pesquisarPessoaFis(self.ui.txtCodigo.text())
            categoria = self.getIndexCategoria()
            motoris = Motorista(None, idPessoa, self.ui.txtCodigo.text(), self.ui.txtNome.text(), self.ui.txtSobrenome.text(), self.ui.txtInscricaoEstadua.text(), self.ui.txtCnpj.text(), self.ui.txtPis.text(), self.ui.txtCnh.text(), categoria, self.ui.txtMarca.text(), self.ui.txtModelo.text(), self.removerCaracter(self.ui.txtPlaca.text()), self.ui.txtObservacao.toPlainText(), 1)
            motoDao.cadastrarMotorista(motoris)
            self.idMotorista = motoDao.ultimoRegistro()
            motoDao.cadastrarVeiculoMotorista(self.ui.txtMarca.text(), self.ui.txtModelo.text(), self.removerCaracter(self.ui.txtPlaca.text()), self.idMotorista)

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
            self.__pesquisarMotorista = Ui_frmConsultarMotoristas()
            self.__pesquisarMotorista.setupUi(self.dialog)

            self.__pesquisarMotorista.txtPesquisar.setValidator(self.validator)

            self.__pesquisarMotorista.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisarMotorista.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisarMotorista.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        __pesDao = MotoristaDao()
        if self.__pesquisarMotorista.radBtnCodigo.isChecked():
                __codigo = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCodigoFisica(__codigo)
                self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarMotorista.radBtnNome.isChecked():
                __razao = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisarNomeFisica(__razao)
                self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarMotorista.radBtnCpf.isChecked():
                __fantasia = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaCpfFisica(__fantasia)
                self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarMotorista.radBtnRg.isChecked():
                __cnpj = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaRgFisica(__cnpj)
                self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarMotorista.radBtnNumCarteira.isChecked():
                __inscricao = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaNumCarteira(__inscricao)
                self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarMotorista.radBtnPis.isChecked():
                __inscricao = self.__pesquisarMotorista.txtPesquisar.text()
                __retorno = __pesDao.pesquisaPis(__inscricao)
                self.setarTabelaPesquisaEditar(__retorno)

        else:
            self.mensagem.warning( 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaEditar(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarMotorista.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            apelido = pesqui[2]
            cnh = pesqui[3]
            cpf = pesqui[4]
            rg = pesqui[5]
            expeditor = pesqui[6]
            uf = pesqui[7]
            pis = pesqui[8]
            aniversario = pesqui[9]
            genero = pesqui[10]
            mae = pesqui[11]
            pai = pesqui[12]
            endereco = pesqui[13]
            numero = pesqui[14]
            complemento = pesqui[15]
            bairro = pesqui[16]
            cidade = pesqui[17]
            estado = pesqui[18]
            cep = pesqui[19]
            categoria = pesqui[20]
            marca = pesqui[21]
            modelo = pesqui[22]
            placa = pesqui[23]
            obs = pesqui[24]
            if pesqui[25] == 1:
                situacao = "Ativo"
            else:
                situacao = "Inativo"


            # preenchendo o grid de pesquisa
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(apelido)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnh)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(pis)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(aniversario)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(genero)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(mae)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(pai)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 19, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 20, QtGui.QTableWidgetItem(str(categoria)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 21, QtGui.QTableWidgetItem(str(marca)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 22, QtGui.QTableWidgetItem(str(modelo)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 23, QtGui.QTableWidgetItem(str(placa)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 24, QtGui.QTableWidgetItem(str(obs)))
            self.__pesquisarMotorista.tabPesquisar.setItem(linha, 25, QtGui.QTableWidgetItem(str(situacao)))

            linha += 1

    def setarCampos(self):
        motoDao = MotoristaDao()
        itens = []

        for item in self.__pesquisarMotorista.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = itens[0]
        nome = itens[1]
        sobrenome = itens[2]
        cnh = itens[3]
        cpf = itens[4]
        rg = itens[5]
        expeditor = itens[6]
        uf = itens[7]
        pis = itens[8]
        data = itens[9]
        sexo = itens[10]
        mae = itens[11]
        pai = itens[12]
        endereco = itens[13]
        numero = itens[14]
        complemento = itens[15]
        bairro = itens[16]
        cidade = itens[17]
        estado = itens[18]
        cep = itens[19]
        categoria = itens[20]
        marca = itens[21]
        modelo = itens[22]
        placa = itens[23]
        obs = itens[24]
        if itens[25] == 'Ativo':
            situacao = True
        else:
            situacao = False


        idPessoa = motoDao.pesquisarPessoaCodigo(codigo)
        idPessoaFisico = motoDao.pesquisarPessoaFisicaId(idPessoa)

        __dados = Motorista(codigo, idPessoa, idPessoaFisico, nome, sobrenome, rg, cpf, pis, cnh, categoria, marca, modelo, placa, obs, situacao)
        self.botoesEditar()
        self.setCampos(__dados)
        self.IdVeiculo = motoDao.pesquisarVeiculo(str(codigo), str(1))
        self.pesquisarTelefone(codigo)
        self.pesquisaEmail(codigo)
        self.dialog.close()


    def setCampos(self, campos):
        self.ui.txtCodigo.setEnabled(False)

        self.idMotorista = int(campos.getIdMotorista)
        self.idPessoa = int(campos.getIdPessoa)
        self.ui.txtCodigo.setText(str(campos.getIdPessoaFisica))
        self.ui.txtCnpj.setText(campos.getCpf)
        self.ui.txtInscricaoEstadua.setText(campos.getRg)
        self.ui.txtNome.setText(campos.getNome)
        self.ui.txtSobrenome.setText(campos.getSobrenome)


        if campos.getSituacao == True:
            self.ui.radBtnAtivo.setChecked(True)
        else:
            self.ui.radBtnDesativo.setChecked(True)

        self.ui.txtObservacao.setText(str(campos.getObservacao))

        self.ui.txtCategoriaCnh.setCurrentIndex(self.ui.txtCategoriaCnh.findText(campos.getCategoria))
        self.ui.txtCnh.setText(campos.getCnh)
        self.ui.txtPis.setText(campos.getPis)

        self.ui.txtModelo.setText(campos.getModelo)
        self.ui.txtMarca.setText(campos.getMarca)
        self.ui.txtPlaca.setText(campos.getPlaca)

        self.ui.btnAddNovoVeiculo.setEnabled(True)
        self.ui.txtModelo.setEnabled(False)
        self.ui.txtMarca.setEnabled(False)
        self.ui.txtPlaca.setEnabled(False)

        self.editar = True

    def pesquisarTelefone(self, campos):
        funcionarioDao = MotoristaDao()
        id = funcionarioDao.pesquisaTelefone(campos)

        if id != []:
            self.setTabelaTelefone(id)

    def setTabelaTelefone(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabContatoTelefone.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            idContato = pesqui[0]
            contato = pesqui[1]
            telefone = pesqui[2]


            self.ui.tabContatoTelefone.setItem(linha, 0, QtGui.QTableWidgetItem(str(contato)))
            self.ui.tabContatoTelefone.setItem(linha, 1, QtGui.QTableWidgetItem(str(telefone)))

            lista = (idContato, contato, telefone)
            self.contatoAdd.append(lista)


            linha += 1

    def pesquisaEmail(self, campos):
        funcionarioDao = MotoristaDao()
        id = funcionarioDao.pesquisaEmail(campos)
        if id != []:

            self.setTabelaEmail(id)

    def setTabelaEmail(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabContatoEmail.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            idEmail = pesqui[0]
            contato = pesqui[1]
            email = pesqui[2]

            self.ui.tabContatoEmail.setItem(linha, 0, QtGui.QTableWidgetItem(str(contato)))
            self.ui.tabContatoEmail.setItem(linha, 1, QtGui.QTableWidgetItem(str(email)))

            lista = (idEmail, contato, email)
            self.emailAdd.append(lista)

            linha += 1


    def deletarTelefone(self):
        emp = MotoristaDao()
        i = 0
        for lista in self.contatoRemove :
            a = self.contatoRemove[i]

            idTelefone = int(a[0])

            emp.deletarTelefone(idTelefone, str(self.idMotorista))
            pesquisa = emp.pesquisaTelefoneMotorista(idTelefone, str(self.idMotorista))
            if pesquisa == "":
                emp.deletarContatoTelefone(idTelefone)

            i += 1

    def deletarEmail(self):
        emp = MotoristaDao()
        i = 0
        for lista in self.emailRemove:
            a = self.emailRemove[i]

            idEmail = a[0]

            emp.deletarEmail(idEmail, str(self.idMotorista))
            pesquisa = emp.pesquisaEmailMotorista(idEmail, str(self.idMotorista))
            if pesquisa == "":
                emp.deletarContatoEmail(idEmail)

            i += 1

    def atualizaTelefone(self):
        emp = MotoristaDao()
        i = 0
        for lista in self.contatoAtualizar:
            a = self.contatoAtualizar[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, str(self.idMotorista))
            emp.cadastrarTelefone(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarTelefoneMotorista(id, str(self.idMotorista))

            i += 1

    def atualizaEmail(self):
        emp = MotoristaDao()
        i = 0
        for lista in self.emailAtualizar:
            a = self.emailAtualizar[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, str(self.idMotorista))
            emp.cadastrarEmail(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarEmailMotorista(id, str(self.idMotorista))

            i += 1

    def atualizar(self):
        if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtNome.text() != '' and self.ui.txtSobrenome.text() != '' and self.ui.txtCnh.text() != '' and self.ui.txtPis.text() != '' and self.ui.txtMarca.text() != '' and self.ui.txtModelo.text() != '' and self.removerCaracter(self.ui.txtPlaca.text()) != '':

            if self.contatoRemove  != []:
                self.deletarTelefone()

            if self.emailRemove != []:
                self.deletarEmail()

            if self.contatoAtualizar != []:
                self.atualizaTelefone()

            if self.emailAtualizar != []:
                self.atualizaEmail()


            if self.ui.radBtnAtivo.isChecked():
                ativo = 1
            elif self.ui.radBtnDesativo.isChecked():
                ativo = 0

            categoria = self.getIndexCategoria()

            motoDao = MotoristaDao()
            motorista = Motorista(self.idMotorista, self.idPessoa, self.ui.txtCodigo.text(), self.ui.txtNome.text(), self.ui.txtSobrenome.text(), self.ui.txtInscricaoEstadua.text(), self.ui.txtCnpj.text(), self.ui.txtPis.text(), self.ui.txtCnh.text(), categoria, self.ui.txtMarca.text(), self.ui.txtModelo.text(), self.removerCaracter(self.ui.txtPlaca.text()), self.ui.txtObservacao.toPlainText(), ativo)

            motoDao.atualizarMotorista(motorista)
            if self.novoVei == True:
                motoDao.alterarVeiculo(0, self.IdVeiculo)
                motoDao.cadastrarVeiculoMotorista(self.ui.txtMarca.text(), self.ui.txtModelo.text(),self.removerCaracter(self.ui.txtPlaca.text()), self.idMotorista)

            self.cancelar()
        else:
            self.mensagem.warning('Atenção', "Por Favor preencha os campos obrigatorios")

    def deletar(self):
        fisicaDao = MotoristaDao()
        nf = fisicaDao.pesquisarTabelaNf(self.idMotorista)

        if nf == []:
            try:
                _fromUtf8 = QtCore.QString.fromUtf8
            except AttributeError:
                def _fromUtf8(s):
                    return s

            self.msgBox = QtGui.QMessageBox()
            self.msgBox.setWindowTitle('Menssagem')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/question.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.msgBox.setWindowIcon(icon)
            self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("./imagens/icon-question.png")))
            self.msgBox.setText("Tem certeza que deseja excluir esse registro")
            btnSim = QtGui.QPushButton('Sim')
            self.msgBox.addButton(btnSim, QtGui.QMessageBox.YesRole)
            btnNao = QtGui.QPushButton('Não')
            self.msgBox.addButton(btnNao, QtGui.QMessageBox.NoRole)
            btnSim.clicked.connect(self.simDeletar)
            btnNao.clicked.connect(self.fechar)
            btnNao.setFocus()
            self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.msgBox.exec_()
        else:
            MensagemBox().warning('Atenção', 'Impossivel fazer essa operação, pois essa pessoa esta relacionada com outro formulario')

    def simDeletar(self):
            motoDao = MotoristaDao()
            codigo = self.idMotorista
            a = motoDao.deletarMotorista(codigo)
            b = motoDao.deletarVeiculoMotorista(codigo)
            if self.contatoAdd != []:
                self.deletarTelefoneFrom()

            if self.emailAdd != []:
                self.deletarEmailFrom()

            if self.contatoRemove != []:
                self.deletarTelefone()

            if self.emailRemove != []:
                self.deletarEmail()

            if a  == True:
                MensagemBox().informacao('Mensagem', 'Cadastro deletar com sucesso!')
                self.desativarCampos()
            else:
                MensagemBox().critico('Erro', 'Erro ao deletar as informações no banco de dados')

            self.cancelar()
            self.msgBox.close()

    def fechar(self):
        self.msgBox.close()

    def deletarTelefoneFrom(self):
        emp = MotoristaDao()
        i = 0
        for lista in self.contatoAdd :
            a = self.contatoAdd[i]

            idTelefone = int(a[0])

            emp.deletarTelefone(idTelefone, str(self.idMotorista))
            pesquisa = emp.pesquisaTelefoneMotorista(idTelefone, str(self.idMotorista))
            if pesquisa == "":
                emp.deletarContatoTelefone(idTelefone)

            i += 1

    def deletarEmailFrom(self):
        emp = MotoristaDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            idEmail = a[0]

            emp.deletarEmail(idEmail, str(self.idMotorista))
            pesquisa = emp.pesquisaEmailMotorista(idEmail, str(self.idMotorista))
            if pesquisa == "":
                emp.deletarContatoEmail(idEmail)

            i += 1
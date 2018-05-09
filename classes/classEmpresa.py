from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetCnae import Cnae
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
from telas.frmPesquisarCnae import Ui_frmPesquisarCnae
from telas.frmPesquisarEmpresa import Ui_frmConsultarEmpresa
from telas.frmPesquisarPessoaJuridica import Ui_frmPesquisarPessoaJuridica

class Empresa(QtGui.QDialog):


    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroEmpresa()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.idPessoaJuridica = int()
        self.idEmpresa = int()
        self.idTipoEmpresa = int()
        self.idCnae = int()
        self.editar = False
        self.contatoAdd = []
        self.contatoRemove = []
        self.contatoAtualizar = []
        self.emailAdd = []
        self.emailRemove = []
        self.emailAtualizar = []
        self.setoresAdd = []
        self.setoresRemove = []
        self.setoresAtualizar = []
        self.cargoAdd = []
        self.cargoRemove = []
        self.cargoAtualizar = []

        self.ui.txtContatoEmail.setValidator(self.validator)
        self.ui.txtContatoTelefone.setValidator(self.validator)
        self.ui.txtCadSetoresSetor.setValidator(self.validator)
        self.ui.txtCadCargoCargo.setValidator(self.validator)


        self.ui.cBoxTipoEmpresa.currentIndexChanged.connect(self.pesquisarTipoEmpresa)


        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnEditar.clicked.connect(self.atualizar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnPesquisarEmpresa.clicked.connect(self.pesquisarPessoaJuridica)
        self.ui.btnPesquisarCnae.clicked.connect(self.pesquisarCnae)


        self.ui.btnAddTelefone.clicked.connect(self.addContatoTelefone)
        self.ui.btnRemoverTelefone.clicked.connect(self.delContatoTelefone)

        self.ui.btnAddEmail.clicked.connect(self.addContatoEmail)
        self.ui.btnRemoverEmail.clicked.connect(self.delContatoEmail)

        self.ui.btnAddSetor.clicked.connect(self.addContatoSetor)
        self.ui.btnRemoverSetor.clicked.connect(self.delContatoSetor)

        self.ui.btnAddCargos.clicked.connect(self.addContatoCargo)
        self.ui.btnRemoverCargos.clicked.connect(self.delContatoCargo)

        self.ui.txtCodigo.returnPressed.connect(self.setEmpresa)
        self.ui.txtCnae.returnPressed.connect(self.setCnae)

        self.ui.txtCodigo.textChanged.connect(self.numberCodigo)
        self.ui.txtNumeroTelefone.textChanged.connect(self.numberTelefone)
        self.ui.txtInscricaoMunicipal.textChanged.connect(self.numberInscricaoMunicipal)

        self.ui.txtCnae.cursorPositionChanged.connect(self.positionCursorCnae)

    def numberCodigo(self):
        if self.ui.txtCodigo.text().isnumeric() == False:
            self.ui.txtCodigo.backspace()

    def numberTelefone(self):
        if self.ui.txtNumeroTelefone.text().isnumeric() == False:
            self.ui.txtNumeroTelefone.backspace()

    def numberInscricaoMunicipal(self):
        if self.ui.txtInscricaoMunicipal.text().isnumeric() == False:
            self.ui.txtInscricaoMunicipal.backspace()

    def positionCursorCnae(self):
        texto = self.removerCaracter(self.ui.txtCnae.text())

        if len(texto) == 0:
            self.ui.txtCnae.setCursorPosition(0)
        elif len(texto) <= 3:
            b = len(texto)
            self.ui.txtCnae.setCursorPosition(b)
        elif len(texto) >= 4 and len(texto) <5:
            b = len(texto)+1
            self.ui.txtCnae.setCursorPosition(b)
        elif len(texto) >= 6 and len(texto) <8:
            c = len(texto)+2
            self.ui.txtCnae.setCursorPosition(c)

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
        self.ui.txtCodigo.setEnabled(True)
        self.ui.btnPesquisarEmpresa.setEnabled(True)
        self.editar = False
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtRazaoSocial.clear()
        self.ui.txtFantasia.clear()
        self.ui.cBoxTipoEmpresa.clear()
        self.ui.txtInscricaoMunicipal.clear()
        self.ui.txtCnae.clear()
        self.ui.txtCnaeDescricao.clear()

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
        self.contatoAtualizar.clear()
        self.emailAtualizar.clear()
        self.setoresAdd.clear()
        self.setoresRemove.clear()
        self.setoresAtualizar.clear()
        self.cargoAdd.clear()
        self.cargoRemove.clear()
        self.cargoAtualizar.clear()


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

    def setCnae(self):
        empresa = EmpresaDao()

        emp = empresa.pesquisarCnaeEmpresa(self.ui.txtCnae.text())
        if emp == []:
            MensagemBox().warning('Mensagem', "Atenção não existe este codigo CNAE")
            self.ui.txtCnaeDescricao.clear()
        else:
            for empres in emp:
                self.ui.txtCnaeDescricao.setText(empres[0])

    def setEmpresa(self):
        empresa = EmpresaDao()
        em = empresa.pesquisarPessoaJuridica(self.ui.txtCodigo.text())

        if em == []:
            emp = empresa.pesquisarEmpresaId(self.ui.txtCodigo.text())

            if emp == []:
                MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro desta empresa")
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
            MensagemBox().warning( 'Mensagem', "Atenção já tem um cadastro desta pessoa")

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
                MensagemBox().warning( 'Mensagem', "Atenção contem digitos do telefone a mais")
            else:
                MensagemBox().warning( 'Mensagem', "Atenção esta faltando digitos do telefone")
        else:
            MensagemBox().warning( 'Mensagem', "Por favor preencha os campos de contato e telefone")

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
                MensagemBox().warning( 'Mensagem',"Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickTelefone()
            #QtCore.QObject.connect(self.ui.tabContatoTelefone, QtCore.SIGNAL("cellClicked()"),self.cellClick())

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
            MensagemBox().warning( 'Mensagem', "Por favor preencha os campos de contato e telefone")

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
                MensagemBox().warning( 'Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickEmail()

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
                if self.editar == False:
                    add = [(__setor)]
                    self.setoresAdd.append([__setor])
                    self.inserirTabelaSetor(add)

                elif self.editar == True:
                    add = [(__setor)]
                    self.setoresAtualizar.append([__setor])
                    self.inserirTabelaSetor(add)

                self.ui.txtCadSetoresSetor.clear()

                self.ui.txtCadSetoresSetor.setFocus()
        else:
            MensagemBox().warning( 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def cellClickSetores(self):
        index = self.ui.tabSetores.currentRow()
        list=[]
        columcount = self.ui.tabSetores.columnCount()
        row = self.ui.tabSetores.currentItem().row()
        for x in range(0, columcount, 1):
            cell = self.ui.tabSetores.item(row, x).text()
            list.append(cell)

        if list in self.setoresAtualizar:
            self.setoresAtualizar.remove(list)
            self.ui.tabSetores.removeRow(index)
        else:
            self.ui.tabSetores.removeRow(index)
            if index >= 0:
                self.setoresRemove.append(self.setoresAdd[index])
                del self.setoresAdd[index]
            else:
                MensagemBox().warning( 'Mensagem',"Impossivel realizar essa ação, por favor selecione um item da lista para excluir")


    def delContatoSetor(self):
        index = self.ui.tabSetores.currentRow()

        if self.editar == False:
            self.ui.tabSetores.removeRow(index)
            if index >= 0:
                self.setoresAdd.append(self.setoresAdd[index])
                del self.setoresAdd[index]
            else:
                MensagemBox().warning( 'Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickSetores()

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
            if self.editar == False:
                add = [(__cargo)]
                self.cargoAdd.append([__cargo])
                self.inserirTabelaCargo(add)
            elif self.editar == True:
                add = [(__cargo)]
                self.cargoAtualizar.append([__cargo])
                self.inserirTabelaCargo(add)

            self.ui.txtCadCargoCargo.clear()

            self.ui.txtCadCargoCargo.setFocus()
        else:
            MensagemBox().warning( 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def cellClickCargo(self):
        index = self.ui.tabCargos.currentRow()
        list=[]
        columcount = self.ui.tabCargos.columnCount()
        row = self.ui.tabCargos.currentItem().row()
        for x in range(0, columcount, 1):
            cell = self.ui.tabCargos.item(row, x).text()
            list.append(cell)

        if list in self.cargoAtualizar:
            print(self.cargoAtualizar)
            self.cargoAtualizar.remove(list)
            self.ui.tabCargos.removeRow(index)
        else:
            self.ui.tabCargos.removeRow(index)
            if index >= 0:
                self.cargoRemove.append(self.cargoAdd[index])
                del self.cargoAdd[index]
            else:
                MensagemBox().warning( 'Mensagem',"Impossivel realizar essa ação, por favor selecione um item da lista para excluir")


    def delContatoCargo(self):
        index = self.ui.tabCargos.currentRow()
        if self.editar == False:
            self.ui.tabCargos.removeRow(index)
            if index >= 0:
                self.cargoRemove.append(self.cargoAdd[index])
                del self.cargoAdd[index]
            else:
                MensagemBox().warning( 'Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickCargo()

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
        self.setEmpresa()
        if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtFantasia.text() != '' and self.ui.txtRazaoSocial.text() != '' and self.removerCaracter(self.ui.txtCnae.text()) != '' and self.ui.txtCnaeDescricao.text() != '':
            empresaDao = EmpresaDao()
            idPessoaJuridica = empresaDao.pesquisarPessoaJuridicaId(self.ui.txtCodigo.text())
            idCnae = empresaDao.pesquisarIdCnae(self.ui.txtCnae.text())
            empresa = Empresas(self.ui.txtCodigo.text(), None, idPessoaJuridica, self.idTipoEmpresa, idCnae, None, None, None, self.ui.txtInscricaoMunicipal.text(), None, None, None, None, None, None, None, None, None, None, 1)
            cad = empresaDao.cadastroEmpresa(empresa)
            self.idEmpresa = empresaDao.ultimoRegistro()


            if self.contatoAdd != []:
                self.cadastrarTelefone()

            if self.emailAdd != []:
                self.cadastrarEmail()

            if self.setoresAdd != []:
                self.cadastrarSetores()

            if self.cargoAdd != []:
                self.cadastrarCargo()

            if cad == True:
                MensagemBox().informacao('Mensagem', 'Cadastro realizado com sucesso!')
                self.cancelar()
        else:
            MensagemBox().warning( 'Atenção', "Preencha os campos obrigatorio")

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
            MensagemBox().warning( 'Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisa(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarEmpresa.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            razao = pesqui[1]
            fantasia = pesqui[2]
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
            subclasse = pesqui[15]

            # preenchendo o grid de pesquisa
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(razao)))
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
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
            self.__pesquisarEmpresa.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(subclasse))


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
        subclasse = itens[15]

        empresaDao = EmpresaDao()
        idPessoa = empresaDao.pesquisarPessoaCodigo(codigo)
        idPessoaJuridica = empresaDao.pesquisarPessoaJuridicaId(codigo)
        self.idCnae = empresaDao.pesquisarIdCnae(subclasse)
        desCnae = empresaDao.pesquisarCnaeDescricao(subclasse)

        __dados = Empresas(idPessoa, codigo, idPessoaJuridica, tipoEmpresa, self.removerCaracter(subclasse), desCnae, cnpj, insEstadual, insMunicipal, fantasia, razao, endereco, numero, complemento, bairro, None, cidade, estado, cep, situacao)
        self.botoesEditar()
        self.setCampos(__dados)
        self.pesquisarTelefone(codigo)
        self.pesquisaEmail(codigo)
        self.pesquisaSetor(codigo)
        self.pesquisaCargo(codigo)
        self.dialog.close()

    def setCampos(self, campos):
        self.setTipoEmpresa()
        self.ui.txtCodigo.setEnabled(False)
        self.ui.btnPesquisarEmpresa.setEnabled(False)
        self.idEmpresa = int(campos.getIdEmpresa)
        self.idPessoaJuridica = int(campos.getIdPessoaJuridica)
        self.ui.txtCodigo.setText(str(campos.getIdPessoa))
        self.ui.txtCnpj.setText(campos.getCnpj)
        self.ui.txtInscricaoEstadua.setText(campos.getInscricaoEstadual)
        self.ui.txtInscricaoMunicipal.setText(campos.getInscricaoMunicipal)
        self.ui.txtFantasia.setText(campos.getFantasia)
        self.ui.txtRazaoSocial.setText(campos.getRazaoSocial)
        self.ui.cBoxTipoEmpresa.setCurrentIndex(self.ui.cBoxTipoEmpresa.findText(campos.getTipoEmpresa))
        if campos.getSituacao == True:
            self.ui.radBtnAtivo.setChecked(True)
        else:
            self.ui.radBtnDesativo.setChecked(True)
        self.ui.txtCnae.setText(campos.getCnae)
        self.ui.txtCnaeDescricao.setText(campos.getDesCnae[0])
        self.editar = True

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
            MensagemBox().warning( 'Atenção', "Selecione uma das opções de pesquisa")


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

        __dados = PessoaJuridica(codigo, None, None, razao, fantasia, cnpj, inscricao, endereco, numero, complemento, bairro, None, cidade, estado, cep, site)
        self.setCamposJuridico(__dados)
        self.ativarCampos()
        self.dialogJuridico.close()

    def pesquisarTelefone(self, campos):
        empresaDao = EmpresaDao()
        id = empresaDao.pesquisaTelefone(campos)
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


    def setCamposJuridico(self, campos):
        self.ui.txtCodigo.setText(campos.getIdPessoa)
        self.ui.txtCnpj.setText(campos.getCnpj)
        self.ui.txtInscricaoEstadua.setText(campos.setInscricao)
        self.ui.txtFantasia.setText(campos.getFantasia)
        self.ui.txtRazaoSocial.setText(campos.getRazao)

    def pesquisaEmail(self, campos):
        empresaDao = EmpresaDao()
        id = empresaDao.pesquisaEmail(campos)
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

    def pesquisaSetor(self, campos):
        empresaDao = EmpresaDao()
        id = empresaDao.pesquisaSetor(campos)

        if id != []:

            self.setTabelaSetores(id)

    def setTabelaSetores(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabSetores.setRowCount(qtde_registros)
        linha = 0
        for pesqui in __retorno:
            idSetor = pesqui[0]
            setor = pesqui[1]
            self.ui.tabSetores.setItem(linha, 0, QtGui.QTableWidgetItem(str(setor)))
            lista = (idSetor, setor)
            self.setoresAdd.append(lista)

            linha += 1

    def pesquisaCargo(self, campos):
        empresaDao = EmpresaDao()
        id = empresaDao.pesquisaCargo(campos)

        if id != []:
            self.setTabelaCargo(id)

    def setTabelaCargo(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabCargos.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            idCargo = pesqui[0]
            cargos = pesqui[1]
            self.ui.tabCargos.setItem(linha, 0, QtGui.QTableWidgetItem(str(cargos)))
            lista = (idCargo, cargos)
            self.cargoAdd.append(lista)
            linha += 1


    def deletarTelefone(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.contatoRemove :
            a = self.contatoRemove[i]

            idTelefone = int(a[0])

            emp.deletarTelefone(idTelefone, self.idEmpresa)
            pesquisa = emp.pesquisaTelefoneEmpresa(idTelefone, self.idEmpresa)
            if pesquisa == "":
                emp.deletarContatoTelefone(idTelefone)

            i += 1

    def deletarEmail(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.emailRemove:
            a = self.emailRemove[i]

            idEmail = a[0]

            emp.deletarEmail(idEmail, self.idEmpresa)
            pesquisa = emp.pesquisaEmailEmpresa(idEmail, self.idEmpresa)
            if pesquisa == "":
                emp.deletarContatoEmail(idEmail)

            i += 1

    def deletarSetores(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.setoresRemove:

            a = self.setoresRemove[i]

            idSetor = str(a[0])

            emp.deletarSetor(idSetor, self.idEmpresa)

            i += 1

    def deletarCargos(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.cargoRemove:
            a = self.cargoRemove[i]
            idCargo = str(a[0])

            emp.deletarCargo(idCargo, self.idEmpresa)

            i += 1

    def atualizaTelefone(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.contatoAtualizar:
            a = self.contatoAtualizar[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, self.idEmpresa)
            emp.cadastrarTelefone(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarTelefoneEmpresa(id, self.idEmpresa)

            i += 1

    def atualizaEmail(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.emailAtualizar:
            a = self.emailAtualizar[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idEmpresa)
            emp.cadastrarEmail(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarEmailEmpresa(id, self.idEmpresa)

            i += 1

    def atualizaSetores(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.setoresAtualizar:
            a = self.setoresAtualizar[i]

            setor = a[0]

            __descricao = Setor(None, setor, self.idEmpresa)
            emp.cadastrarSetor(__descricao)

            i += 1

    def atualizaCargo(self):
        emp = EmpresaDao()
        i = 0
        for lista in self.cargoAtualizar:
            a = self.cargoAtualizar[i]

            cargo = a[0]

            __descricao = Cargo(None, cargo, self.idEmpresa)
            emp.cadastrarCargo(__descricao)

            i += 1

    def atualizar(self):
        if self.contatoRemove  != []:
            self.deletarTelefone()

        if self.emailRemove != []:
            self.deletarEmail()

        if self.setoresRemove != []:
            self.deletarSetores()

        if self.cargoRemove != []:
            self.deletarCargos()

        if self.contatoAtualizar != []:
            self.atualizaTelefone()

        if self.emailAtualizar != []:
            self.atualizaEmail()

        if self.setoresAtualizar != []:
            self.atualizaSetores()

        if self.cargoAtualizar != []:
            self.atualizaCargo()

        if self.ui.radBtnAtivo.isChecked():
            ativo = 1
        elif self.ui.radBtnDesativo.isChecked():
            ativo = 0

        empresaDao = EmpresaDao()
        empresa = Empresas(self.ui.txtCodigo.text(), self.idEmpresa, self.idPessoaJuridica, self.idTipoEmpresa, self.idCnae, None, None, None, self.ui.txtInscricaoMunicipal.text(), None, None, None, None, None, None, None, None, None, None, ativo)
        empresaDao.atualizarEmpresa(empresa)

        self.cancelar()



    def pesquisarCnae(self):
        self.dialogCnae = QDialog(self)
        self.__pesquisarCnae = Ui_frmPesquisarCnae()
        self.__pesquisarCnae.setupUi(self.dialogCnae)

        self.__pesquisarCnae.txtPesquisar.setValidator(self.validator)

        self.__pesquisarCnae.txtPesquisar.returnPressed.connect(self.pesquisarCodCnae)

        self.__pesquisarCnae.btnPesquisar.clicked.connect(self.pesquisarCodCnae)

        self.__pesquisarCnae.tabPesquisar.doubleClicked.connect(self.setarCamposCnae)

        self.dialogCnae.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogCnae.exec_()


    def pesquisarCodCnae(self):
        __empDao = EmpresaDao()
        if self.__pesquisarCnae.radBtnCodigo.isChecked():
            __codigo = self.__pesquisarCnae.txtPesquisar.text()
            __retorno = __empDao.pesquisarCnaeCodigo(__codigo)

            self.setarTabelaPesquisaCnae(__retorno)

        elif self.__pesquisarCnae.radBtnCodSubclasse.isChecked():
            __razao = self.__pesquisarCnae.txtPesquisar.text()
            __retorno = __empDao.pesquisarCnaeCodigoSubclasse(__razao)

            self.setarTabelaPesquisaCnae(__retorno)

        elif self.__pesquisarCnae.radBtnSecao.isChecked():
            __fantasia = self.__pesquisarCnae.txtPesquisar.text()
            __retorno = __empDao.pesquisarCnaeSecao(__fantasia)

            self.setarTabelaPesquisaCnae(__retorno)

        elif self.__pesquisarCnae.radBtnDivisao.isChecked():
            __cnpj = self.__pesquisarCnae.txtPesquisar.text()
            __retorno = __empDao.pesquisarCnaeDivisao(__cnpj)

            self.setarTabelaPesquisaCnae(__retorno)

        elif self.__pesquisarCnae.radBtnGrupo.isChecked():
            __inscricao = self.__pesquisarCnae.txtPesquisar.text()
            __retorno = __empDao.pesquisarCnaeGrupo(__inscricao)

            self.setarTabelaPesquisaCnae(__retorno)

        elif self.__pesquisarCnae.radBtnClasse.isChecked():
            __inscricao = self.__pesquisarCnae.txtPesquisar.text()
            __retorno = __empDao.pesquisarCnaeClasse(__inscricao)

            self.setarTabelaPesquisaCnae(__retorno)

        elif self.__pesquisarCnae.radBtnSubclasse.isChecked():
            __inscricao = self.__pesquisarCnae.txtPesquisar.text()
            __retorno = __empDao.pesquisarCnaeSubclasse(__inscricao)

            self.setarTabelaPesquisaCnae(__retorno)

        else:
            MensagemBox().warning( 'Atenção', "Selecione uma das opções de pesquisa")


    def setarTabelaPesquisaCnae(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarCnae.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            codSubclasse = pesqui[1]
            secao = pesqui[2]
            divisao = pesqui[3]
            grupo = pesqui[4]
            classe = pesqui[5]
            subclasse = pesqui[6]


            # preenchendo o grid de pesquisa
            self.__pesquisarCnae.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarCnae.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(codSubclasse)))
            self.__pesquisarCnae.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(secao)))
            self.__pesquisarCnae.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(divisao)))
            self.__pesquisarCnae.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(grupo)))
            self.__pesquisarCnae.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(classe)))
            self.__pesquisarCnae.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(subclasse)))

            linha += 1


    def setarCamposCnae(self):
        itens = []

        for item in self.__pesquisarCnae.tabPesquisar.selectedItems():
            itens.append(item.text())


        codigo = str(itens[1])
        descricao = str(itens[6])

        __dados = Cnae(codigo, descricao)
        self.setCamposCnae(__dados)
        self.dialogCnae.close()

    def setCamposCnae(self, campos):
        self.ui.txtCnae.setText(campos.getCodSubclasse)
        self.ui.txtCnaeDescricao.setText(campos.getSubclasse)
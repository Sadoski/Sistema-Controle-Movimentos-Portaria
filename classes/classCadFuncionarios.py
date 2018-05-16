import sys
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime, timedelta, time


from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetContatoEmail import ContatoEmail
from controller.getSetContatoTelefone import ContatoTelefone
from controller.getSetFuncionario import Funcionario
from controller.getSetPessoaFisica import PessoaFisica
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.funcionarioDao import FuncionarioDao
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from dao.setoresCargosDao import SetoresCargosDao
from telas.frmCadFuncionario import Ui_frmCadastroFuncionario
from telas.frmPesquisarPessoaFisica import Ui_frmPesquisarPessoaFisica


class CadastroFuncionario(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroFuncionario()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.addTableHorarios()
        self.idFuncionrio = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.editar = False
        self.contatoAdd = []
        self.contatoRemove = []
        self.contatoAtualizar = []
        self.emailAdd = []
        self.emailRemove = []
        self.emailAtualizar = []
        self.estadoCivil = []
        self.deficiencia = []
        self.categoriaTrabalho = []
        self.setor = []
        self.cargo = []
        self.jornada = []
        self.horarios = []

        self.ui.txtContatoEmail.setValidator(self.validator)
        self.ui.txtContatoTelefone.setValidator(self.validator)

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnSalvar.clicked.connect(self.getTime)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        #self.ui.btnEditar.clicked.connect(self.atualizar)
        self.ui.btnPesquisarPessoaFisica.clicked.connect(self.pesquisarPessoaFisica)



        self.ui.txtCodigo.returnPressed.connect(self.setPessoaFisica)
        self.ui.txtCodigo.editingFinished.connect(self.setPessoaFisicaEditFinish)

        self.ui.cBoxTabelaHorario.currentIndexChanged.connect(self.setTableHorarios)



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
        self.ui.grbDadosPessoaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)


        self.setEstadoCivil()
        self.setDeficiencia()
        self.setCategoriaTrabalho()
        self.setSetores()
        self.setCargo()
        self.setJornadaTrabalho()

    def botaoNovo(self):
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtNome.clear()
        self.ui.txtSobrenome.clear()

        self.ui.tabWiAdicionais.setEnabled(True)

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

    def ativarCampos(self):
        self.ui.tabWiAdicionais.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)


    def limparCampos(self):
        self.idFuncionrio = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.ui.txtCodigo.setEnabled(True)
        self.ui.btnPesquisarPessoaFisica.setEnabled(True)
        self.editar = False
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtNome.clear()
        self.ui.txtSobrenome.clear()

        self.ui.txtObservacao.clear()

        self.ui.txtNumCarteira.clear()
        self.ui.txtSerie.clear()
        self.ui.txtPis.clear()
        self.ui.txtDataAdmissao.setSpecialValueText("Null")

        self.ui.txtContatoTelefone.clear()
        self.ui.txtNumeroTelefone.clear()
        self.ui.txtEnderecoEmail.clear()
        self.ui.txtContatoEmail.clear()

        self.ui.cBoxEstadoCivil.clear()
        self.ui.cBoxDeficiencia.clear()
        self.ui.cBoxCateTrabalhador.clear()
        self.ui.cBoxCargo.clear()
        self.ui.cBoxSetor.clear()
        self.ui.cBoxTabelaHorario.clear()

        self.contatoAdd.clear()
        self.contatoRemove.clear()
        self.contatoAtualizar.clear()
        self.emailAdd.clear()
        self.emailRemove.clear()
        self.emailAtualizar.clear()
        self.estadoCivil.clear()
        self.categoriaTrabalho.clear()
        self.setor.clear()
        self.cargo.clear()
        self.jornada.clear()
        self.horarios.clear()

        self.deletarContatoTelefone()
        self.deletarContatoEmail()

        self.ui.tabWiAdicionais.setCurrentIndex(0)

        self.ui.radBtnAtivo.setCheckable(False)
        self.ui.radBtnDesativo.setCheckable(False)

    def deletarContatoTelefone(self):
        for i in reversed(range(self.ui.tabContatoTelefone.rowCount())):
            self.ui.tabContatoTelefone.removeRow(i)

    def deletarContatoEmail(self):
        for i in reversed(range(self.ui.tabContatoEmail.rowCount())):
            self.ui.tabContatoEmail.removeRow(i)

    def getTabe(self):
        for row in range(0, self.ui.tabHorario.rowCount()):
            semana = self.ui.tabHorario.item(row, 0).text()
            inicio = self.ui.tabHorario.cellWidget(row, 1).text()
            iniIntervalo = self.ui.tabHorario.cellWidget(row, 2).text()
            fimIntervalo = self.ui.tabHorario.cellWidget(row, 3).text()
            termino = self.ui.tabHorario.cellWidget(row, 4).text()

            self.horarios.append((semana, inicio, iniIntervalo, fimIntervalo, termino))


    def addTableHorarios(self):
        linha = 0
        for add in range(7):
            self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit())
            self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit())
            self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit())
            self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit())

            linha+=1

    def setTableHorarios(self):
        if self.ui.cBoxTabelaHorario.currentIndex() == 0:
           # 8 horas e mais 4 horas
            linha = 0
            for add in range(5):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(6,0,0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(11,0,0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(13,0,0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(16,48,0)))

                linha+=1

            linhas = 5
            for add in range(2):
                self.ui.tabHorario.setCellWidget(linhas , 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linhas , 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linhas , 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linhas , 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                linhas +=1

        elif self.ui.cBoxTabelaHorario.currentIndex() == 1:
            # 7 horas
            linha = 0
            for add in range(6):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(6, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(11, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(13, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(15, 0, 0)))

                linha += 1

            self.ui.tabHorario.setCellWidget(6, 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))


        elif self.ui.cBoxTabelaHorario.currentIndex() == 2:
            # 6 horas mais 40
            linha = 0
            for add in range(6):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(6, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(11, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(13, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(14, 40, 0)))

                linha += 1


            self.ui.tabHorario.setCellWidget(6, 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))

        elif self.ui.cBoxTabelaHorario.currentIndex() == 3:
            # 6 horas
            linha = 0
            for add in range(6):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(6, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(12, 0, 0)))

                linha += 1

            self.ui.tabHorario.setCellWidget(6, 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))

        elif self.ui.cBoxTabelaHorario.currentIndex() == 4:
            # 5 horas
            linha = 0
            for add in range(6):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(6, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(11, 0, 0)))

                linha += 1

            self.ui.tabHorario.setCellWidget(6, 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))

        elif self.ui.cBoxTabelaHorario.currentIndex() == 5:
            # 4 horas
            linha = 0
            for add in range(6):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(6, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(10, 0, 0)))

                linha += 1

            self.ui.tabHorario.setCellWidget(6, 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))

        elif self.ui.cBoxTabelaHorario.currentIndex() == 6:
            # 2 horas
            linha = 0
            for add in range(6):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(6, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(8, 0, 0)))

                linha += 1

            self.ui.tabHorario.setCellWidget(6, 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
            self.ui.tabHorario.setCellWidget(6, 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))

        elif self.ui.cBoxTabelaHorario.currentIndex() == 7:
            linha = 0
            for add in range(6):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                linha+=2

            linha = 1
            for add in range(6):
                self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(0, 0, 0)))
                linha += 2


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

    def setEstadoCivil(self):
        funcionario = FuncionarioDao()
        lista = funcionario.estadoCivil()

        self.estadoCivil.append(lista)
        for tipo in lista:
            self.ui.cBoxEstadoCivil.addItem(tipo[1])

    def setDeficiencia(self):
        funcionario = FuncionarioDao()
        lista = funcionario.deficiencia()

        self.deficiencia.append(lista)
        for tipo in lista:
            self.ui.cBoxDeficiencia.addItem(tipo[1])

    def setCategoriaTrabalho(self):
        funcionario = FuncionarioDao()
        lista = funcionario.categoriaTrabalho()

        self.categoriaTrabalho.append(lista)
        for tipo in lista:
            self.ui.cBoxCateTrabalhador.addItem(tipo[1])

    def setSetores(self):
        funcionario = FuncionarioDao()
        lista = funcionario.setores()

        self.setor.append(lista)
        for tipo in lista:
            self.ui.cBoxSetor.addItem(tipo[1])

    def setCargo(self):
        funcionario = FuncionarioDao()
        lista = funcionario.cargos()

        self.cargo.append(lista)
        for tipo in lista:
            self.ui.cBoxCargo.addItem(tipo[1])

    def setJornadaTrabalho(self):
        funcionario = FuncionarioDao()
        lista = funcionario.jornada()

        self.jornada.append(lista)
        for tipo in lista:
            self.ui.cBoxTabelaHorario.addItem(tipo[1])

    def setPessoaFisica(self):
        empresa = FuncionarioDao()
        em = empresa.pesquisarFuncionarioIdFisico(self.ui.txtCodigo.text())

        if em == []:
            emp = empresa.pesquisarPessoaFisica(self.ui.txtCodigo.text())

            if emp == []:
                MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro desta empresa")
                self.ui.txtCnpj.clear()
                self.ui.txtInscricaoEstadua.clear()
                self.ui.txtNome.clear()
                self.ui.txtSobrenome.clear()
            else:
                for empres in emp:
                    self.ui.txtCnpj.setText(str(empres[0]))
                    self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                    self.ui.txtNome.setText(str(empres[2]))
                    self.ui.txtSobrenome.setText(str(empres[3]))
        else:
            MensagemBox().warning( 'Mensagem', "Atenção já tem um cadastro desta pessoa")

    def setPessoaFisicaEditFinish(self):
        empresa = FuncionarioDao()
        em = empresa.pesquisarFuncionarioIdFisico(self.ui.txtCodigo.text())

        if em == []:
            emp = empresa.pesquisarPessoaFisica(self.ui.txtCodigo.text())

            if emp == []:
                self.ui.txtCnpj.clear()
                self.ui.txtInscricaoEstadua.clear()
                self.ui.txtNome.clear()
                self.ui.txtSobrenome.clear()
            else:
                for empres in emp:
                    self.ui.txtCnpj.setText(str(empres[0]))
                    self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                    self.ui.txtNome.setText(str(empres[2]))

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
        funcionario = FuncionarioDao()
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

        fun = funcionario.pesquisarFuncionarioFisico(codigo)
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

    def getIndexCivil(self):
        index = self.ui.cBoxEstadoCivil.currentIndex()

        for lista in self.estadoCivil:
            a = lista[index]
        idCivil = int(a[0])

        return idCivil

    def getIndexDeficiencia(self):
        index = self.ui.cBoxDeficiencia.currentIndex()

        for lista in self.deficiencia:
            a = lista[index]
        idDeficiencia = int(a[0])

        return idDeficiencia

    def getIndexCategoria(self):
        index = self.ui.cBoxCateTrabalhador.currentIndex()

        for lista in self.categoriaTrabalho:
            a = lista[index]
        idCategoria = int(a[0])

        return idCategoria

    def getIndexSetor(self):
        index = self.ui.cBoxSetor.currentIndex()

        for lista in self.setor:
            a = lista[index]
        idSetor = int(a[0])

        return idSetor

    def getIndexCargo(self):
        index = self.ui.cBoxCargo.currentIndex()

        for lista in self.cargo:
            a = lista[index]
        idCargo = int(a[0])

        return idCargo

    def getIndexJornada(self):
        index = self.ui.cBoxTabelaHorario.currentIndex()

        for lista in self.jornada:
            a = lista[index]
        idJornada = int(a[0])

        return idJornada

    def cadastrarTelefone(self):
        cli = FuncionarioDao()
        i = 0
        for lista in self.contatoAdd:
            a = self.contatoAdd[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, self.idCliente)
            cli.cadastrarTelefone(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarTelefoneFuncionario(id, self.idCliente)

            i += 1

    def cadastrarEmail(self):
        cli = FuncionarioDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idCliente)
            cli.cadastrarEmail(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarEmailFuncionario(id, self.idCliente)

            i += 1

    def getHoraMinutos(self, minutos, dias):
        hora, minuto, segundo = minutos
        segundos = timedelta(hours=hora, minutes=minuto, seconds=segundo).total_seconds()*dias
        return segundos//3600

    def getIntervalo(self, inicio, fim, intervalo):

        now = datetime.now()
        inicio = datetime(now.year, now.month, now.day, *inicio)
        fim = datetime(now.year, now.month, now.day, *fim)

        iHoras, iMinutos, iSegundos = intervalo

        intervalo = timedelta(hours=iHoras, minutes=iMinutos, seconds=iSegundos)

        while inicio <= fim:
            yield inicio.time()
            inicio += intervalo

    def convertTime(self, time):
        h = time[:2]
        m = time[3:5]
        s = time[6:8]

        return (int(h), int(m), int(s))


    def intervalo(self, inicio, fim, intervalo):
        lista = []
        for hora in self.getIntervalo(inicio, fim, intervalo):
            lista.append(hora)

        qtd = len(lista)
        qtd -= 1
        return qtd


    def getTime(self):
        self.getTabe()

        listaMatutino = []
        listaVespertino = []
        intervalo = (1, 0, 0)

        horario = []
        for horarios in self.horarios:
            inicio = self.convertTime(horarios[1])
            iniIntervalo = self.convertTime(horarios[2])
            fimIntervalo = self.convertTime(horarios[3])
            fim = self.convertTime(horarios[4])
            horario.append((inicio, iniIntervalo, fimIntervalo, fim))
        i=0
        segunda = int()
        terca = int()
        quarta = int()
        quinta = int()
        sexta = int()
        sabado = int()
        domingo = int()
        for a in range(7):
            h = horario[i]
            hora1 = self.intervalo(h[0], h[1], intervalo)
            if a == 0:
                segunda=hora1
            elif a == 1:
                terca=hora1
            elif a == 2:
                quarta=hora1
            elif a == 3:
                quinta=hora1
            elif a == 4:
                sexta=hora1
            elif a == 5:
                sabado=hora1
            elif a == 6:
                domingo=hora1
            i+=1

        segunda2 = int()
        terca2 = int()
        quarta2 = int()
        quinta2 = int()
        sexta2 = int()
        sabado2 = int()
        domingo2 = int()
        i=0
        for a in range(7):
            h = horario[i]
            hora2 = self.intervalo(h[2], h[3], intervalo)
            if a == 0:
                segunda2 = hora2
            elif a == 1:
                terca2 = hora2
            elif a == 2:
                quarta2 = hora2
            elif a == 3:
                quinta2 = hora2
            elif a == 4:
                sexta2 = hora2
            elif a == 5:
                sabado2 = hora2
            elif a == 6:
                domingo2 = hora2
            i += 1


        listaDia = []
        for dia in self.horarios:
            h1, m1, s1 = self.convertTime(dia[1])
            h2, m2, s2 = self.convertTime(dia[2])
            h3, m3, s3 = self.convertTime(dia[3])
            h4, m4, s4 = self.convertTime(dia[4])

            if h1 != 0 or m1 != 0 or s1 != 0 and h2 != 0 or m2 != 0 or s2 != 0 and h3 != 0 or m3 != 0 or s3 != 0 and h4 != 0 or m4 != 0 or s4 != 0:
                listaDia.append("DIA DE TRABALHO")

        dia = len(listaDia)

        seg = (segunda + segunda2)*dia
        ter = (terca + terca2)*dia
        qua = (quarta + quarta2)*dia
        qui = (quinta + quinta2)*dia
        sex = (sexta + sexta2)*dia
        sab = (sabado + sabado2)*dia
        dom = (domingo + domingo2)*dia

        print(seg)








    def cadastrar(self):
        if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtNome.text() != '' and self.ui.txtSobrenome.text() != '' and self.ui.txtNumCarteira.text() != '' and self.ui.txtSerie.text() != '' and self.ui.txtUf.text() != '' and self.ui.txtPis.text() != '':
            funcionarioDao = FuncionarioDao()
            idPessoa = funcionarioDao.pesquisarPessoaFisico(self.ui.txtCodigo.text())
            idCivil = self.getIndexCivil()
            idDeficiencia = self.getIndexDeficiencia()
            idCategoria = self.getIndexCategoria()
            idSetor = self.getIndexSetor()
            idCargo = self.getIndexCargo()
            idJornada = self.getIndexJornada()
            funcionario = Funcionario(None, idPessoa, self.ui.txtCodigo.text, self.ui.txtCnpj.text(), self.ui.txtInscricaoEstadua.text(), self.ui.txtNome.text(), self.ui.txtSobrenome.text(), self.ui.txtObservacao.toPlainText(), 1, idCivil, idDeficiencia, idCategoria, idSetor, idCargo, idJornada, self.ui.txtDataAdmissao.text(), self.ui.txtDataDemissao.text(), self.ui.txtDataEmissao.text())

            funcionarioDao.cadastrarFuncionarioFisico(funcionario)
            self.idFuncionrio = funcionarioDao.ultimoRegistro()

            if self.contatoAdd != []:
                self.cadastrarTelefone()

            if self.emailAdd != []:
                self.cadastrarEmail()

            self.cancelar()
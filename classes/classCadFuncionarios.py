import sys
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime, timedelta


from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetContatoEmail import ContatoEmail
from controller.getSetContatoTelefone import ContatoTelefone
from controller.getSetFuncionario import Funcionario
from controller.getSetPessoaFisica import PessoaFisica
from dao.funcionarioDao import FuncionarioDao
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from telas.frmCadFuncionario import Ui_frmCadastroFuncionario
from telas.frmPesquisarFuncionario import Ui_frmPesquisarFuncionario
from telas.frmPesquisarPessoaFisica import Ui_frmPesquisarPessoaFisica


class CadastroFuncionario(QtGui.QDialog):
    def __init__(self, cadatra, cancela, deleta, edita):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroFuncionario()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.addTableHorarios()
        self.idFuncionrio = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.idJornada = int()
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
        self.cada = cadatra
        self.canc = cancela
        self.dele = deleta
        self.edit = edita

        self.ui.btnNovo.setEnabled(self.cada)

        self.ui.txtContatoEmail.setValidator(self.validator)
        self.ui.txtContatoTelefone.setValidator(self.validator)
        self.ui.txtUf.setValidator(self.validator)

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnEditar.clicked.connect(self.atualizar)
        self.ui.btnDeletar.clicked.connect(self.deletar)
        self.ui.btnPesquisarPessoaFisica.clicked.connect(self.pesquisarPessoaFisica)
        self.ui.radBtnDesativo.clicked.connect(self.btnDesativar)
        self.ui.radBtnAtivo.clicked.connect(self.btnAtivo)

        self.ui.txtCodigo.returnPressed.connect(self.setPessoaFisica)
        self.ui.txtCodigo.editingFinished.connect(self.setPessoaFisicaEditFinish)

        self.ui.cBoxTabelaHorario.currentIndexChanged.connect(self.setTableHorarios)

        self.ui.txtCodigo.textChanged.connect(self.numberCodigo)
        self.ui.txtNumCarteira.textChanged.connect(self.numberCarteira)
        self.ui.txtSerie.textChanged.connect(self.numberSerie)
        self.ui.txtPis.textChanged.connect(self.numberPis)
        self.ui.txtNumeroTelefone.textChanged.connect(self.numberTelefone)
        self.ui.txtObservacao.textChanged.connect(self.textEdite)
        self.ui.txtDataAdmissao.textChanged.connect(self.changeDataAdimissao)
        self.ui.txtDataDemissao.textChanged.connect(self.changeDataDemissao)
        self.ui.txtDataEmissao.textChanged.connect(self.changeDataEmissao)

        self.ui.txtDataAdmissao.cursorPositionChanged.connect(self.positionCursorDataAdmissao)
        self.ui.txtDataDemissao.cursorPositionChanged.connect(self.positionCursorDataDemissao)
        self.ui.txtDataEmissao.cursorPositionChanged.connect(self.positionCursorDataEmissao)

        self.ui.btnAddTelefone.clicked.connect(self.addContatoTelefone)
        self.ui.btnRemoverTelefone.clicked.connect(self.delContatoTelefone)

        self.ui.btnAddEmail.clicked.connect(self.addContatoEmail)
        self.ui.btnRemoverEmail.clicked.connect(self.delContatoEmail)


    def btnDesativar(self):
        self.ui.txtDataDemissao.setEnabled(True)

    def btnAtivo(self):
        self.ui.txtDataAdmissao.clear()
        self.ui.txtDataAdmissao.setEnabled(True)

    def numberCodigo(self):
        if self.ui.txtCodigo.text().isnumeric() == False:
            self.ui.txtCodigo.backspace()

    def numberCarteira(self):
        if self.ui.txtNumCarteira.text().isnumeric() == False:
            self.ui.txtNumCarteira.backspace()

    def numberSerie(self):
        if self.ui.txtSerie.text().isnumeric() == False:
            self.ui.txtSerie.backspace()

    def numberPis(self):
        if self.ui.txtPis.text().isnumeric() == False:
            self.ui.txtPis.backspace()

    def numberTelefone(self):
        if self.ui.txtNumeroTelefone.text().isnumeric() == False:
            self.ui.txtNumeroTelefone.backspace()

    def textEdite(self):
        if (len(self.ui.txtObservacao.toPlainText()) > 255):
            self.ui.txtObservacao.textCursor().deletePreviousChar()

    def positionCursorDataAdmissao(self):
        texto = self.removerCaracter(self.ui.txtDataAdmissao.text())
        if len(texto) == 0:
            self.ui.txtDataAdmissao.setCursorPosition(0)
        elif len(texto) <= 1:
            b = len(texto)
            self.ui.txtDataAdmissao.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) < 4:
            b = len(texto) + 1
            self.ui.txtDataAdmissao.setCursorPosition(b)
        elif len(texto) >= 4 and len(texto) < 9:
            b = len(texto) + 2
            self.ui.txtDataAdmissao.setCursorPosition(b)

    def positionCursorDataDemissao(self):
        texto = self.removerCaracter(self.ui.txtDataDemissao.text())
        if len(texto) == 0:
            self.ui.txtDataDemissao.setCursorPosition(0)
        elif len(texto) <= 1:
            b = len(texto)
            self.ui.txtDataDemissao.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) < 4:
            b = len(texto) + 1
            self.ui.txtDataDemissao.setCursorPosition(b)
        elif len(texto) >= 4 and len(texto) < 9:
            b = len(texto) + 2
            self.ui.txtDataDemissao.setCursorPosition(b)

    def positionCursorDataEmissao(self):
        texto = self.removerCaracter(self.ui.txtDataEmissao.text())
        if len(texto) == 0:
            self.ui.txtDataEmissao.setCursorPosition(0)
        elif len(texto) <= 1:
            b = len(texto)
            self.ui.txtDataEmissao.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) < 4:
            b = len(texto) + 1
            self.ui.txtDataEmissao.setCursorPosition(b)
        elif len(texto) >= 4 and len(texto) < 9:
            b = len(texto) + 2
            self.ui.txtDataEmissao.setCursorPosition(b)

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

    def changeDataAdimissao(self):
        if self.changeData(self.ui.txtDataAdmissao.text()) == False:
            self.ui.txtDataAdmissao.clear()

    def changeDataDemissao(self):
        if self.changeData(self.ui.txtDataDemissao.text()) == False:
            self.ui.txtDataDemissao.clear()

    def changeDataEmissao(self):
        if self.changeData(self.ui.txtDataEmissao.text()) == False:
            self.ui.txtDataEmissao.clear()

    def changeData(self, data):
        if len(str(self.removerCaracter(data))) ==2 and int(data[:2]) >31:
            self.mensagem.warning('Mensagem', "Atenção dia inexitente")
            return False
        elif len(str(self.removerCaracter(data))) == 4 and int(data[3:5]) >12:
            self.mensagem.warning('Mensagem', "Atenção mes inexitente")
            return False
        elif len(str(self.removerCaracter(data))) == 4 and data[3:5] == "02" and int(data[:2]) >28:
            self.mensagem.warning('Mensagem', "Atenção mes com menos dias")
            return False
        elif len(str(self.removerCaracter(data))) == 8 and int(data[6:10]) <1500:
            self.mensagem.warning('Mensagem', "Atenção ano muito antigo")
            return False

    def novo(self):
        self.limparCampos()
        self.ui.grbDadosPessoaJuridica.setEnabled(self.cada)
        self.ui.tabWiAdicionais.setEnabled(self.cada)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(self.cada)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(self.canc)
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
        self.ui.btnNovo.setEnabled(self.cada)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def botoesEditar(self):
        self.limparCampos()
        self.ui.grbAtivo.setEnabled(self.edit)
        self.ui.radBtnAtivo.setCheckable(self.edit)
        self.ui.radBtnDesativo.setCheckable(self.edit)
        self.ui.tabWiAdicionais.setEnabled(self.edit)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(self.edit)
        self.ui.btnCancelar.setEnabled(self.canc)
        self.ui.btnDeletar.setEnabled(self.dele)

        self.setSetores()
        self.setCargo()
        self.setJornadaTrabalho()
        self.setCategoriaTrabalho()
        self.setEstadoCivil()
        self.setDeficiencia()

    def ativarCampos(self):
        self.ui.tabWiAdicionais.setEnabled(self.cada)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(self.cada)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(self.canc)
        self.ui.btnDeletar.setEnabled(False)


    def limparCampos(self):
        self.idFuncionrio = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.idJornada = int()
        self.ui.txtCodigo.setEnabled(True)
        self.ui.btnPesquisarPessoaFisica.setEnabled(True)
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtNome.clear()
        self.ui.txtSobrenome.clear()

        self.ui.txtObservacao.clear()

        self.ui.txtDataAdmissao.clear()
        self.ui.txtDataDemissao.clear()
        self.ui.txtNumCarteira.clear()
        self.ui.txtSerie.clear()
        self.ui.txtUf.clear()
        self.ui.txtDataEmissao.clear()
        self.ui.txtPis.clear()

        self.ui.txtContatoTelefone.clear()
        self.ui.txtNumeroTelefone.clear()
        self.ui.txtEnderecoEmail.clear()
        self.ui.txtContatoEmail.clear()

        self.ui.cBoxEstadoCivil.clear()
        self.ui.cBoxDeficiencia.clear()
        self.ui.cBoxCateTrabalhador.clear()
        self.ui.cBoxTabelaHorario.clear()
        self.ui.cBoxSetor.clear()
        self.ui.cBoxCargo.clear()


        self.contatoAdd.clear()
        self.contatoRemove.clear()
        self.contatoAtualizar.clear()
        self.emailAdd.clear()
        self.emailRemove.clear()
        self.emailAtualizar.clear()
        self.estadoCivil.clear()
        self.deficiencia.clear()
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
        self.editar = False

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
                MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro desta pessoa")
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
                    self.ui.txtSobrenome.setText(str(empres[3]))

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

            __descricao = ContatoTelefone(None, contato, telefone, self.idFuncionrio)
            cli.cadastrarTelefone(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarTelefoneFuncionario(id, self.idFuncionrio)

            i += 1

    def cadastrarEmail(self):
        cli = FuncionarioDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idFuncionrio)
            cli.cadastrarEmail(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarEmailFuncionario(id, self.idFuncionrio)

            i += 1

    def getHoraMinutos(self, minutos, dias):
        hora, minuto, segundo = minutos
        segundos = timedelta(hours=hora, minutes=minuto, seconds=segundo).total_seconds()*dias
        return segundos//3600


    def convertTime(self, time):
        h = time[:2]
        m = time[3:5]
        s = time[6:8]
        return (int(h), int(m), int(s))

    def convertTimeReal(self, time):
        t = str(time)

        if len(t) == 7:
            h = time[:1]
            m = time[2:4]
            s = time[5:7]
            return (int(h), int(m), int(s))
        else:
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

        segundaH = int()
        segundaM = int()
        segundaS = int()
        tercaH= int()
        tercaM= int()
        tercaS = int()
        quartaH= int()
        quartaM= int()
        quartaS = int()
        quintaH= int()
        quintaM= int()
        quintaS = int()
        sextaH= int()
        sextaM= int()
        sextaS = int()
        sabadoH= int()
        sabadoM= int()
        sabadoS = int()
        domingoH= int()
        domingoM= int()
        domingoS = int()

        dias = []

        i= 0
        for dia in self.horarios:
            h1, m1, s1 = self.convertTime(dia[1])
            h2, m2, s2 = self.convertTime(dia[2])
            h3, m3, s3 = self.convertTime(dia[3])
            h4, m4, s4 = self.convertTime(dia[4])
            
            time1 = (timedelta(hours=h1, minutes=m1, seconds=s1))
            time2 = (timedelta(hours=h2, minutes=m2, seconds=s2))
            time3 = (timedelta(hours=h3, minutes=m3, seconds=s3))
            time4 = (timedelta(hours=h4, minutes=m4, seconds=s4))

            turno1 = (time2-time1)
            turno2 = (time4-time3)
            total = turno1+turno2
            dias.append(str(total))

            i +=1

        index = 0
        for d in dias:
            h1, m1, s1 = self.convertTimeReal(str(dias[index]))

            if index  == 0:
                segundaH = h1
                segundaM = m1
                segundaS = s1
            elif index  == 1:
                tercaH = h1
                tercaM = m1
                tercaS = s1
            elif index  == 2:
                quartaH = h1
                quartaM = m1
                quartaS = s1
            elif index  == 3:
                quintaH = h1
                quintaM = m1
                quintaS = s1
            elif index  == 4:
                sextaH = h1
                sextaM = m1
                sextaS = s1
            elif index  == 5:
                sabadoH = h1
                sabadoM = m1
                sabadoS = s1
            elif index  == 6:
                domingoH = h1
                domingoM = m1
                domingoS = s1
            index +=1


        hhs = (segundaH+tercaH+quartaH+quintaH+sextaH+sabadoH+domingoH)
        mms = (segundaM+tercaM+quartaM+quintaM+sextaM+sabadoM+domingoM)
        sss = (segundaS+tercaS+quartaS+quintaS+sextaS+sabadoS+domingoS)
        hor, min, seg = self.convertTimeReal(str(timedelta(minutes=mms, seconds=sss)))

        timeFinal  = hhs+hor+min+seg
        self.horarios.clear()
        dias.clear()



        if self.ui.cBoxTabelaHorario.currentIndex() == 0 and timeFinal != 44:
            self.mensagem.warning('Atenção', "Quantidade de horas não equivale as 44h selecionada em Carga Horaria, total de " + str(hhs + hor) + ":" + str(min) + ":" + str(seg))
            return False
        elif self.ui.cBoxTabelaHorario.currentIndex() == 1 and timeFinal != 42:
            self.mensagem.warning('Atenção', "Quantidade de horas não equivale as 42h selecionada em Carga Horaria, total de " + str(hhs + hor) + ":" + str(min) + ":" + str(seg))
            return False
        elif self.ui.cBoxTabelaHorario.currentIndex() == 2 and timeFinal != 40:
            self.mensagem.warning('Atenção', "Quantidade de horas não equivale as 40h selecionada em Carga Horaria, total de " + str(hhs + hor) + ":" + str(min) + ":" + str(seg))
            return False
        elif self.ui.cBoxTabelaHorario.currentIndex() == 3 and timeFinal != 36:
            self.mensagem.warning('Atenção', "Quantidade de horas não equivale as 36h selecionada em Carga Horaria, total de " + str(hhs + hor) + ":" + str(min) + ":" + str(seg))
            return False
        elif self.ui.cBoxTabelaHorario.currentIndex() == 4 and timeFinal != 30:
            self.mensagem.warning('Atenção', "Quantidade de horas não equivale as 30h selecionada em Carga Horaria, total de " + str(hhs + hor) + ":" + str(min) + ":" + str(seg))
            return False
        elif self.ui.cBoxTabelaHorario.currentIndex() == 5 and timeFinal != 24:
            self.mensagem.warning('Atenção', "Quantidade de horas não equivale as 24h selecionada em Carga Horaria, total de " + str(hhs + hor) + ":" + str(min) + ":" + str(seg))
            return False
        elif self.ui.cBoxTabelaHorario.currentIndex() == 6 and timeFinal != 12:
            self.mensagem.warning('Atenção', "Quantidade de horas não equivale as 12h selecionada em Carga Horaria, total de " + str(hhs + hor) + ":" + str(min) + ":" + str(seg))
            return False
        else:
            return True

    def cadastrarHorarios(self):
        for row in range(0, self.ui.tabHorario.rowCount()):
            semana = self.ui.tabHorario.item(row, 0).text()
            inicio = self.ui.tabHorario.cellWidget(row, 1).text()
            iniIntervalo = self.ui.tabHorario.cellWidget(row, 2).text()
            fimIntervalo = self.ui.tabHorario.cellWidget(row, 3).text()
            termino = self.ui.tabHorario.cellWidget(row, 4).text()

            funcionarioDao = FuncionarioDao()
            funcionarioDao.cadastrarHorarios(semana, inicio, iniIntervalo, fimIntervalo, termino, self.idJornada, self.idFuncionrio)

    def converterData(self, data):
        if len(self.removerCaracter(data)) == 8:
            dia = data[:2]
            mes = data[3:5]
            ano = data[6:10]
            return ("%s%s%s"%(ano,mes,dia))
        elif len(self.removerCaracter(data)) > 0 and len(self.removerCaracter(data)) <8:
            self.mensagem.warning('Atenção', "Data invalidas, por favor insira uma data valida")

    def cadastrar(self):
        if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtNome.text() != '' and self.ui.txtSobrenome.text() != '' and self.ui.txtNumCarteira.text() != '' and self.ui.txtSerie.text() != '' and self.ui.txtUf.text() != '' and self.ui.txtPis.text() != '' and len(self.removerCaracter(self.ui.txtDataEmissao.text())) != '' and len(self.removerCaracter(self.ui.txtDataAdmissao.text())) != '' :
            if self.getTime() == True:
                funcionarioDao = FuncionarioDao()
                idPessoa = funcionarioDao.pesquisarPessoaFisico(self.ui.txtCodigo.text())
                idCivil = self.getIndexCivil()
                idDeficiencia = self.getIndexDeficiencia()
                idCategoria = self.getIndexCategoria()
                idSetor = self.getIndexSetor()
                idCargo = self.getIndexCargo()
                self.idJornada = self.getIndexJornada()
                funcionario = Funcionario(None, idPessoa, self.ui.txtCodigo.text, self.ui.txtCnpj.text(), self.ui.txtInscricaoEstadua.text(), self.ui.txtNome.text(), self.ui.txtSobrenome.text(), self.ui.txtObservacao.toPlainText(), 1, idCivil, idDeficiencia, idCategoria, idSetor, idCargo, self.idJornada, self.converterData(self.ui.txtDataAdmissao.text()), self.converterData(self.ui.txtDataDemissao.text()), self.ui.txtNumCarteira.text(), self.ui.txtPis.text(), self.ui.txtSerie.text(), self.ui.txtUf.text(), self.converterData(self.ui.txtDataEmissao.text()))

                funcionarioDao.cadastrarFuncionarioFisico(funcionario)
                self.idFuncionrio = funcionarioDao.ultimoRegistro()

                self.cadastrarHorarios()

                if self.contatoAdd != []:
                    self.cadastrarTelefone()

                if self.emailAdd != []:
                    self.cadastrarEmail()

                self.cancelar()
        else:
            self.mensagem.warning('Atenção',"Por Favor preencha os campos obrigatorios")

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialog = QDialog(self)
            self.__pesquisarPessoa =  Ui_frmPesquisarFuncionario()
            self.__pesquisarPessoa.setupUi(self.dialog)

            self.__pesquisarPessoa.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisarPessoa.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisarPessoa.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        if self.__pesquisarPessoa.radBtnCodigo.isChecked():
            __nome = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioCodigo(__nome)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnNome.isChecked():
            __nome = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioNome(__nome)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtncPF.isChecked():
            __cpf= self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioCPF(__cpf)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnRg.isChecked():
            __rg = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioRg(__rg)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnNumCarteira.isChecked():
            __mae = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioNumCarteira(__mae)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnPis.isChecked():
            __pai = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = FuncionarioDao()
            __retorno = __pesDao.pesquisarFuncionarioPis(__pai)

            self.setarTabelaPesquisa(__retorno)

        else:
            MensagemBox().warning('Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisa(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarPessoa.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            segundoNome = pesqui[2]
            cpf = pesqui[3]
            rg = pesqui[4]
            expeditor = pesqui[5]
            uf = pesqui[6]
            data = pesqui[7]
            sexo = pesqui[8]
            endereco = pesqui[9]
            numero = pesqui[10]
            complemento = pesqui[11]
            bairro = pesqui[12]
            mae = pesqui[13]
            pai = pesqui[14]
            cidade = pesqui[15]
            estado = pesqui[16]
            cep = pesqui[17]
            admissao = pesqui[18]
            demissao = pesqui[19]
            carteira = pesqui[20]
            serie = pesqui[21]
            uff = pesqui[22]
            emissao = pesqui[23]
            pis = pesqui[24]
            civil = pesqui[25]
            deficiencia = pesqui[26]
            categoria = pesqui[27]
            setor = pesqui[28]
            cargo = pesqui[29]
            obs =pesqui[30]
            jornada = pesqui[31]
            if pesqui[32] == 1:
                situacao = "Ativo"
            else:
                situacao = "Desativo"



            # preenchendo o grid de pesquisa
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(segundoNome)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(data)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(sexo)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(mae)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(pai)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(admissao)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 19, QtGui.QTableWidgetItem(str(demissao)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 20, QtGui.QTableWidgetItem(str(carteira)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 21, QtGui.QTableWidgetItem(str(serie)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 22, QtGui.QTableWidgetItem(str(uff)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 23, QtGui.QTableWidgetItem(str(emissao)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 24, QtGui.QTableWidgetItem(str(pis)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 25, QtGui.QTableWidgetItem(str(civil)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 26, QtGui.QTableWidgetItem(str(deficiencia)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 27, QtGui.QTableWidgetItem(str(categoria)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 28, QtGui.QTableWidgetItem(str(cargo)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 29, QtGui.QTableWidgetItem(str(setor)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 30, QtGui.QTableWidgetItem(str(obs)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 31, QtGui.QTableWidgetItem(str(jornada)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 32, QtGui.QTableWidgetItem(str(situacao)))

            linha += 1

    def setarCampos(self):
        funcionarioDao = FuncionarioDao()
        itens = []

        for item in self.__pesquisarPessoa.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = itens[0]
        nome = itens[1]
        sobrenome = itens[2]
        cpf = itens[3]
        rg = itens[4]
        expeditor = itens[5]
        uf = itens[6]
        data = itens[7]
        sexo = itens[8]
        endereco = itens[9]
        numero = itens[10]
        complemento = itens[11]
        bairro = itens[12]
        mae = itens[13]
        pai = itens[14]
        cidade = itens[15]
        estado = itens[16]
        cep = itens[17]
        admissao = itens[18]
        demissao = itens[19]
        carteira = itens[20]
        serie = itens[21]
        uff = itens[22]
        emissao = itens[23]
        pis = itens[24]
        civil = itens[25]
        deficiencia = itens[26]
        categoria = itens[27]
        setor = itens[28]
        cargo = itens[29]
        obs = itens[30]
        jornada = itens[31]
        if itens[32] == 'Ativo':
            situacao = True
        else:
            situacao = False


        idPessoa = funcionarioDao.pesquisarPessoaCodigo(codigo)
        idPessoaFisico = funcionarioDao.pesquisarPessoaFisicaId(idPessoa)

        __dados = Funcionario(codigo, idPessoa, idPessoaFisico, cpf, rg, nome, sobrenome, obs, situacao, civil, deficiencia, categoria, setor, cargo, jornada, admissao, demissao, carteira, pis, serie, uf,  emissao)
        self.botoesEditar()
        self.setCampos(__dados)
        self.pesquisarTelefone(codigo)
        self.pesquisaEmail(codigo)
        self.pesquisaHorarios(codigo)
        self.dialog.close()

    def retornoData(self, data):
            ano = data[:4]
            mes = data[5:7]
            dia = data[8:10]
            return '%s%s%s'%(str(dia),str(mes),str(ano))

    def setCampos(self, campos):
        self.ui.txtCodigo.setEnabled(False)

        self.idFuncionrio = int(campos.getIdFuncionario)
        self.idPessoa = int(campos.getIdPessoa)
        self.ui.txtCodigo.setText(str(campos.getIdPessoaFisica))
        self.ui.txtCnpj.setText(campos.getCpf)
        self.ui.txtInscricaoEstadua.setText(campos.getRg)
        self.ui.txtNome.setText(campos.getNome)
        self.ui.txtSobrenome.setText(campos.getSobrenome)

        self.ui.cBoxEstadoCivil.setCurrentIndex(self.ui.cBoxEstadoCivil.findText(campos.getCivil))
        self.ui.cBoxDeficiencia.setCurrentIndex(self.ui.cBoxDeficiencia.findText(campos.getDeficiencia))
        if campos.getSituacao == True:
            self.ui.radBtnAtivo.setChecked(True)
        else:
            self.ui.radBtnDesativo.setChecked(True)

        self.ui.txtObservacao.setText(str(campos.getObservacao))
        self.ui.cBoxCateTrabalhador.setCurrentIndex(self.ui.cBoxCateTrabalhador.findText(campos.getCategoria))
        self.ui.cBoxSetor.setCurrentIndex(self.test(campos.getCargo))
        self.ui.cBoxCargo.setCurrentIndex(self.ui.cBoxCargo.findText(campos.getSetor))


        self.ui.txtDataAdmissao.setText(self.retornoData(campos.getAdmissao))
        self.ui.txtDataDemissao.setText(self.retornoData(campos.getDemissao))
        self.ui.txtNumCarteira.setText(campos.getNumCarteira)
        self.ui.txtSerie.setText(campos.getSerie)
        self.ui.txtUf.setText(campos.getUf)
        self.ui.txtDataEmissao.setText(self.retornoData(campos.getEmissao))
        self.ui.txtPis.setText(campos.getPis)
        self.ui.cBoxTabelaHorario.setCurrentIndex(self.ui.cBoxTabelaHorario.findText(campos.getJornada))


        self.editar = True


    def pesquisarTelefone(self, campos):
        funcionarioDao = FuncionarioDao()
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
        funcionarioDao = FuncionarioDao()
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

    def pesquisaHorarios(self, campos):
        funcionarioDao = FuncionarioDao()
        id = funcionarioDao.pesquisaHorarios(campos)
        if id != []:

            self.setTabHorarios(id)

    def retornoHoras(self, dado):
        if len( dado) == 7:
            h =  dado[:1]
            m =  dado[2:4]
            s =  dado[5:7]
            return (int(h), int(m), int(s))
        else:
            h =  dado[:2]
            m =  dado[3:5]
            s =  dado[6:8]
            return (int(h), int(m), int(s))

    def setTabHorarios(self, __retorno):
        linha=0
        for pesqui in __retorno:
            h1, m1, s1 = self.retornoHoras(str(pesqui[1]))
            h2, m2, s2 = self.retornoHoras(str(pesqui[2]))
            h3, m3, s3 = self.retornoHoras(str(pesqui[3]))
            h4, m4, s4 = self.retornoHoras(str(pesqui[4]))

            self.ui.tabHorario.setCellWidget(linha, 1, QtGui.QTimeEdit(QtCore.QTime(h1, m1, s1)))
            self.ui.tabHorario.setCellWidget(linha, 2, QtGui.QTimeEdit(QtCore.QTime(h2, m2, s2)))
            self.ui.tabHorario.setCellWidget(linha, 3, QtGui.QTimeEdit(QtCore.QTime(h3, m3, s3)))
            self.ui.tabHorario.setCellWidget(linha, 4, QtGui.QTimeEdit(QtCore.QTime(h4, m4, s4)))

            linha+=1

    def deletarTelefone(self):
        emp = FuncionarioDao()
        i = 0
        for lista in self.contatoRemove :
            a = self.contatoRemove[i]

            idTelefone = int(a[0])

            emp.deletarTelefone(idTelefone, self.idFuncionrio)
            pesquisa = emp.pesquisaTelefoneFuncionario(idTelefone, self.idFuncionrio)
            if pesquisa == "":
                emp.deletarContatoTelefone(idTelefone)

            i += 1

    def deletarEmail(self):
        emp = FuncionarioDao()
        i = 0
        for lista in self.emailRemove:
            a = self.emailRemove[i]

            idEmail = a[0]

            emp.deletarEmail(idEmail, self.idFuncionrio)
            pesquisa = emp.pesquisaEmailFuncionario(idEmail, self.idFuncionrio)
            if pesquisa == "":
                emp.deletarContatoEmail(idEmail)

            i += 1

    def atualizaTelefone(self):
        emp = FuncionarioDao()
        i = 0
        for lista in self.contatoAtualizar:
            a = self.contatoAtualizar[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, self.idFuncionrio)
            emp.cadastrarTelefone(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarTelefoneFuncionario(id, self.idFuncionrio)

            i += 1

    def atualizaEmail(self):
        emp = FuncionarioDao()
        i = 0
        for lista in self.emailAtualizar:
            a = self.emailAtualizar[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idFuncionrio)
            emp.cadastrarEmail(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarEmailFuncionario(id, self.idFuncionrio)

            i += 1

    def atualizar(self):
        if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtNome.text() != '' and self.ui.txtSobrenome.text() != '' and self.ui.txtNumCarteira.text() != '' and self.ui.txtSerie.text() != '' and self.ui.txtUf.text() != '' and self.ui.txtPis.text() != '' and len(self.removerCaracter(self.ui.txtDataEmissao.text())) != '' and len(self.removerCaracter(self.ui.txtDataAdmissao.text())) != '' :
            if self.ui.radBtnDesativo.isChecked() and len(self.removerCaracter(self.ui.txtDataDemissao.text())) != '':
                self.mensagem.warning('Atenção', "Por Favor preencha os campos obrigatorios")
            else:
                if self.getTime() == True:
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


                    idCivil = self.getIndexCivil()
                    idDeficiencia = self.getIndexDeficiencia()
                    idCategoria = self.getIndexCategoria()
                    idSetor = self.getIndexSetor()
                    idCargo = self.getIndexCargo()
                    self.idJornada = self.getIndexJornada()

                    funcionarioDao = FuncionarioDao()
                    funcionario = Funcionario(self.idFuncionrio, self.idPessoa, self.ui.txtCodigo.text, self.ui.txtCnpj.text(), self.ui.txtInscricaoEstadua.text(), self.ui.txtNome.text(), self.ui.txtSobrenome.text(), self.ui.txtObservacao.toPlainText(), ativo, idCivil, idDeficiencia, idCategoria, idSetor, idCargo, self.idJornada, self.converterData(self.ui.txtDataAdmissao.text()), self.converterData(self.ui.txtDataDemissao.text()), self.ui.txtNumCarteira.text(), self.ui.txtPis.text(), self.ui.txtSerie.text(), self.ui.txtUf.text(), self.converterData(self.ui.txtDataEmissao.text()))
                    funcionarioDao.atualizarFuncionario(funcionario)

                    self.atualizarHorarios()
                    self.cancelar()
        else:
            self.mensagem.warning('Atenção', "Por Favor preencha os campos obrigatorios")

    def atualizarHorarios(self):
        for row in range(0, self.ui.tabHorario.rowCount()):
            semana = self.ui.tabHorario.item(row, 0).text()
            inicio = self.ui.tabHorario.cellWidget(row, 1).text()
            iniIntervalo = self.ui.tabHorario.cellWidget(row, 2).text()
            fimIntervalo = self.ui.tabHorario.cellWidget(row, 3).text()
            termino = self.ui.tabHorario.cellWidget(row, 4).text()

            funcionarioDao = FuncionarioDao()
            funcionarioDao.atualizarHorarios(semana, inicio, iniIntervalo, fimIntervalo, termino, self.idJornada, self.idFuncionrio)

    def deletar(self):
        fisicaDao = FuncionarioDao()
        usuario = fisicaDao.pesquisarTabelaUsuario(self.idFuncionrio)

        if usuario == []:
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
            fisicaDao = FuncionarioDao()
            codigo = self.idFuncionrio
            a = fisicaDao.deletarFuncionario(codigo)
            b = fisicaDao.deletarHorario(codigo)

            if self.contatoAdd != []:
                self.deletarTelefoneFrom()

            if self.emailAdd != []:
                self.deletarEmailFrom()

            if self.contatoRemove != []:
                self.deletarTelefone()

            if self.emailRemove != []:
                self.deletarEmail()

            if a  == True and b == True:
                MensagemBox().informacao('Mensagem', 'Cadastro deletar com sucesso!')
                self.desativarCampos()
            else:
                MensagemBox().critico('Erro', 'Erro ao deletar as informações no banco de dados')

            self.cancelar()
            self.msgBox.close()

    def fechar(self):
        self.msgBox.close()

    def deletarTelefoneFrom(self):
        emp = FuncionarioDao()
        i = 0
        for lista in self.contatoAdd :
            a = self.contatoAdd[i]

            idTelefone = int(a[0])

            emp.deletarTelefone(idTelefone, self.idFuncionrio)
            pesquisa = emp.pesquisaTelefoneFuncionario(idTelefone, self.idFuncionrio)
            if pesquisa == "":
                emp.deletarContatoTelefone(idTelefone)

            i += 1

    def deletarEmailFrom(self):
        emp = FuncionarioDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            idEmail = a[0]

            emp.deletarEmail(idEmail, self.idFuncionrio)
            pesquisa = emp.pesquisaEmailFuncionario(idEmail, self.idFuncionrio)
            if pesquisa == "":
                emp.deletarContatoEmail(idEmail)

            i += 1
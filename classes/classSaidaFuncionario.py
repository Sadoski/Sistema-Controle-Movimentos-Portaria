import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetFuncionario import Funcionario
from controller.saidaFuncionario import FuncionarioSaida
from dao.funcionarioDao import FuncionarioDao
from dao.saidaFuncionarioDao import SaidaFuncionarioDao
from telas.frmPesquisarFuncionario import Ui_frmPesquisarFuncionario
from telas.frmSaidaFuncionario import Ui_frmSaidaFuncionario

class SaidaFuncionario(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmSaidaFuncionario()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()

        self.ui.btnNovo.clicked.connect(self.botaoNovoCadastro)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnPesquisar.clicked.connect(self.pesquisarFuncionario)
        self.ui.btnCancelar.clicked.connect(self.cancelarCad)

        self.ui.txtidFuncionario.returnPressed.connect(self.pesquisarFuncionario)
        self.ui.txtidFuncionario.editingFinished.connect(self.pesquisarFuncionarioEditFinish)

        self.ui.btnPesquisar.clicked.connect(self.pesquiFunc)

    def limparCampos(self):
        self.ui.txtNomeFuncionario.clear()
        self.ui.txtidFuncionario.clear()
        self.ui.txtSetor.clear()
        self.ui.txtCargos.clear()

    def pesquisarFuncionario(self):
        __nome = self.ui.txtidFuncionario.text()
        __funDao = SaidaFuncionarioDao()
        __resultada = __funDao.pesquisarFuncionario(__nome)
        if __resultada == False:
            self.ui.txtNomeFuncionario.clear()
            self.ui.txtSetor.clear()
            self.ui.txtCargos.clear()
            MensagemBox().warning('Mensagem', "Atenção não existe nenhum cadastro deste funcionario")
        else:
            self.limparCampos()
            for non in __resultada:
                self.ui.txtidFuncionario.setText(str(non[0]))
                self.ui.txtNomeFuncionario.setText(non[1] + ' ' + non[2])
                self.ui.txtSetor.setText(non[28])
                self.ui.txtCargos.setText(non[29])

    def pesquisarFuncionarioEditFinish(self):
        __nome = self.ui.txtidFuncionario.text()
        __funDao = SaidaFuncionarioDao()
        __resultada = __funDao.pesquisarFuncionario(__nome)
        if __resultada == False:
            self.ui.txtNomeFuncionario.clear()
            self.ui.txtSetor.clear()
            self.ui.txtCargos.clear()
        else:
            self.limparCampos()
            for non in __resultada:
                self.ui.txtidFuncionario.setText(str(non[0]))
                self.ui.txtNomeFuncionario.setText(non[1] + ' ' + non[2])
                self.ui.txtSetor.setText(non[28])
                self.ui.txtCargos.setText(non[29])

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

    def formatarData(self, data):
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:8]

        return ("%s-%s-%s" % (ano, mes, dia))

    def limparCamposCad(self):
        self.ui.txtidFuncionario.clear()
        self.ui.txtNomeFuncionario.clear()
        self.ui.txtDataSaida.setDate(QDate.currentDate())
        self.ui.txtHoraSaida.setTime(QTime.currentTime())
        self.ui.txtSetor.clear()
        self.ui.txtCargos.clear()


    def cadastrar(self):
        __idFuncionario = self.ui.txtidFuncionario.text()
        __data = self.formatarData(self.removerCaracter(self.ui.txtDataSaida.text()))
        __hora = self.ui.txtHoraSaida.text()

        __funcionario = FuncionarioSaida(None, __idFuncionario, __data, __hora)
        __funDao = SaidaFuncionarioDao()
        __funDao.cadastro(__funcionario)
        self.botaoCancelarCadastro()
        self.limparCamposCad()

    def cancelarCad(self):
        self.botaoCancelarCadastro()
        self.limparCamposCad()

    def botaoEditarCadastro(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)

        self.ui.grbDadosSaidaFuncionario.setEnabled(True)

    def botaoNovoCadastro(self):
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)

        self.ui.grbDadosSaidaFuncionario.setEnabled(True)

    def botaoCancelarCadastro(self):
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)

        self.ui.grbDadosSaidaFuncionario.setEnabled(False)

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def formatarHorasRetorno(self, hora):
        horas = hora[0:2]
        minutos = hora[3:5]
        segundos = hora[6:8]

        return QtCore.QTime(int(horas), int(minutos), int(segundos))

    def pesquiFunc(self):
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


        __dados = Funcionario(codigo, None, None, cpf, rg, nome, sobrenome, obs, situacao, civil, deficiencia, categoria, setor, cargo, jornada, admissao, demissao, carteira, pis, serie, uf,  emissao)
        self.setCampos(__dados)
        self.dialog.close()


    def setCampos(self, campos):
        self.ui.txtidFuncionario.setText(str(campos.getIdFuncionario))
        self.ui.txtNomeFuncionario.setText(campos.getNome + ' ' + campos.getSobrenome)
        self.ui.txtSetor.setText(campos.getCargo)
        self.ui.txtCargos.setText(campos.getSetor)




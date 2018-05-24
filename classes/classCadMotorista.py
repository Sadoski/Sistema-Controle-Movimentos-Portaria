import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetMotorista import Motorista
from controller.getSetPessoaFisica import PessoaFisica
from controller.getSetVeiculoMotorista import VeiculoMotorista
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.motoristaDao import MotoristaDao
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from telas.frmCadMotorista import Ui_frmCadastroMotorista
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
        self.editar = False
        self.contatoAdd = []
        self.contatoRemove = []
        self.contatoAtualizar = []
        self.emailAdd = []
        self.emailRemove = []
        self.emailAtualizar = []

        self.ui.btnNovo.clicked.connect(self.novo)
        #self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        #self.ui.btnEditar.clicked.connect(self.atualizar)
        #self.ui.btnDeletar.clicked.connect(self.deletar)
        self.ui.btnPesquisarEmpresa.clicked.connect(self.pesquisarPessoaFisica)

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

        self.setSetores()
        self.setCargo()
        self.setJornadaTrabalho()
        self.setCategoriaTrabalho()
        self.setEstadoCivil()
        self.setDeficiencia()

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
        self.idJornada = int()
        self.ui.txtCodigo.setEnabled(True)
        self.ui.btnPesquisarEmpresa.setEnabled(True)
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtNome.clear()
        self.ui.txtSobrenome.clear()

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





    '''
    def positionCursorCpf(self):
        texto = self.removerCaracter(self.ui.txtCpf.text())
        if len(texto) == 0:
            self.ui.txtCpf.setCursorPosition(0)
        elif len(texto) <= 2:
            b = len(texto)
            self.ui.txtCpf.setCursorPosition(b)
        elif len(texto) >= 3 and len(texto) <6:
            b = len(texto)+1
            self.ui.txtCpf.setCursorPosition(b)
        elif len(texto) >= 6 and len(texto) <9:
            b = len(texto)+2
            self.ui.txtCpf.setCursorPosition(b)
        elif len(texto) >= 9 and len(texto) <12:
            b = len(texto)+3
            self.ui.txtCpf.setCursorPosition(b)

    def positionCursorRg(self):
        texto = self.removerCaracter(self.ui.txtRg.text())
        if len(texto) == 0:
            self.ui.txtRg.setCursorPosition(0)
        elif len(texto) <= 6:
            b = len(texto)
            self.ui.txtRg.setCursorPosition(b)
        elif len(texto) >= 7 and len(texto) < 10:
            b = len(texto) + 1
            self.ui.txtRg.setCursorPosition(b)

    def positionCursorCep(self):
        texto = self.removerCaracter(self.ui.txtCep.text())
        if len(texto) == 0:
            self.ui.txtCep.setCursorPosition(0)
        elif len(texto) <= 4:
            b = len(texto)
            self.ui.txtCep.setCursorPosition(b)
        elif len(texto) >= 5 and len(texto) < 9:
            b = len(texto) + 1
            self.ui.txtCep.setCursorPosition(b)


    def positionCursorTelefone(self):
        texto = self.removerCaracter(self.ui.txtTelefone.text())
        if len(texto) == 0:
            self.ui.txtTelefone.setCursorPosition(1)
        elif len(texto) <= 1:
            b = len(texto) + 1
            self.ui.txtTelefone.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) < 6:
            b = len(texto) + 2
            self.ui.txtTelefone.setCursorPosition(b)
        elif len(texto) >= 6 and len(texto) < 11:
            b = len(texto) + 3
            self.ui.txtTelefone.setCursorPosition(b)


    def positionCursorCelular(self):
        texto = self.removerCaracter(self.ui.txtCelular.text())
        if len(texto) == 0:
            self.ui.txtCelular.setCursorPosition(1)
        elif len(texto) <= 1:
            b = len(texto) + 1
            self.ui.txtCelular.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) < 7:
            b = len(texto) + 2
            self.ui.txtCelular.setCursorPosition(b)
        elif len(texto) >= 7 and len(texto) < 12:
            b = len(texto) + 3
            self.ui.txtCelular.setCursorPosition(b)


    def positionCursorPlaca(self):
        texto = self.removerCaracter(self.ui.txtPlaca.text())
        a = self.ui.txtPlaca.cursorPosition()
        print(a)
        if len(texto) == 0:
            self.ui.txtPlaca.setCursorPosition(0)
        elif len(texto) <= 2:
            b = len(texto)
            self.ui.txtPlaca.setCursorPosition(b)
        elif len(texto) >= 3 and len(texto) <9:
            b = len(texto)+1
            self.ui.txtPlaca.setCursorPosition(b)



    def upperNome(self):
        self.ui.txtNomeMotorista.setText(self.ui.txtNomeMotorista.text().upper())

    def upperExpeditor(self):
        self.ui.txtExpeditor.setText(self.ui.txtExpeditor.text().upper())

    def upperEndereco(self):
        self.ui.txtEndereco.setText(self.ui.txtEndereco.text().upper())

    def upperNumero(self):
        self.ui.txtNumero.setText(self.ui.txtNumero.text().upper())

    def upperComplemento(self):
        self.ui.txtComplemento.setText(self.ui.txtComplemento.text().upper())

    def upperMarca(self):
        self.ui.txtMarca.setText(self.ui.txtMarca.text().upper())

    def upperModelo(self):
        self.ui.txtModelo.setText(self.ui.txtModelo.text().upper())

    def upperPlaca(self):
        self.ui.txtPlaca.setText(self.ui.txtPlaca.text().upper())

    def upperBairro(self):
        self.ui.txtBairro.setText(self.ui.txtBairro.text().upper())

    def focusDataNacimento(self):
        self.ui.txtDataNascimento.setFocus()

    def focusRg(self):
        self.ui.txtRg.setFocus()

    def focusExpeditor(self):
        self.ui.txtExpeditor.setFocus()

    def focusCpf(self):
        self.ui.txtCpf.setFocus()

    def focusPis(self):
        self.ui.txtPis.setFocus()

    def focusCnh(self):
        self.ui.txtCnh.setFocus()

    def focusCategoriaCnh(self):
        self.ui.txtCategoriaCnh.setFocus()

    def focusEndereco(self):
        self.ui.txtEndereco.setFocus()

    def focusNumero(self):
        self.ui.txtNumero.setFocus()

    def focusComplemento(self):
        self.ui.txtComplemento.setFocus()

    def focusBairro(self):
        self.ui.txtBairro.setFocus()

    def focusCep(self):
        self.ui.txtCep.setFocus()

    def focusTelefone(self):
        self.ui.txtTelefone.setFocus()

    def focusCelular(self):
        self.ui.txtCelular.setFocus()

    def focusTipoVeiculo(self):
        self.ui.txtTipoVeiculo.setFocus()

    def focusMarca(self):
        self.ui.txtMarca.setFocus()

    def focusModelo(self):
        self.ui.txtModelo.setFocus()

    def focusPlaca(self):
        self.ui.txtPlaca.setFocus()

    def botaoNovoCad(self):
        self.ui.btnCadNovo.setEnabled(False)
        self.ui.btnCadSalvar.setEnabled(True)
        self.ui.btnCadCancelar.setEnabled(True)

        self.ui.grbMotorista.setEnabled(True)
        self.ui.grbVeiculo.setEnabled(True)

        self.ui.txtNomeMotorista.setFocus()

        self.addCategoria()
        self.addTipoVeiculo()

    def botaoEditarCad(self):
        self.ui.btnCadNovo.setEnabled(False)
        self.ui.btnCadSalvar.setEnabled(False)
        self.ui.btnCadEditar.setEnabled(True)
        self.ui.btnCadCancelar.setEnabled(True)
        self.ui.btnCadDeletar.setEnabled(True)

        self.ui.grbMotorista.setEnabled(True)
        self.ui.grbVeiculo.setEnabled(True)

        self.ui.txtNomeMotorista.setFocus()

    def botaoCancelar(self):
        self.ui.btnCadNovo.setEnabled(True)
        self.ui.btnCadSalvar.setEnabled(False)
        self.ui.btnCadEditar.setEnabled(False)
        self.ui.btnCadCancelar.setEnabled(False)
        self.ui.btnCadDeletar.setEnabled(False)

        self.ui.grbMotorista.setEnabled(False)
        self.ui.grbVeiculo.setEnabled(False)

    def limparCampos(self):
        self.ui.txtidMotorista.clear()
        self.ui.txtNomeMotorista.clear()
        self.ui.txtRg.clear()
        self.ui.txtExpeditor.clear()
        self.ui.txtCpf.clear()
        self.ui.txtPis.clear()
        self.ui.txtCnh.clear()
        self.ui.txtCategoriaCnh.clear()
        self.ui.txtEndereco.clear()
        self.ui.txtNumero.clear()
        self.ui.txtComplemento.clear()
        self.ui.txtBairro.clear()
        self.ui.txtCep.clear()
        self.ui.txtCidades.clear()
        self.ui.txtEstados.clear()
        self.ui.txtTelefone.clear()
        self.ui.txtCelular.clear()
        self.ui.txtTipoVeiculo.clear()
        self.ui.txtMarca.clear()
        self.ui.txtModelo.clear()
        self.ui.txtPlaca.clear()

    def addCategoria(self):
        __motoDao = MotoristaDao()
        __categoria = __motoDao.pesquisarCategoria()
        for cate in __categoria:
            self.ui.txtCategoriaCnh.addItem(cate[0])

    def addTipoVeiculo(self):
        __motoDao = MotoristaDao()
        __tipo = __motoDao.pesquisarTipoVeiculo()
        for cate in __tipo:
            self.ui.txtTipoVeiculo.addItem(cate[0])

    def pesquisarCidade(self):
        _cep = self.removerCaracter(self.ui.txtCep.text())
        if len(_cep) < 8:
            self.ui.txtCidades.clear()
            self.ui.txtEstados.clear()
        else:
            cidades = CidadesEstadosDao()
            cid = cidades.cidade(_cep)

            for cidade in cid:
                self.ui.txtCidades.setText(cidade[0])
                self.ui.txtEstados.setText(cidade[1])
            if cid == []:
                self.ui.txtCidades.clear()
                self.ui.txtEstados.clear()

    def validacaoCpf(self):
        _cpf = self.removerCaracter(self.ui.txtCpf.text())

        _val = self.validarCpf(_cpf)

        if _val  != False:
            _valCpf = self.cpf(_cpf)
            if _valCpf == False:
                w = QWidget()
                QMessageBox.warning(w, 'Atenção', "CPF Invalido, por favor insira um CPF Valido")
                return False
        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "CPF Invalido, por favor insira um CPF Valido")
            return False

    def formatarCpf(self, cpf):
        return ("%s.%s.%s-%s" % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11]))

    def validarCpf(self, cpf):

        cpf_invalidos = [11 * str(i) for i in range(10)]
        if cpf in cpf_invalidos:
            return False

    def cpf(self, cpf):

        selfcpf = [int(x) for x in cpf]

        cpf = selfcpf[:9]

        while len(cpf) < 11:

            r = sum([(len(cpf)+1-i)*v for i, v in [(x, cpf[x]) for x in range(len(cpf))]]) % 11

            if r > 1:
                f = 11 - r
                cpf.append(f)
            else:
                f = 0
                cpf.append(f)

        return bool(cpf == selfcpf)

    def cancelarCadastro(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja realmente cancelar a operação",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botaoCancelar()
            self.limparCampos()

    def cadastrarCadastro(self):
        if self.ui.txtNomeMotorista.text() != "" and self.ui.txtNomeMotorista.text() != "" and self.ui.txtCnh.text() != "" and self.ui.txtEndereco.text() != "" and self.ui.txtNumero.text() != "" and self.ui.txtBairro.text() != "" and self.ui.txtCidades.text() != "" and self.ui.txtEstados.text() and self.ui.txtMarca.text() != "" and self.ui.txtModelo.text() != "":
            _cidade = CidadesEstadosDao()
            __motoDao = MotoristaDao()

            nome = self.ui.txtNomeMotorista.text()
            nascimento = self.formatarData(self.removerCaracter(self.ui.txtDataNascimento.text()))
            rg = self.removerCaracter(self.ui.txtRg.text())
            expeditor = self.ui.txtExpeditor.text()
            cpf = self.removerCaracter(self.ui.txtCpf.text())
            pis = self.ui.txtPis.text()
            cnh = self.ui.txtCnh.text()
            categoria = __motoDao.pesquisarIdCategoriaCnh(self.ui.txtCategoriaCnh.currentText())
            endereco = self.ui.txtEndereco.text()
            numero = self.ui.txtNumero.text()
            complemento = self.ui.txtComplemento.text()
            bairro = self.ui.txtBairro.text()
            telefone = self.removerCaracter(self.ui.txtTelefone.text())
            celular = self.removerCaracter(self.ui.txtCelular.text())
            _cep = self.removerCaracter(self.ui.txtCep.text())
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self.ui.txtCidades.text(), self.ui.txtEstados.text())
            else:
                return False

            if self.ui.radBtnMasculino.isChecked():
                sexo = 'MASCULINO'
            elif self.ui.radBtnFeminino.isChecked():
                sexo = 'FEMININO'
            else:
                sexo = None

            __motorista = Motorista(None, nome, nascimento, rg, expeditor, cpf, pis, cnh, categoria, endereco, numero, complemento, bairro, _cida, telefone, celular, sexo)
            __mot = __motoDao.cadastrarMotorista(__motorista)

            if __mot != False:
                if self.ui.txtMarca.text() != "" and self.ui.txtModelo.text() != "":
                    __idMotorista = __motoDao.pesquisarIdMotorista(__motorista)
                    tipoVei = __motoDao.pesquisarIdTipoVeiculo(self.ui.txtTipoVeiculo.currentText())
                    marca = self.ui.txtMarca.text()
                    modelo = self.ui.txtModelo.text()
                    placa = self.removerCaracter(self.ui.txtPlaca.text())

                    __veiculo = VeiculoMotorista(None, __idMotorista, tipoVei, marca, modelo, placa)
                    __vei = __motoDao.cadastrarVeiculoMotorista(__veiculo)

                if __mot and __vei != False:
                    self.limparCampos()
                    self.botaoCancelar()
                else:
                    w = QWidget()
                    QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")
        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")


    def atualizarCadastro(self):
        if self.ui.txtNomeMotorista.text() != "" and self.ui.txtNomeMotorista.text() != "" and self.ui.txtCnh.text() != "" and self.ui.txtEndereco.text() != "" and self.ui.txtNumero.text() != "" and self.ui.txtBairro.text() != "" and self.ui.txtCidades.text() != "" and self.ui.txtEstados.text():
            _cidade = CidadesEstadosDao()
            __motoDao = MotoristaDao()

            idMotorista = self.ui.txtNomeMotorista.text()
            nome = self.ui.txtNomeMotorista.text()
            nascimento = self.formatarData(self.removerCaracter(self.ui.txtDataNascimento.text()))
            rg = self.removerCaracter(self.ui.txtRg.text())
            expeditor = self.ui.txtNomeMotorista.text()
            cpf = self.removerCaracter(self.ui.txtCpf.text())
            pis = self.ui.txtPis.text()
            cnh = self.ui.txtCnh.text()
            categoria = __motoDao.pesquisarIdCategoriaCnh(self.ui.txtCategoriaCnh.currentText())
            endereco = self.ui.txtEndereco.text()
            numero = self.ui.txtNumero.text()
            complemento = self.ui.txtComplemento.text()
            bairro = self.ui.txtBairro.text()
            telefone = self.removerCaracter(self.ui.txtTelefone.text())
            celular = self.removerCaracter(self.ui.txtCelular.text())
            _cep = self.removerCaracter(self.ui.txtCep.text())
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self.ui.txtCidades.text(), self.ui.txtEstados.text())
            else:
                return False

            if self.ui.radBtnMasculino.isChecked():
                sexo = 'MASCULINO'
            elif self.ui.radBtnFeminino.isChecked():
                sexo = 'FEMININO'
            else:
                sexo = None

            __motorista = Motorista(idMotorista, nome, nascimento, rg, expeditor, cpf, pis, cnh, categoria, endereco, numero, complemento, bairro, _cida, telefone, celular, sexo)
            __mot = __motoDao.atualizarMotorista(__motorista)

            if __mot != False:
                if self.ui.txtMarca.text() != "" and self.ui.txtModelo.text() != "":
                    tipoVei = __motoDao.pesquisarIdTipoVeiculo(self.ui.txtTipoVeiculo.currentText())
                    marca = self.ui.txtMarca.text()
                    modelo = self.ui.txtModelo.text()
                    placa = self.removerCaracter(self.ui.txtPlaca.text())

                    __veiculo = VeiculoMotorista(self.__idVeiculo, idMotorista, tipoVei, marca, modelo, placa)
                    __vei = __motoDao.atualizarVeiculoMotorista(__veiculo)

                if __mot and __vei != False:
                    self.limparCampos()
                    self.botaoCancelar()
                else:
                    w = QWidget()
                    QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")
        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")


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

    def pesquisar(self):
        __motoDao = MotoristaDao()
        if self.ui.radBtnCodigo.isChecked():
            _pesquisarCod = __motoDao.pesquisarCodigoMotorista(self.ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarCod)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarCod:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                nascimento = pesqui[2]
                rg = pesqui[3]
                expeditor = pesqui[4]
                cpf = pesqui[5]
                pis = pesqui[6]
                cnh = pesqui[7]
                categoria = pesqui[8]
                sexo = pesqui[9]
                endereco = pesqui[10]
                numero = pesqui[11]
                complemento = pesqui[12]
                bairro = pesqui[13]
                telefone = pesqui[14]
                celular = pesqui[15]
                cep = pesqui[16]
                cidade = pesqui[17]
                estado = pesqui[18]
                tipoVei = pesqui[19]
                marca = pesqui[20]
                modelo = pesqui[21]
                placa = pesqui[22]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nascimento)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(pis)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(cnh)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(categoria)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(sexo)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(celular)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(tipoVei)))
                self.ui.tbPesquisa.setItem(linha, 20, QtGui.QTableWidgetItem(str(marca)))
                self.ui.tbPesquisa.setItem(linha, 21, QtGui.QTableWidgetItem(str(modelo)))
                self.ui.tbPesquisa.setItem(linha, 22, QtGui.QTableWidgetItem(str(placa)))

                linha += 1

        elif self.ui.radBtnNome.isChecked():
            _pesquisarNome = __motoDao.pesquisarNomeMotorista(str(self.ui.txtPesquisa.text()))

            qtde_registros = len(_pesquisarNome)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarNome:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                nascimento = pesqui[2]
                rg = pesqui[3]
                expeditor = pesqui[4]
                cpf = pesqui[5]
                pis = pesqui[6]
                cnh = pesqui[7]
                categoria = pesqui[8]
                sexo = pesqui[9]
                endereco = pesqui[10]
                numero = pesqui[11]
                complemento = pesqui[12]
                bairro = pesqui[13]
                telefone = pesqui[14]
                celular = pesqui[15]
                cep = pesqui[16]
                cidade = pesqui[17]
                estado = pesqui[18]
                tipoVei = pesqui[19]
                marca = pesqui[20]
                modelo = pesqui[21]
                placa = pesqui[22]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nascimento)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(pis)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(cnh)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(categoria)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(sexo)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(celular)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(tipoVei)))
                self.ui.tbPesquisa.setItem(linha, 20, QtGui.QTableWidgetItem(str(marca)))
                self.ui.tbPesquisa.setItem(linha, 21, QtGui.QTableWidgetItem(str(modelo)))
                self.ui.tbPesquisa.setItem(linha, 22, QtGui.QTableWidgetItem(str(placa)))

                linha += 1

        elif self.ui.radBtnCpf.isChecked():
            _pesquisarCpf = __motoDao.pesquisarCpfMotorista(str(self.ui.txtPesquisa.text()))

            qtde_registros = len(_pesquisarCpf)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarCpf:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                nascimento = pesqui[2]
                rg = pesqui[3]
                expeditor = pesqui[4]
                cpf = pesqui[5]
                pis = pesqui[6]
                cnh = pesqui[7]
                categoria = pesqui[8]
                sexo = pesqui[9]
                endereco = pesqui[10]
                numero = pesqui[11]
                complemento = pesqui[12]
                bairro = pesqui[13]
                telefone = pesqui[14]
                celular = pesqui[15]
                cep = pesqui[16]
                cidade = pesqui[17]
                estado = pesqui[18]
                tipoVei = pesqui[19]
                marca = pesqui[20]
                modelo = pesqui[21]
                placa = pesqui[22]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nascimento)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(pis)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(cnh)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(categoria)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(sexo)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(celular)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(tipoVei)))
                self.ui.tbPesquisa.setItem(linha, 20, QtGui.QTableWidgetItem(str(marca)))
                self.ui.tbPesquisa.setItem(linha, 21, QtGui.QTableWidgetItem(str(modelo)))
                self.ui.tbPesquisa.setItem(linha, 22, QtGui.QTableWidgetItem(str(placa)))

                linha += 1

        elif self.ui.radBtnRg.isChecked():
            _pesquisarRg = __motoDao.pesquisarRgMotorista(self.ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarRg)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarRg:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                nascimento = pesqui[2]
                rg = pesqui[3]
                expeditor = pesqui[4]
                cpf = pesqui[5]
                pis = pesqui[6]
                cnh = pesqui[7]
                categoria = pesqui[8]
                sexo = pesqui[9]
                endereco = pesqui[10]
                numero = pesqui[11]
                complemento = pesqui[12]
                bairro = pesqui[13]
                telefone = pesqui[14]
                celular = pesqui[15]
                cep = pesqui[16]
                cidade = pesqui[17]
                estado = pesqui[18]
                tipoVei = pesqui[19]
                marca = pesqui[20]
                modelo = pesqui[21]
                placa = pesqui[22]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nascimento)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(pis)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(cnh)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(categoria)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(sexo)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(celular)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(tipoVei)))
                self.ui.tbPesquisa.setItem(linha, 20, QtGui.QTableWidgetItem(str(marca)))
                self.ui.tbPesquisa.setItem(linha, 21, QtGui.QTableWidgetItem(str(modelo)))
                self.ui.tbPesquisa.setItem(linha, 22, QtGui.QTableWidgetItem(str(placa)))

                linha += 1

        elif self.ui.radBtnNumCnh.isChecked():
            _pesquisarChn = __motoDao.pesquisarCnhMotorista(self.ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarChn)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarChn:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                nascimento = pesqui[2]
                rg = pesqui[3]
                expeditor = pesqui[4]
                cpf = pesqui[5]
                pis = pesqui[6]
                cnh = pesqui[7]
                categoria = pesqui[8]
                sexo = pesqui[9]
                endereco = pesqui[10]
                numero = pesqui[11]
                complemento = pesqui[12]
                bairro = pesqui[13]
                telefone = pesqui[14]
                celular = pesqui[15]
                cep = pesqui[16]
                cidade = pesqui[17]
                estado = pesqui[18]
                tipoVei = pesqui[19]
                marca = pesqui[20]
                modelo = pesqui[21]
                placa = pesqui[22]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nascimento)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(pis)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(cnh)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(categoria)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(sexo)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(celular)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(tipoVei)))
                self.ui.tbPesquisa.setItem(linha, 20, QtGui.QTableWidgetItem(str(marca)))
                self.ui.tbPesquisa.setItem(linha, 21, QtGui.QTableWidgetItem(str(modelo)))
                self.ui.tbPesquisa.setItem(linha, 22, QtGui.QTableWidgetItem(str(placa)))

                linha += 1
        elif self.ui.radBtnPis.isChecked():
            _pesquisarPis = __motoDao.pesquisarPisMotorista(self.ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarPis)
            self.ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarPis:
                # capturando os dados da tupla

                codigo = pesqui[0]
                nome = pesqui[1]
                nascimento = pesqui[2]
                rg = pesqui[3]
                expeditor = pesqui[4]
                cpf = pesqui[5]
                pis = pesqui[6]
                cnh = pesqui[7]
                categoria = pesqui[8]
                sexo = pesqui[9]
                endereco = pesqui[10]
                numero = pesqui[11]
                complemento = pesqui[12]
                bairro = pesqui[13]
                telefone = pesqui[14]
                celular = pesqui[15]
                cep = pesqui[16]
                cidade = pesqui[17]
                estado = pesqui[18]
                tipoVei = pesqui[19]
                marca = pesqui[20]
                modelo = pesqui[21]
                placa = pesqui[22]

                # preenchendo o grid de pesquisa
                self.ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self.ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
                self.ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(nascimento)))
                self.ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(rg)))
                self.ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(expeditor)))
                self.ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(cpf)))
                self.ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(pis)))
                self.ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(cnh)))
                self.ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(categoria)))
                self.ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(sexo)))
                self.ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(endereco)))
                self.ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(numero)))
                self.ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(complemento)))
                self.ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(bairro)))
                self.ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(telefone)))
                self.ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(celular)))
                self.ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(cep)))
                self.ui.tbPesquisa.setItem(linha, 17, QtGui.QTableWidgetItem(str(cidade)))
                self.ui.tbPesquisa.setItem(linha, 18, QtGui.QTableWidgetItem(str(estado)))
                self.ui.tbPesquisa.setItem(linha, 19, QtGui.QTableWidgetItem(str(tipoVei)))
                self.ui.tbPesquisa.setItem(linha, 20, QtGui.QTableWidgetItem(str(marca)))
                self.ui.tbPesquisa.setItem(linha, 21, QtGui.QTableWidgetItem(str(modelo)))
                self.ui.tbPesquisa.setItem(linha, 22, QtGui.QTableWidgetItem(str(placa)))

                linha += 1

        else:
            result = QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")

    def addCategoriaAtualizacao(self, dados):
        __motoDao = MotoristaDao()
        __categoria = __motoDao.pesquisarCategoria()
        for cate in __categoria:
            if cate[0] != dados:
                self.ui.txtCategoriaCnh.addItem(cate[0])

    def addTipoVeiculoAtualizacao(self, dados):
        __motoDao = MotoristaDao()
        __tipo = __motoDao.pesquisarTipoVeiculo()
        for cate in __tipo:
            if cate[0] != dados:
                self.ui.txtTipoVeiculo.addItem(cate[0])


    def tablePesquisa(self, pesquisa):
        if self.ui.txtNomeMotorista.text() != "" and self.ui.txtNomeMotorista.text() != "" and self.ui.txtCnh.text() != "" and self.ui.txtEndereco.text() != "" and self.ui.txtNumero.text() != "" and self.ui.txtBairro.text() != "" and self.ui.txtCidades.text() != "" and self.ui.txtEstados.text():
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
        if len(itens) == 23:
            self.botaoEditarCad()
            self.ui.txtidMotorista.setText(str(itens[0]))
            self.ui.txtNomeMotorista.setText(str(itens[1]))
            self.ui.txtDataNascimento.setDate(self.formatarDataRetorno(str(itens[2])))
            self.ui.txtRg.setText(str(itens[3]))
            self.ui.txtExpeditor.setText(str(itens[4]))
            self.ui.txtCpf.setText(str(itens[5]))
            self.ui.txtPis.setText(str(itens[6]))
            self.ui.txtCnh.setText(str(itens[7]))
            categoria = str(itens[8])
            self.ui.txtCategoriaCnh.addItem(categoria)
            self.addCategoriaAtualizacao(categoria)
            if str(itens[9]) == 'MASCULINO':
                self.ui.radBtnMasculino.setChecked(True)
            elif str(itens[9]) == 'FEMININO':
                self.ui.radBtnFeminino.setChecked(True)
            else:
                return None
            self.ui.txtEndereco.setText(str(itens[10]))
            self.ui.txtNumero.setText(str(itens[11]))
            self.ui.txtComplemento.setText(str(itens[12]))
            self.ui.txtBairro.setText(str(itens[13]))
            self.ui.txtTelefone.setText(str(itens[14]))
            self.ui.txtCelular.setText(str(itens[15]))
            self.ui.txtCep.setText(str(itens[16]))
            self.ui.txtCidades.setText(str(itens[17]))
            self.ui.txtEstados.setText(str(itens[18]))
            tipo = str(itens[19])
            self.ui.txtTipoVeiculo.addItem(tipo)
            self.addTipoVeiculoAtualizacao(tipo)
            self.ui.txtMarca.setText(str(itens[20]))
            self.ui.txtModelo.setText(str(itens[21]))
            self.ui.txtPlaca.setText(str(itens[22]))

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def deletarMotorista(self):

        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja excluir essa empresa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            __motoDao = MotoristaDao()
            __dao = __motoDao.deletarMotorista(self.ui.txtidMotorista.text())
            if __dao != False:
                self.limparCampos()
                self.botaoCancelar()
    '''
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetCidade import Cidades
from controller.getSetPessoaFisica import PessoaFisica
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from dao.pessoaFisicaDao import PessoaFisicaDao
from telas.frmCadastroPessoaFisica import Ui_frmCadastroPessoaFisica
from telas.frmPesquisarCidades import Ui_frmConsultarCidades
from telas.frmPesquisarPessoaFisica import Ui_frmPesquisarPessoaFisica


class CadastroPessoaFisica(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroPessoaFisica()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.pessoa = int()
        self.idCidade= int()

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnSalvar.clicked.connect(self.cadastrar)
        self.ui.btnEditar.clicked.connect(self.editar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnDeletar.clicked.connect(self.deletar)

        self.ui.btnPesquisarCidade.clicked.connect(self.pesquisarCidadesBotao)

        self.ui.txtNome.returnPressed.connect(self.focusSobrenome)
        self.ui.txtSobrenome.returnPressed.connect(self.focusCpf)
        self.ui.txtCpf.returnPressed.connect(self.focusRg)
        self.ui.txtRg.returnPressed.connect(self.focusExpeditor)
        self.ui.txtExpeditor.returnPressed.connect(self.focusUf)
        self.ui.txtUf.returnPressed.connect(self.focusData)
        self.ui.txtEndereco.returnPressed.connect(self.focusNumero)
        self.ui.txtNumero.returnPressed.connect(self.focusComplemento)
        self.ui.txtComplemento.returnPressed.connect(self.focusBairro)
        self.ui.txtBairro.returnPressed.connect(self.focusCep)
        self.ui.txtCep.returnPressed.connect(self.focusMae)
        self.ui.txtMae.returnPressed.connect(self.focusPai)

        self.ui.txtCep.returnPressed.connect(self.pesquisarCidade)
        self.ui.txtCep.editingFinished.connect(self.pesquisarCidade)

        self.ui.txtNome.setValidator(self.validator)
        self.ui.txtSobrenome.setValidator(self.validator)
        self.ui.txtRg.textChanged.connect(self.numberRg)
        self.ui.txtExpeditor.setValidator(self.validator)
        self.ui.txtUf.setValidator(self.validator)
        self.ui.txtEndereco.setValidator(self.validator)
        self.ui.txtNumero.setValidator(self.validator)
        self.ui.txtComplemento.setValidator(self.validator)
        self.ui.txtBairro.setValidator(self.validator)
        self.ui.txtMae.setValidator(self.validator)
        self.ui.txtPai.setValidator(self.validator)

        self.ui.txtCpf.editingFinished.connect(self.validacaoCpf)

        self.ui.txtCep.cursorPositionChanged.connect(self.positionCursorCep)
        self.ui.txtCpf.cursorPositionChanged.connect(self.positionCursorCpf)


    def numberRg(self):
        if self.ui.txtRg.text().isnumeric() == False:
            self.ui.txtRg.backspace()

    def focusNome(self):
        self.ui.txtNome.setFocus()

    def focusSobrenome(self):
        self.ui.txtSobrenome.setFocus()

    def focusCpf(self):
        self.ui.txtCpf.setFocus()

    def focusRg(self):
        self.ui.txtRg.setFocus()

    def focusExpeditor(self):
        self.ui.txtExpeditor.setFocus()

    def focusUf(self):
        self.ui.txtUf.setFocus()

    def focusData(self):
        self.ui.dateData.setFocus()

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

    def focusMae(self):
        self.ui.txtMae.setFocus()

    def focusPai(self):
        self.ui.txtPai.setFocus()


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

    def pesquisarCidade(self):
        _cep = self.removerCaracter(self.ui.txtCep.text())
        if len(_cep) < 8:
            self.idCidade = ''
            self.ui.txtCidade.clear()
            self.ui.txtEstado.clear()
        else:
            cidades = CidadesEstadosDao()
            cid = cidades.cidade(_cep)

            for cidade in cid:
                self.idCidade = cidade[0]
                self.ui.txtCidade.setText(cidade[1])
                self.ui.txtEstado.setText(cidade[2])
            if cid == []:
                self.idCidade = ''
                self.ui.txtCidade.clear()
                self.ui.txtEstado.clear()

    def novo(self):
        self.limparCampos()
        self.ui.grbDados.setEnabled(True)
        self.ui.radBtnMasculino.setCheckable(True)
        self.ui.radBtnFeminino.setCheckable(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(False)

    def desativarCampos(self):
        self.limparCampos()
        self.ui.grbDados.setEnabled(False)
        self.ui.radBtnMasculino.setCheckable(True)
        self.ui.radBtnFeminino.setCheckable(True)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def cancelar(self):
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
        self.msgBox.setText("Deseja realmente cancelar a operação")
        btnSim = QtGui.QPushButton('Sim')
        self.msgBox.addButton(btnSim, QtGui.QMessageBox.YesRole)
        btnNao = QtGui.QPushButton('Não')
        self.msgBox.addButton(btnNao, QtGui.QMessageBox.NoRole)
        btnSim.clicked.connect(self.desativarCampos)
        btnNao.clicked.connect(self.fechar)
        btnNao.setFocus()
        self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.msgBox.exec_()

    def limparCampos(self):
        self.ui.txtNome.clear()
        self.ui.txtSobrenome.clear()
        self.ui.txtCpf.clear()
        self.ui.txtRg.clear()
        self.ui.txtExpeditor.clear()
        self.ui.txtUf.clear()
        self.ui.dateData.setDate(QDate.currentDate())
        self.ui.radBtnMasculino.setCheckable(False)
        self.ui.radBtnFeminino.setCheckable(False)
        self.ui.txtEndereco.clear()
        self.ui.txtNumero.clear()
        self.ui.txtComplemento.clear()
        self.ui.txtBairro.clear()
        self.ui.txtCep.clear()
        self.ui.txtCidade.clear()
        self.ui.txtEstado.clear()
        self.ui.txtMae.clear()
        self.ui.txtPai.clear()
        self.pessoa=int()
        self.idCidade=int()

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
        mes = data[4:6]
        ano = data[8:10]

        return ("%s-%s-%s" % (ano, mes, dia))

    def validacaoCpf(self):
        _cpf = self.removerCaracter(self.ui.txtCpf.text())
        if len(_cpf) > 0:
            _val = self.validarCpf(_cpf)

            if _val  != False:
                _valCpf = self.cpf(_cpf)
                if _valCpf == False:
                    MensagemBox().warning( 'Atenção', "CPF Invalido, por favor insira um CPF Valido")
                    return False
                else:
                    return True
            else:
                MensagemBox().warning('Atenção', "CPF Invalido, por favor insira um CPF Valido")
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

    def cadastrar(self):
        if self.ui.txtNome.text() != '' and self.ui.txtRg.text() != '' and self.ui.txtExpeditor.text() != '' and self.ui.txtEndereco.text() != '' and self.ui.txtNumero.text() != '' and self.ui.txtBairro.text() != '' and self.ui.txtMae.text() and self.ui.txtPai.text() != '' and self.ui.txtCidade.text() != '' and self.ui.txtEstado.text() != '':
            if self.removerCaracter(self.ui.txtCpf.text()) != '':
                valCpf = self.validacaoCpf()
                if valCpf != False:
                    if self.ui.radBtnMasculino.isChecked() or self.ui.radBtnFeminino.isChecked():
                        nome = self.ui.txtNome.text()
                        segundoNome = self.ui.txtSobrenome.text()
                        cpf = self.removerCaracter(self.ui.txtCpf.text())
                        rg = self.ui.txtRg.text()
                        expeditor = self.ui.txtExpeditor.text()
                        uf = self.ui.txtUf.text()
                        data = self.removerCaracter(self.ui.dateData.text())
                        if self.ui.radBtnMasculino.isChecked():
                            sexo = '1'
                        elif self.ui.radBtnFeminino.isChecked():
                            sexo = '2'
                        else:
                            return None
                        nascimento = self.formatarData(data)
                        endereco = self.ui.txtEndereco.text()
                        numero = self.ui.txtNumero.text()
                        complemento = self.ui.txtComplemento.text()
                        bairro = self.ui.txtBairro.text()
                        mae = self.ui.txtMae.text()
                        pai = self.ui.txtPai.text()
                        cidade = self.idCidade


                        pessoaFisico = PessoaFisica(None, None, 1, nome, segundoNome, cpf, rg, expeditor,  uf, nascimento, sexo, endereco, numero, complemento, bairro, mae, pai, cidade, None, None, None)
                        fisicaDao = PessoaFisicaDao()
                        pes = fisicaDao.pesquisarPessoaFisica(pessoaFisico)
                        if pes == []:
                            a = fisicaDao.cadastrarPessoa(pessoaFisico)
                            if a == True:
                                id = fisicaDao.ultimoRegistro()
                                pessoaFisico = PessoaFisica(id, None, 1, nome, segundoNome, cpf, rg, expeditor, uf, nascimento, sexo, endereco, numero, complemento, bairro, mae, pai, cidade, None, None, None)
                                b = fisicaDao.cadastrarPessoaFisica(pessoaFisico)
                                if b == True:
                                    MensagemBox().informacao('Mensagem', 'Cadastro realizado com sucesso!')
                                    self.desativarCampos()
                                else:
                                    MensagemBox().critico('Erro', 'Erro ao atualizar as informações no banco de dados')
                            else:
                                MensagemBox().critico('Erro', 'Erro ao atualizar as informações no banco de dados')
                        else:
                            MensagemBox().warning( 'Atenção', "Já existe um registro desta Pessoa")
                    else:
                        MensagemBox().warning( 'Atenção', "Selecione o sexo da pessoa")
            else:
                MensagemBox().warning( 'Atenção', "Insira o CPF")

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialog = QDialog(self)
            self.__pesquisarPessoa =  Ui_frmPesquisarPessoaFisica()
            self.__pesquisarPessoa.setupUi(self.dialog)

            self.__pesquisarPessoa.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisarPessoa.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisarPessoa.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        if self.__pesquisarPessoa.radBtnCodigo.isChecked():
            __nome = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaCodigo(__nome)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnNome.isChecked():
            __nome = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaNome(__nome)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtncPF.isChecked():
            __cpf= self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaCpf(__cpf)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnRg.isChecked():
            __rg = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaRg(__rg)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnMae.isChecked():
            __mae = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaMae(__mae)

            self.setarTabelaPesquisa(__retorno)

        elif self.__pesquisarPessoa.radBtnPai.isChecked():
            __pai = self.__pesquisarPessoa.txtPesquisar.text()
            __pesDao = PesquisarPessoaFisicaDao()
            __retorno = __pesDao.pesquisaPai(__pai)

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
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(segundoNome)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(data)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(sexo)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(mae)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(pai)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarPessoa.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cep)))



            linha += 1

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def setarCampos(self):
        itens = []

        for item in self.__pesquisarPessoa.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = str(itens[0])
        nome = str(itens[1])
        segundoNome = str(itens[2])
        cpf = str(itens[3])
        rg = str(itens[4])
        expeditor = str(itens[5])
        uf = str(itens[6])
        data = self.formatarDataRetorno(itens[7])
        sexo = str(itens[8])
        mae = str(itens[9])
        pai = itens[10]
        endereco = str(itens[11])
        numero = str(itens[12])
        complemento = str(itens[13])
        bairro = str(itens[14])
        cidade = str(itens[15])
        estado = str(itens[16])
        cep = str(itens[17])



        __dados = PessoaFisica(codigo, None, None, nome, segundoNome, cpf, rg, expeditor, uf, data, sexo, endereco, numero, complemento, bairro, mae, pai, None, cidade, estado, cep)
        self.setCampos(__dados)
        self.botoesEditar()
        self.dialog.close()

    def setCampos(self, campos):
        self.pessoa = campos.getIdPessoa
        self.ui.txtNome.setText(campos.getNome)
        self.ui.txtSobrenome.setText(campos.getApelido)
        self.ui.txtCpf.setText(campos.getCpf)
        self.ui.txtRg.setText(campos.getRg)
        self.ui.txtExpeditor.setText(campos.getExpeditor)
        self.ui.txtUf.setText(campos.getUf)
        self.ui.dateData.setDate(campos.getData)
        if campos.getSexo == 'MASCULINO':
            self.ui.radBtnMasculino.setChecked(True)
        elif campos.getSexo == 'FEMININO':
            self.ui.radBtnFeminino.setChecked(True)
        self.ui.txtEndereco.setText(campos.getEndereco)
        self.ui.txtNumero.setText(campos.getNumero)
        self.ui.txtComplemento.setText(campos.getComplemento)
        self.ui.txtBairro.setText(campos.getBairro)
        self.ui.txtCep.setText(campos.getCep)
        self.ui.txtCidade.setText(campos.getCidade)
        self.ui.txtEstado.setText(campos.getEstado)
        self.ui.txtMae.setText(campos.getMae)
        self.ui.txtPai.setText(campos.getPai)

    def botoesEditar(self):
        self.ui.grbDados.setEnabled(True)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnCancelar.setEnabled(True)
        self.ui.btnDeletar.setEnabled(True)

    def editar(self):
        if self.ui.txtNome.text() != '' and self.ui.txtRg.text() != '' and self.ui.txtExpeditor.text() != '' and self.ui.txtEndereco.text() != '' and self.ui.txtNumero.text() != '' and self.ui.txtBairro.text() != '' and self.ui.txtMae.text() and self.ui.txtPai.text() != '' and self.removerCaracter(self.ui.txtCep.text()) != '' and self.ui.txtCidade.text() != '' and self.ui.txtEstado.text() != '':
            if self.removerCaracter(self.ui.txtCpf.text()) != '':
                valCpf = self.validacaoCpf()
                if valCpf != False:
                    if self.ui.radBtnMasculino.isChecked() or self.ui.radBtnFeminino.isChecked():
                        pessoa = self.pessoa
                        nome = self.ui.txtNome.text()
                        sobrenome = self.ui.txtSobrenome.text()
                        cpf = self.removerCaracter(self.ui.txtCpf.text())
                        rg = self.ui.txtRg.text()
                        expeditor = self.ui.txtExpeditor.text()
                        uf = self.ui.txtUf.text()
                        data = self.removerCaracter(self.ui.dateData.text())
                        if self.ui.radBtnMasculino.isChecked():
                            sexo = '1'
                        elif self.ui.radBtnFeminino.isChecked():
                            sexo = '2'

                        nascimento = self.formatarData(data)
                        endereco = self.ui.txtEndereco.text()
                        numero = self.ui.txtNumero.text()
                        complemento = self.ui.txtComplemento.text()
                        bairro = self.ui.txtBairro.text()
                        mae = self.ui.txtMae.text()
                        pai = self.ui.txtPai.text()
                        cid = CidadesEstadosDao()
                        cidade = cid.idCidade(self.removerCaracter(self.ui.txtCep.text()), self.ui.txtCidade.text(), self.ui.txtEstado.text())

                        fisicaDao = PessoaFisicaDao()
                        idPessoaFisica = fisicaDao.pesquisarIdPessoaFisica(pessoa)
                        pessoaFisico = PessoaFisica(pessoa, idPessoaFisica, 1, nome, sobrenome, cpf, rg, expeditor, uf, nascimento, sexo, endereco, numero, complemento, bairro, mae, pai, cidade, None, None, None)
                        a = fisicaDao.atualizarPessoa(pessoaFisico)
                        if a == True:
                            b = fisicaDao.atualizarPessoaFisica(pessoaFisico)
                            if b == True:
                                MensagemBox().informacao('Mensagem', 'Cadastro atualizado com sucesso!')
                                self.desativarCampos()
                            else:
                                MensagemBox().critico('Erro', 'Erro ao atualizar as informações no banco de dados')
                        else:
                            MensagemBox().critico('Erro', 'Erro ao atualizar as informações no banco de dados')
                    else:
                        MensagemBox().warning( 'Atenção', 'Selecione o sexo da pessoa')
            else:
                MensagemBox().warning( 'Atenção', 'Insira o CPF')
        else:
            MensagemBox().warning( 'Atenção', 'Por Favor, preencham os campos obrigtorios ')

    def deletar(self):
        fisicaDao = PessoaFisicaDao()
        clie = fisicaDao.pesquisarTabelaCliente(self.pessoa)
        forn = fisicaDao.pesquisarTabelaFornecedor(self.pessoa)
        func = fisicaDao.pesquisarTabelaFuncionario(self.pessoa)
        if clie == "" or forn == "" or func == "":
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
            fisicaDao = PessoaFisicaDao()
            codigo = self.pessoa
            idPessoaFisica = fisicaDao.pesquisarIdPessoaFisica(codigo)
            a = fisicaDao.deletarPessoaFisica(idPessoaFisica)
            b = fisicaDao.deletarPessoa(codigo)
            if a == True and b == True:
                MensagemBox().informacao('Mensagem', 'Cadastro deletar com sucesso!')
                self.desativarCampos()
            else:
                MensagemBox().critico('Erro', 'Erro ao deletar as informações no banco de dados')

            self.msgBox.close()

    def fechar(self):
        self.msgBox.close()


    def pesquisarCidadesBotao(self):
        self.dialogCidade = QDialog(self)
        self.__pesquisar = Ui_frmConsultarCidades()
        self.__pesquisar.setupUi(self.dialogCidade)

        self.__pesquisar.txtPesquisar.returnPressed.connect(self.pesquisarDadosCidade)

        self.__pesquisar.btnPesquisar.clicked.connect(self.pesquisarDadosCidade)

        self.__pesquisar.tabPesquisar.doubleClicked.connect(self.setarCamposCidades)

        self.__pesquisar.txtPesquisar.setValidator(self.validator)


        self.dialogCidade.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogCidade.exec_()

    def pesquisarDadosCidade(self):
        if self.__pesquisar.radBtnCodigoCidade.isChecked():
            __codigo = self.__pesquisar.txtPesquisar.text()
            __pesDao = CidadesEstadosDao()
            __retorno = __pesDao.pesquisarCodigoCidade(__codigo)


            self.setarTabelaPesquisaCidade(__retorno)

        elif self.__pesquisar.radBtnCidade.isChecked():
            __cidade = self.__pesquisar.txtPesquisar.text()
            __pesDao = CidadesEstadosDao()
            __retorno = __pesDao.pesquisarNomeCidade(__cidade)

            self.setarTabelaPesquisaCidade(__retorno)

        elif self.__pesquisar.radBtnEstado.isChecked():
            __estado = self.__pesquisar.txtPesquisar.text()
            __pesDao = CidadesEstadosDao()
            __retorno = __pesDao.pesquisarEstadoCidade(__estado)

            self.setarTabelaPesquisaCidade(__retorno)

        elif self.__pesquisar.radBtnCep.isChecked():
            __cep = self.__pesquisar.txtPesquisar.text()
            __pesDao = CidadesEstadosDao()
            __retorno = __pesDao.pesquisarCepCidade(__cep)

            self.setarTabelaPesquisaCidade(__retorno)

        else:
            MensagemBox().warning('Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaCidade(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisar.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            cidade = pesqui[1]
            estado = pesqui[2]
            cep = pesqui[3]


            # preenchendo o grid de pesquisa
            self.__pesquisar.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisar.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisar.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisar.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cep)))


            linha += 1

    def setarCamposCidades(self):
        itens = []

        for item in self.__pesquisar.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = str(itens[0])
        cidade = str(itens[1])
        estado = str(itens[2])
        cep = str(itens[3])

        __dados = Cidades(codigo, estado,cidade, cep)
        self.setCamposCidade(__dados)
        self.dialogCidade.close()

    def setCamposCidade(self, campos):
        self.idCidade = campos.getIdCidade
        self.ui.txtCep.setText(campos.getCep)
        self.ui.txtCidade.setText(campos.getNomeCidade)
        self.ui.txtEstado.setText(campos.getNomeEstado)

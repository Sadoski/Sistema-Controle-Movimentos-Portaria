import sys
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.getSetFuncionario import Funcionario
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.empresaDao import EmpresaDao
from dao.funcionarioDao import FuncionarioDao
from dao.setoresCargosDao import SetoresCargosDao
from telas.frmCadastroFuncionario import Ui_frmCadastroFuncionario

class CadastroFuncionario(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.__ui = Ui_frmCadastroFuncionario()
        self.__ui.setupUi(self)

        self.__ui.txtFantasia.returnPressed.connect(self.focusNomeFun)
        self.__ui.txtNomeFuncionario.returnPressed.connect(self.focusRg)
        self.__ui.txtRg.returnPressed.connect(self.focusExpeditor)
        self.__ui.txtExpeditor.returnPressed.connect(self.focusCpf)
        self.__ui.txtCpf.returnPressed.connect(self.focusData)
        self.__ui.txtNomeMae.returnPressed.connect(self.focusNomePai)
        self.__ui.txtNomePai.returnPressed.connect(self.focusEndereco)
        self.__ui.txtEndereco.returnPressed.connect(self.focusNumero)
        self.__ui.txtNumero.returnPressed.connect(self.focusComplemento)
        self.__ui.txtComplemento.returnPressed.connect(self.focusBairro)
        self.__ui.txtBairro.returnPressed.connect(self.focusCep)
        self.__ui.txtCep.returnPressed.connect(self.focusTelefone)
        self.__ui.txtTelefone.returnPressed.connect(self.focusCelular)
        self.__ui.txtCelular.returnPressed.connect(self.focusSetores)

        self.__ui.txtPesquisaFuncionario.returnPressed.connect(self.pesquisarFuncionario)

        self.__ui.txtFantasia.editingFinished.connect(self.pesquisarEmpresa)
        self.__ui.txtCpf.editingFinished.connect(self.validacaoCpf)
        self.__ui.txtCep.editingFinished.connect(self.pesquisarCidade)


        self.__ui.btnCadNovo.clicked.connect(self.botaoNovoCadastro)
        self.__ui.btnCadSalvar.clicked.connect(self.cadastrarFuncionario)
        self.__ui.btnCadCancelar.clicked.connect(self.cancelarCadastro)
        self.__ui.btnCadEditar.clicked.connect(self.atualizarFuncionario)

        self.__ui.txtSetor.currentIndexChanged.connect(self.pesquisarCargo)

        self.__ui.tbPesquisaFuncionario.doubleClicked.connect(self.tablePesquisa)

    def focusNomeFun(self):
        self.__ui.txtNomeFuncionario.setFocus()

    def focusRg(self):
        self.__ui.txtRg.setFocus()

    def focusExpeditor(self):
        self.__ui.txtExpeditor.setFocus()

    def focusCpf(self):
        self.__ui.txtCpf.setFocus()

    def focusData(self):
        self.__ui.txtDataNascimento.setFocus()

    def focusNomeMae(self):
        self.__ui.txtNomeMae.setFocus()

    def focusNomePai(self):
        self.__ui.txtNomePai.setFocus()

    def focusEndereco(self):
        self.__ui.txtEndereco.setFocus()

    def focusNumero(self):
        self.__ui.txtNumero.setFocus()

    def focusComplemento(self):
        self.__ui.txtComplemento.setFocus()

    def focusBairro(self):
        self.__ui.txtBairro.setFocus()

    def focusCep(self):
        self.__ui.txtCep.setFocus()

    def focusTelefone(self):
        self.__ui.txtTelefone.setFocus()

    def focusCelular(self):
        self.__ui.txtCelular.setFocus()

    def focusSetores(self):
        self.__ui.txtSetor.setFocus()

    def pesquisarSetor(self):
        __setor = SetoresCargosDao()
        setores = __setor.pesquisaSetor()

        for sett in setores:
            self.__ui.txtSetor.addItem(sett[0])

        self.pesquisarCargo()


    def pesquisarCargo(self):
        self.__ui.txtCargo.clear()

        __cargo = SetoresCargosDao()
        cargos = __cargo.pesquisarFuncao(str(self.__ui.txtSetor.currentText()))
        for carg in cargos:
            self.__ui.txtCargo.addItem(carg[0])


    def pesquisarEmpresa(self):
        _empresaDao = EmpresaDao()

        _empresa = _empresaDao.pesquisaEmpresa(str(self.__ui.txtFantasia.text()))
        if _empresa == False:
            self.limparCamposEmp()
        else:
            self.limparCamposEmp()
            for empe in _empresa:
                self.__ui.txtIdEmpresa.setText(str(empe[0]))
                self.__ui.txtRazaoSocial.setText(empe[1])
                self.__ui.txtCnpj.setText(empe[2])
                self.__ui.txtInscricaoEstadua.setText(empe[3])

    def pesquisarCidade(self):
        _cep = self.removerCaracter(self.__ui.txtCep.text())
        if len(_cep) < 8:
            self.__ui.txtCidades.clear()
            self.__ui.txtEstados.clear()
        else:
            cidades = CidadesEstadosDao()
            cid = cidades.cidade(_cep)

            for cidade in cid:
                self.__ui.txtCidades.setText(cidade[0])
                self.__ui.txtEstados.setText(cidade[1])
            if cid == []:
                self.__ui.txtCidades.clear()
                self.__ui.txtEstados.clear()

    def limparCamposEmp(self):
        self.__ui.txtIdEmpresa.clear()
        self.__ui.txtRazaoSocial.clear()
        self.__ui.txtCnpj.clear()
        self.__ui.txtInscricaoEstadua.clear()

    def validacaoCpf(self):
        _cpf = self.removerCaracter(self.__ui.txtCpf.text())

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

    def botaoNovoCadastro(self):
        self.__ui.btnCadNovo.setEnabled(False)
        self.__ui.btnCadSalvar.setEnabled(True)
        self.__ui.btnCadCancelar.setEnabled(True)

        self.__ui.txtFantasia.setEnabled(True)
        self.__ui.grbFuncionario.setEnabled(True)

        self.__ui.txtFantasia.setFocus()
        self.pesquisarSetor()

    def cadastrarFuncionario(self):
        if self.__ui.txtNomeFuncionario.text() and self.__ui.txtRg.text() and self.__ui.txtExpeditor.text() and self.__ui.txtCpf.text() and self.__ui.txtNomeMae.text() and self.__ui.txtNomePai.text() and self.__ui.txtEndereco.text() and self.__ui.txtNumero.text() and self.__ui.txtComplemento.text() and self.__ui.txtBairro.text() and self.__ui.txtCidades.text() and self.__ui.txtEstados.text() != "":
            _cidade = CidadesEstadosDao()
            _funDao = FuncionarioDao()

            idEmpresa = self.__ui.txtIdEmpresa.text()
            fantasia = self.__ui.txtFantasia.text()
            razaoSocial = self.__ui.txtRazaoSocial.text()

            nome = self.__ui.txtNomeFuncionario.text()
            rg = self.removerCaracter(self.__ui.txtRg.text())
            expeditor = self.__ui.txtExpeditor.text()
            cpf = self.removerCaracter(self.__ui.txtCpf.text())
            data = self.removerCaracter(self.__ui.txtDataNascimento.text())
            nascimento = self.formatarData(data)
            if self.__ui.radBtnMasculino.isChecked():
                sexo = 'MASCULINO'
            elif self.__ui.radBtnFeminino.isChecked():
                sexo = 'FEMININO'
            else:
                return None
            mae = self.__ui.txtNomeMae.text()
            pai = self.__ui.txtNomePai.text()
            endereco = self.__ui.txtEndereco.text()
            numero = self.__ui.txtNumero.text()
            complemento = self.__ui.txtComplemento.text()
            bairro = self.__ui.txtBairro.text()
            _cep = self.removerCaracter(self.__ui.txtCep.text())
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self.__ui.txtCidades.text(), self.__ui.txtEstados.text())
            else:
                return False
            telefone = self.removerCaracter(self.__ui.txtTelefone.text())
            celular = self.removerCaracter(self.__ui.txtCelular.text())

            funcao = _funDao.funcao(self.__ui.txtSetor.currentText(), self.__ui.txtCargo.currentText())
            print(_cida)
            __funcionario = Funcionario(None, nome, rg, expeditor, cpf, nascimento, sexo, mae, pai, endereco, numero, complemento, bairro, _cida, telefone, celular, funcao, idEmpresa)
            _funDao.cadastroFuncionario(__funcionario)
            self.botaoCancelar()
        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")


    def formatarData(self, data):
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:8]

        return ("%s-%s-%s" % (ano, mes, dia))

    def limparCampos(self):
        self.__ui.txtIdEmpresa.clear()
        self.__ui.txtFantasia.clear()
        self.__ui.txtRazaoSocial.clear()
        self.__ui.txtCnpj.clear()
        self.__ui.txtInscricaoEstadua.clear()

        self.__ui.txtidFuncionario.clear()
        self.__ui.txtNomeFuncionario.clear()
        self.__ui.txtRg.clear()
        self.__ui.txtExpeditor.clear()
        self.__ui.txtCpf.clear()
        self.__ui.txtDataNascimento.setDate(QDate.currentDate())
        self.__ui.txtNomeMae.clear()
        self.__ui.txtNomePai.clear()
        self.__ui.txtEndereco.clear()
        self.__ui.txtNumero.clear()
        self.__ui.txtComplemento.clear()
        self.__ui.txtBairro.clear()
        self.__ui.txtCep.clear()
        self.__ui.txtCidades.clear()
        self.__ui.txtEstados.clear()
        self.__ui.txtTelefone.clear()
        self.__ui.txtCelular.clear()

        self.__ui.txtSetor.clear()
        self.__ui.txtCargo.clear()

    def botaoCancelar(self):
        self.__ui.btnCadNovo.setEnabled(True)
        self.__ui.btnCadSalvar.setEnabled(False)
        self.__ui.btnCadEditar.setEnabled(False)
        self.__ui.btnCadCancelar.setEnabled(False)
        self.__ui.btnCadDeletar.setEnabled(False)

        self.__ui.txtFantasia.setEnabled(False)
        self.__ui.grbFuncionario.setEnabled(False)

        self.__ui.radBtnMasculino.setChecked(False)
        self.__ui.radBtnFeminino.setChecked(False)

    def cancelarCadastro(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja realmente cancelar a operação",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.botaoCancelar()
            self.limparCampos()

    def pesquisarFuncionario(self):
        if self.__ui.radBtnCodigoFuncionario.isChecked():
            _funId = FuncionarioDao()
            _pesquisar = _funId.pesquisarCodigoFuncionario(self.__ui.txtPesquisaFuncionario.text())

            self.setarTambelaPesquisa(_pesquisar)

        elif self.__ui.radBtnNomeFuncionario.isChecked():
            _funNome = FuncionarioDao()
            _pesquisar = _funNome.pesquisarNomeFuncionario(self.__ui.txtPesquisaFuncionario.text())

            self.setarTambelaPesquisa(_pesquisar)

        elif self.__ui.radBtnRg.isChecked():
            _funRg = FuncionarioDao()
            _pesquisar = _funRg.pesquisarRgFuncionario(self.__ui.txtPesquisaFuncionario.text())

            self.setarTambelaPesquisa(_pesquisar)

        elif self.__ui.radBtnCpf.isChecked():
            _funCpf = FuncionarioDao()
            _pesquisar = _funCpf.pesquisarCpfFuncionario(self.__ui.txtPesquisaFuncionario.text())

            self.setarTambelaPesquisa(_pesquisar)

        elif self.__ui.radBtnFantasia.isChecked():
            _funFantasia = FuncionarioDao()
            _pesquisar = _funFantasia.pesquisarFantasiaEmpFuncionario(self.__ui.txtPesquisaFuncionario.text())

            self.setarTambelaPesquisa(_pesquisar)

        elif self.__ui.radBtnRazaoSocial.isChecked():
            _funRazaoSocial = FuncionarioDao()
            _pesquisar = _funRazaoSocial.pesquisarRazaoSocialEmpFuncionario(self.__ui.txtPesquisaFuncionario.text())

            self.setarTambelaPesquisa(_pesquisar)

        else:
            result = QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")


    def setarTambelaPesquisa(self, _pesquisar):
        qtde_registros = len(_pesquisar)
        self.__ui.tbPesquisaFuncionario.setRowCount(qtde_registros)

        linha = 0
        for pesqui in _pesquisar:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            rg = pesqui[2]
            expeditor = pesqui[3]
            cpf = pesqui[4]
            nascimento = pesqui[5]
            sexo = pesqui[6]
            mae = pesqui[7]
            pai = pesqui[8]
            endereco = pesqui[9]
            numero = pesqui[10]
            complemento = pesqui[11]
            bairro = pesqui[12]
            cep = pesqui[13]
            cidade = pesqui[14]
            estado = pesqui[15]
            telefone = pesqui[16]
            celular = pesqui[17]
            setor = pesqui[18]
            cargo = pesqui[19]
            fantasia = pesqui[20]
            razaoSocial = pesqui[21]
            cnpj = pesqui[22]
            inscrEstadual = pesqui[23]

            # preenchendo o grid de pesquisa
            self.__ui.tbPesquisaFuncionario.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 2, QtGui.QTableWidgetItem(str(rg)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 3, QtGui.QTableWidgetItem(str(expeditor)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 5, QtGui.QTableWidgetItem(str(nascimento)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 6, QtGui.QTableWidgetItem(str(sexo)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 7, QtGui.QTableWidgetItem(str(mae)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 8, QtGui.QTableWidgetItem(str(pai)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 9, QtGui.QTableWidgetItem(str(endereco)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 10, QtGui.QTableWidgetItem(str(numero)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 11, QtGui.QTableWidgetItem(str(complemento)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 12, QtGui.QTableWidgetItem(str(bairro)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 13, QtGui.QTableWidgetItem(str(cep)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 14, QtGui.QTableWidgetItem(str(cidade)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 15, QtGui.QTableWidgetItem(str(estado)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 16, QtGui.QTableWidgetItem(str(telefone)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 17, QtGui.QTableWidgetItem(str(celular)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 18, QtGui.QTableWidgetItem(str(setor)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 19, QtGui.QTableWidgetItem(str(cargo)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 20, QtGui.QTableWidgetItem(str(fantasia)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 21, QtGui.QTableWidgetItem(str(razaoSocial)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 22, QtGui.QTableWidgetItem(str(cnpj)))
            self.__ui.tbPesquisaFuncionario.setItem(linha, 23, QtGui.QTableWidgetItem(str(inscrEstadual)))

            linha += 1

    def tablePesquisa(self, pesquisa):
        if self.__ui.txtNomeFuncionario.text() and self.__ui.txtRg.text() and self.__ui.txtExpeditor.text() and self.__ui.txtCpf.text() and self.__ui.txtNomeMae.text() and self.__ui.txtNomePai.text() and self.__ui.txtEndereco.text() and self.__ui.txtNumero.text() and self.__ui.txtComplemento.text() and self.__ui.txtBairro.text() and self.__ui.txtCidades.text() and self.__ui.txtEstados.text() != "":
                self.setarCampos()
                self.botaoEditarCadastro()
        else:
                w = QWidget()
                result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.setarCampos()
                    self.botaoEditarCadastro()

    def pesquisarSetorAtualizar(self, dado):
        __setor = SetoresCargosDao()
        setores = __setor.pesquisaSetor()

        for sett in setores:
            if sett[0] != dado:
                self.__ui.txtSetor.addItem(sett[0])

    def pesquisarCargoAtualizar(self, dado, pesquisa):

        __cargo = SetoresCargosDao()
        cargos = __cargo.pesquisarFuncao(pesquisa)
        for carg in cargos:
            if carg[0] != dado:
                self.__ui.txtCargo.addItem(carg[0])

    def setarCampos(self):

        itens = []
        for item in self.__ui.tbPesquisaFuncionario.selectedItems():
            itens.append(item.text())

        if len(itens) == 24:
            self.__ui.txtidFuncionario.setText(str(itens[0]))
            self.__ui.txtNomeFuncionario.setText(str(itens[1]))
            self.__ui.txtRg.setText(str(itens[2]))
            self.__ui.txtExpeditor.setText(str(itens[3]))
            self.__ui.txtCpf.setText(str(itens[4]))
            self.__ui.txtDataNascimento.setDate(self.formatarDataRetorno(itens[5]))
            if str(itens[6]) == 'MASCULINO':
                self.__ui.radBtnMasculino.setChecked(True)
            elif str(itens[6]) == 'FEMININO':
                self.__ui.radBtnFeminino.setChecked(True)
            else:
                return None
            self.__ui.txtNomeMae.setText(str(itens[7]))
            self.__ui.txtNomePai.setText(str(itens[8]))
            self.__ui.txtEndereco.setText(str(itens[9]))
            self.__ui.txtNumero.setText(str(itens[10]))
            self.__ui.txtComplemento.setText(str(itens[11]))
            self.__ui.txtBairro.setText(str(itens[12]))
            self.__ui.txtCep.setText(str(itens[13]))
            self.__ui.txtCidades.setText(str(itens[14]))
            self.__ui.txtEstados.setText(str(itens[15]))
            self.__ui.txtTelefone.setText(str(itens[16]))
            self.__ui.txtCelular.setText(str(itens[17]))
            #self.__ui.txtSetor.addItem(str(itens[18]))
            setor = str(itens[18])
            self.__ui.txtSetor.addItem(setor)
            self.pesquisarSetorAtualizar(setor)
            self.__ui.txtCargo.clear()
            cargo = str(itens[19])
            self.__ui.txtCargo.addItem(cargo)
            self.pesquisarCargoAtualizar(cargo, setor)
            self.__ui.txtFantasia.setText(str(itens[20]))
            self.__ui.txtRazaoSocial.setText(str(itens[21]))
            self.__ui.txtCnpj.setText(str(itens[22]))
            self.__ui.txtInscricaoEstadua.setText(str(itens[23]))

    def formatarDataRetorno(self, data):
        dia = data[8:10]
        mes = data[5:7]
        ano = data[:4]

        return QtCore.QDate(int(ano), int(mes), int(dia))

    def botaoEditarCadastro(self):
        self.__ui.btnCadNovo.setEnabled(False)
        self.__ui.btnCadEditar.setEnabled(True)
        self.__ui.btnCadCancelar.setEnabled(True)
        self.__ui.btnCadDeletar.setEnabled(True)

        self.__ui.txtFantasia.setEnabled(True)
        self.__ui.grbFuncionario.setEnabled(True)

        self.__ui.txtFantasia.setFocus()

    def _deletarEmpresa(self):

        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja excluir esse funcionario", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            __funDao = FuncionarioDao()
            __funDao.deletarFuncionario(self.__ui.txtidFuncionario.text())
            self.botaoCancelar()
            self.limparCampos()



    def atualizarFuncionario(self):
        if self.__ui.txtNomeFuncionario.text() and self.__ui.txtRg.text() and self.__ui.txtExpeditor.text() and self.__ui.txtCpf.text() and self.__ui.txtNomeMae.text() and self.__ui.txtNomePai.text() and self.__ui.txtEndereco.text() and self.__ui.txtNumero.text() and self.__ui.txtComplemento.text() and self.__ui.txtBairro.text() and self.__ui.txtCidades.text() and self.__ui.txtEstados.text() != "":
            _cidade = CidadesEstadosDao()
            _funDao = FuncionarioDao()

            idEmpresa = self.__ui.txtIdEmpresa.text()
            fantasia = self.__ui.txtFantasia.text()
            razaoSocial = self.__ui.txtRazaoSocial.text()

            idFuncionario = self.__ui.txtidFuncionario.text()
            nome = self.__ui.txtNomeFuncionario.text()
            rg = self.removerCaracter(self.__ui.txtRg.text())
            expeditor = self.__ui.txtExpeditor.text()
            cpf = self.removerCaracter(self.__ui.txtCpf.text())
            data = self.removerCaracter(self.__ui.txtDataNascimento.text())
            nascimento = self.formatarData(data)
            if self.__ui.radBtnMasculino.isChecked():
                sexo = 'MASCULINO'
            elif self.__ui.radBtnFeminino.isChecked():
                sexo = 'FEMININO'
            else:
                return None
            mae = self.__ui.txtNomeMae.text()
            pai = self.__ui.txtNomePai.text()
            endereco = self.__ui.txtEndereco.text()
            numero = self.__ui.txtNumero.text()
            complemento = self.__ui.txtComplemento.text()
            bairro = self.__ui.txtBairro.text()
            _cep = self.removerCaracter(self.__ui.txtCep.text())
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self.__ui.txtCidades.text(), self.__ui.txtEstados.text())
            else:
                return False
            telefone = self.removerCaracter(self.__ui.txtTelefone.text())
            celular = self.removerCaracter(self.__ui.txtCelular.text())

            funcao = _funDao.funcao(self.__ui.txtSetor.currentText(), self.__ui.txtCargo.currentText())
            __funcionario = Funcionario(idFuncionario, nome, rg, expeditor, cpf, nascimento, sexo, mae, pai, endereco, numero, complemento, bairro, _cida, telefone, celular, funcao, idEmpresa)
            _funDao.atualizarFuncioario(__funcionario)

            self.botaoCancelar()
            self.limparCampos()
        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from controller.ContatoEmail import ContatoEmail
from controller.ContatoTelefone import ContatoTelefone
from controller.getSetTipoEmpresa import TipoEmpresa
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.tipoEmpresaDao import TipoEmpresaDao
from telas.frmCadEmpresa import Ui_frmCadastroEmpresa
from dao.empresaDao import EmpresaDao
from controller.getSetEmpresa import Empresas
from .classCadSetoresCargos import SetoresCargos

class Empresa(QtGui.QDialog):


    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroEmpresa()
        self.ui.setupUi(self)
        self.contatoAdd = []
        self.contatoRemove = []
        self.emailAdd = []
        self.emailRemove = []

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnCancelar.clicked.connect(self.cancelar)


        self.ui.btnAddTelefone.clicked.connect(self.addDescricaoProduto)
        self.ui.btnRemoverTelefone.clicked.connect(self.delContatoTelefone)

        self.ui.txtCodigo.returnPressed.connect(self.setEmpresa)

        self.ui.txtCodigo.textChanged.connect(self.numberCodigo)
        self.ui.txtNumeroTelefone.textChanged.connect(self.numberTelefone)
        self.ui.txtInscricaoMunicipal.textChanged.connect(self.numberInscricaoMunicipal)

    def numberCodigo(self):
        if self.ui.txtCodigo.text().isnumeric() == False:
            self.ui.txtCodigo.backspace()

    def numberTelefone(self):
        if self.ui.txtNumeroTelefone.text().isnumeric() == False:
            self.ui.txtNumeroTelefone.backspace()

    def numberInscricaoMunicipal(self):
        if self.ui.txtInscricaoMunicipal.text().isnumeric() == False:
            self.ui.txtInscricaoMunicipal.backspace()

    def novo(self):
        self.limparCampos()
        self.ui.grbDadosPessoaJuridica.setEnabled(True)
        self.ui.grbTipoEmpresa.setEnabled(True)
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
        self.deletarRelacao()
        self.ui.grbDadosPessoaJuridica.setEnabled(False)
        self.ui.grbTipoEmpresa.setEnabled(False)
        self.ui.tabWiAdicionais.setEnabled(False)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)


    def limparCampos(self):
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtRazaoSocial.clear()
        self.ui.txtFantasia.clear()
        self.ui.cBoxTipoEmpresa.clear()
        self.ui.txtInscricaoMunicipal.clear()

        self.ui.txtContatoTelefone.clear()
        self.ui.txtContatoEmail.clear()

        self.ui.txtCadSetoresSetor.clear()
        self.ui.txtCadCargoCargo.clear()
        self.ui.txtRelacaoSetor.clear()
        self.ui.txtRelacaoCargo.clear()

        self.contatoAdd.clear()
        self.contatoRemove.clear()
        self.emailAdd.clear()
        self.emailRemove.clear()

        self.deletarContatoTelefone()
        self.deletarContatoEmail()
        self.deletarSetor()
        self.deletarCargo()
        self.deletarRelacao()

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

    def deletarRelacao(self):
        for i in reversed(range(self.ui.tabRelacao.rowCount())):
            self.ui.tabRelacao.removeRow(i)

    def desativarCampos(self):
        self.ui.grbDadosPessoaJuridica.setEnabled(False)
        self.ui.grbTipoEmpresa.setEnabled(False)
        self.ui.tabWiAdicionais.setEnabled(False)
        self.ui.btnNovo.setEnabled(True)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def setTipoEmpresa(self):
        empresa = EmpresaDao()
        lista = empresa.tipoEmpresa()

        for tipo in lista:
            self.ui.cBoxTipoEmpresa.addItem(tipo[0])

    def setEmpresa(self):
        empresa = EmpresaDao()
        emp = empresa.pesquisarPessoaJuridica(self.ui.txtCodigo.text())
        print(emp)
        for empres in emp:
            self.ui.txtCnpj.setText(str(empres[0]))
            self.ui.txtInscricaoEstadua.setText(str(empres[1]))
            self.ui.txtRazaoSocial.setText(str(empres[2]))
            self.ui.txtFantasia.setText(str(empres[3]))
        if emp == []:
            self.ui.txtCnpj.clear()
            self.ui.txtInscricaoEstadua.clear()
            self.ui.txtRazaoSocial.clear()
            self.ui.txtInscricaoEstadua.clear()

    def addDescricaoProduto(self):
        if self.ui.txtContatoTelefone.text() != "" and self.ui.txtNumeroTelefone.text() != "":
            __contato = str(self.ui.txtContatoTelefone.text())
            __telefone = str(self.ui.txtNumeroTelefone.text())

            add = [(__contato, __telefone)]
            self.contatoAdd.append([__contato, __telefone])
            self.inserirTabela(add)

            self.ui.txtContatoTelefone.clear()
            self.ui.txtNumeroTelefone.clear()

            self.ui.txtContatoTelefone.setFocus()
        else:
            QMessageBox.warning(QWidget(), 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def inserirTabela(self, dado):

        linha = self.ui.tabContatoTelefone.rowCount()
        for info in dado:
            self.ui.tabContatoTelefone.insertRow(linha)
            __contato = info[0]
            __telefone = info[1]


            self.ui.tabContatoTelefone.setItem(linha, 0, QtGui.QTableWidgetItem(str(__contato)))
            self.ui.tabContatoTelefone.setItem(linha, 1, QtGui.QTableWidgetItem(str(__telefone)))


            linha += 1
        print(self.contatoAdd)

    def contatoRemovido(self):
        itens = []
        for item in self.ui.tabContatoTelefone.selectedItems():
            itens.append(item.text())
        self.contatoRemove.append(itens)

    def delContatoTelefone(self):
        self.contatoRemovido()
        index = self.ui.tabContatoTelefone.currentRow()
        self.ui.tabContatoTelefone.removeRow(index)

        if index >= 0:
            del self.contatoAdd[index]
        else:
            QMessageBox.warning(QWidget(), 'Mensagem',"Impossivel realizar essa ação, por favor selecione um item da lista para excluir")


    def cadastrarTelefone(self):
        emp = EmpresaDao()
        empresa = emp.pesquisaEmpresa(self.ui.txtCodigo.text())
        i = 0
        for lista in self.contatoAdd:
            a = self.contatoAdd[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, empresa)
            emp.cadastrarTelefone(__descricao)

            i += 1

    def cadastrarEmail(self):
        emp = EmpresaDao()
        empresa = emp.pesquisaEmpresa(self.ui.txtCodigo.text())
        i = 0
        for lista in self.contatoAdd:
            a = self.emailAdd[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, empresa)
            emp.cadastrarEmail(__descricao)

            i += 1



    '''
        self._ui.btnPesquisar.clicked.connect(self.pesquisar)
        self._ui.txtPesquisa.returnPressed.connect(self.pesquisar)


        self._ui.btnNovo.clicked.connect(self._botoesNovo)
        self._ui.btnSalvar.clicked.connect(self._cadastroEmpresa)
        self._ui.btnCancelar.clicked.connect(self._cancelar)
        self._ui.btnEditar.clicked.connect(self._alterarEmpresa)
        self._ui.btnDeletar.clicked.connect(self._deletarEmpresa)
        self._ui.btnSetoressCargos.clicked.connect(self.setoresCargos)

        self._ui.txtCnpj.returnPressed.connect(self.focusInsEst)
        self._ui.txtInscricaoEstadua.returnPressed.connect(self.focusInsMun)
        self._ui.txtInscricaoMunicipal.returnPressed.connect(self.focusFantasia)
        self._ui.txtFantasia.returnPressed.connect(self.focusRazaoSocial)
        self._ui.txtRazaoSocial.returnPressed.connect(self.focusEndereco)
        self._ui.txtEndereco.returnPressed.connect(self.focusNumero)
        self._ui.txtNumero.returnPressed.connect(self.focusComplemento)
        self._ui.txtComplemento.returnPressed.connect(self.focusBairro)
        self._ui.txtBairro.returnPressed.connect(self.focusCep)
        self._ui.txtCep.returnPressed.connect(self.focusTelefone)
        self._ui.txtCep.editingFinished.connect(self.pesquisarCidade)
        self._ui.txtTelefone.returnPressed.connect(self.focusBotaoSalvar)

        self._ui.txtCnpj.editingFinished.connect(self.validacaoCnpj)


        self._ui.tbPesquisa.doubleClicked.connect(self.tablePesquisa)

        self._ui.txtCep.cursorPositionChanged.connect(self.positionCursorCep)
        self._ui.txtTelefone.cursorPositionChanged.connect(self.positionCursorTelefone)
        self._ui.txtCnpj.cursorPositionChanged.connect(self.positionCursorCnpj)

        self._ui.txtFantasia.textChanged.connect(self.upperFantasia)
        self._ui.txtRazaoSocial.textChanged.connect(self.upperRazao)
        self._ui.txtEndereco.textChanged.connect(self.upperEndereco)
        self._ui.txtNumero.textChanged.connect(self.upperNumero)
        self._ui.txtComplemento.textChanged.connect(self.upperComplemento)
        self._ui.txtBairro.textChanged.connect(self.upperBairro)


    def upperFantasia(self):
        self._ui.txtFantasia.setText(self._ui.txtFantasia.text().upper())

    def upperRazao(self):
        self._ui.txtRazaoSocial.setText(self._ui.txtRazaoSocial.text().upper())

    def upperEndereco(self):
        self._ui.txtEndereco.setText(self._ui.txtEndereco.text().upper())

    def upperNumero(self):
        self._ui.txtNumero.setText(self._ui.txtNumero.text().upper())

    def upperComplemento(self):
        self._ui.txtComplemento.setText(self._ui.txtComplemento.text().upper())

    def upperBairro(self):
        self._ui.txtBairro.setText(self._ui.txtBairro.text().upper())


    def positionCursorCep(self):
        texto = self.removerCaracter(self._ui.txtCep.text())
        if len(texto) == 0:
            self._ui.txtCep.setCursorPosition(0)
        elif len(texto) <= 4:
            b = len(texto)
            self._ui.txtCep.setCursorPosition(b)
        elif len(texto) >= 5 and len(texto) < 9:
            b = len(texto) + 1
            self._ui.txtCep.setCursorPosition(b)


    def positionCursorTelefone(self):
        texto = self.removerCaracter(self._ui.txtTelefone.text())
        if len(texto) == 0:
            self._ui.txtTelefone.setCursorPosition(1)
        elif len(texto) <= 1:
            b = len(texto) + 1
            self._ui.txtTelefone.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) < 7:
            b = len(texto) + 2
            self._ui.txtTelefone.setCursorPosition(b)
        elif len(texto) >= 7 and len(texto) < 12:
            b = len(texto) + 3
            self._ui.txtTelefone.setCursorPosition(b)


    def positionCursorCnpj(self):
        texto = self.removerCaracter(self._ui.txtCnpj.text())

        if len(texto) == 0:
            self._ui.txtCnpj.setCursorPosition(0)
        elif len(texto) <= 1:
            b = len(texto)
            self._ui.txtCnpj.setCursorPosition(b)
        elif len(texto) >= 2 and len(texto) < 5:
            b = len(texto) + 1
            self._ui.txtCnpj.setCursorPosition(b)
        elif len(texto) >= 5 and len(texto) < 8:
            b = len(texto) + 2
            self._ui.txtCnpj.setCursorPosition(b)
        elif len(texto) >= 8 and len(texto) < 12:
            b = len(texto) + 3
            self._ui.txtCnpj.setCursorPosition(b)
        elif len(texto) >= 12:
            b = len(texto) + 4
            self._ui.txtCnpj.setCursorPosition(b)


    def focusCnpj(self):
        self._ui.txtCnpj.setFocus()

    def focusInsEst(self):
        self._ui.txtInscricaoEstadua.setFocus()

    def focusInsMun(self):
        self._ui.txtInscricaoMunicipal.setFocus()

    def focusFantasia(self):
        self._ui.txtFantasia.setFocus()

    def focusRazaoSocial(self):
        self._ui.txtRazaoSocial.setFocus()

    def focusEndereco(self):
        self._ui.txtEndereco.setFocus()

    def focusNumero(self):
        self._ui.txtNumero.setFocus()

    def focusComplemento(self):
        self._ui.txtComplemento.setFocus()

    def focusBairro(self):
        self._ui.txtBairro.setFocus()

    def focusCep(self):
        self._ui.txtCep.setFocus()

    def focusTelefone(self):
        self._ui.txtTelefone.setFocus()

    def focusBotaoSalvar(self):
        self._ui.btnSalvar.setFocus()

    def _setTipoEmpresa(self):

        lista = self._empresa.tipoEmpresa()

        for tipo in lista:
            self._ui.txtTipoEmpresa.addItem(tipo[0])


    def setoresCargos(self):
        __setoresCargos = SetoresCargos()
        __setoresCargos.show()
        __setoresCargos.exec_()


    def pesquisarCidade(self):
        _cep = self.removerCaracter(self._ui.txtCep.text())
        if len(_cep) < 8:
            self._ui.txtCidades.clear()
            self._ui.txtEstados.clear()
        else:
            cidades = CidadesEstadosDao()
            cid = cidades.cidade(_cep)

            for cidade in cid:
                self._ui.txtCidades.setText(cidade[0])
                self._ui.txtEstados.setText(cidade[1])
            if cid == []:
                self._ui.txtCidades.clear()
                self._ui.txtEstados.clear()

    def validacaoCnpj(self):
        _cnpj = self.removerCaracter(self._ui.txtCnpj.text())
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

    def _cadastroEmpresa(self):
        _cnpj = self.removerCaracter(self._ui.txtCnpj.text())
        _cep = self.removerCaracter(self._ui.txtCep.text())
        _telefone = self.removerCaracter(self._ui.txtTelefone.text())

        if self._ui.txtInscricaoEstadua.text() != '' or self._ui.txtInscricaoMunicipal.text() == '' or self._ui.txtFantasia.text() == '' or self._ui.txtRazaoSocial.text() == '' or self._ui.txtEndereco.text() == '' or self._ui.txtNumero.text() == '' or self._ui.txtComplemento.text() == '' or self._ui.txtBairro.text() == '' or self._ui.txtCidades.text() == '' or self._ui.txtEstados.text() == '' or len(_cep) == 8 or len(_telefone) == 11 or len(_cnpj) == 14 :
            _valCnpj = self.validaCnpj(_cnpj)
            if _valCnpj == True :
                _empresa = EmpresaDao()
                _cidade = CidadesEstadosDao()



                _tipoEmpresa = _empresa.idTipoEmpresa(str(self._ui.txtTipoEmpresa.currentText()))
                _inscricaoEstadual = self._ui.txtInscricaoEstadua.text()
                _inscricaoMunicipal = self._ui.txtInscricaoMunicipal.text()
                _fantasia = self._ui.txtFantasia.text()
                _razaoSocial = self._ui.txtRazaoSocial.text()
                _endereco = self._ui.txtEndereco.text()
                _numero = self._ui.txtNumero.text()
                _complemento = self._ui.txtComplemento.text()
                _bairro = self._ui.txtBairro.text()
                _cel = _telefone
                _site = self._ui.txtSite.text()
                if len(_cep) == 8:
                    _cida = _cidade.idCidade(_cep, self._ui.txtCidades.text(), self._ui.txtEstados.text())
                else:
                    return None

                _cadastrar = Empresas(None, _tipoEmpresa, _cnpj, _inscricaoEstadual, _inscricaoMunicipal, _fantasia, _razaoSocial, _endereco, _numero, _complemento, _bairro, _cida, _cel, _site, 'Operando')
                self._empresa.cadastroEmpresa(_cadastrar)
                self._limparCampos()
                self._botoes()
        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")

    def _alterarEmpresa(self):
        _cnpj = self.removerCaracter(self._ui.txtCnpj.text())
        _cep = self.removerCaracter(self._ui.txtCep.text())
        _telefone = self.removerCaracter(self._ui.txtTelefone.text())

        if self._ui.txtInscricaoEstadua.text() != '' or self._ui.txtInscricaoMunicipal.text() == '' or self._ui.txtFantasia.text() == '' or self._ui.txtRazaoSocial.text() == '' or self._ui.txtEndereco.text() == '' or self._ui.txtNumero.text() == '' or self._ui.txtComplemento.text() == '' or self._ui.txtBairro.text() == '' or self._ui.txtCidades.text() == '' or self._ui.txtEstados.text() == '' or len(_cep) == 8 or len(_telefone) == 11 or len(_cnpj) == 14 :
            _empresa = EmpresaDao()
            _cidade = CidadesEstadosDao()


            _idEmpresa = self._ui.txtId.text()
            _tipoEmpresa = _empresa.idTipoEmpresa(str(self._ui.txtTipoEmpresa.currentText()))
            _inscricaoEstadual = self._ui.txtInscricaoEstadua.text()
            _inscricaoMunicipal = self._ui.txtInscricaoMunicipal.text()
            _fantasia = self._ui.txtFantasia.text()
            _razaoSocial = self._ui.txtRazaoSocial.text()
            _endereco = self._ui.txtEndereco.text()
            _numero = self._ui.txtNumero.text()
            _complemento = self._ui.txtComplemento.text()
            _bairro = self._ui.txtBairro.text()
            _cel = _telefone
            _site = self._ui.txtSite.text()
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self._ui.txtCidades.text(), self._ui.txtEstados.text())
            else:
                return False


            _atualizar = Empresas(_idEmpresa, _tipoEmpresa, _cnpj, _inscricaoEstadual, _inscricaoMunicipal, _fantasia, _razaoSocial, _endereco, _numero, _complemento, _bairro, _cida, _cel, _site, 'Operando')
            self._empresa.atualizarEmpresa(_atualizar)
            self._limparCampos()
            self._botoes()
        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")

    def _deletarEmpresa(self):

        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja excluir essa empresa", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self._empresa.deletarEmpresa(self._ui.txtId.text())
            self._limparCampos()
            self._botoes()



    def _cancelar(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Menssagem', "Deseja realmente cancelar a operação", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self._limparCampos()
            self._botoes()


    def _limparCampos(self):
        self._ui.txtId.clear()
        self._ui.txtTipoEmpresa.clear()
        self._ui.txtCnpj.clear()
        self._ui.txtInscricaoEstadua.clear()
        self._ui.txtInscricaoMunicipal.clear()
        self._ui.txtFantasia.clear()
        self._ui.txtRazaoSocial.clear()
        self._ui.txtEndereco.clear()
        self._ui.txtNumero.clear()
        self._ui.txtComplemento.clear()
        self._ui.txtBairro.clear()
        self._ui.txtCep.clear()
        self._ui.txtCidades.clear()
        self._ui.txtEstados.clear()
        self._ui.txtTelefone.clear()
        self._ui.txtSite.clear()
        self._ui.ckBoOperacional.setChecked(False)

    def _botoes(self):
        self._ui.btnNovo.setEnabled(True)

        self._ui.grubTextos.setEnabled(False)
        self._ui.btnSalvar.setEnabled(False)
        self._ui.btnEditar.setEnabled(False)
        self._ui.btnCancelar.setEnabled(False)
        self._ui.btnDeletar.setEnabled(False)
        self._ui.ckBoOperacional.setChecked(False)
        self._ui.ckBoOperacional.setEnabled(False)

    def _botoesNovo(self):

        self._ui.btnNovo.setEnabled(False)

        self._ui.grubTextos.setEnabled(True)
        self._ui.btnSalvar.setEnabled(True)
        self._ui.btnCancelar.setEnabled(True)
        self._setTipoEmpresa()

    def _botoesEditar(self):
        self._ui.btnNovo.setEnabled(False)

        self._ui.grubTextos.setEnabled(True)
        self._ui.btnEditar.setEnabled(True)
        self._ui.btnCancelar.setEnabled(True)
        self._ui.btnDeletar.setEnabled(True)
        self._ui.ckBoOperacional.setEnabled(True)
        #self._setTipoEmpresa()

    def pesquisar(self):
        if self._ui.radBtnCodigo.isChecked():
            _pesquisar = self._empresa.pesquisaCodigo(self._ui.txtPesquisa.text())

            qtde_registros = len(_pesquisar)
            self._ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisar:
                # capturando os dados da tupla

                codigo = pesqui[0]
                tipoEmpresa = pesqui[1]
                cnpj = pesqui[2]
                inscrEstadual = pesqui[3]
                inscrMunicipal = pesqui[4]
                fantasia = pesqui[5]
                razaoSocial = pesqui[6]
                endereco = pesqui[7]
                numero = pesqui[8]
                complemento = pesqui[9]
                bairro = pesqui[10]
                telefone = pesqui[11]
                site = pesqui[12]
                cep = pesqui[13]
                cidade = pesqui[14]
                estado = pesqui[15]
                situacao = pesqui[16]

                # preenchendo o grid de pesquisa
                self._ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self._ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipoEmpresa)))
                self._ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cnpj)))
                self._ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self._ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrMunicipal)))
                self._ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(fantasia)))
                self._ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(razaoSocial)))
                self._ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(endereco)))
                self._ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(numero)))
                self._ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(complemento)))
                self._ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(bairro)))
                self._ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(telefone)))
                self._ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(site)))
                self._ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cep)))
                self._ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(cidade)))
                self._ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(estado)))
                self._ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(situacao)))

                linha += 1

        elif self._ui.radBtnFantasia.isChecked():
            _pesquisarFantasia = self._empresa.pesquisaFantasia(str(self._ui.txtPesquisa.text()))

            qtde_registros = len(_pesquisarFantasia)
            self._ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarFantasia:
                # capturando os dados da tupla

                codigo = pesqui[0]
                tipoEmpresa = pesqui[1]
                cnpj = pesqui[2]
                inscrEstadual = pesqui[3]
                inscrMunicipal = pesqui[4]
                fantasia = pesqui[5]
                razaoSocial = pesqui[6]
                endereco = pesqui[7]
                numero = pesqui[8]
                complemento = pesqui[9]
                bairro = pesqui[10]
                telefone = pesqui[11]
                site = pesqui[12]
                cep = pesqui[13]
                cidade = pesqui[14]
                estado = pesqui[15]
                situacao = pesqui[16]

                # preenchendo o grid de pesquisa
                self._ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self._ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipoEmpresa)))
                self._ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cnpj)))
                self._ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self._ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrMunicipal)))
                self._ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(fantasia)))
                self._ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(razaoSocial)))
                self._ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(endereco)))
                self._ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(numero)))
                self._ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(complemento)))
                self._ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(bairro)))
                self._ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(telefone)))
                self._ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(site)))
                self._ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cep)))
                self._ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(cidade)))
                self._ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(estado)))
                self._ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(situacao)))

                linha += 1

        elif self._ui.radBtnRazaoSocial.isChecked():
            _pesquisarRazaoSocial = self._empresa.pesquisaRazaoSocial(str(self._ui.txtPesquisa.text()))

            qtde_registros = len(_pesquisarRazaoSocial)
            self._ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarRazaoSocial:
                # capturando os dados da tupla

                codigo = pesqui[0]
                tipoEmpresa = pesqui[1]
                cnpj = pesqui[2]
                inscrEstadual = pesqui[3]
                inscrMunicipal = pesqui[4]
                fantasia = pesqui[5]
                razaoSocial = pesqui[6]
                endereco = pesqui[7]
                numero = pesqui[8]
                complemento = pesqui[9]
                bairro = pesqui[10]
                telefone = pesqui[11]
                site = pesqui[12]
                cep = pesqui[13]
                cidade = pesqui[14]
                estado = pesqui[15]
                situacao = pesqui[16]

                # preenchendo o grid de pesquisa
                self._ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self._ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipoEmpresa)))
                self._ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cnpj)))
                self._ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self._ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrMunicipal)))
                self._ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(fantasia)))
                self._ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(razaoSocial)))
                self._ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(endereco)))
                self._ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(numero)))
                self._ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(complemento)))
                self._ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(bairro)))
                self._ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(telefone)))
                self._ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(site)))
                self._ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cep)))
                self._ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(cidade)))
                self._ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(estado)))
                self._ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(situacao)))

                linha += 1

        elif self._ui.radBtnCnpj.isChecked():
            _pesquisarCnpj = self._empresa.pesquisaCnpj(self._ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarCnpj)
            self._ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarCnpj:
                # capturando os dados da tupla

                codigo = pesqui[0]
                tipoEmpresa = pesqui[1]
                cnpj = pesqui[2]
                inscrEstadual = pesqui[3]
                inscrMunicipal = pesqui[4]
                fantasia = pesqui[5]
                razaoSocial = pesqui[6]
                endereco = pesqui[7]
                numero = pesqui[8]
                complemento = pesqui[9]
                bairro = pesqui[10]
                telefone = pesqui[11]
                site = pesqui[12]
                cep = pesqui[13]
                cidade = pesqui[14]
                estado = pesqui[15]
                situacao = pesqui[16]

                # preenchendo o grid de pesquisa
                self._ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self._ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipoEmpresa)))
                self._ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cnpj)))
                self._ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self._ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrMunicipal)))
                self._ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(fantasia)))
                self._ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(razaoSocial)))
                self._ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(endereco)))
                self._ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(numero)))
                self._ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(complemento)))
                self._ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(bairro)))
                self._ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(telefone)))
                self._ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(site)))
                self._ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cep)))
                self._ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(cidade)))
                self._ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(estado)))
                self._ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(situacao)))

                linha += 1

        elif self._ui.radBtnInsEstadual.isChecked():
            _pesquisarInsEstadual = self._empresa.pesquisaInscEstadual(self._ui.txtPesquisa.text())

            qtde_registros = len(_pesquisarInsEstadual)
            self._ui.tbPesquisa.setRowCount(qtde_registros)

            linha = 0
            for pesqui in _pesquisarInsEstadual:
                # capturando os dados da tupla

                codigo = pesqui[0]
                tipoEmpresa = pesqui[1]
                cnpj = pesqui[2]
                inscrEstadual = pesqui[3]
                inscrMunicipal = pesqui[4]
                fantasia = pesqui[5]
                razaoSocial = pesqui[6]
                endereco = pesqui[7]
                numero = pesqui[8]
                complemento = pesqui[9]
                bairro = pesqui[10]
                telefone = pesqui[11]
                site = pesqui[12]
                cep = pesqui[13]
                cidade = pesqui[14]
                estado = pesqui[15]
                situacao = pesqui[16]


                # preenchendo o grid de pesquisa
                self._ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self._ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipoEmpresa)))
                self._ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cnpj)))
                self._ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(inscrEstadual)))
                self._ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrMunicipal)))
                self._ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(fantasia)))
                self._ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(razaoSocial)))
                self._ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(endereco)))
                self._ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(numero)))
                self._ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(complemento)))
                self._ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(bairro)))
                self._ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(telefone)))
                self._ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(site)))
                self._ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(cep)))
                self._ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(cidade)))
                self._ui.tbPesquisa.setItem(linha, 15, QtGui.QTableWidgetItem(str(estado)))
                self._ui.tbPesquisa.setItem(linha, 16, QtGui.QTableWidgetItem(str(situacao)))

                linha += 1

        else:
            result = QMessageBox.warning(self, 'ATENÇÃO', "Selecione o dados de pesquisa desejado para realiza e pesquisa!")

    def _setTipoEmpresaAtualizar(self, dados):

        lista = self._empresa.tipoEmpresa()

        for tipo in lista:
            if tipo[0] != dados:
                self._ui.txtTipoEmpresa.addItem(tipo[0])

    def tablePesquisa(self, pesquisa):
        _cnpj = self.removerCaracter(self._ui.txtCnpj.text())
        _cep = self.removerCaracter(self._ui.txtCep.text())
        _telefone = self.removerCaracter(self._ui.txtTelefone.text())
        if self._ui.txtInscricaoEstadua.text() == '' and self._ui.txtInscricaoMunicipal.text() == '' and self._ui.txtFantasia.text() == '' and self._ui.txtRazaoSocial.text() == '' and self._ui.txtEndereco.text() == '' and self._ui.txtNumero.text() == '' and self._ui.txtComplemento.text() == '' and self._ui.txtBairro.text() == '' and self._ui.txtCidades.text() == '' and self._ui.txtEstados.text() == '' :
                self.setarCampos()
                self._ui.btnSetoressCargos.setEnabled(True)
        else:
                w = QWidget()
                result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em processo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.setarCampos()

    def setarCampos(self):

        itens = []
        for item in self._ui.tbPesquisa.selectedItems():
            itens.append(item.text())
        if len(itens) == 17:
            self._botoes()
            self._botoesEditar()
            self._ui.txtId.setText(str(itens[0]))
            tipo = str(itens[1])
            self._ui.txtTipoEmpresa.addItem(tipo)
            self._setTipoEmpresaAtualizar(tipo)
            self._ui.txtCnpj.setText(str(itens[2]))
            self._ui.txtInscricaoEstadua.setText(str(itens[3]))
            self._ui.txtInscricaoMunicipal.setText(str(itens[4]))
            self._ui.txtFantasia.setText(str(itens[5]))
            self._ui.txtRazaoSocial.setText(str(itens[6]))
            self._ui.txtEndereco.setText(str(itens[7]))
            self._ui.txtNumero.setText(str(itens[8]))
            self._ui.txtComplemento.setText(str(itens[9]))
            self._ui.txtBairro.setText(str(itens[10]))
            self._ui.txtTelefone.setText(str(itens[11]))
            self._ui.txtSite.setText(str(itens[12]))
            self._ui.txtCep.setText(str(itens[13]))
            self._ui.txtCidades.setText(str(itens[14]))
            self._ui.txtEstados.setText(str(itens[15]))
            if str(itens[16]) == 'Operando':
                self._ui.ckBoOperacional.setChecked(True)
            elif str(itens[16]) == 'Fechado':
                self._ui.ckBoOperacional.setChecked(False)


    def limparTela(self):
        self._ui.tbPesquisa.clear()
        self._ui.tbPesquisa.setColumnCount(17)
        self._ui.tbPesquisa.setHorizontalHeaderLabels(['COD.', 'Tipo Empresa', 'CNPJ', 'Ins. Estadual', 'Insc. Municipal', 'Fantasia', 'Razao Socil', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Telefone', 'Site', 'Cep', 'Cidade', 'Estado', 'Situação'])
    '''
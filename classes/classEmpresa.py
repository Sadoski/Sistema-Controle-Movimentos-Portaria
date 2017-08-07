import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from controller.getSetTipoEmpresa import TipoEmpresa
from dao.cidadesEstadosDao import CidadesEstadosDao
from dao.tipoEmpresaDao import TipoEmpresaDao
from telas.frmCadastroEmpresa import Ui_frmCadastroEmpresa
from dao.empresaDao import EmpresaDao
from controller.getSetEmpresa import Empresas

class Empresa(QtGui.QDialog):


    def __init__(self):
        QtGui.QDialog.__init__(self)
        self._ui = Ui_frmCadastroEmpresa()
        self._ui.setupUi(self)
        self._empresa = EmpresaDao()


        self._ui.btnPesquisar.clicked.connect(self.pesquisar)
        self._ui.txtPesquisa.returnPressed.connect(self.pesquisar)

        self._ui.btnNovo.clicked.connect(self._botoesNovo)
        self._ui.btnSalvar.clicked.connect(self._cadastroEmpresa)
        self._ui.btnCancelar.clicked.connect(self._cancelar)

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

    def validacaoCnpj(self):
        _cnpj = self.removerCaracter(self._ui.txtCnpj.text())
        if len(_cnpj) == 14:
            _val = self.validaCnpj(_cnpj)
            if _val == False:
                w = QWidget()
                result = QMessageBox.critical(w, 'Atenção', "CNPJ Invalido, por favor insira um CNPJ Valido")
                return False

    def formatarCpf(self, cnpj):
        return ("%s.%s.%s-%s" % (cnpj[0:3], cnpj[3:6], cnpj[6:9], cnpj[9:11]))

    def validarCpf(self, cpf):

        lista_validacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]

        cpf_invalidos = [11*str(i) for i in range(10)]
        if cpf in cpf_invalidos:
            w = QWidget()
            result = QMessageBox.critical(w, 'Atenção', "CNPJ Invalido, por favor insira um CNPJ Valido 1")
            return False

        if not cpf.isdigit():
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")

        if len(cpf) < 11:
            w = QWidget()
            result = QMessageBox.critical(w, 'Atenção', "CPF Invalido, por favor insira um CPF Valido 2")
            return False

        if len(cpf) > 11:
            w = QWidget()
            result = QMessageBox.critical(w, 'Atenção', "CPF Invalido, por favor insira um CPF Valido 3")
            return False

        selfcpf = [int(x) for x in cpf]

        cpf = selfcpf[:9]

        while len(cpf) < 11:

            r = sum([(len(cpf)+1-i)*v for i, v in [(x, cpf[x]) for x in range(len(cpf))]]) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
                cpf.append(f)

            return bool(cpf == selfcpf)


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

        if len(_cnpj) == 0 and self._ui.txtInscricaoEstadua.text() != "" and self._ui.txtFantasia.text() != "" and self._ui.txtRazaoSocial.text() != "" and self._ui.txtEndereco.text() != "" and self._ui.txtNumero.text() != "" and self._ui.txtBairro.text() != "" and len(_cep) == 0 and self._ui.txtCidades.text() != "" and self._ui.txtEstados.text() != "" and self._ui.txtTelefone.text() == "":
            _empresa = EmpresaDao()
            _cidade = CidadesEstadosDao()



            _tipoEmpresa = _empresa.idTipoEmpresa(str(self._ui.txtTipoEmpresa.currentText()))
            #_cnpj = self._ui.txtCnpj.text()
            _inscricaoEstadual = self._ui.txtInscricaoEstadua.text()
            _inscricaoMunicipal = self._ui.txtInscricaoMunicipal.text()
            _fantasia = self._ui.txtFantasia.text()
            _razaoSocial = self._ui.txtRazaoSocial.text()
            _endereco = self._ui.txtEndereco.text()
            _numero = self._ui.txtNumero.text()
            _complemento = self._ui.txtComplemento.text()
            _bairro = self._ui.txtBairro.text()
            _cel = _telefone
            if len(_cep) == 8:
                _cida = _cidade.idCidade(_cep, self._ui.txtCidades.text(), self._ui.txtEstados.text())
            else:
                return False

            #_site = self.__ui.txtSite.text()

            #_cadastrar = Empresas(None, _tipoEmpresa, _cnpj, _inscricaoEstadual, _inscricaoMunicipal, _fantasia, _razaoSocial, _endereco, _numero, _complemento, _bairro, _cida, _telefone)
            _cadastrar = self._empresa.cadastroEmpresa(_tipoEmpresa, _cnpj, _inscricaoEstadual, _fantasia, _razaoSocial, _endereco, _numero, _complemento, _bairro, _cida, _cel)
            self._limparCampos()
            self._botoesCad()
        else:
            w = QWidget()
            QMessageBox.warning(w, 'Atenção', "Por Favor preencha todos os campos!")



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

    def _botoes(self):
        self._ui.btnNovo.setEnabled(True)

        self._ui.grubTextos.setEnabled(False)
        self._ui.btnSalvar.setEnabled(False)
        self._ui.btnEditar.setEnabled(False)
        self._ui.btnCancelar.setEnabled(False)
        self._ui.btnDeletar.setEnabled(False)

    def _botoesNovo(self):

        self._ui.btnNovo.setEnabled(False)

        self._ui.grubTextos.setEnabled(True)
        self._ui.btnSalvar.setEnabled(True)
        self._ui.btnCancelar.setEnabled(True)
        self._setTipoEmpresa()

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
                #inscrMunicipal = pesqui[4]
                fantasia = pesqui[4]
                razaoSocial = pesqui[5]
                endereco = pesqui[6]
                numero = pesqui[7]
                complemento = pesqui[8]
                bairro = pesqui[9]
                telefone = pesqui[10]
                cep = pesqui[11]
                cidade = pesqui[12]
                estado = pesqui[13]
                #site = pesqui[14]


                # preenchendo o grid de pesquisa
                self._ui.tbPesquisa.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
                self._ui.tbPesquisa.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipoEmpresa)))
                self._ui.tbPesquisa.setItem(linha, 2, QtGui.QTableWidgetItem(str(cnpj)))
                self._ui.tbPesquisa.setItem(linha, 3, QtGui.QTableWidgetItem(str(inscrEstadual)))
                #self._ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscrMunicipal)))
                self._ui.tbPesquisa.setItem(linha, 4, QtGui.QTableWidgetItem(str(fantasia)))
                self._ui.tbPesquisa.setItem(linha, 5, QtGui.QTableWidgetItem(str(razaoSocial)))
                self._ui.tbPesquisa.setItem(linha, 6, QtGui.QTableWidgetItem(str(endereco)))
                self._ui.tbPesquisa.setItem(linha, 7, QtGui.QTableWidgetItem(str(numero)))
                self._ui.tbPesquisa.setItem(linha, 8, QtGui.QTableWidgetItem(str(complemento)))
                self._ui.tbPesquisa.setItem(linha, 9, QtGui.QTableWidgetItem(str(bairro)))
                self._ui.tbPesquisa.setItem(linha, 10, QtGui.QTableWidgetItem(str(telefone)))
                self._ui.tbPesquisa.setItem(linha, 11, QtGui.QTableWidgetItem(str(cep)))
                self._ui.tbPesquisa.setItem(linha, 12, QtGui.QTableWidgetItem(str(cidade)))
                self._ui.tbPesquisa.setItem(linha, 13, QtGui.QTableWidgetItem(str(estado)))
                #self._ui.tbPesquisa.setItem(linha, 14, QtGui.QTableWidgetItem(str(site)))
                linha += 1


        elif self._ui.radBtnFantasia.isChecked():
            pesquisar = self._empresa.pesquisaFantasia()
        elif self._ui.radBtnRazaoSocial.isChecked():
            pesquisar = self._empresa.pesquisaRazaoSocial()
        elif self._ui.radBtnCnpj.isChecked():
            pesquisar = self._empresa.pesquisaCnpj()
        elif self._ui.radBtnInsEstadual.isChecked():
            pesquisar = self._empresa.pesquisaInscEstadual()
        else:
            result = QMessageBox.warning(self, 'ATENÇÃO', "Um dos campos 'Marca' ou 'Barra' dever ser selecionado")

    def tablePesquisa(self, pesquisa):
        _tabela = self.tbPesquisa.model().data(pesquisa).toString()
        self._empresa.pesquisa(_tabela)




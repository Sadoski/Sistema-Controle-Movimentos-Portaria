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
        self._ui.btnEditar.clicked.connect(self._alterarEmpresa)
        self._ui.btnDeletar.clicked.connect(self._deletarEmpresa)

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
            self._botoes



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

    def tablePesquisa(self, pesquisa):
        ''''
                indexes = []
        for selectionRange in self._ui.tbPesquisa.selectedRanges():
            indexes.extend(range(selectionRange.topRow(), selectionRange.bottomRow() + 1))
            print("indexes", indexes)

        for i in indexes:
            print("specific item", self._ui.tbPesquisa.item(i, 1).text())
            #print(results.append(str(self._ui.tbPesquisa.item(i, 1).text())))
        '''
        if self._ui.txtInscricaoEstadua.text() != '' or self._ui.txtInscricaoMunicipal.text() == '' or self._ui.txtFantasia.text() == '' or self._ui.txtRazaoSocial.text() == '' or self._ui.txtEndereco.text() == '' or self._ui.txtNumero.text() == '' or self._ui.txtComplemento.text() == '' or self._ui.txtBairro.text() == '' or self._ui.txtCidades.text() == '' or self._ui.txtEstados.text() == '' or len(_cep) == 8 or len(_telefone) == 11 or len(_cnpj) == 14 :
            w = QWidget()
            result = QMessageBox.question(w, 'Menssagem', "Tem certeza que deseja realizar essa operação sem finalizar a operação em precesso", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                itens = []
                for item in self._ui.tbPesquisa.selectedItems():
                    itens.append(item.text())
                if len(itens) == 17:
                    self._botoes()
                    self._botoesEditar()
                    self._ui.txtId.setText(str(itens[0]))
                    self._ui.txtTipoEmpresa.addItem(str(itens[1]))
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

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
        self._setTipoEmpresa()



        self._ui.btnSalvar.clicked.connect(self._cadastroEmpresa)

        self._ui.txtCnpj.returnPressed.connect(self.focusInsEst)
        self._ui.txtInscricaoEstadua.returnPressed.connect(self.focusInsMun)
        self._ui.txtInscricaoMunicipal.returnPressed.connect(self.focusFantasia)
        self._ui.txtFantasia.returnPressed.connect(self.focusRazaoSocial)
        self._ui.txtRazaoSocial.returnPressed.connect(self.focusEndereco)
        self._ui.txtEndereco.returnPressed.connect(self.focusNumero)
        self._ui.txtNumero.returnPressed.connect(self.focusComplemento)
        self._ui.txtComplemento.returnPressed.connect(self.focusBairro)
        self._ui.txtBairro.returnPressed.connect(self.focusCep)
        self._ui.txtCep.returnPressed.connect(self.pesquisarCidade)
        self._ui.txtTelefone.returnPressed.connect(self.focusBotaoSalvar)

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
        cidades = CidadesEstadosDao()
        cid = cidades.cidade(_cep)

        for cidade in cid:
            self._ui.txtCidades.setText(cidade[0])
            self._ui.txtEstados.setText(cidade[1])
        self._ui.txtTelefone.setFocus()


    def formatarCpf(self, cnpj):
        return ("%s.%s.%s-%s" % (cnpj[0:3], cnpj[3:6], cnpj[6:9], cnpj[9:11]))

    def validarCpf(self, cpf):

        lista_validacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]

        cpf_invalidos = [11*str(i) for i in range(10)]
        if cpf in cpf_invalidos:
            w = QWidget()
            result = QMessageBox.critical(w, 'Atenção', "CNPJ Invalido, por favor insira um CNPJ Valido")
            return False

        if not cpf.isdigit():
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")

        if len(cpf) < 11:
            w = QWidget()
            result = QMessageBox.critical(w, 'Atenção', "CPF Invalido, por favor insira um CPF Valido")
            return False

        if len(cpf) > 11:
            w = QWidget()
            result = QMessageBox.critical(w, 'Atenção', "CPF Invalido, por favor insira um CPF Valido")
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
        i = i.replace('\\', '')
        return i

    def _cadastroEmpresa(self):
        _cnpj = self.removerCaracter(self._ui.txtCnpj.text())
        _cep = self.removerCaracter(self._ui.txtCep.text())
        _telefone = self.removerCaracter(self._ui.txtTelefone.text())

        #if self._ui.txtCnpj.text() == "" or self._ui.txtInscricaoEstadua.text() == "" or self._ui.txtFantasia.text() == "" or self._ui.txtRazaoSocial.text() == "" or self._ui.txtEndereco.text() == "" or self._ui.txtNumero.text() == "" or self._ui.txtBairro.text() == "" or self._ui.txtCep.text() == "" or self._ui.txtCidades.text() == "" or self._ui.txtEstados.text() == "" or self._ui.txtTelefone.text() == "":
        _empresa = EmpresaDao()
        _cidade = CidadesEstadosDao()



        _tipoEmpresa = _empresa.idTipoEmpresa(str(self._ui.txtTipoEmpresa.currentText()))
        _cnpj = self._ui.txtCnpj.text()
        _inscricaoEstadual = self._ui.txtInscricaoEstadua.text()
        _inscricaoMunicipal = self._ui.txtInscricaoMunicipal.text()
        _fantasia = self._ui.txtFantasia.text()
        _razaoSocial = self._ui.txtRazaoSocial.text()
        _endereco = self._ui.txtEndereco.text()
        _numero = self._ui.txtNumero.text()
        _complemento = self._ui.txtComplemento.text()
        _bairro = self._ui.txtBairro.text()
        _telefone = self._ui.txtTelefone.text()
        if len(_cep) == 8:
            _cida = _cidade.idCidade(_cep, self._ui.txtCidades.text(), self._ui.txtEstados.text())
        else:
            _cida = None

        #_site = self.__ui.txtSite.text()

        #_cadastrar = Empresas(None, _tipoEmpresa, _cnpj, _inscricaoEstadual, _inscricaoMunicipal, _fantasia, _razaoSocial, _endereco, _numero, _complemento, _bairro, _cida, _telefone)
        _cadastrar = self._empresa.cadastroEmpresa(_tipoEmpresa, _cnpj, _inscricaoEstadual, _fantasia, _razaoSocial, _endereco, _numero, _complemento, _bairro, _cida, _telefone)



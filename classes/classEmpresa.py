import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmCadastroEmpresa import Ui_frmCadastroEmpresa
from dao.tipoEmpresaDao import tipoEmpresaDao

class Empresa(QtGui.QDialog):
    __idCidade = 0

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.__ui = Ui_frmCadastroEmpresa()
        self.__ui.setupUi(self)
        self.__tipoEmpresa = tipoEmpresaDao()
        self.__setTipoEmpresa()



        self.__ui.btnSalvar.clicked.connect(self.__cadastroEmpresa)

    def __setTipoEmpresa(self):

        lista = self.__tipoEmpresa.tipoEmpresa()

        for tipo in lista:
            self.__ui.txtTipoEmpresa.addItem(tipo[0])


    def pesquisarCidade(self):
        __cep = self.removerCaracter(self.__ui.txtCep.text())
        cid = self.__tipoEmpresa.pesquisarCidades(__cep)

        for cidade in cid:
            self.__idCidade = cidade[0]
            self.__ui.txtCidades.setText(cidade[1])
            self.__ui.txtEstados.setText(cidade[2])



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

    def __cadastroEmpresa(self):
        __empresa = tipoEmpresaDao()

        __tipoEmpresa = self.__ui.txtTipoEmpresa.currentText()
        __cnpj = self.__ui.txtCnpj.text()
        __inscricaoEstadual = self.__ui.txtInscricaoEstadua.text()
        __inscricaoMunicipal = self.__ui.txtInscricaoMunicipal.text()
        __fantasia = self.__ui.txtFantasia.text()
        __razaoSocial = self.__ui.txtRazaoSocial.text()
        __endereco = self.__ui.txtEndereco.text()
        __numero = self.__ui.txtNumero.text()
        __complemento = self.__ui.txtComplemento.text()
        __bairro = self.__ui.txtBairro.text()
        __cidade = self.__idCidade
        __telefone = self.__ui.txtTelefone.text()
        #__site = self.__ui.txtSite.text()

        __empresa.cadastroEmpresa(__tipoEmpresa, __cnpj, __inscricaoEstadual, __inscricaoMunicipal, __fantasia, __razaoSocial, __endereco, __numero, __complemento, __bairro, __cidade, __telefone)
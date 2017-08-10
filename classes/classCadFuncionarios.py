import sys
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dao.empresaDao import EmpresaDao
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
        #self.__ui.txtDataNascimento.returnPressed.connect(self.focusNomeMae)
        self.__ui.txtNomeMae.returnPressed.connect(self.focusNomePai)
        self.__ui.txtNomePai.returnPressed.connect(self.focusEndereco)
        self.__ui.txtEndereco.returnPressed.connect(self.focusNumero)
        self.__ui.txtNumero.returnPressed.connect(self.focusComplemento)
        self.__ui.txtComplemento.returnPressed.connect(self.focusBairro)
        self.__ui.txtBairro.returnPressed.connect(self.focusCep)
        self.__ui.txtCep.returnPressed.connect(self.focusTelefone)
        self.__ui.txtTelefone.returnPressed.connect(self.focusCelular)
        self.__ui.txtCelular.returnPressed.connect(self.focusSetores)

        self.__ui.txtFantasia.editingFinished.connect(self.pesquisarEmpresa)
        self.__ui.txtCpf.editingFinished.connect(self.validacaoCpf)

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

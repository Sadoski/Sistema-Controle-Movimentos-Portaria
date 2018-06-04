# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmRelatorio.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmRelatorio(object):
    def setupUi(self, frmRelatorio):
        frmRelatorio.setObjectName(_fromUtf8("frmRelatorio"))
        frmRelatorio.resize(979, 590)
        font = QtGui.QFont()
        font.setPointSize(9)
        frmRelatorio.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/relatorio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmRelatorio.setWindowIcon(icon)
        frmRelatorio.setSizeGripEnabled(True)
        frmRelatorio.setModal(True)

        self.tabPesquisar = QtGui.QTableWidget(frmRelatorio)
        self.tabPesquisar.setEnabled(False)
        self.tabPesquisar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 140, 960, 371))
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.verticalHeader().setVisible(False)
        self.tabPesquisar.verticalHeader().setCascadingSectionResizes(True)

        self.btnPesquisar = QtGui.QPushButton(frmRelatorio)
        self.btnPesquisar.setEnabled(False)
        self.btnPesquisar.setGeometry(QtCore.QRect(930, 100, 31, 26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.txtPesquisar = QtGui.QLineEdit(frmRelatorio)
        self.txtPesquisar.setEnabled(False)
        self.txtPesquisar.setGeometry(QtCore.QRect(560, 100, 361, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.btnGerarCsv = QtGui.QPushButton(frmRelatorio)
        self.btnGerarCsv.setEnabled(False)
        self.btnGerarCsv.setGeometry(QtCore.QRect(600, 530, 161, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/csv.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGerarCsv.setIcon(icon1)
        self.btnGerarCsv.setIconSize(QtCore.QSize(20, 20))
        self.btnGerarCsv.setObjectName(_fromUtf8("btnGerarCsv"))

        self.btnGerarHtml = QtGui.QPushButton(frmRelatorio)
        self.btnGerarHtml.setEnabled(False)
        self.btnGerarHtml.setGeometry(QtCore.QRect(770, 530, 161, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/html.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGerarHtml.setIcon(icon2)
        self.btnGerarHtml.setIconSize(QtCore.QSize(20, 20))
        self.btnGerarHtml.setObjectName(_fromUtf8("btnGerarHtml"))

        self.grbTipoRelatorio = QtGui.QGroupBox(frmRelatorio)
        self.grbTipoRelatorio.setGeometry(QtCore.QRect(10, 10, 511, 111))
        self.grbTipoRelatorio.setObjectName(_fromUtf8("grbTipoRelatorio"))

        self.radBtnFuncionario = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnFuncionario.setGeometry(QtCore.QRect(20, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnFuncionario.setFont(font)
        self.radBtnFuncionario.setObjectName(_fromUtf8("radBtnFuncionario"))

        self.radBtnPessoaJuridica = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnPessoaJuridica.setGeometry(QtCore.QRect(20, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnPessoaJuridica.setFont(font)
        self.radBtnPessoaJuridica.setObjectName(_fromUtf8("radBtnPessoaJuridica"))

        self.radBtnEmpresa = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnEmpresa.setGeometry(QtCore.QRect(20, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnEmpresa.setFont(font)
        self.radBtnEmpresa.setObjectName(_fromUtf8("radBtnEmpresa"))
        self.radBtnEntSaiFuncionario = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnEntSaiFuncionario.setGeometry(QtCore.QRect(270, 60, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnEntSaiFuncionario.setFont(font)
        self.radBtnEntSaiFuncionario.setObjectName(_fromUtf8("radBtnEntSaiFuncionario"))

        self.radBtnEntSaiDescarregamento = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnEntSaiDescarregamento.setGeometry(QtCore.QRect(270, 40, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnEntSaiDescarregamento.setFont(font)
        self.radBtnEntSaiDescarregamento.setObjectName(_fromUtf8("radBtnEntSaiDescarregamento"))

        self.radBtnPessoaFisica = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnPessoaFisica.setGeometry(QtCore.QRect(20, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnPessoaFisica.setFont(font)
        self.radBtnPessoaFisica.setObjectName(_fromUtf8("radBtnPessoaFisica"))

        self.radBtnNf = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnNf.setGeometry(QtCore.QRect(150, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnNf.setFont(font)
        self.radBtnNf.setObjectName(_fromUtf8("radBtnNf"))

        self.radBtnFornecedor = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnFornecedor.setGeometry(QtCore.QRect(150, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnFornecedor.setFont(font)
        self.radBtnFornecedor.setObjectName(_fromUtf8("radBtnFornecedor"))

        self.radBtnEntSaiCarregamento = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnEntSaiCarregamento.setGeometry(QtCore.QRect(270, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnEntSaiCarregamento.setFont(font)
        self.radBtnEntSaiCarregamento.setObjectName(_fromUtf8("radBtnEntSaiCarregamento"))

        self.radBtnUsuarios = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnUsuarios.setGeometry(QtCore.QRect(150, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnUsuarios.setFont(font)
        self.radBtnUsuarios.setObjectName(_fromUtf8("radBtnUsuarios"))

        self.radBtnCliente = QtGui.QRadioButton(self.grbTipoRelatorio)
        self.radBtnCliente.setGeometry(QtCore.QRect(150, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radBtnCliente.setFont(font)
        self.radBtnCliente.setObjectName(_fromUtf8("radBtnCliente"))

        self.grbPesquisaRelatorio = QtGui.QGroupBox(frmRelatorio)
        self.grbPesquisaRelatorio.setEnabled(False)
        self.grbPesquisaRelatorio.setGeometry(QtCore.QRect(530, 10, 431, 71))
        self.grbPesquisaRelatorio.setObjectName(_fromUtf8("grbPesquisaRelatorio"))

        self.radBtn1 = QtGui.QRadioButton(self.grbPesquisaRelatorio)
        self.radBtn1.setGeometry(QtCore.QRect(20, 20, 131, 17))
        self.radBtn1.setText(_fromUtf8(""))
        self.radBtn1.setObjectName(_fromUtf8("radBtn1"))

        self.radBtn2 = QtGui.QRadioButton(self.grbPesquisaRelatorio)
        self.radBtn2.setGeometry(QtCore.QRect(20, 40, 131, 17))
        self.radBtn2.setText(_fromUtf8(""))
        self.radBtn2.setObjectName(_fromUtf8("radBtn2"))

        self.radBtn4 = QtGui.QRadioButton(self.grbPesquisaRelatorio)
        self.radBtn4.setGeometry(QtCore.QRect(160, 40, 121, 17))
        self.radBtn4.setText(_fromUtf8(""))
        self.radBtn4.setObjectName(_fromUtf8("radBtn4"))

        self.radBtn3 = QtGui.QRadioButton(self.grbPesquisaRelatorio)
        self.radBtn3.setGeometry(QtCore.QRect(160, 20, 121, 17))
        self.radBtn3.setText(_fromUtf8(""))
        self.radBtn3.setObjectName(_fromUtf8("radBtn3"))

        self.radBtn5 = QtGui.QRadioButton(self.grbPesquisaRelatorio)
        self.radBtn5.setGeometry(QtCore.QRect(300, 20, 121, 17))
        self.radBtn5.setText(_fromUtf8(""))
        self.radBtn5.setObjectName(_fromUtf8("radBtn5"))

        self.radBtn6 = QtGui.QRadioButton(self.grbPesquisaRelatorio)
        self.radBtn6.setGeometry(QtCore.QRect(300, 40, 121, 17))
        self.radBtn6.setText(_fromUtf8(""))
        self.radBtn6.setObjectName(_fromUtf8("radBtn6"))

        self.retranslateUi(frmRelatorio)
        QtCore.QMetaObject.connectSlotsByName(frmRelatorio)

    def retranslateUi(self, frmRelatorio):
        frmRelatorio.setWindowTitle(_translate("frmRelatorio", "Relatório", None))
        self.tabPesquisar.setWhatsThis(_translate("frmRelatorio", "Tabela de pré-visualização", None))
        self.txtPesquisar.setToolTip(_translate("frmRelatorio", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmRelatorio", "Campo para inserir o dado para pesquisar e gerar a pré-vicualização e relatório", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmRelatorio", "Pesquisar", None))
        self.btnGerarCsv.setToolTip(_translate("frmRelatorio", "Gerar Relatório CSV", None))
        self.btnGerarCsv.setWhatsThis(_translate("frmRelatorio", "Botão para gerar o relatório e arquivo CSV", None))
        self.btnGerarCsv.setText(_translate("frmRelatorio", "Gerar Relatório CSV", None))
        self.btnGerarHtml.setToolTip(_translate("frmRelatorio", "Gerar Relatório HTML", None))
        self.btnGerarHtml.setWhatsThis(_translate("frmRelatorio", "Botão para gerar o relatório e arquivo HTML", None))
        self.btnGerarHtml.setText(_translate("frmRelatorio", "Gerar Relatório HTML", None))
        self.grbTipoRelatorio.setTitle(_translate("frmRelatorio", "Escolha de Relatório", None))
        self.radBtnFuncionario.setText(_translate("frmRelatorio", "Funcionario", None))
        self.radBtnPessoaJuridica.setText(_translate("frmRelatorio", "Pessoa Jurídica", None))
        self.radBtnEmpresa.setText(_translate("frmRelatorio", "Empresa", None))
        self.radBtnEntSaiFuncionario.setText(_translate("frmRelatorio", "Entrada e Saída Funcionario", None))
        self.radBtnEntSaiDescarregamento.setText(_translate("frmRelatorio", "Entrada e Saída Descarregamento", None))
        self.radBtnPessoaFisica.setText(_translate("frmRelatorio", "Pessoa Fisíca", None))
        self.radBtnNf.setText(_translate("frmRelatorio", "Notas Fiscal", None))
        self.radBtnFornecedor.setText(_translate("frmRelatorio", "Fornecedor", None))
        self.radBtnEntSaiCarregamento.setText(_translate("frmRelatorio", "Entrada e Saída Carregmento", None))
        self.radBtnUsuarios.setText(_translate("frmRelatorio", "Usuario", None))
        self.radBtnCliente.setText(_translate("frmRelatorio", "Cliente", None))
        self.grbPesquisaRelatorio.setTitle(_translate("frmRelatorio", "Pesquisa Relatorio", None))
        self.radBtn1.setWhatsThis(_translate("frmRelatorio", "Item de seleção para pesquisa", None))
        self.radBtn2.setWhatsThis(_translate("frmRelatorio", "Item de seleção para pesquisa", None))
        self.radBtn4.setWhatsThis(_translate("frmRelatorio", "Item de seleção para pesquisa", None))
        self.radBtn3.setWhatsThis(_translate("frmRelatorio", "Item de seleção para pesquisa", None))
        self.radBtn5.setWhatsThis(_translate("frmRelatorio", "Item de seleção para pesquisa", None))
        self.radBtn6.setWhatsThis(_translate("frmRelatorio", "Item de seleção para pesquisa", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCadastroVeiculosEmpresa.ui'
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

class Ui_frmCadastroVeiculosEmpresa(object):
    def setupUi(self, frmCadastroVeiculosEmpresa):
        frmCadastroVeiculosEmpresa.setObjectName(_fromUtf8("frmCadastroVeiculosEmpresa"))
        frmCadastroVeiculosEmpresa.resize(591, 420)
        font = QtGui.QFont()
        font.setPointSize(11)
        frmCadastroVeiculosEmpresa.setFont(font)
        self.grbBotoes = QtGui.QGroupBox(frmCadastroVeiculosEmpresa)
        self.grbBotoes.setGeometry(QtCore.QRect(10, 335, 571, 80))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))
        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(80, 10, 81, 61))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))
        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setGeometry(QtCore.QRect(380, 10, 81, 61))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnDeletar = QtGui.QPushButton(self.grbBotoes)
        self.btnDeletar.setGeometry(QtCore.QRect(480, 10, 81, 61))
        self.btnDeletar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnDeletar.setObjectName(_fromUtf8("btnDeletar"))
        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setGeometry(QtCore.QRect(180, 10, 81, 61))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        self.btnEditar = QtGui.QPushButton(self.grbBotoes)
        self.btnEditar.setGeometry(QtCore.QRect(280, 10, 81, 61))
        self.btnEditar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))
        self.grbDadosVeiculos = QtGui.QGroupBox(frmCadastroVeiculosEmpresa)
        self.grbDadosVeiculos.setGeometry(QtCore.QRect(10, 160, 571, 171))
        self.grbDadosVeiculos.setObjectName(_fromUtf8("grbDadosVeiculos"))
        self.txtMarca = QtGui.QLineEdit(self.grbDadosVeiculos)
        self.txtMarca.setGeometry(QtCore.QRect(230, 60, 331, 25))
        self.txtMarca.setMaxLength(50)
        self.txtMarca.setObjectName(_fromUtf8("txtMarca"))
        self.txtModelo = QtGui.QLineEdit(self.grbDadosVeiculos)
        self.txtModelo.setGeometry(QtCore.QRect(10, 130, 331, 25))
        self.txtModelo.setMaxLength(50)
        self.txtModelo.setObjectName(_fromUtf8("txtModelo"))
        self.txtPlaca = QtGui.QLineEdit(self.grbDadosVeiculos)
        self.txtPlaca.setGeometry(QtCore.QRect(350, 130, 211, 25))
        self.txtPlaca.setObjectName(_fromUtf8("txtPlaca"))
        self.lblMarca = QtGui.QLabel(self.grbDadosVeiculos)
        self.lblMarca.setGeometry(QtCore.QRect(230, 40, 51, 19))
        self.lblMarca.setObjectName(_fromUtf8("lblMarca"))
        self.lblModelo = QtGui.QLabel(self.grbDadosVeiculos)
        self.lblModelo.setGeometry(QtCore.QRect(10, 110, 61, 19))
        self.lblModelo.setObjectName(_fromUtf8("lblModelo"))
        self.lblPlaca = QtGui.QLabel(self.grbDadosVeiculos)
        self.lblPlaca.setGeometry(QtCore.QRect(350, 110, 51, 19))
        self.lblPlaca.setObjectName(_fromUtf8("lblPlaca"))
        self.comboBox = QtGui.QComboBox(self.grbDadosVeiculos)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 211, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lblTipoVeiculo = QtGui.QLabel(self.grbDadosVeiculos)
        self.lblTipoVeiculo.setGeometry(QtCore.QRect(10, 40, 111, 19))
        self.lblTipoVeiculo.setObjectName(_fromUtf8("lblTipoVeiculo"))
        self.grbEmpresa = QtGui.QGroupBox(frmCadastroVeiculosEmpresa)
        self.grbEmpresa.setGeometry(QtCore.QRect(10, 10, 571, 151))
        self.grbEmpresa.setObjectName(_fromUtf8("grbEmpresa"))
        self.lblCadSetoresCnpj = QtGui.QLabel(self.grbEmpresa)
        self.lblCadSetoresCnpj.setGeometry(QtCore.QRect(196, 82, 66, 19))
        self.lblCadSetoresCnpj.setObjectName(_fromUtf8("lblCadSetoresCnpj"))
        self.lblCadSetoresCodigo = QtGui.QLabel(self.grbEmpresa)
        self.lblCadSetoresCodigo.setGeometry(QtCore.QRect(14, 30, 51, 19))
        self.lblCadSetoresCodigo.setObjectName(_fromUtf8("lblCadSetoresCodigo"))
        self.txtCadSetoresCodigo = QtGui.QLineEdit(self.grbEmpresa)
        self.txtCadSetoresCodigo.setGeometry(QtCore.QRect(11, 50, 155, 25))
        self.txtCadSetoresCodigo.setMaxLength(11)
        self.txtCadSetoresCodigo.setObjectName(_fromUtf8("txtCadSetoresCodigo"))
        self.txtCadSetoresTipoEmpresa = QtGui.QLineEdit(self.grbEmpresa)
        self.txtCadSetoresTipoEmpresa.setEnabled(False)
        self.txtCadSetoresTipoEmpresa.setGeometry(QtCore.QRect(10, 102, 183, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtCadSetoresTipoEmpresa.setPalette(palette)
        self.txtCadSetoresTipoEmpresa.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCadSetoresTipoEmpresa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtCadSetoresTipoEmpresa.setMaxLength(50)
        self.txtCadSetoresTipoEmpresa.setObjectName(_fromUtf8("txtCadSetoresTipoEmpresa"))
        self.btnCadSetoresPesquisar = QtGui.QPushButton(self.grbEmpresa)
        self.btnCadSetoresPesquisar.setGeometry(QtCore.QRect(530, 50, 31, 27))
        self.btnCadSetoresPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCadSetoresPesquisar.setText(_fromUtf8(""))
        self.btnCadSetoresPesquisar.setObjectName(_fromUtf8("btnCadSetoresPesquisar"))
        self.txtCadSetoresInscricaoEstadual = QtGui.QLineEdit(self.grbEmpresa)
        self.txtCadSetoresInscricaoEstadual.setEnabled(False)
        self.txtCadSetoresInscricaoEstadual.setGeometry(QtCore.QRect(380, 102, 181, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtCadSetoresInscricaoEstadual.setPalette(palette)
        self.txtCadSetoresInscricaoEstadual.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCadSetoresInscricaoEstadual.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtCadSetoresInscricaoEstadual.setMaxLength(8)
        self.txtCadSetoresInscricaoEstadual.setObjectName(_fromUtf8("txtCadSetoresInscricaoEstadual"))
        self.txtCadSetoresNomeFantasia = QtGui.QLineEdit(self.grbEmpresa)
        self.txtCadSetoresNomeFantasia.setGeometry(QtCore.QRect(170, 50, 351, 25))
        self.txtCadSetoresNomeFantasia.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCadSetoresNomeFantasia.setMaxLength(70)
        self.txtCadSetoresNomeFantasia.setObjectName(_fromUtf8("txtCadSetoresNomeFantasia"))
        self.lblCadSetoresNomeFantasia = QtGui.QLabel(self.grbEmpresa)
        self.lblCadSetoresNomeFantasia.setGeometry(QtCore.QRect(170, 30, 111, 19))
        self.lblCadSetoresNomeFantasia.setObjectName(_fromUtf8("lblCadSetoresNomeFantasia"))
        self.txtCadSetoresCnpj = QtGui.QLineEdit(self.grbEmpresa)
        self.txtCadSetoresCnpj.setEnabled(False)
        self.txtCadSetoresCnpj.setGeometry(QtCore.QRect(196, 102, 181, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtCadSetoresCnpj.setPalette(palette)
        self.txtCadSetoresCnpj.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCadSetoresCnpj.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtCadSetoresCnpj.setObjectName(_fromUtf8("txtCadSetoresCnpj"))
        self.lblCadSetoresIncricaoEstadual = QtGui.QLabel(self.grbEmpresa)
        self.lblCadSetoresIncricaoEstadual.setGeometry(QtCore.QRect(380, 82, 131, 19))
        self.lblCadSetoresIncricaoEstadual.setObjectName(_fromUtf8("lblCadSetoresIncricaoEstadual"))
        self.lblCadSetoresTipoEmpresa = QtGui.QLabel(self.grbEmpresa)
        self.lblCadSetoresTipoEmpresa.setGeometry(QtCore.QRect(12, 82, 131, 19))
        self.lblCadSetoresTipoEmpresa.setObjectName(_fromUtf8("lblCadSetoresTipoEmpresa"))
        self.lblMarca.setBuddy(self.txtMarca)
        self.lblModelo.setBuddy(self.txtModelo)
        self.lblPlaca.setBuddy(self.txtPlaca)
        self.lblTipoVeiculo.setBuddy(self.comboBox)
        self.lblCadSetoresCnpj.setBuddy(self.txtCadSetoresCnpj)
        self.lblCadSetoresCodigo.setBuddy(self.txtCadSetoresCodigo)
        self.lblCadSetoresNomeFantasia.setBuddy(self.txtCadSetoresNomeFantasia)
        self.lblCadSetoresIncricaoEstadual.setBuddy(self.txtCadSetoresInscricaoEstadual)
        self.lblCadSetoresTipoEmpresa.setBuddy(self.txtCadSetoresTipoEmpresa)

        self.retranslateUi(frmCadastroVeiculosEmpresa)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroVeiculosEmpresa)
        frmCadastroVeiculosEmpresa.setTabOrder(self.txtCadSetoresCodigo, self.txtCadSetoresNomeFantasia)
        frmCadastroVeiculosEmpresa.setTabOrder(self.txtCadSetoresNomeFantasia, self.comboBox)
        frmCadastroVeiculosEmpresa.setTabOrder(self.comboBox, self.txtMarca)
        frmCadastroVeiculosEmpresa.setTabOrder(self.txtMarca, self.txtModelo)
        frmCadastroVeiculosEmpresa.setTabOrder(self.txtModelo, self.txtPlaca)

    def retranslateUi(self, frmCadastroVeiculosEmpresa):
        frmCadastroVeiculosEmpresa.setWindowTitle(_translate("frmCadastroVeiculosEmpresa", "Cadastro de Veiculos Empresa", None))
        self.grbBotoes.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Grupo de botões referente as suas funções", None))
        self.btnNovo.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Botão de Criação de um novo registro", None))
        self.btnNovo.setText(_translate("frmCadastroVeiculosEmpresa", "Novo", None))
        self.btnCancelar.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Botão de cancelar a operação iniciada", None))
        self.btnCancelar.setText(_translate("frmCadastroVeiculosEmpresa", "Cancelar", None))
        self.btnDeletar.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Botão de deleção de um registro existente", None))
        self.btnDeletar.setText(_translate("frmCadastroVeiculosEmpresa", "Deletar", None))
        self.btnSalvar.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Botão para salvar um novo registro", None))
        self.btnSalvar.setText(_translate("frmCadastroVeiculosEmpresa", "Salvar", None))
        self.btnEditar.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Botão para salvar edição de um registro existente", None))
        self.btnEditar.setText(_translate("frmCadastroVeiculosEmpresa", "Editar", None))
        self.grbDadosVeiculos.setTitle(_translate("frmCadastroVeiculosEmpresa", "Dados de Veiculo", None))
        self.txtMarca.setToolTip(_translate("frmCadastroVeiculosEmpresa", "Marca", None))
        self.txtMarca.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo do nome da marca do veiculo", None))
        self.txtModelo.setToolTip(_translate("frmCadastroVeiculosEmpresa", "Modelo", None))
        self.txtModelo.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo do nome da modelo do veiculo", None))
        self.txtPlaca.setToolTip(_translate("frmCadastroVeiculosEmpresa", "Placa", None))
        self.txtPlaca.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo de identificação da placa do veiculo", None))
        self.txtPlaca.setInputMask(_translate("frmCadastroVeiculosEmpresa", "nnn-0000; ", None))
        self.txtPlaca.setText(_translate("frmCadastroVeiculosEmpresa", "-", None))
        self.lblMarca.setText(_translate("frmCadastroVeiculosEmpresa", "Marca", None))
        self.lblModelo.setText(_translate("frmCadastroVeiculosEmpresa", "Modelo", None))
        self.lblPlaca.setText(_translate("frmCadastroVeiculosEmpresa", "Placa", None))
        self.comboBox.setToolTip(_translate("frmCadastroVeiculosEmpresa", "Tipo de Veiculo", None))
        self.comboBox.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo de escolha do tipo de veiculo", None))
        self.lblTipoVeiculo.setText(_translate("frmCadastroVeiculosEmpresa", "Tipo de Veiculo", None))
        self.grbEmpresa.setTitle(_translate("frmCadastroVeiculosEmpresa", "Empresa", None))
        self.lblCadSetoresCnpj.setText(_translate("frmCadastroVeiculosEmpresa", "CNPJ", None))
        self.lblCadSetoresCodigo.setText(_translate("frmCadastroVeiculosEmpresa", "Codigo", None))
        self.txtCadSetoresCodigo.setToolTip(_translate("frmCadastroVeiculosEmpresa", "Codigo", None))
        self.txtCadSetoresCodigo.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo do Codigo de identificação da empresa", None))
        self.txtCadSetoresTipoEmpresa.setToolTip(_translate("frmCadastroVeiculosEmpresa", "Tipo de Empresa", None))
        self.txtCadSetoresTipoEmpresa.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo do tipo da empresa", None))
        self.txtCadSetoresInscricaoEstadual.setToolTip(_translate("frmCadastroVeiculosEmpresa", "Incrição Estadual", None))
        self.txtCadSetoresInscricaoEstadual.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo do numero da iscrição estadual da empresa", None))
        self.txtCadSetoresNomeFantasia.setToolTip(_translate("frmCadastroVeiculosEmpresa", "Nome Fantasia", None))
        self.txtCadSetoresNomeFantasia.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo do nome fantasia da empresa", None))
        self.lblCadSetoresNomeFantasia.setText(_translate("frmCadastroVeiculosEmpresa", "Nome Fantasia", None))
        self.txtCadSetoresCnpj.setToolTip(_translate("frmCadastroVeiculosEmpresa", "CNPJ", None))
        self.txtCadSetoresCnpj.setWhatsThis(_translate("frmCadastroVeiculosEmpresa", "Campo numero do CNPJ da empresa", None))
        self.txtCadSetoresCnpj.setInputMask(_translate("frmCadastroVeiculosEmpresa", "00.000.000/0000-00; ", None))
        self.lblCadSetoresIncricaoEstadual.setText(_translate("frmCadastroVeiculosEmpresa", "Inscrição Estadual", None))
        self.lblCadSetoresTipoEmpresa.setText(_translate("frmCadastroVeiculosEmpresa", "Tipo de Empresa", None))


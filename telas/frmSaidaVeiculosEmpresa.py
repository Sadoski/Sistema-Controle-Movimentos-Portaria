# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmSaidaVeiculosEmpresa.ui'
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

class Ui_frmSaidaVeiculosEmpresa(object):
    def setupUi(self, frmSaidaVeiculosEmpresa):
        frmSaidaVeiculosEmpresa.setObjectName(_fromUtf8("frmSaidaVeiculosEmpresa"))
        frmSaidaVeiculosEmpresa.resize(572, 478)
        frmSaidaVeiculosEmpresa.setMinimumSize(QtCore.QSize(572, 478))
        frmSaidaVeiculosEmpresa.setMaximumSize(QtCore.QSize(572, 478))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/carro.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSaidaVeiculosEmpresa.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(11)
        frmSaidaVeiculosEmpresa.setFont(font)

        self.grbBotoes = QtGui.QGroupBox(frmSaidaVeiculosEmpresa)
        self.grbBotoes.setGeometry(QtCore.QRect(4, 390, 562, 80))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))
        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(270, 10, 81, 61))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))
        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setGeometry(QtCore.QRect(470, 10, 81, 61))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setGeometry(QtCore.QRect(370, 10, 81, 61))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        self.grbDadosFuncionario = QtGui.QGroupBox(frmSaidaVeiculosEmpresa)
        self.grbDadosFuncionario.setGeometry(QtCore.QRect(5, 10, 563, 122))
        self.grbDadosFuncionario.setObjectName(_fromUtf8("grbDadosFuncionario"))
        self.txtidFuncionario = QtGui.QLineEdit(self.grbDadosFuncionario)
        self.txtidFuncionario.setEnabled(True)
        self.txtidFuncionario.setGeometry(QtCore.QRect(10, 40, 161, 25))
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
        self.txtidFuncionario.setPalette(palette)
        self.txtidFuncionario.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtidFuncionario.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtidFuncionario.setMaxLength(11)
        self.txtidFuncionario.setObjectName(_fromUtf8("txtidFuncionario"))
        self.lblCodigoFuncionario = QtGui.QLabel(self.grbDadosFuncionario)
        self.lblCodigoFuncionario.setGeometry(QtCore.QRect(10, 20, 121, 19))
        self.lblCodigoFuncionario.setObjectName(_fromUtf8("lblCodigoFuncionario"))
        self.lblNomeFuncionario = QtGui.QLabel(self.grbDadosFuncionario)
        self.lblNomeFuncionario.setGeometry(QtCore.QRect(180, 20, 151, 19))
        self.lblNomeFuncionario.setObjectName(_fromUtf8("lblNomeFuncionario"))
        self.btnPesquisar = QtGui.QPushButton(self.grbDadosFuncionario)
        self.btnPesquisar.setGeometry(QtCore.QRect(520, 40, 31, 28))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))
        self.txtNomeFuncionario = QtGui.QLineEdit(self.grbDadosFuncionario)
        self.txtNomeFuncionario.setGeometry(QtCore.QRect(180, 40, 331, 25))
        self.txtNomeFuncionario.setMaxLength(70)
        self.txtNomeFuncionario.setObjectName(_fromUtf8("txtNomeFuncionario"))
        self.lblSetor = QtGui.QLabel(self.grbDadosFuncionario)
        self.lblSetor.setGeometry(QtCore.QRect(10, 70, 66, 19))
        self.lblSetor.setObjectName(_fromUtf8("lblSetor"))
        self.lblCargo = QtGui.QLabel(self.grbDadosFuncionario)
        self.lblCargo.setGeometry(QtCore.QRect(230, 70, 66, 19))
        self.lblCargo.setObjectName(_fromUtf8("lblCargo"))
        self.txtCargos = QtGui.QLineEdit(self.grbDadosFuncionario)
        self.txtCargos.setEnabled(False)
        self.txtCargos.setGeometry(QtCore.QRect(230, 90, 211, 25))
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
        self.txtCargos.setPalette(palette)
        self.txtCargos.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCargos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtCargos.setMaxLength(50)
        self.txtCargos.setObjectName(_fromUtf8("txtCargos"))
        self.txtSetor = QtGui.QLineEdit(self.grbDadosFuncionario)
        self.txtSetor.setEnabled(False)
        self.txtSetor.setGeometry(QtCore.QRect(10, 90, 211, 25))
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
        self.txtSetor.setPalette(palette)
        self.txtSetor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtSetor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtSetor.setMaxLength(50)
        self.txtSetor.setObjectName(_fromUtf8("txtSetor"))
        self.grbDadosVeiculo = QtGui.QGroupBox(frmSaidaVeiculosEmpresa)
        self.grbDadosVeiculo.setGeometry(QtCore.QRect(5, 131, 563, 171))
        self.grbDadosVeiculo.setObjectName(_fromUtf8("grbDadosVeiculo"))
        self.lblTipoVeiculo = QtGui.QLabel(self.grbDadosVeiculo)
        self.lblTipoVeiculo.setGeometry(QtCore.QRect(10, 70, 111, 19))
        self.lblTipoVeiculo.setObjectName(_fromUtf8("lblTipoVeiculo"))
        self.lineEdit = QtGui.QLineEdit(self.grbDadosVeiculo)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 211, 25))
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
        self.lineEdit.setPalette(palette)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit.setMaxLength(40)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.txtPlaca = QtGui.QLineEdit(self.grbDadosVeiculo)
        self.txtPlaca.setEnabled(False)
        self.txtPlaca.setGeometry(QtCore.QRect(350, 140, 211, 25))
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
        self.txtPlaca.setPalette(palette)
        self.txtPlaca.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtPlaca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtPlaca.setObjectName(_fromUtf8("txtPlaca"))
        self.lblMarca = QtGui.QLabel(self.grbDadosVeiculo)
        self.lblMarca.setGeometry(QtCore.QRect(10, 120, 51, 19))
        self.lblMarca.setObjectName(_fromUtf8("lblMarca"))
        self.lblPlaca = QtGui.QLabel(self.grbDadosVeiculo)
        self.lblPlaca.setGeometry(QtCore.QRect(350, 120, 51, 19))
        self.lblPlaca.setObjectName(_fromUtf8("lblPlaca"))
        self.txtModelo = QtGui.QComboBox(self.grbDadosVeiculo)
        self.txtModelo.setGeometry(QtCore.QRect(10, 40, 331, 25))
        self.txtModelo.setObjectName(_fromUtf8("txtModelo"))
        self.lblModelo = QtGui.QLabel(self.grbDadosVeiculo)
        self.lblModelo.setGeometry(QtCore.QRect(10, 20, 61, 19))
        self.lblModelo.setObjectName(_fromUtf8("lblModelo"))
        self.txtMarca = QtGui.QLineEdit(self.grbDadosVeiculo)
        self.txtMarca.setEnabled(False)
        self.txtMarca.setGeometry(QtCore.QRect(10, 140, 331, 25))
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
        self.txtMarca.setPalette(palette)
        self.txtMarca.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtMarca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtMarca.setMaxLength(50)
        self.txtMarca.setObjectName(_fromUtf8("txtMarca"))
        self.grbDadosSaida = QtGui.QGroupBox(frmSaidaVeiculosEmpresa)
        self.grbDadosSaida.setGeometry(QtCore.QRect(4, 304, 564, 80))
        self.grbDadosSaida.setObjectName(_fromUtf8("grbDadosSaida"))
        self.lblDataSaida = QtGui.QLabel(self.grbDadosSaida)
        self.lblDataSaida.setGeometry(QtCore.QRect(10, 20, 101, 19))
        self.lblDataSaida.setObjectName(_fromUtf8("lblDataSaida"))
        self.txtHora = QtGui.QTimeEdit(self.grbDadosSaida)
        self.txtHora.setGeometry(QtCore.QRect(150, 40, 118, 25))
        self.txtHora.setObjectName(_fromUtf8("txtHora"))
        self.lblHoraSaida = QtGui.QLabel(self.grbDadosSaida)
        self.lblHoraSaida.setGeometry(QtCore.QRect(150, 20, 91, 19))
        self.lblHoraSaida.setObjectName(_fromUtf8("lblHoraSaida"))
        self.txtData = QtGui.QDateEdit(self.grbDadosSaida)
        self.txtData.setGeometry(QtCore.QRect(10, 40, 110, 25))
        self.txtData.setObjectName(_fromUtf8("txtData"))
        self.lblCodigoFuncionario.setBuddy(self.txtidFuncionario)
        self.lblNomeFuncionario.setBuddy(self.txtNomeFuncionario)
        self.lblSetor.setBuddy(self.txtSetor)
        self.lblCargo.setBuddy(self.txtCargos)
        self.lblTipoVeiculo.setBuddy(self.lineEdit)
        self.lblMarca.setBuddy(self.txtMarca)
        self.lblPlaca.setBuddy(self.txtPlaca)
        self.lblDataSaida.setBuddy(self.txtData)
        self.lblHoraSaida.setBuddy(self.txtHora)

        self.retranslateUi(frmSaidaVeiculosEmpresa)
        QtCore.QMetaObject.connectSlotsByName(frmSaidaVeiculosEmpresa)

    def retranslateUi(self, frmSaidaVeiculosEmpresa):
        frmSaidaVeiculosEmpresa.setWindowTitle(_translate("frmSaidaVeiculosEmpresa", "Saida de Veiculos Empresa", None))
        self.grbBotoes.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Grupo de botões referente as suas funções", None))
        self.btnNovo.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Botão de Criação de um novo registro", None))
        self.btnNovo.setText(_translate("frmSaidaVeiculosEmpresa", "Novo", None))
        self.btnCancelar.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Botão de cancelar a operação iniciada", None))
        self.btnCancelar.setText(_translate("frmSaidaVeiculosEmpresa", "Cancelar", None))
        self.btnSalvar.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Botão para salvar um novo registro", None))
        self.btnSalvar.setText(_translate("frmSaidaVeiculosEmpresa", "Salvar", None))
        self.grbDadosFuncionario.setTitle(_translate("frmSaidaVeiculosEmpresa", "Dados do Funcionario", None))
        self.txtidFuncionario.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Codigo Funcionario", None))
        self.txtidFuncionario.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo do Codigo de identificação do Funcionario", None))
        self.lblCodigoFuncionario.setText(_translate("frmSaidaVeiculosEmpresa", "Codigo Funcionario", None))
        self.lblNomeFuncionario.setText(_translate("frmSaidaVeiculosEmpresa", "Nome Funcionario", None))
        self.txtNomeFuncionario.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Nome Funcionario", None))
        self.txtNomeFuncionario.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo do nome do funcionario", None))
        self.lblSetor.setText(_translate("frmSaidaVeiculosEmpresa", "Setor", None))
        self.lblCargo.setText(_translate("frmSaidaVeiculosEmpresa", "Cargo", None))
        self.txtCargos.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Cargo ", None))
        self.txtCargos.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo de descrição do cargo de trabalho do funcionario", None))
        self.txtSetor.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Setor ", None))
        self.txtSetor.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo de descrição do setor de trabalho do funcionario", None))
        self.grbDadosVeiculo.setTitle(_translate("frmSaidaVeiculosEmpresa", "Dados do Veiculo", None))
        self.lblTipoVeiculo.setText(_translate("frmSaidaVeiculosEmpresa", "Tipo de Veiculos", None))
        self.lineEdit.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Tipo do Veiculo", None))
        self.lineEdit.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo do tipo de veiculo", None))
        self.txtPlaca.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Placa do Veiculo", None))
        self.txtPlaca.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo de identificação da placa do veiculo", None))
        self.txtPlaca.setInputMask(_translate("frmSaidaVeiculosEmpresa", "nnn-0000; ", None))
        self.txtPlaca.setText(_translate("frmSaidaVeiculosEmpresa", "-", None))
        self.lblMarca.setText(_translate("frmSaidaVeiculosEmpresa", "Marca", None))
        self.lblPlaca.setText(_translate("frmSaidaVeiculosEmpresa", "Placa", None))
        self.txtModelo.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Modelo do Veiculo", None))
        self.txtModelo.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo de escolha do modelo de veiculo", None))
        self.lblModelo.setText(_translate("frmSaidaVeiculosEmpresa", "Modelo", None))
        self.txtMarca.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Marca do Veiculo", None))
        self.txtMarca.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo do nome na marca do veiculo", None))
        self.grbDadosSaida.setTitle(_translate("frmSaidaVeiculosEmpresa", "Dados da Saida", None))
        self.lblDataSaida.setText(_translate("frmSaidaVeiculosEmpresa", "Data de Saida", None))
        self.txtHora.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Hora Saida", None))
        self.txtHora.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo da hora de saida", None))
        self.lblHoraSaida.setText(_translate("frmSaidaVeiculosEmpresa", "Hora de Saida", None))
        self.txtData.setToolTip(_translate("frmSaidaVeiculosEmpresa", "Data Saida ", None))
        self.txtData.setWhatsThis(_translate("frmSaidaVeiculosEmpresa", "Campo da data de saida", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEntradaFuncionario.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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

class Ui_frmCadastroEntradaFuncionario(object):
    def setupUi(self, frmCadastroEntradaFuncionario):
        frmCadastroEntradaFuncionario.setObjectName(_fromUtf8("frmCadastroEntradaFuncionario"))
        frmCadastroEntradaFuncionario.resize(662, 539)
        frmCadastroEntradaFuncionario.setMinimumSize(QtCore.QSize(662, 539))
        frmCadastroEntradaFuncionario.setMaximumSize(QtCore.QSize(662, 539))
        frmCadastroEntradaFuncionario.setSizeGripEnabled(False)
        frmCadastroEntradaFuncionario.setModal(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        frmCadastroEntradaFuncionario.setFont(font)

        self.txtPesquisaidFuncionario = QtGui.QLineEdit(frmCadastroEntradaFuncionario)
        self.txtPesquisaidFuncionario.setEnabled(True)
        self.txtPesquisaidFuncionario.setGeometry(QtCore.QRect(10, 42, 161, 25))
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
        self.txtPesquisaidFuncionario.setPalette(palette)
        self.txtPesquisaidFuncionario.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtPesquisaidFuncionario.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtPesquisaidFuncionario.setMaxLength(11)
        self.txtPesquisaidFuncionario.setObjectName(_fromUtf8("txtPesquisaidFuncionario"))

        self.lblPesquisaCodigoFuncionario = QtGui.QLabel(frmCadastroEntradaFuncionario)
        self.lblPesquisaCodigoFuncionario.setGeometry(QtCore.QRect(10, 22, 161, 19))
        self.lblPesquisaCodigoFuncionario.setObjectName(_fromUtf8("lblPesquisaCodigoFuncionario"))

        self.txtPesquisaNomeFuncionario = QtGui.QLineEdit(frmCadastroEntradaFuncionario)
        self.txtPesquisaNomeFuncionario.setGeometry(QtCore.QRect(182, 42, 421, 25))
        self.txtPesquisaNomeFuncionario.setMaxLength(70)
        self.txtPesquisaNomeFuncionario.setObjectName(_fromUtf8("txtPesquisaNomeFuncionario"))

        self.lblPesquisaNomeFuncionario = QtGui.QLabel(frmCadastroEntradaFuncionario)
        self.lblPesquisaNomeFuncionario.setGeometry(QtCore.QRect(182, 22, 161, 19))
        self.lblPesquisaNomeFuncionario.setObjectName(_fromUtf8("lblPesquisaNomeFuncionario"))

        self.btnPesquisar = QtGui.QPushButton(frmCadastroEntradaFuncionario)
        self.btnPesquisar.setGeometry(QtCore.QRect(620, 40, 31, 28))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisa = QtGui.QTableWidget(frmCadastroEntradaFuncionario)
        self.tabPesquisa.setGeometry(QtCore.QRect(10, 81, 641, 191))
        self.tabPesquisa.setColumnCount(6)
        self.tabPesquisa.setHorizontalHeaderLabels(['COD.', 'Nome', 'Setor', 'Função', 'Data Saída', 'Hora Saída'])
        self.tabPesquisa.setEditTriggers(self.tabPesquisa.NoEditTriggers)
        self.tabPesquisa.setSelectionBehavior(self.tabPesquisa.SelectRows)
        self.tabPesquisa.setSelectionMode(self.tabPesquisa.SingleSelection)
        self.tabPesquisa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisa.setObjectName(_fromUtf8("tabPesquisa"))

        self.grbDadosSaidaFuncionario = QtGui.QGroupBox(frmCadastroEntradaFuncionario)
        self.grbDadosSaidaFuncionario.setEnabled(True)
        self.grbDadosSaidaFuncionario.setGeometry(QtCore.QRect(5, 278, 651, 171))
        self.grbDadosSaidaFuncionario.setTitle(_fromUtf8(""))
        self.grbDadosSaidaFuncionario.setObjectName(_fromUtf8("grbDadosSaidaFuncionario"))

        self.lblDataSaida = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblDataSaida.setEnabled(True)
        self.lblDataSaida.setGeometry(QtCore.QRect(7, 120, 91, 19))
        self.lblDataSaida.setObjectName(_fromUtf8("lblDataSaida"))

        self.lblCargo = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblCargo.setGeometry(QtCore.QRect(226, 52, 66, 19))
        self.lblCargo.setObjectName(_fromUtf8("lblCargo"))

        self.lblNomeFuncionario = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblNomeFuncionario.setGeometry(QtCore.QRect(178, 4, 151, 19))
        self.lblNomeFuncionario.setObjectName(_fromUtf8("lblNomeFuncionario"))

        self.lblCodigoFuncionario = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblCodigoFuncionario.setGeometry(QtCore.QRect(6, 4, 121, 19))
        self.lblCodigoFuncionario.setObjectName(_fromUtf8("lblCodigoFuncionario"))

        self.txtidFuncionario = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtidFuncionario.setEnabled(False)
        self.txtidFuncionario.setGeometry(QtCore.QRect(6, 24, 161, 25))
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
        self.txtidFuncionario.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtidFuncionario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtidFuncionario.setMaxLength(11)
        self.txtidFuncionario.setObjectName(_fromUtf8("txtidFuncionario"))

        self.txtNomeFuncionario = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtNomeFuncionario.setEnabled(False)
        self.txtNomeFuncionario.setGeometry(QtCore.QRect(178, 24, 421, 25))
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
        self.txtNomeFuncionario.setPalette(palette)
        self.txtNomeFuncionario.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtNomeFuncionario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtNomeFuncionario.setMaxLength(70)
        self.txtNomeFuncionario.setObjectName(_fromUtf8("txtNomeFuncionario"))

        self.lblSetor = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblSetor.setGeometry(QtCore.QRect(6, 52, 66, 19))
        self.lblSetor.setObjectName(_fromUtf8("lblSetor"))

        self.txtCargos = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtCargos.setEnabled(False)
        self.txtCargos.setGeometry(QtCore.QRect(226, 72, 211, 25))
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

        self.lblHoraSaida = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblHoraSaida.setGeometry(QtCore.QRect(146, 120, 101, 19))
        self.lblHoraSaida.setObjectName(_fromUtf8("lblHoraSaida"))

        self.txtHoraEntrda = QtGui.QTimeEdit(self.grbDadosSaidaFuncionario)
        self.txtHoraEntrda.setTime(QTime.currentTime())
        self.txtHoraEntrda.setGeometry(QtCore.QRect(146, 140, 118, 25))
        self.txtHoraEntrda.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtHoraEntrda.setObjectName(_fromUtf8("txtHoraEntrda"))

        self.txtSetor = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtSetor.setEnabled(False)
        self.txtSetor.setGeometry(QtCore.QRect(6, 72, 211, 25))
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

        self.txtData = QtGui.QDateEdit(self.grbDadosSaidaFuncionario)
        self.txtData.setDate(QDate.currentDate())
        self.txtData.setGeometry(QtCore.QRect(7, 140, 110, 25))
        self.txtData.setCalendarPopup(True)
        self.txtData.setObjectName(_fromUtf8("txtData"))

        self.grbBotoes = QtGui.QGroupBox(frmCadastroEntradaFuncionario)
        self.grbBotoes.setGeometry(QtCore.QRect(5, 452, 651, 81))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setGeometry(QtCore.QRect(260, 10, 81, 61))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setGeometry(QtCore.QRect(450, 10, 81, 61))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(160, 10, 81, 61))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))
        self.btnEditar = QtGui.QPushButton(self.grbBotoes)
        self.btnEditar.setEnabled(False)
        self.btnEditar.setGeometry(QtCore.QRect(350, 10, 81, 61))
        self.btnEditar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))
        self.btnDeletar = QtGui.QPushButton(self.grbBotoes)
        self.btnDeletar.setEnabled(False)
        self.btnDeletar.setGeometry(QtCore.QRect(550, 10, 81, 61))
        self.btnDeletar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnDeletar.setObjectName(_fromUtf8("btnDeletar"))
        self.lblPesquisaCodigoFuncionario.setBuddy(self.txtPesquisaidFuncionario)
        self.lblPesquisaNomeFuncionario.setBuddy(self.txtPesquisaNomeFuncionario)
        self.lblCargo.setBuddy(self.txtCargos)
        self.lblNomeFuncionario.setBuddy(self.txtNomeFuncionario)
        self.lblCodigoFuncionario.setBuddy(self.txtidFuncionario)
        self.lblSetor.setBuddy(self.txtSetor)
        self.lblHoraSaida.setBuddy(self.txtHoraEntrda)

        self.retranslateUi(frmCadastroEntradaFuncionario)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroEntradaFuncionario)
        frmCadastroEntradaFuncionario.setTabOrder(self.txtPesquisaidFuncionario, self.txtPesquisaNomeFuncionario)
        frmCadastroEntradaFuncionario.setTabOrder(self.txtPesquisaNomeFuncionario, self.tabPesquisa)
        frmCadastroEntradaFuncionario.setTabOrder(self.tabPesquisa, self.txtHoraEntrda)

    def retranslateUi(self, frmCadastroEntradaFuncionario):
        frmCadastroEntradaFuncionario.setWindowTitle(_translate("frmCadastroEntradaFuncionario", "Entrada de Funcionarios em Horario de Serviço", None))
        self.txtPesquisaidFuncionario.setToolTip(_translate("frmCadastroEntradaFuncionario", "Pesquisar Codigo Funcionario", None))
        self.txtPesquisaidFuncionario.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo do Codigo de identificação do Funcionario", None))
        self.lblPesquisaCodigoFuncionario.setText(_translate("frmCadastroEntradaFuncionario", "Pesq. Codigo Funcionario", None))
        self.txtPesquisaNomeFuncionario.setToolTip(_translate("frmCadastroEntradaFuncionario", "Pesquisar Nome Funcionario", None))
        self.txtPesquisaNomeFuncionario.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo do nome do funcionario", None))
        self.lblPesquisaNomeFuncionario.setText(_translate("frmCadastroEntradaFuncionario", "Pesq. Nome Funcionario", None))
        self.tabPesquisa.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Tabela dos resultados da pesquisa", None))
        self.lblDataSaida.setText(_translate("frmCadastroEntradaFuncionario", "Data Entrada", None))
        self.lblCargo.setText(_translate("frmCadastroEntradaFuncionario", "Cargo", None))
        self.lblNomeFuncionario.setText(_translate("frmCadastroEntradaFuncionario", "Nome Funcionario", None))
        self.lblCodigoFuncionario.setText(_translate("frmCadastroEntradaFuncionario", "Codigo Funcionario", None))
        self.txtidFuncionario.setToolTip(_translate("frmCadastroEntradaFuncionario", "Codigo Funcionario", None))
        self.txtidFuncionario.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo do Codigo de identificação do Funcionario", None))
        self.txtNomeFuncionario.setToolTip(_translate("frmCadastroEntradaFuncionario", "Nome Funcionario", None))
        self.txtNomeFuncionario.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo do nome do funcionario", None))
        self.lblSetor.setText(_translate("frmCadastroEntradaFuncionario", "Setor", None))
        self.txtCargos.setToolTip(_translate("frmCadastroEntradaFuncionario", "Cargo", None))
        self.txtCargos.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo de descrição do cargo de trabalho do funcionario", None))
        self.lblHoraSaida.setText(_translate("frmCadastroEntradaFuncionario", "Hora Entrada", None))
        self.txtHoraEntrda.setToolTip(_translate("frmCadastroEntradaFuncionario", "Hora Saida", None))
        self.txtHoraEntrda.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo de hora de entrada", None))
        self.txtSetor.setToolTip(_translate("frmCadastroEntradaFuncionario", "Setor", None))
        self.txtSetor.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo de descrição do setor de trabalho do funcionario", None))
        self.txtData.setToolTip(_translate("frmCadastroEntradaFuncionario", "Data Entrada", None))
        self.txtData.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo de data de entrada", None))
        self.btnSalvar.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Botão para salvar um novo registro", None))
        self.btnSalvar.setText(_translate("frmCadastroEntradaFuncionario", "Salvar", None))
        self.btnCancelar.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Botão de cancelar a operação iniciada", None))
        self.btnCancelar.setText(_translate("frmCadastroEntradaFuncionario", "Cancelar", None))
        self.btnNovo.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Botão de Criação de um novo registro", None))
        self.btnNovo.setText(_translate("frmCadastroEntradaFuncionario", "Novo", None))
        self.btnEditar.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Botão para salvar edição de um registro existente", None))
        self.btnEditar.setText(_translate("frmCadastroEntradaFuncionario", "Editar", None))
        self.btnDeletar.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Botão de deleção de um registro existente", None))
        self.btnDeletar.setText(_translate("frmCadastroEntradaFuncionario", "Deletar", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEntradaFuncionario.ui'
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

class Ui_frmCadastroEntradaFuncionario(object):
    def setupUi(self, frmCadastroEntradaFuncionario):
        frmCadastroEntradaFuncionario.setObjectName(_fromUtf8("frmCadastroEntradaFuncionario"))
        frmCadastroEntradaFuncionario.resize(659, 385)
        frmCadastroEntradaFuncionario.setMinimumSize(QtCore.QSize(659, 385))
        frmCadastroEntradaFuncionario.setMaximumSize(QtCore.QSize(659, 385))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        frmCadastroEntradaFuncionario.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/funcionario-saida")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCadastroEntradaFuncionario.setWindowIcon(icon)
        frmCadastroEntradaFuncionario.setSizeGripEnabled(True)
        frmCadastroEntradaFuncionario.setModal(True)

        self.tabPesquisa = QtGui.QTableWidget(frmCadastroEntradaFuncionario)
        self.tabPesquisa.setEnabled(False)
        self.tabPesquisa.setGeometry(QtCore.QRect(10, 10, 641, 131))
        self.tabPesquisa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisa.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisa.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisa.setObjectName(_fromUtf8("tabPesquisa"))
        self.tabPesquisa.setColumnCount(6)
        self.tabPesquisa.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisa.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisa.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisa.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisa.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisa.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisa.setHorizontalHeaderItem(5, item)
        self.tabPesquisa.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisa.verticalHeader().setVisible(False)

        self.grbDadosSaidaFuncionario = QtGui.QGroupBox(frmCadastroEntradaFuncionario)
        self.grbDadosSaidaFuncionario.setEnabled(False)
        self.grbDadosSaidaFuncionario.setGeometry(QtCore.QRect(10, 150, 641, 171))
        self.grbDadosSaidaFuncionario.setTitle(_fromUtf8(""))
        self.grbDadosSaidaFuncionario.setObjectName(_fromUtf8("grbDadosSaidaFuncionario"))

        self.lblDataSaida = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblDataSaida.setGeometry(QtCore.QRect(10, 10, 81, 19))
        self.lblDataSaida.setObjectName(_fromUtf8("lblDataSaida"))

        self.lblCargo = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblCargo.setGeometry(QtCore.QRect(227, 110, 66, 19))
        self.lblCargo.setObjectName(_fromUtf8("lblCargo"))

        self.lblNomeFuncionario = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblNomeFuncionario.setGeometry(QtCore.QRect(179, 64, 151, 19))
        self.lblNomeFuncionario.setObjectName(_fromUtf8("lblNomeFuncionario"))

        self.lblCodigoFuncionario = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblCodigoFuncionario.setGeometry(QtCore.QRect(7, 64, 121, 19))
        self.lblCodigoFuncionario.setObjectName(_fromUtf8("lblCodigoFuncionario"))

        self.txtidFuncionario = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtidFuncionario.setEnabled(False)
        self.txtidFuncionario.setGeometry(QtCore.QRect(7, 84, 161, 25))
        self.txtidFuncionario.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtidFuncionario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtidFuncionario.setMaxLength(11)
        self.txtidFuncionario.setObjectName(_fromUtf8("txtidFuncionario"))

        self.txtNomeFuncionario = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtNomeFuncionario.setEnabled(False)
        self.txtNomeFuncionario.setGeometry(QtCore.QRect(179, 84, 421, 25))
        self.txtNomeFuncionario.setMaxLength(70)
        self.txtNomeFuncionario.setObjectName(_fromUtf8("txtNomeFuncionario"))

        self.lblSetor = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblSetor.setGeometry(QtCore.QRect(7, 110, 66, 19))
        self.lblSetor.setObjectName(_fromUtf8("lblSetor"))

        self.txtCargos = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtCargos.setEnabled(False)
        self.txtCargos.setGeometry(QtCore.QRect(227, 130, 211, 25))
        self.txtCargos.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCargos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtCargos.setMaxLength(50)
        self.txtCargos.setObjectName(_fromUtf8("txtCargos"))

        self.lblHoraSaida = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblHoraSaida.setGeometry(QtCore.QRect(150, 10, 91, 19))
        self.lblHoraSaida.setObjectName(_fromUtf8("lblHoraSaida"))

        self.txtHoraEntrada = QtGui.QTimeEdit(self.grbDadosSaidaFuncionario)
        self.txtHoraEntrada.setTime(QtCore.QTime.currentTime())
        self.txtHoraEntrada.setGeometry(QtCore.QRect(150, 30, 118, 25))
        self.txtHoraEntrada.setObjectName(_fromUtf8("txtHoraEntrada"))

        self.txtDataEntrada = QtGui.QDateEdit(self.grbDadosSaidaFuncionario)
        self.txtDataEntrada.setDate(QtCore.QDate.currentDate())
        self.txtDataEntrada.setGeometry(QtCore.QRect(10, 30, 110, 25))
        self.txtDataEntrada.setCalendarPopup(True)
        self.txtDataEntrada.setObjectName(_fromUtf8("txtDataEntrada"))

        self.txtSetor = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtSetor.setEnabled(False)
        self.txtSetor.setGeometry(QtCore.QRect(7, 130, 211, 25))
        self.txtSetor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtSetor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtSetor.setMaxLength(50)
        self.txtSetor.setObjectName(_fromUtf8("txtSetor"))

        self.grbBotoes = QtGui.QGroupBox(frmCadastroEntradaFuncionario)
        self.grbBotoes.setGeometry(QtCore.QRect(10, 330, 641, 51))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(320, 12, 88, 27))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNovo.setIcon(icon)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(420, 12, 88, 27))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))

        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(520, 12, 88, 27))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.lblDataSaida.setBuddy(self.txtDataEntrada)
        self.lblCargo.setBuddy(self.txtCargos)
        self.lblNomeFuncionario.setBuddy(self.txtNomeFuncionario)
        self.lblCodigoFuncionario.setBuddy(self.txtidFuncionario)
        self.lblSetor.setBuddy(self.txtSetor)
        self.lblHoraSaida.setBuddy(self.txtHoraEntrada)

        self.retranslateUi(frmCadastroEntradaFuncionario)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroEntradaFuncionario)

    def retranslateUi(self, frmCadastroEntradaFuncionario):
        frmCadastroEntradaFuncionario.setWindowTitle(_translate("frmCadastroEntradaFuncionario", "Entrada de Funcionarios em Horario de Serviço", None))
        self.tabPesquisa.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Tabela dos resultados da pesquisa", None))
        item = self.tabPesquisa.horizontalHeaderItem(0)
        item.setText(_translate("frmCadastroEntradaFuncionario", "ID", None))
        item = self.tabPesquisa.horizontalHeaderItem(1)
        item.setText(_translate("frmCadastroEntradaFuncionario", "Data", None))
        item = self.tabPesquisa.horizontalHeaderItem(2)
        item.setText(_translate("frmCadastroEntradaFuncionario", "Hora", None))
        item = self.tabPesquisa.horizontalHeaderItem(3)
        item.setText(_translate("frmCadastroEntradaFuncionario", "Funcionario", None))
        item = self.tabPesquisa.horizontalHeaderItem(4)
        item.setText(_translate("frmCadastroEntradaFuncionario", "Setor", None))
        item = self.tabPesquisa.horizontalHeaderItem(5)
        item.setText(_translate("frmCadastroEntradaFuncionario", "Cargo", None))
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
        self.txtHoraEntrada.setToolTip(_translate("frmCadastroEntradaFuncionario", "Hora Saida", None))
        self.txtHoraEntrada.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo de hora de saida", None))
        self.txtDataEntrada.setToolTip(_translate("frmCadastroEntradaFuncionario", "Data Saida", None))
        self.txtDataEntrada.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo de data da saida", None))
        self.txtSetor.setToolTip(_translate("frmCadastroEntradaFuncionario", "Setor", None))
        self.txtSetor.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Campo de descrição do setor de trabalho do funcionario", None))
        self.btnNovo.setToolTip(_translate("frmCadastroEntradaFuncionario", "Novo", None))
        self.btnNovo.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "<html><head/><body><p>Botão para cadastrar uma novo registro da pessoa jurídica</p></body></html>", None))
        self.btnNovo.setText(_translate("frmCadastroEntradaFuncionario", "Novo", None))
        self.btnSalvar.setToolTip(_translate("frmCadastroEntradaFuncionario", "Salvar", None))
        self.btnSalvar.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "<html><head/><body><p>Botão para salvar um novo registro da pessoa jurídica</p></body></html>", None))
        self.btnSalvar.setText(_translate("frmCadastroEntradaFuncionario", "Salvar", None))
        self.btnCancelar.setToolTip(_translate("frmCadastroEntradaFuncionario", "Cancelar", None))
        self.btnCancelar.setWhatsThis(_translate("frmCadastroEntradaFuncionario", "Botão para cancelar a operação ", None))
        self.btnCancelar.setText(_translate("frmCadastroEntradaFuncionario", "Cancelar", None))


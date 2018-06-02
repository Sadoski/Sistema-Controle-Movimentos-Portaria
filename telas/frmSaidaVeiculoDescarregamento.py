# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmSaidaVeiculoDescarregamento.ui'
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

class Ui_frmSaidaVeiculoDescarregamento(object):
    def setupUi(self, frmSaidaVeiculoDescarregamento):
        frmSaidaVeiculoDescarregamento.setObjectName(_fromUtf8("frmSaidaVeiculoDescarregamento"))
        frmSaidaVeiculoDescarregamento.resize(790, 418)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        frmSaidaVeiculoDescarregamento.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/descarregamento.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSaidaVeiculoDescarregamento.setWindowIcon(icon)
        frmSaidaVeiculoDescarregamento.setSizeGripEnabled(True)
        frmSaidaVeiculoDescarregamento.setModal(True)

        self.tabPesquisa = QtGui.QTableWidget(frmSaidaVeiculoDescarregamento)
        self.tabPesquisa.setEnabled(False)
        self.tabPesquisa.setGeometry(QtCore.QRect(7, 10, 771, 161))
        self.tabPesquisa.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisa.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisa.setObjectName(_fromUtf8("tabPesquisa"))
        self.tabPesquisa.setColumnCount(7)
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
        item = QtGui.QTableWidgetItem()
        self.tabPesquisa.setHorizontalHeaderItem(6, item)
        self.tabPesquisa.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisa.verticalHeader().setVisible(False)

        self.lblHoraSaida = QtGui.QLabel(frmSaidaVeiculoDescarregamento)
        self.lblHoraSaida.setGeometry(QtCore.QRect(147, 190, 91, 16))
        self.lblHoraSaida.setObjectName(_fromUtf8("lblHoraSaida"))

        self.txtData = QtGui.QDateEdit(frmSaidaVeiculoDescarregamento)
        self.txtData.setDate(QtCore.QDate.currentDate())
        self.txtData.setEnabled(False)
        self.txtData.setGeometry(QtCore.QRect(17, 210, 110, 22))
        self.txtData.setCalendarPopup(True)
        self.txtData.setObjectName(_fromUtf8("txtData"))

        self.lblDataSaida = QtGui.QLabel(frmSaidaVeiculoDescarregamento)
        self.lblDataSaida.setGeometry(QtCore.QRect(17, 190, 101, 16))
        self.lblDataSaida.setObjectName(_fromUtf8("lblDataSaida"))

        self.txtHora = QtGui.QTimeEdit(frmSaidaVeiculoDescarregamento)
        self.txtHora.setTime(QtCore.QTime.currentTime())
        self.txtHora.setEnabled(False)
        self.txtHora.setGeometry(QtCore.QRect(147, 210, 118, 22))
        self.txtHora.setObjectName(_fromUtf8("txtHora"))

        self.grbBotoes = QtGui.QGroupBox(frmSaidaVeiculoDescarregamento)
        self.grbBotoes.setGeometry(QtCore.QRect(10, 360, 771, 51))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(460, 12, 88, 27))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNovo.setIcon(icon)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(560, 12, 88, 27))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))

        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(660, 12, 88, 27))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.grbDadosMotorista = QtGui.QGroupBox(frmSaidaVeiculoDescarregamento)
        self.grbDadosMotorista.setEnabled(False)
        self.grbDadosMotorista.setGeometry(QtCore.QRect(10, 240, 771, 107))
        self.grbDadosMotorista.setObjectName(_fromUtf8("grbDadosMotorista"))

        self.txtModeloMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtModeloMotorista.setGeometry(QtCore.QRect(10, 76, 251, 25))
        self.txtModeloMotorista.setMaxLength(50)
        self.txtModeloMotorista.setObjectName(_fromUtf8("txtModeloMotorista"))

        self.lblMarcaMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblMarcaMotorista.setGeometry(QtCore.QRect(270, 58, 51, 19))
        self.lblMarcaMotorista.setObjectName(_fromUtf8("lblMarcaMotorista"))

        self.txtMarcaMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtMarcaMotorista.setGeometry(QtCore.QRect(270, 78, 311, 25))
        self.txtMarcaMotorista.setMaxLength(50)
        self.txtMarcaMotorista.setObjectName(_fromUtf8("txtMarcaMotorista"))

        self.txtNomeMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtNomeMotorista.setGeometry(QtCore.QRect(180, 33, 361, 25))
        self.txtNomeMotorista.setMaxLength(70)
        self.txtNomeMotorista.setObjectName(_fromUtf8("txtNomeMotorista"))

        self.lblNomeMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblNomeMotorista.setGeometry(QtCore.QRect(180, 13, 151, 19))
        self.lblNomeMotorista.setObjectName(_fromUtf8("lblNomeMotorista"))

        self.txtPlacaMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtPlacaMotorista.setGeometry(QtCore.QRect(590, 78, 171, 25))
        self.txtPlacaMotorista.setObjectName(_fromUtf8("txtPlacaMotorista"))

        self.lblModeloMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblModeloMotorista.setGeometry(QtCore.QRect(10, 57, 51, 19))
        self.lblModeloMotorista.setObjectName(_fromUtf8("lblModeloMotorista"))

        self.txtidFuncionario = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtidFuncionario.setGeometry(QtCore.QRect(10, 33, 161, 25))
        self.txtidFuncionario.setMaxLength(11)
        self.txtidFuncionario.setObjectName(_fromUtf8("txtidFuncionario"))

        self.lblCodigoMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblCodigoMotorista.setGeometry(QtCore.QRect(10, 13, 121, 19))
        self.lblCodigoMotorista.setObjectName(_fromUtf8("lblCodigoMotorista"))

        self.lblPlacaMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblPlacaMotorista.setGeometry(QtCore.QRect(590, 58, 51, 19))
        self.lblPlacaMotorista.setObjectName(_fromUtf8("lblPlacaMotorista"))

        self.lblHoraSaida.setBuddy(self.txtHora)
        self.lblDataSaida.setBuddy(self.txtData)
        self.lblMarcaMotorista.setBuddy(self.txtMarcaMotorista)
        self.lblNomeMotorista.setBuddy(self.txtNomeMotorista)
        self.lblModeloMotorista.setBuddy(self.txtModeloMotorista)
        self.lblCodigoMotorista.setBuddy(self.txtidFuncionario)
        self.lblPlacaMotorista.setBuddy(self.txtPlacaMotorista)

        self.retranslateUi(frmSaidaVeiculoDescarregamento)
        QtCore.QMetaObject.connectSlotsByName(frmSaidaVeiculoDescarregamento)
        frmSaidaVeiculoDescarregamento.setTabOrder(self.tabPesquisa, self.txtData)
        frmSaidaVeiculoDescarregamento.setTabOrder(self.txtData, self.txtHora)

    def retranslateUi(self, frmSaidaVeiculoDescarregamento):
        frmSaidaVeiculoDescarregamento.setWindowTitle(_translate("frmSaidaVeiculoDescarregamento", "Saida de Veiculo Descarregamento", None))
        self.tabPesquisa.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Tabela de Resultados da pesquisa", None))
        item = self.tabPesquisa.horizontalHeaderItem(0)
        item.setText(_translate("frmSaidaVeiculoDescarregamento", "ID", None))
        item = self.tabPesquisa.horizontalHeaderItem(1)
        item.setText(_translate("frmSaidaVeiculoDescarregamento", "Data", None))
        item = self.tabPesquisa.horizontalHeaderItem(2)
        item.setText(_translate("frmSaidaVeiculoDescarregamento", "Hora", None))
        item = self.tabPesquisa.horizontalHeaderItem(3)
        item.setText(_translate("frmSaidaVeiculoDescarregamento", "Motorista", None))
        item = self.tabPesquisa.horizontalHeaderItem(4)
        item.setText(_translate("frmSaidaVeiculoDescarregamento", "Marca", None))
        item = self.tabPesquisa.horizontalHeaderItem(5)
        item.setText(_translate("frmSaidaVeiculoDescarregamento", "Modelo", None))
        item = self.tabPesquisa.horizontalHeaderItem(6)
        item.setText(_translate("frmSaidaVeiculoDescarregamento", "Placa", None))
        self.lblHoraSaida.setText(_translate("frmSaidaVeiculoDescarregamento", "Hora Saida", None))
        self.txtData.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Data Saida", None))
        self.txtData.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Campo da data de saida", None))
        self.lblDataSaida.setText(_translate("frmSaidaVeiculoDescarregamento", "Data Saida", None))
        self.txtHora.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Hora Saida", None))
        self.txtHora.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Campo da hora de saida", None))
        self.btnNovo.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Novo", None))
        self.btnNovo.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "<html><head/><body><p>Botão para cadastrar uma novo registro da pessoa jurídica</p></body></html>", None))
        self.btnNovo.setText(_translate("frmSaidaVeiculoDescarregamento", "Novo", None))
        self.btnSalvar.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Salvar", None))
        self.btnSalvar.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "<html><head/><body><p>Botão para salvar um novo registro da pessoa jurídica</p></body></html>", None))
        self.btnSalvar.setText(_translate("frmSaidaVeiculoDescarregamento", "Salvar", None))
        self.btnCancelar.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Cancelar", None))
        self.btnCancelar.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Botão para cancelar a operação ", None))
        self.btnCancelar.setText(_translate("frmSaidaVeiculoDescarregamento", "Cancelar", None))
        self.grbDadosMotorista.setTitle(_translate("frmSaidaVeiculoDescarregamento", "Motorista", None))
        self.txtModeloMotorista.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Marca do Veiculo", None))
        self.txtModeloMotorista.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Campo do nome do modelo do veiculo", None))
        self.lblMarcaMotorista.setText(_translate("frmSaidaVeiculoDescarregamento", "Marca", None))
        self.txtMarcaMotorista.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Marca do Veiculo", None))
        self.txtMarcaMotorista.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Campo do nome da marca do veiculo", None))
        self.txtNomeMotorista.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Nome Motorista", None))
        self.txtNomeMotorista.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Campo do nome do motorista", None))
        self.lblNomeMotorista.setText(_translate("frmSaidaVeiculoDescarregamento", "Nome Motorista", None))
        self.txtPlacaMotorista.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Placa do Veiculo", None))
        self.txtPlacaMotorista.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Campo de identificação da placa do veiculo", None))
        self.txtPlacaMotorista.setInputMask(_translate("frmSaidaVeiculoDescarregamento", "nnn-0000; ", None))
        self.txtPlacaMotorista.setText(_translate("frmSaidaVeiculoDescarregamento", "-", None))
        self.lblModeloMotorista.setText(_translate("frmSaidaVeiculoDescarregamento", "Modelo", None))
        self.txtidFuncionario.setToolTip(_translate("frmSaidaVeiculoDescarregamento", "Codigo Motorista", None))
        self.txtidFuncionario.setWhatsThis(_translate("frmSaidaVeiculoDescarregamento", "Campo do Codigo de identificação do motorista", None))
        self.lblCodigoMotorista.setText(_translate("frmSaidaVeiculoDescarregamento", "Codigo Motorista", None))
        self.lblPlacaMotorista.setText(_translate("frmSaidaVeiculoDescarregamento", "Placa", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarNotasFiscais.ui'
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

class Ui_frmConsultarNotasFiscais(object):
    def setupUi(self, frmConsultarNotasFiscais):
        frmConsultarNotasFiscais.setObjectName(_fromUtf8("frmConsultarNotasFiscais"))
        frmConsultarNotasFiscais.resize(793, 502)
        font = QtGui.QFont()
        font.setPointSize(11)
        frmConsultarNotasFiscais.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmConsultarNotasFiscais.setWindowIcon(icon)
        frmConsultarNotasFiscais.setSizeGripEnabled(True)
        frmConsultarNotasFiscais.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmConsultarNotasFiscais)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 161, 101))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnNumNotaFiscal = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnNumNotaFiscal.setGeometry(QtCore.QRect(10, 20, 111, 23))
        self.radBtnNumNotaFiscal.setObjectName(_fromUtf8("radBtnNumNotaFiscal"))

        self.radBtnDataEntrada = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnDataEntrada.setGeometry(QtCore.QRect(10, 40, 141, 23))
        self.radBtnDataEntrada.setObjectName(_fromUtf8("radBtnDataEntrada"))
        self.radBtnDataPeriodos = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnDataPeriodos.setGeometry(QtCore.QRect(10, 80, 111, 23))
        self.radBtnDataPeriodos.setObjectName(_fromUtf8("radBtnDataPeriodos"))

        self.radBtnDataEmitido = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnDataEmitido.setGeometry(QtCore.QRect(10, 60, 111, 23))
        self.radBtnDataEmitido.setObjectName(_fromUtf8("radBtnDataEmitido"))

        self.txtPesquisar = QtGui.QLineEdit(frmConsultarNotasFiscais)
        self.txtPesquisar.setEnabled(False)
        self.txtPesquisar.setGeometry(QtCore.QRect(380, 80, 361, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmConsultarNotasFiscais)
        self.btnPesquisar.setEnabled(False)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 80, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmConsultarNotasFiscais)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 120, 771, 371))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.setColumnCount(11)
        self.tabPesquisar.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(10, item)
        self.tabPesquisar.verticalHeader().setVisible(False)
        self.tabPesquisar.verticalHeader().setCascadingSectionResizes(True)

        self.txtDataInicial = QtGui.QDateEdit(frmConsultarNotasFiscais)
        self.txtDataInicial.setDate(QtCore.QDate.currentDate())
        self.txtDataInicial.setEnabled(False)
        self.txtDataInicial.setGeometry(QtCore.QRect(250, 20, 110, 25))
        self.txtDataInicial.setCalendarPopup(True)
        self.txtDataInicial.setObjectName(_fromUtf8("txtDataInicial"))

        self.txtDataFinal = QtGui.QDateEdit(frmConsultarNotasFiscais)
        self.txtDataFinal.setDate(QtCore.QDate.currentDate())
        self.txtDataFinal.setEnabled(False)
        self.txtDataFinal.setGeometry(QtCore.QRect(250, 67, 110, 25))
        self.txtDataFinal.setCalendarPopup(True)
        self.txtDataFinal.setObjectName(_fromUtf8("txtDataFinal"))

        self.lblDataInicio = QtGui.QLabel(frmConsultarNotasFiscais)
        self.lblDataInicio.setGeometry(QtCore.QRect(180, 23, 66, 19))
        self.lblDataInicio.setObjectName(_fromUtf8("lblDataInicio"))

        self.lblDataFinal = QtGui.QLabel(frmConsultarNotasFiscais)
        self.lblDataFinal.setGeometry(QtCore.QRect(180, 70, 66, 19))
        self.lblDataFinal.setObjectName(_fromUtf8("lblDataFinal"))

        self.lblDataInicio.setBuddy(self.txtDataInicial)
        self.lblDataFinal.setBuddy(self.txtDataFinal)

        self.retranslateUi(frmConsultarNotasFiscais)
        QtCore.QMetaObject.connectSlotsByName(frmConsultarNotasFiscais)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnNumNotaFiscal, self.radBtnDataEntrada)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnDataEntrada, self.radBtnDataPeriodos)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnDataPeriodos, self.txtPesquisar)
        frmConsultarNotasFiscais.setTabOrder(self.txtPesquisar, self.txtDataInicial)
        frmConsultarNotasFiscais.setTabOrder(self.txtDataInicial, self.txtDataFinal)

    def retranslateUi(self, frmConsultarNotasFiscais):
        frmConsultarNotasFiscais.setWindowTitle(_translate("frmConsultarNotasFiscais", "Consultar Notas Fiscal", None))
        self.grbTipoPesquisa.setTitle(_translate("frmConsultarNotasFiscais", "Tipo Pesquisa", None))
        self.radBtnNumNotaFiscal.setWhatsThis(_translate("frmConsultarNotasFiscais", "<html><head/><body><p>Campo de seleção para pesquisa por numero de NF</p></body></html>", None))
        self.radBtnNumNotaFiscal.setText(_translate("frmConsultarNotasFiscais", "Nº Nota Fiscal", None))
        self.radBtnDataEntrada.setToolTip(_translate("frmConsultarNotasFiscais", "Inscrição Estadual", None))
        self.radBtnDataEntrada.setWhatsThis(_translate("frmConsultarNotasFiscais", "<html><head/><body><p>Campo de seleção para pesquisa por data de entrada de NF</p></body></html>", None))
        self.radBtnDataEntrada.setText(_translate("frmConsultarNotasFiscais", "Data Entrada", None))
        self.radBtnDataPeriodos.setToolTip(_translate("frmConsultarNotasFiscais", "Inscrição Estadual", None))
        self.radBtnDataPeriodos.setWhatsThis(_translate("frmConsultarNotasFiscais", "<html><head/><body><p>Campo de seleção para pesquisa por periodo de data de entrada de NF</p></body></html>", None))
        self.radBtnDataPeriodos.setText(_translate("frmConsultarNotasFiscais", "Data Periodos", None))
        self.radBtnDataEmitido.setToolTip(_translate("frmConsultarNotasFiscais", "Inscrição Estadual", None))
        self.radBtnDataEmitido.setWhatsThis(_translate("frmConsultarNotasFiscais", "<html><head/><body><p>Campo de seleção para pesquisa por data de emitido NF</p></body></html>", None))
        self.radBtnDataEmitido.setText(_translate("frmConsultarNotasFiscais", "Data Emitido", None))
        self.txtPesquisar.setToolTip(_translate("frmConsultarNotasFiscais", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmConsultarNotasFiscais", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmConsultarNotasFiscais", "Pesquisar", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmConsultarNotasFiscais", "Codigo", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmConsultarNotasFiscais", "Serie", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmConsultarNotasFiscais", "Serie", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmConsultarNotasFiscais", "Número Nf", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmConsultarNotasFiscais", "Data Emissão", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmConsultarNotasFiscais", "Data Entrada", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmConsultarNotasFiscais", "Valor Total", None))
        item = self.tabPesquisar.horizontalHeaderItem(7)
        item.setText(_translate("frmConsultarNotasFiscais", "Valor ICMS", None))
        item = self.tabPesquisar.horizontalHeaderItem(8)
        item.setText(_translate("frmConsultarNotasFiscais", "Valor IPI", None))
        item = self.tabPesquisar.horizontalHeaderItem(9)
        item.setText(_translate("frmConsultarNotasFiscais", "Alicota ICMS", None))
        item = self.tabPesquisar.horizontalHeaderItem(10)
        item.setText(_translate("frmConsultarNotasFiscais", "Alicota IPI", None))
        self.txtDataInicial.setToolTip(_translate("frmConsultarNotasFiscais", "Data Inicio", None))
        self.txtDataInicial.setWhatsThis(_translate("frmConsultarNotasFiscais", "Campo de data inicial", None))
        self.txtDataFinal.setToolTip(_translate("frmConsultarNotasFiscais", "Data Final", None))
        self.txtDataFinal.setWhatsThis(_translate("frmConsultarNotasFiscais", "Campo de data final", None))
        self.lblDataInicio.setText(_translate("frmConsultarNotasFiscais", "Data Incio", None))
        self.lblDataFinal.setText(_translate("frmConsultarNotasFiscais", "Data Final", None))


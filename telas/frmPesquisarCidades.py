# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarCidades.ui'
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

class Ui_frmConsultarCidades(object):
    def setupUi(self, frmConsultarCidades):
        frmConsultarCidades.setObjectName(_fromUtf8("frmConsultarCidades"))
        frmConsultarCidades.resize(731, 481)
        frmConsultarCidades.setMinimumSize(QtCore.QSize(731, 481))
        frmConsultarCidades.setMaximumSize(QtCore.QSize(731, 481))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmConsultarCidades.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmConsultarCidades.setWindowIcon(icon)
        frmConsultarCidades.setSizeGripEnabled(True)
        frmConsultarCidades.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmConsultarCidades)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 221, 71))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnCidade = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCidade.setGeometry(QtCore.QRect(10, 38, 81, 23))
        self.radBtnCidade.setObjectName(_fromUtf8("radBtnCidade"))

        self.radBtnEstado = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnEstado.setGeometry(QtCore.QRect(140, 15, 71, 23))
        self.radBtnEstado.setObjectName(_fromUtf8("radBtnEstado"))

        self.radBtnCep = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCep.setGeometry(QtCore.QRect(140, 40, 61, 23))
        self.radBtnCep.setObjectName(_fromUtf8("radBtnCep"))

        self.radBtnCodigoCidade = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCodigoCidade.setGeometry(QtCore.QRect(10, 15, 101, 23))
        self.radBtnCodigoCidade.setObjectName(_fromUtf8("radBtnCodigoCidade"))

        self.txtPesquisar = QtGui.QLineEdit(frmConsultarCidades)
        self.txtPesquisar.setGeometry(QtCore.QRect(240, 52, 441, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmConsultarCidades)
        self.btnPesquisar.setGeometry(QtCore.QRect(690, 50, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmConsultarCidades)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 90, 711, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tabPesquisar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.setColumnCount(4)
        self.tabPesquisar.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(3, item)
        self.tabPesquisar.setEditTriggers(self.tabPesquisar.NoEditTriggers)
        self.tabPesquisar.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisar.verticalHeader().setVisible(False)

        self.retranslateUi(frmConsultarCidades)
        QtCore.QMetaObject.connectSlotsByName(frmConsultarCidades)
        frmConsultarCidades.setTabOrder(self.radBtnCidade, self.radBtnEstado)
        frmConsultarCidades.setTabOrder(self.radBtnEstado, self.radBtnCep)
        frmConsultarCidades.setTabOrder(self.radBtnCep, self.txtPesquisar)
        frmConsultarCidades.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmConsultarCidades.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmConsultarCidades):
        frmConsultarCidades.setWindowTitle(_translate("frmConsultarCidades", "Pesquisar Cidades", None))
        frmConsultarCidades.setToolTip(_translate("frmConsultarCidades", "Pesquisar", None))
        frmConsultarCidades.setWhatsThis(_translate("frmConsultarCidades", "<html><head/><body><p>Campo de inserir os dados para pesquisar</p></body></html>", None))
        self.grbTipoPesquisa.setTitle(_translate("frmConsultarCidades", "Tipo Pesquisa", None))
        self.radBtnCidade.setToolTip(_translate("frmConsultarCidades", "Cidade", None))
        self.radBtnCidade.setWhatsThis(_translate("frmConsultarCidades", "<html><head/><body><p>Item de seleção para a pesquisa por nome da cidade</p></body></html>", None))
        self.radBtnCidade.setText(_translate("frmConsultarCidades", "Cidade", None))
        self.radBtnEstado.setToolTip(_translate("frmConsultarCidades", "Estado", None))
        self.radBtnEstado.setWhatsThis(_translate("frmConsultarCidades", "<html><head/><body><p>Item de seleção para a pesquisa por estado</p></body></html>", None))
        self.radBtnEstado.setText(_translate("frmConsultarCidades", "Estado", None))
        self.radBtnCep.setToolTip(_translate("frmConsultarCidades", "CEP", None))
        self.radBtnCep.setWhatsThis(_translate("frmConsultarCidades", "<html><head/><body><p>Item de seleção para a pesquisa por CEP</p></body></html>", None))
        self.radBtnCep.setText(_translate("frmConsultarCidades", "Cep", None))
        self.radBtnCodigoCidade.setToolTip(_translate("frmConsultarCidades", "Codigo Cidade", None))
        self.radBtnCodigoCidade.setWhatsThis(_translate("frmConsultarCidades", "<html><head/><body><p>Item de seleção para a pesquisa por Codigo da Cidade</p></body></html>", None))
        self.radBtnCodigoCidade.setText(_translate("frmConsultarCidades", "Cod. Cidade", None))
        self.txtPesquisar.setToolTip(_translate("frmConsultarCidades", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmConsultarCidades", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmConsultarCidades", "Pesquisar", None))
        self.btnPesquisar.setWhatsThis(_translate("frmConsultarCidades", "<html><head/><body><p>Botão para pesquisar as informações</p></body></html>", None))
        self.tabPesquisar.setWhatsThis(_translate("frmConsultarCidades", "<html><head/><body><p>Tabela dos dados pesquisados</p></body></html>", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmConsultarCidades", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmConsultarCidades", "Cidade", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmConsultarCidades", "Estado", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmConsultarCidades", "CEP", None))


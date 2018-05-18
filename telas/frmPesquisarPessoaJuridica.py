# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarPessoaJuridica.ui'
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

class Ui_frmPesquisarPessoaJuridica(object):
    def setupUi(self, frmPesquisarPessoaJuridica):
        frmPesquisarPessoaJuridica.setObjectName(_fromUtf8("frmPesquisarPessoaJuridica"))
        frmPesquisarPessoaJuridica.resize(794, 504)
        frmPesquisarPessoaJuridica.setMinimumSize(QtCore.QSize(794, 504))
        frmPesquisarPessoaJuridica.setMaximumSize(QtCore.QSize(794, 504))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmPesquisarPessoaJuridica.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmPesquisarPessoaJuridica.setWindowIcon(icon)
        frmPesquisarPessoaJuridica.setSizeGripEnabled(True)
        frmPesquisarPessoaJuridica.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmPesquisarPessoaJuridica)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 251, 91))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnRazaoSocial = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRazaoSocial.setGeometry(QtCore.QRect(20, 40, 101, 23))
        self.radBtnRazaoSocial.setObjectName(_fromUtf8("radBtnRazaoSocial"))

        self.radBtnFantasia = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnFantasia.setGeometry(QtCore.QRect(20, 60, 81, 23))
        self.radBtnFantasia.setObjectName(_fromUtf8("radBtnFantasia"))

        self.radBtnCnpj = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCnpj.setGeometry(QtCore.QRect(130, 20, 51, 23))
        self.radBtnCnpj.setObjectName(_fromUtf8("radBtnCnpj"))

        self.radBtnInsEstadual = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnInsEstadual.setGeometry(QtCore.QRect(130, 40, 111, 23))
        self.radBtnInsEstadual.setObjectName(_fromUtf8("radBtnInsEstadual"))

        self.radBtnCodigo = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCodigo.setGeometry(QtCore.QRect(20, 20, 63, 23))
        self.radBtnCodigo.setObjectName(_fromUtf8("radBtnCodigo"))

        self.txtPesquisar = QtGui.QLineEdit(frmPesquisarPessoaJuridica)
        self.txtPesquisar.setGeometry(QtCore.QRect(300, 70, 441, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmPesquisarPessoaJuridica)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 70, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmPesquisarPessoaJuridica)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 110, 771, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.setColumnCount(13)
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
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(12, item)
        self.tabPesquisar.verticalHeader().setVisible(False)
        self.tabPesquisar.verticalHeader().setCascadingSectionResizes(True)

        self.retranslateUi(frmPesquisarPessoaJuridica)
        QtCore.QMetaObject.connectSlotsByName(frmPesquisarPessoaJuridica)
        frmPesquisarPessoaJuridica.setTabOrder(self.radBtnRazaoSocial, self.radBtnFantasia)
        frmPesquisarPessoaJuridica.setTabOrder(self.radBtnFantasia, self.radBtnCnpj)
        frmPesquisarPessoaJuridica.setTabOrder(self.radBtnCnpj, self.radBtnInsEstadual)
        frmPesquisarPessoaJuridica.setTabOrder(self.radBtnInsEstadual, self.txtPesquisar)
        frmPesquisarPessoaJuridica.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmPesquisarPessoaJuridica.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmPesquisarPessoaJuridica):
        frmPesquisarPessoaJuridica.setWindowTitle(_translate("frmPesquisarPessoaJuridica", "Pesquisar Pessoa Jurídica", None))
        self.grbTipoPesquisa.setTitle(_translate("frmPesquisarPessoaJuridica", "Tipo Pesquisa", None))
        self.radBtnRazaoSocial.setToolTip(_translate("frmPesquisarPessoaJuridica", "Nome", None))
        self.radBtnRazaoSocial.setWhatsThis(_translate("frmPesquisarPessoaJuridica", "Item de seleção para a pesquisa por nome", None))
        self.radBtnRazaoSocial.setText(_translate("frmPesquisarPessoaJuridica", "Razão Social", None))
        self.radBtnFantasia.setToolTip(_translate("frmPesquisarPessoaJuridica", "CPF", None))
        self.radBtnFantasia.setWhatsThis(_translate("frmPesquisarPessoaJuridica", "Item de seleção para a pesquisa por CPF", None))
        self.radBtnFantasia.setText(_translate("frmPesquisarPessoaJuridica", "Fantasia", None))
        self.radBtnCnpj.setToolTip(_translate("frmPesquisarPessoaJuridica", "RG", None))
        self.radBtnCnpj.setWhatsThis(_translate("frmPesquisarPessoaJuridica", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCnpj.setText(_translate("frmPesquisarPessoaJuridica", "CNPJ", None))
        self.radBtnInsEstadual.setToolTip(_translate("frmPesquisarPessoaJuridica", "Mãe", None))
        self.radBtnInsEstadual.setWhatsThis(_translate("frmPesquisarPessoaJuridica", "Item de seleção para a pesquisa por mãe", None))
        self.radBtnInsEstadual.setText(_translate("frmPesquisarPessoaJuridica", "Ins. Estadual", None))
        self.radBtnCodigo.setToolTip(_translate("frmPesquisarPessoaJuridica", "RG", None))
        self.radBtnCodigo.setWhatsThis(_translate("frmPesquisarPessoaJuridica", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCodigo.setText(_translate("frmPesquisarPessoaJuridica", "Codigo", None))
        self.txtPesquisar.setToolTip(_translate("frmPesquisarPessoaJuridica", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmPesquisarPessoaJuridica", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmPesquisarPessoaJuridica", "Pesquisa", None))
        self.btnPesquisar.setWhatsThis(_translate("frmPesquisarPessoaJuridica", "Botão para pesquisar as informações", None))
        self.tabPesquisar.setWhatsThis(_translate("frmPesquisarPessoaJuridica", "Tabela dos dados pesquisados", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Razão Social", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Fantasia", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmPesquisarPessoaJuridica", "CNPJ", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Ins. Estadual", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Endereço", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Número", None))
        item = self.tabPesquisar.horizontalHeaderItem(7)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Complemento", None))
        item = self.tabPesquisar.horizontalHeaderItem(8)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Bairro", None))
        item = self.tabPesquisar.horizontalHeaderItem(9)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Cidade", None))
        item = self.tabPesquisar.horizontalHeaderItem(10)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Estado", None))
        item = self.tabPesquisar.horizontalHeaderItem(11)
        item.setText(_translate("frmPesquisarPessoaJuridica", "CEP", None))
        item = self.tabPesquisar.horizontalHeaderItem(12)
        item.setText(_translate("frmPesquisarPessoaJuridica", "Site", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarPessoaFisicaJuridica.ui'
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

class Ui_frmPesquisarPessoaFisicaJuridica(object):
    def setupUi(self, frmPesquisarPessoaFisicaJuridica):
        frmPesquisarPessoaFisicaJuridica.setObjectName(_fromUtf8("frmPesquisarPessoaFisicaJuridica"))
        frmPesquisarPessoaFisicaJuridica.resize(794, 504)
        frmPesquisarPessoaFisicaJuridica.setMinimumSize(QtCore.QSize(794, 504))
        frmPesquisarPessoaFisicaJuridica.setMaximumSize(QtCore.QSize(794, 504))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmPesquisarPessoaFisicaJuridica.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/folder_saved_search.png")), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        frmPesquisarPessoaFisicaJuridica.setWindowIcon(icon)
        frmPesquisarPessoaFisicaJuridica.setSizeGripEnabled(True)
        frmPesquisarPessoaFisicaJuridica.setModal(True)
        
        self.grbTipoPesquisa = QtGui.QGroupBox(frmPesquisarPessoaFisicaJuridica)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 331, 91))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))
        
        self.radBtnRazaoSocial = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRazaoSocial.setGeometry(QtCore.QRect(10, 40, 151, 23))
        self.radBtnRazaoSocial.setObjectName(_fromUtf8("radBtnRazaoSocial"))
        
        self.radBtnFantasia = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnFantasia.setGeometry(QtCore.QRect(10, 60, 141, 23))
        self.radBtnFantasia.setObjectName(_fromUtf8("radBtnFantasia"))
        
        self.radBtnCnpj = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCnpj.setGeometry(QtCore.QRect(180, 20, 51, 23))
        self.radBtnCnpj.setObjectName(_fromUtf8("radBtnCnpj"))
        
        self.radBtnInsEstadual = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnInsEstadual.setGeometry(QtCore.QRect(180, 40, 141, 23))
        self.radBtnInsEstadual.setObjectName(_fromUtf8("radBtnInsEstadual"))
        
        self.radBtnCodigo = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCodigo.setGeometry(QtCore.QRect(10, 20, 63, 23))
        self.radBtnCodigo.setObjectName(_fromUtf8("radBtnCodigo"))
        
        self.txtPesquisar = QtGui.QLineEdit(frmPesquisarPessoaFisicaJuridica)
        self.txtPesquisar.setGeometry(QtCore.QRect(350, 70, 391, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))
        
        self.btnPesquisar = QtGui.QPushButton(frmPesquisarPessoaFisicaJuridica)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 70, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))
        
        self.tabPesquisar = QtGui.QTableWidget(frmPesquisarPessoaFisicaJuridica)
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

        self.retranslateUi(frmPesquisarPessoaFisicaJuridica)
        QtCore.QMetaObject.connectSlotsByName(frmPesquisarPessoaFisicaJuridica)
        frmPesquisarPessoaFisicaJuridica.setTabOrder(self.radBtnRazaoSocial, self.radBtnFantasia)
        frmPesquisarPessoaFisicaJuridica.setTabOrder(self.radBtnFantasia, self.radBtnCnpj)
        frmPesquisarPessoaFisicaJuridica.setTabOrder(self.radBtnCnpj, self.radBtnInsEstadual)
        frmPesquisarPessoaFisicaJuridica.setTabOrder(self.radBtnInsEstadual, self.txtPesquisar)
        frmPesquisarPessoaFisicaJuridica.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmPesquisarPessoaFisicaJuridica.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmPesquisarPessoaFisicaJuridica):
        frmPesquisarPessoaFisicaJuridica.setWindowTitle(_translate("frmPesquisarPessoaFisicaJuridica", "Pesquisar Pessoa Fisica / Juridica", None))
        self.grbTipoPesquisa.setTitle(_translate("frmPesquisarPessoaFisicaJuridica", "Tipo Pesquisa", None))
        self.radBtnRazaoSocial.setToolTip(_translate("frmPesquisarPessoaFisicaJuridica", "Nome", None))
        self.radBtnRazaoSocial.setWhatsThis(_translate("frmPesquisarPessoaFisicaJuridica", "Item de seleção para a pesquisa por nome", None))
        self.radBtnRazaoSocial.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Razão Social / nome", None))
        self.radBtnFantasia.setToolTip(_translate("frmPesquisarPessoaFisicaJuridica", "CPF", None))
        self.radBtnFantasia.setWhatsThis(_translate("frmPesquisarPessoaFisicaJuridica", "Item de seleção para a pesquisa por CPF", None))
        self.radBtnFantasia.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Fantasia / Apelido", None))
        self.radBtnCnpj.setToolTip(_translate("frmPesquisarPessoaFisicaJuridica", "RG", None))
        self.radBtnCnpj.setWhatsThis(_translate("frmPesquisarPessoaFisicaJuridica", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCnpj.setText(_translate("frmPesquisarPessoaFisicaJuridica", "CNPJ/ CPF", None))
        self.radBtnInsEstadual.setToolTip(_translate("frmPesquisarPessoaFisicaJuridica", "Mãe", None))
        self.radBtnInsEstadual.setWhatsThis(_translate("frmPesquisarPessoaFisicaJuridica", "Item de seleção para a pesquisa por mãe", None))
        self.radBtnInsEstadual.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Ins. Estadual / RG", None))
        self.radBtnCodigo.setToolTip(_translate("frmPesquisarPessoaFisicaJuridica", "RG", None))
        self.radBtnCodigo.setWhatsThis(_translate("frmPesquisarPessoaFisicaJuridica", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCodigo.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Codigo", None))
        self.txtPesquisar.setToolTip(_translate("frmPesquisarPessoaFisicaJuridica", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmPesquisarPessoaFisicaJuridica", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmPesquisarPessoaFisicaJuridica", "Pesquisa", None))
        self.btnPesquisar.setWhatsThis(_translate("frmPesquisarPessoaFisicaJuridica", "Botão para pesquisar as informações", None))
        self.tabPesquisar.setWhatsThis(_translate("frmPesquisarPessoaFisicaJuridica", "Tabela dos dados pesquisados", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "R. Social / Nome", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Fantasia / Apelido", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "CNPJ / CPF", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Ins. Estadual / RG", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Endereço", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Número", None))
        item = self.tabPesquisar.horizontalHeaderItem(7)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Complemento", None))
        item = self.tabPesquisar.horizontalHeaderItem(8)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Bairro", None))
        item = self.tabPesquisar.horizontalHeaderItem(9)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Cidade", None))
        item = self.tabPesquisar.horizontalHeaderItem(10)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "Estado", None))
        item = self.tabPesquisar.horizontalHeaderItem(11)
        item.setText(_translate("frmPesquisarPessoaFisicaJuridica", "CEP", None))


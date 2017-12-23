# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarClientes.ui'
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

class Ui_frmPesquisarCliente(object):
    def setupUi(self, frmPesquisarCliente):
        frmPesquisarCliente.setObjectName(_fromUtf8("frmPesquisarCliente"))
        frmPesquisarCliente.resize(794, 504)
        frmPesquisarCliente.setMinimumSize(QtCore.QSize(794, 504))
        frmPesquisarCliente.setMaximumSize(QtCore.QSize(794, 504))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmPesquisarCliente.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmPesquisarCliente.setWindowIcon(icon)
        frmPesquisarCliente.setSizeGripEnabled(True)
        frmPesquisarCliente.setModal(True)
        
        self.grbTipoPesquisa = QtGui.QGroupBox(frmPesquisarCliente)
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
        
        self.txtPesquisar = QtGui.QLineEdit(frmPesquisarCliente)
        self.txtPesquisar.setGeometry(QtCore.QRect(350, 70, 391, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))
        
        self.btnPesquisar = QtGui.QPushButton(frmPesquisarCliente)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 70, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))
        
        self.tabPesquisar = QtGui.QTableWidget(frmPesquisarCliente)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 110, 771, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.verticalHeader().setVisible(False)
        self.tabPesquisar.verticalHeader().setCascadingSectionResizes(True)

        self.retranslateUi(frmPesquisarCliente)
        QtCore.QMetaObject.connectSlotsByName(frmPesquisarCliente)
        frmPesquisarCliente.setTabOrder(self.radBtnRazaoSocial, self.radBtnFantasia)
        frmPesquisarCliente.setTabOrder(self.radBtnFantasia, self.radBtnCnpj)
        frmPesquisarCliente.setTabOrder(self.radBtnCnpj, self.radBtnInsEstadual)
        frmPesquisarCliente.setTabOrder(self.radBtnInsEstadual, self.txtPesquisar)
        frmPesquisarCliente.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmPesquisarCliente.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmPesquisarCliente):
        frmPesquisarCliente.setWindowTitle(_translate("frmPesquisarCliente", "Pesquisar Cliente", None))
        self.grbTipoPesquisa.setTitle(_translate("frmPesquisarCliente", "Tipo Pesquisa", None))
        self.radBtnRazaoSocial.setToolTip(_translate("frmPesquisarCliente", "Nome", None))
        self.radBtnRazaoSocial.setWhatsThis(_translate("frmPesquisarCliente", "Item de seleção para a pesquisa por nome", None))
        self.radBtnRazaoSocial.setText(_translate("frmPesquisarCliente", "Razão Social / nome", None))
        self.radBtnFantasia.setToolTip(_translate("frmPesquisarCliente", "CPF", None))
        self.radBtnFantasia.setWhatsThis(_translate("frmPesquisarCliente", "Item de seleção para a pesquisa por CPF", None))
        self.radBtnFantasia.setText(_translate("frmPesquisarCliente", "Fantasia / Apelido", None))
        self.radBtnCnpj.setToolTip(_translate("frmPesquisarCliente", "RG", None))
        self.radBtnCnpj.setWhatsThis(_translate("frmPesquisarCliente", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCnpj.setText(_translate("frmPesquisarCliente", "CNPJ/ CPF", None))
        self.radBtnInsEstadual.setToolTip(_translate("frmPesquisarCliente", "Mãe", None))
        self.radBtnInsEstadual.setWhatsThis(_translate("frmPesquisarCliente", "Item de seleção para a pesquisa por mãe", None))
        self.radBtnInsEstadual.setText(_translate("frmPesquisarCliente", "Ins. Estadual / RG", None))
        self.radBtnCodigo.setToolTip(_translate("frmPesquisarCliente", "RG", None))
        self.radBtnCodigo.setWhatsThis(_translate("frmPesquisarCliente", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCodigo.setText(_translate("frmPesquisarCliente", "Codigo", None))
        self.txtPesquisar.setToolTip(_translate("frmPesquisarCliente", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmPesquisarCliente", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmPesquisarCliente", "Pesquisa", None))
        self.btnPesquisar.setWhatsThis(_translate("frmPesquisarCliente", "Botão para pesquisar as informações", None))
        self.tabPesquisar.setWhatsThis(_translate("frmPesquisarCliente", "Tabela dos dados pesquisados", None))



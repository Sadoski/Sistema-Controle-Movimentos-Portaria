# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarFornecedor.ui'
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

class Ui_frmConsultarFornecedores(object):
    def setupUi(self, frmConsultarFornecedores):
        frmConsultarFornecedores.setObjectName(_fromUtf8("frmConsultarFornecedores"))
        frmConsultarFornecedores.resize(793, 502)
        frmConsultarFornecedores.setMinimumSize(QtCore.QSize(793, 502))
        frmConsultarFornecedores.setMaximumSize(QtCore.QSize(793, 502))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmConsultarFornecedores.setFont(font)

        self.txtPesquisar = QtGui.QLineEdit(frmConsultarFornecedores)
        self.txtPesquisar.setGeometry(QtCore.QRect(300, 70, 441, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.lblPesquisar = QtGui.QLabel(frmConsultarFornecedores)
        self.lblPesquisar.setGeometry(QtCore.QRect(300, 50, 71, 19))
        self.lblPesquisar.setObjectName(_fromUtf8("lblPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmConsultarFornecedores)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 70, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.grbTipoPesquisa = QtGui.QGroupBox(frmConsultarFornecedores)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 281, 91))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnFantasia = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnFantasia.setGeometry(QtCore.QRect(10, 38, 81, 23))
        self.radBtnFantasia.setObjectName(_fromUtf8("radBtnFantasia"))

        self.radBtnRazaoSocial = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRazaoSocial.setGeometry(QtCore.QRect(10, 64, 109, 23))
        self.radBtnRazaoSocial.setObjectName(_fromUtf8("radBtnRazaoSocial"))

        self.radBtnCnpj = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCnpj.setGeometry(QtCore.QRect(130, 13, 61, 23))
        self.radBtnCnpj.setObjectName(_fromUtf8("radBtnCnpj"))

        self.radBtnIncrisaoEstadual = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnIncrisaoEstadual.setGeometry(QtCore.QRect(130, 37, 141, 23))
        self.radBtnIncrisaoEstadual.setObjectName(_fromUtf8("radBtnIncrisaoEstadual"))

        self.radBtnCodigo = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCodigo.setGeometry(QtCore.QRect(10, 15, 81, 23))
        self.radBtnCodigo.setObjectName(_fromUtf8("radBtnCodigo"))

        self.tabPesquisar = QtGui.QTableWidget(frmConsultarFornecedores)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 110, 771, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
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
        self.tabPesquisar.setEditTriggers(self.tabPesquisar.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(self.tabPesquisar.SelectRows)
        self.tabPesquisar.setSelectionMode(self.tabPesquisar.SingleSelection)
        self.lblPesquisar.setBuddy(self.txtPesquisar)

        self.retranslateUi(frmConsultarFornecedores)
        QtCore.QMetaObject.connectSlotsByName(frmConsultarFornecedores)
        frmConsultarFornecedores.setTabOrder(self.txtPesquisar, self.btnPesquisar)

    def retranslateUi(self, frmConsultarFornecedores):
        frmConsultarFornecedores.setWindowTitle(_translate("frmConsultarFornecedores", "Pesquisar Fornecedores", None))
        self.txtPesquisar.setToolTip(_translate("frmConsultarFornecedores", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmConsultarFornecedores", "Campo de inserir os dados para pesquisar", None))
        self.lblPesquisar.setText(_translate("frmConsultarFornecedores", "Pesquisar", None))
        self.grbTipoPesquisa.setTitle(_translate("frmConsultarFornecedores", "Tipo Pesquisa", None))
        self.radBtnFantasia.setToolTip(_translate("frmConsultarFornecedores", "Fantasia", None))
        self.radBtnFantasia.setText(_translate("frmConsultarFornecedores", "Fantasia", None))
        self.radBtnRazaoSocial.setToolTip(_translate("frmConsultarFornecedores", "Razão Social", None))
        self.radBtnRazaoSocial.setText(_translate("frmConsultarFornecedores", "Razão Social", None))
        self.radBtnCnpj.setToolTip(_translate("frmConsultarFornecedores", "CNPJ", None))
        self.radBtnCnpj.setText(_translate("frmConsultarFornecedores", "CNPJ", None))
        self.radBtnIncrisaoEstadual.setToolTip(_translate("frmConsultarFornecedores", "Inscrição Estadual", None))
        self.radBtnIncrisaoEstadual.setText(_translate("frmConsultarFornecedores", "Inscrição Estadual", None))
        self.radBtnCodigo.setToolTip(_translate("frmConsultarFornecedores", "Fantasia", None))
        self.radBtnCodigo.setText(_translate("frmConsultarFornecedores", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmConsultarFornecedores", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmConsultarFornecedores", "Fantasia", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmConsultarFornecedores", "Razão Social", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmConsultarFornecedores", "CPNJ", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmConsultarFornecedores", "Ins. Estdual", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmConsultarFornecedores", "Endereco", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmConsultarFornecedores", "Numero", None))
        item = self.tabPesquisar.horizontalHeaderItem(7)
        item.setText(_translate("frmConsultarFornecedores", "Bairro", None))
        item = self.tabPesquisar.horizontalHeaderItem(8)
        item.setText(_translate("frmConsultarFornecedores", "Cidade", None))
        item = self.tabPesquisar.horizontalHeaderItem(9)
        item.setText(_translate("frmConsultarFornecedores", "Estado", None))
        item = self.tabPesquisar.horizontalHeaderItem(10)
        item.setText(_translate("frmConsultarFornecedores", "CEP", None))


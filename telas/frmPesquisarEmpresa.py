# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarEmpresa.ui'
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

class Ui_frmConsultarEmpresa(object):
    def setupUi(self, frmConsultarEmpresa):
        frmConsultarEmpresa.setObjectName(_fromUtf8("frmConsultarEmpresa"))
        frmConsultarEmpresa.resize(793, 502)
        frmConsultarEmpresa.setMinimumSize(QtCore.QSize(793, 502))
        frmConsultarEmpresa.setMaximumSize(QtCore.QSize(793, 502))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmConsultarEmpresa.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmConsultarEmpresa.setWindowIcon(icon)
        frmConsultarEmpresa.setSizeGripEnabled(True)
        frmConsultarEmpresa.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmConsultarEmpresa)
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

        self.radBtnIncrisaoMunicipal = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnIncrisaoMunicipal.setGeometry(QtCore.QRect(130, 64, 141, 23))
        self.radBtnIncrisaoMunicipal.setObjectName(_fromUtf8("radBtnIncrisaoMunicipal"))

        self.txtPesquisar = QtGui.QLineEdit(frmConsultarEmpresa)
        self.txtPesquisar.setGeometry(QtCore.QRect(300, 70, 441, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))
        self.btnPesquisar = QtGui.QPushButton(frmConsultarEmpresa)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 68, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))
        self.tabPesquisar = QtGui.QTableWidget(frmConsultarEmpresa)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 110, 771, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.setColumnCount(16)
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
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(15, item)
        self.tabPesquisar.setEditTriggers(self.tabPesquisar.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(self.tabPesquisar.SelectRows)
        self.tabPesquisar.setSelectionMode(self.tabPesquisar.SingleSelection)
        self.tabPesquisar.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisar.verticalHeader().setVisible(False)

        self.retranslateUi(frmConsultarEmpresa)
        QtCore.QMetaObject.connectSlotsByName(frmConsultarEmpresa)
        frmConsultarEmpresa.setTabOrder(self.radBtnFantasia, self.radBtnRazaoSocial)
        frmConsultarEmpresa.setTabOrder(self.radBtnRazaoSocial, self.radBtnCnpj)
        frmConsultarEmpresa.setTabOrder(self.radBtnCnpj, self.radBtnIncrisaoEstadual)
        frmConsultarEmpresa.setTabOrder(self.radBtnIncrisaoEstadual, self.txtPesquisar)
        frmConsultarEmpresa.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmConsultarEmpresa.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmConsultarEmpresa):
        frmConsultarEmpresa.setWindowTitle(_translate("frmConsultarEmpresa", "Pesquisar Empresas", None))
        self.grbTipoPesquisa.setTitle(_translate("frmConsultarEmpresa", "Tipo Pesquisa", None))
        self.radBtnFantasia.setToolTip(_translate("frmConsultarEmpresa", "Fantasia", None))
        self.radBtnFantasia.setWhatsThis(_translate("frmConsultarEmpresa", "<html><head/><body><p>Item de seleção para a pesquisa por fantasia</p></body></html>", None))
        self.radBtnFantasia.setText(_translate("frmConsultarEmpresa", "Fantasia", None))
        self.radBtnRazaoSocial.setToolTip(_translate("frmConsultarEmpresa", "Razão Social", None))
        self.radBtnRazaoSocial.setWhatsThis(_translate("frmConsultarEmpresa", "<html><head/><body><p>Item de seleção para a pesquisa por razão social</p></body></html>", None))
        self.radBtnRazaoSocial.setText(_translate("frmConsultarEmpresa", "Razão Social", None))
        self.radBtnCnpj.setToolTip(_translate("frmConsultarEmpresa", "CNPJ", None))
        self.radBtnCnpj.setWhatsThis(_translate("frmConsultarEmpresa", "<html><head/><body><p>Item de seleção para a pesquisa por CNPJ</p></body></html>", None))
        self.radBtnCnpj.setText(_translate("frmConsultarEmpresa", "CNPJ", None))
        self.radBtnIncrisaoEstadual.setToolTip(_translate("frmConsultarEmpresa", "Inscrição Estadual", None))
        self.radBtnIncrisaoEstadual.setWhatsThis(_translate("frmConsultarEmpresa", "<html><head/><body><p>Item de seleção para a pesquisa por inscrição estadual</p></body></html>", None))
        self.radBtnIncrisaoEstadual.setText(_translate("frmConsultarEmpresa", "Inscrição Estadual", None))
        self.radBtnCodigo.setToolTip(_translate("frmConsultarEmpresa", "Codigo", None))
        self.radBtnCodigo.setWhatsThis(_translate("frmConsultarEmpresa", "<html><head/><body><p>Item de seleção para a pesquisa por codigo</p></body></html>", None))
        self.radBtnCodigo.setText(_translate("frmConsultarEmpresa", "Cod.", None))
        self.radBtnIncrisaoMunicipal.setToolTip(_translate("frmConsultarEmpresa", "Inscrição Municipal", None))
        self.radBtnIncrisaoMunicipal.setWhatsThis(_translate("frmConsultarEmpresa", "<html><head/><body><p>Item de seleção para a pesquisa por inscrição municipal</p></body></html>", None))
        self.radBtnIncrisaoMunicipal.setText(_translate("frmConsultarEmpresa", "Inscrição Municipal", None))
        self.txtPesquisar.setToolTip(_translate("frmConsultarEmpresa", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmConsultarEmpresa", "<html><head/><body><p>Campo de inserir os dados para pesquisar</p></body></html>", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmConsultarEmpresa", "Pesquisar", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmConsultarEmpresa", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmConsultarEmpresa", "Fantasia", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmConsultarEmpresa", "Razão Social", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmConsultarEmpresa", "CPNJ", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmConsultarEmpresa", "Ins. Estadual", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmConsultarEmpresa", "Ins. Municipal", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmConsultarEmpresa", "Tipo Emp.", None))
        item = self.tabPesquisar.horizontalHeaderItem(7)
        item.setText(_translate("frmConsultarEmpresa", "Endereco", None))
        item = self.tabPesquisar.horizontalHeaderItem(8)
        item.setText(_translate("frmConsultarEmpresa", "Numero", None))
        item = self.tabPesquisar.horizontalHeaderItem(9)
        item.setText(_translate("frmConsultarEmpresa", "Bairro", None))
        item = self.tabPesquisar.horizontalHeaderItem(10)
        item.setText(_translate("frmConsultarEmpresa", "Complemento", None))
        item = self.tabPesquisar.horizontalHeaderItem(11)
        item.setText(_translate("frmConsultarEmpresa", "Cidade", None))
        item = self.tabPesquisar.horizontalHeaderItem(12)
        item.setText(_translate("frmConsultarEmpresa", "Estado", None))
        item = self.tabPesquisar.horizontalHeaderItem(13)
        item.setText(_translate("frmConsultarEmpresa", "CEP", None))
        item = self.tabPesquisar.horizontalHeaderItem(14)
        item.setText(_translate("frmConsultarEmpresa", "Situação", None))
        item = self.tabPesquisar.horizontalHeaderItem(15)
        item.setText(_translate("frmConsultarEmpresa", "CNAE", None))




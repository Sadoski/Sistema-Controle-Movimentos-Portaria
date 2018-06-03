# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarUsuario.ui'
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

class Ui_frmPesquisarPessoaUsuario(object):
    def setupUi(self, frmPesquisarPessoaUsuario):
        frmPesquisarPessoaUsuario.setObjectName(_fromUtf8("frmPesquisarPessoaUsuario"))
        frmPesquisarPessoaUsuario.resize(794, 504)
        frmPesquisarPessoaUsuario.setMinimumSize(QtCore.QSize(794, 504))
        frmPesquisarPessoaUsuario.setMaximumSize(QtCore.QSize(794, 504))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmPesquisarPessoaUsuario.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmPesquisarPessoaUsuario.setWindowIcon(icon)
        frmPesquisarPessoaUsuario.setSizeGripEnabled(True)
        frmPesquisarPessoaUsuario.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmPesquisarPessoaUsuario)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 201, 91))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnFuncionario = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnFuncionario.setGeometry(QtCore.QRect(10, 40, 111, 23))
        self.radBtnFuncionario.setObjectName(_fromUtf8("radBtnFuncionario"))

        self.radBtnSetor = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnSetor.setGeometry(QtCore.QRect(10, 60, 81, 23))
        self.radBtnSetor.setObjectName(_fromUtf8("radBtnSetor"))

        self.radBtnCargo = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCargo.setGeometry(QtCore.QRect(130, 20, 81, 23))
        self.radBtnCargo.setObjectName(_fromUtf8("radBtnCargo"))

        self.radBtnLogin = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnLogin.setGeometry(QtCore.QRect(130, 40, 61, 23))
        self.radBtnLogin.setObjectName(_fromUtf8("radBtnLogin"))

        self.radBtnCodigo = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCodigo.setGeometry(QtCore.QRect(10, 20, 63, 23))
        self.radBtnCodigo.setObjectName(_fromUtf8("radBtnCodigo"))

        self.txtPesquisar = QtGui.QLineEdit(frmPesquisarPessoaUsuario)
        self.txtPesquisar.setGeometry(QtCore.QRect(310, 70, 431, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmPesquisarPessoaUsuario)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 70, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon1)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmPesquisarPessoaUsuario)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 110, 771, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.setColumnCount(5)
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
        self.tabPesquisar.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisar.verticalHeader().setVisible(False)

        self.retranslateUi(frmPesquisarPessoaUsuario)
        QtCore.QMetaObject.connectSlotsByName(frmPesquisarPessoaUsuario)
        frmPesquisarPessoaUsuario.setTabOrder(self.radBtnFuncionario, self.radBtnSetor)
        frmPesquisarPessoaUsuario.setTabOrder(self.radBtnSetor, self.radBtnCargo)
        frmPesquisarPessoaUsuario.setTabOrder(self.radBtnCargo, self.radBtnLogin)
        frmPesquisarPessoaUsuario.setTabOrder(self.radBtnLogin, self.txtPesquisar)
        frmPesquisarPessoaUsuario.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmPesquisarPessoaUsuario.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmPesquisarPessoaUsuario):
        frmPesquisarPessoaUsuario.setWindowTitle(_translate("frmPesquisarPessoaUsuario", "Pesquisar Usuario", None))
        self.grbTipoPesquisa.setTitle(_translate("frmPesquisarPessoaUsuario", "Tipo Pesquisa", None))
        self.radBtnFuncionario.setToolTip(_translate("frmPesquisarPessoaUsuario", "Nome", None))
        self.radBtnFuncionario.setWhatsThis(_translate("frmPesquisarPessoaUsuario", "Item de seleção para a pesquisa por nome", None))
        self.radBtnFuncionario.setText(_translate("frmPesquisarPessoaUsuario", "Funcionario", None))
        self.radBtnSetor.setToolTip(_translate("frmPesquisarPessoaUsuario", "CPF", None))
        self.radBtnSetor.setWhatsThis(_translate("frmPesquisarPessoaUsuario", "Item de seleção para a pesquisa por CPF", None))
        self.radBtnSetor.setText(_translate("frmPesquisarPessoaUsuario", "Setor", None))
        self.radBtnCargo.setToolTip(_translate("frmPesquisarPessoaUsuario", "RG", None))
        self.radBtnCargo.setWhatsThis(_translate("frmPesquisarPessoaUsuario", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCargo.setText(_translate("frmPesquisarPessoaUsuario", "Cargo", None))
        self.radBtnLogin.setToolTip(_translate("frmPesquisarPessoaUsuario", "Mãe", None))
        self.radBtnLogin.setWhatsThis(_translate("frmPesquisarPessoaUsuario", "Item de seleção para a pesquisa por mãe", None))
        self.radBtnLogin.setText(_translate("frmPesquisarPessoaUsuario", "Login", None))
        self.radBtnCodigo.setToolTip(_translate("frmPesquisarPessoaUsuario", "RG", None))
        self.radBtnCodigo.setWhatsThis(_translate("frmPesquisarPessoaUsuario", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCodigo.setText(_translate("frmPesquisarPessoaUsuario", "Codigo", None))
        self.txtPesquisar.setToolTip(_translate("frmPesquisarPessoaUsuario", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmPesquisarPessoaUsuario", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmPesquisarPessoaUsuario", "Pesquisa", None))
        self.btnPesquisar.setWhatsThis(_translate("frmPesquisarPessoaUsuario", "Botão para pesquisar as informações", None))
        self.tabPesquisar.setWhatsThis(_translate("frmPesquisarPessoaUsuario", "Tabela dos dados pesquisados", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmPesquisarPessoaUsuario", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmPesquisarPessoaUsuario", "Funcionario", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmPesquisarPessoaUsuario", "Setor", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmPesquisarPessoaUsuario", "Cargo", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmPesquisarPessoaUsuario", "Login", None))


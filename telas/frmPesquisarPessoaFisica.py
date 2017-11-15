# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarPessoaFisica.ui'
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

class Ui_frmPesquisarPessoaFisica(object):
    def setupUi(self, frmPesquisarPessoaFisica):
        frmPesquisarPessoaFisica.setObjectName(_fromUtf8("frmPesquisarPessoaFisica"))
        frmPesquisarPessoaFisica.resize(794, 504)
        frmPesquisarPessoaFisica.setMinimumSize(QtCore.QSize(794, 504))
        frmPesquisarPessoaFisica.setMaximumSize(QtCore.QSize(794, 504))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmPesquisarPessoaFisica.setFont(font)
        frmPesquisarPessoaFisica.setSizeGripEnabled(True)
        frmPesquisarPessoaFisica.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmPesquisarPessoaFisica)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 161, 91))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnNome = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnNome.setGeometry(QtCore.QRect(20, 20, 61, 23))
        self.radBtnNome.setObjectName(_fromUtf8("radBtnNome"))

        self.radBtncPF = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtncPF.setGeometry(QtCore.QRect(20, 40, 51, 23))
        self.radBtncPF.setObjectName(_fromUtf8("radBtncPF"))

        self.radBtnRg = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRg.setGeometry(QtCore.QRect(20, 60, 51, 23))
        self.radBtnRg.setObjectName(_fromUtf8("radBtnRg"))

        self.radBtnMae = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnMae.setGeometry(QtCore.QRect(90, 20, 51, 23))
        self.radBtnMae.setObjectName(_fromUtf8("radBtnMae"))

        self.radBtnPai = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnPai.setGeometry(QtCore.QRect(90, 40, 51, 23))
        self.radBtnPai.setObjectName(_fromUtf8("radBtnPai"))

        self.txtPesquisar = QtGui.QLineEdit(frmPesquisarPessoaFisica)
        self.txtPesquisar.setGeometry(QtCore.QRect(180, 70, 441, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmPesquisarPessoaFisica)
        self.btnPesquisar.setGeometry(QtCore.QRect(630, 70, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmPesquisarPessoaFisica)
        self.tabPesquisar.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisar.verticalHeader().setVisible(False)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 110, 771, 381))
        self.tabPesquisar.setEditTriggers(self.tabPesquisar.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(self.tabPesquisar.SelectRows)
        self.tabPesquisar.setSelectionMode(self.tabPesquisar.SingleSelection)
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
        self.tabPesquisar.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisar.verticalHeader().setVisible(False)

        self.retranslateUi(frmPesquisarPessoaFisica)
        QtCore.QMetaObject.connectSlotsByName(frmPesquisarPessoaFisica)
        frmPesquisarPessoaFisica.setTabOrder(self.radBtnNome, self.radBtncPF)
        frmPesquisarPessoaFisica.setTabOrder(self.radBtncPF, self.radBtnRg)
        frmPesquisarPessoaFisica.setTabOrder(self.radBtnRg, self.radBtnMae)
        frmPesquisarPessoaFisica.setTabOrder(self.radBtnMae, self.txtPesquisar)
        frmPesquisarPessoaFisica.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmPesquisarPessoaFisica.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmPesquisarPessoaFisica):
        frmPesquisarPessoaFisica.setWindowTitle(_translate("frmPesquisarPessoaFisica", "Pesquisar Pessoa Física", None))
        self.grbTipoPesquisa.setTitle(_translate("frmPesquisarPessoaFisica", "Tipo Pesquisa", None))
        self.radBtnNome.setToolTip(_translate("frmPesquisarPessoaFisica", "Nome", None))
        self.radBtnNome.setWhatsThis(_translate("frmPesquisarPessoaFisica", "Item de seleção para a pesquisa por nome", None))
        self.radBtnNome.setText(_translate("frmPesquisarPessoaFisica", "Nome", None))
        self.radBtncPF.setToolTip(_translate("frmPesquisarPessoaFisica", "CPF", None))
        self.radBtncPF.setWhatsThis(_translate("frmPesquisarPessoaFisica", "Item de seleção para a pesquisa por CPF", None))
        self.radBtncPF.setText(_translate("frmPesquisarPessoaFisica", "CPF", None))
        self.radBtnRg.setToolTip(_translate("frmPesquisarPessoaFisica", "RG", None))
        self.radBtnRg.setWhatsThis(_translate("frmPesquisarPessoaFisica", "Item de seleção para a pesquisa por RG", None))
        self.radBtnRg.setText(_translate("frmPesquisarPessoaFisica", "RG", None))
        self.radBtnMae.setToolTip(_translate("frmPesquisarPessoaFisica", "Mãe", None))
        self.radBtnMae.setWhatsThis(_translate("frmPesquisarPessoaFisica", "Item de seleção para a pesquisa por mãe", None))
        self.radBtnMae.setText(_translate("frmPesquisarPessoaFisica", "Mãe", None))
        self.radBtnPai.setToolTip(_translate("frmPesquisarPessoaFisica", "Pai", None))
        self.radBtnPai.setWhatsThis(_translate("frmPesquisarPessoaFisica", "Item de seleção para a pesquisa por pai", None))
        self.radBtnPai.setText(_translate("frmPesquisarPessoaFisica", "Pai", None))
        self.txtPesquisar.setToolTip(_translate("frmPesquisarPessoaFisica", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmPesquisarPessoaFisica", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmPesquisarPessoaFisica", "Pesquisa", None))
        self.btnPesquisar.setWhatsThis(_translate("frmPesquisarPessoaFisica", "Botão para pesquisar as informações", None))
        self.tabPesquisar.setWhatsThis(_translate("frmPesquisarPessoaFisica", "Tabela dos dados pesquisados", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmPesquisarPessoaFisica", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmPesquisarPessoaFisica", "Nome", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmPesquisarPessoaFisica", "CPF", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmPesquisarPessoaFisica", "RG", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmPesquisarPessoaFisica", "Expeditor", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmPesquisarPessoaFisica", "Data", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmPesquisarPessoaFisica", "Sexo", None))
        item = self.tabPesquisar.horizontalHeaderItem(7)
        item.setText(_translate("frmPesquisarPessoaFisica", "Endereço", None))
        item = self.tabPesquisar.horizontalHeaderItem(8)
        item.setText(_translate("frmPesquisarPessoaFisica", "Número", None))
        item = self.tabPesquisar.horizontalHeaderItem(9)
        item.setText(_translate("frmPesquisarPessoaFisica", "Complemento", None))
        item = self.tabPesquisar.horizontalHeaderItem(10)
        item.setText(_translate("frmPesquisarPessoaFisica", "Bairro", None))
        item = self.tabPesquisar.horizontalHeaderItem(11)
        item.setText(_translate("frmPesquisarPessoaFisica", "Cidade", None))
        item = self.tabPesquisar.horizontalHeaderItem(12)
        item.setText(_translate("frmPesquisarPessoaFisica", "Estado", None))
        item = self.tabPesquisar.horizontalHeaderItem(13)
        item.setText(_translate("frmPesquisarPessoaFisica", "CEP", None))
        item = self.tabPesquisar.horizontalHeaderItem(14)
        item.setText(_translate("frmPesquisarPessoaFisica", "Mãe", None))
        item = self.tabPesquisar.horizontalHeaderItem(15)
        item.setText(_translate("frmPesquisarPessoaFisica", "Pai", None))


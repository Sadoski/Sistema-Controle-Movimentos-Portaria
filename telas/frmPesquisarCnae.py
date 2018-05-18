# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarCnae.ui'
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

class Ui_frmPesquisarCnae(object):
    def setupUi(self, frmPesquisarCnae):
        frmPesquisarCnae.setObjectName(_fromUtf8("frmPesquisarCnae"))
        frmPesquisarCnae.resize(794, 504)
        frmPesquisarCnae.setMinimumSize(QtCore.QSize(794, 504))
        frmPesquisarCnae.setMaximumSize(QtCore.QSize(794, 504))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmPesquisarCnae.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmPesquisarCnae.setWindowIcon(icon)
        frmPesquisarCnae.setSizeGripEnabled(True)
        frmPesquisarCnae.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmPesquisarCnae)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 291, 91))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnCodSubclasse = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCodSubclasse.setGeometry(QtCore.QRect(10, 40, 111, 23))
        self.radBtnCodSubclasse.setObjectName(_fromUtf8("radBtnCodSubclasse"))

        self.radBtnSecao = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnSecao.setGeometry(QtCore.QRect(10, 60, 81, 23))
        self.radBtnSecao.setObjectName(_fromUtf8("radBtnSecao"))

        self.radBtnDivisao = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnDivisao.setGeometry(QtCore.QRect(130, 20, 81, 23))
        self.radBtnDivisao.setObjectName(_fromUtf8("radBtnDivisao"))

        self.radBtnGrupo = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnGrupo.setGeometry(QtCore.QRect(130, 40, 61, 23))
        self.radBtnGrupo.setObjectName(_fromUtf8("radBtnGrupo"))

        self.radBtnCodigo = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCodigo.setGeometry(QtCore.QRect(10, 20, 63, 23))
        self.radBtnCodigo.setObjectName(_fromUtf8("radBtnCodigo"))

        self.radBtnClasse = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnClasse.setGeometry(QtCore.QRect(130, 60, 71, 23))
        self.radBtnClasse.setObjectName(_fromUtf8("radBtnClasse"))

        self.radBtnSubclasse = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnSubclasse.setGeometry(QtCore.QRect(202, 20, 81, 23))
        self.radBtnSubclasse.setObjectName(_fromUtf8("Subclasse"))

        self.txtPesquisar = QtGui.QLineEdit(frmPesquisarCnae)
        self.txtPesquisar.setGeometry(QtCore.QRect(310, 70, 431, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmPesquisarCnae)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 70, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmPesquisarCnae)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 110, 771, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.setColumnCount(7)
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
        self.tabPesquisar.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisar.verticalHeader().setVisible(False)

        self.retranslateUi(frmPesquisarCnae)
        QtCore.QMetaObject.connectSlotsByName(frmPesquisarCnae)
        frmPesquisarCnae.setTabOrder(self.radBtnCodSubclasse, self.radBtnSecao)
        frmPesquisarCnae.setTabOrder(self.radBtnSecao, self.radBtnDivisao)
        frmPesquisarCnae.setTabOrder(self.radBtnDivisao, self.radBtnGrupo)
        frmPesquisarCnae.setTabOrder(self.radBtnGrupo, self.txtPesquisar)
        frmPesquisarCnae.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmPesquisarCnae.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmPesquisarCnae):
        frmPesquisarCnae.setWindowTitle(_translate("frmPesquisarCnae", "Pesquisar CNAE", None))
        self.grbTipoPesquisa.setTitle(_translate("frmPesquisarCnae", "Tipo Pesquisa", None))
        self.radBtnCodSubclasse.setToolTip(_translate("frmPesquisarCnae", "Nome", None))
        self.radBtnCodSubclasse.setWhatsThis(_translate("frmPesquisarCnae", "Item de seleção para a pesquisa por nome", None))
        self.radBtnCodSubclasse.setText(_translate("frmPesquisarCnae", "Cod. Suclasse", None))
        self.radBtnSecao.setToolTip(_translate("frmPesquisarCnae", "CPF", None))
        self.radBtnSecao.setWhatsThis(_translate("frmPesquisarCnae", "Item de seleção para a pesquisa por CPF", None))
        self.radBtnSecao.setText(_translate("frmPesquisarCnae", "Seção", None))
        self.radBtnDivisao.setToolTip(_translate("frmPesquisarCnae", "RG", None))
        self.radBtnDivisao.setWhatsThis(_translate("frmPesquisarCnae", "Item de seleção para a pesquisa por RG", None))
        self.radBtnDivisao.setText(_translate("frmPesquisarCnae", "Divisão", None))
        self.radBtnGrupo.setToolTip(_translate("frmPesquisarCnae", "Mãe", None))
        self.radBtnGrupo.setWhatsThis(_translate("frmPesquisarCnae", "Item de seleção para a pesquisa por mãe", None))
        self.radBtnGrupo.setText(_translate("frmPesquisarCnae", "Grupo", None))
        self.radBtnCodigo.setToolTip(_translate("frmPesquisarCnae", "RG", None))
        self.radBtnCodigo.setWhatsThis(_translate("frmPesquisarCnae", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCodigo.setText(_translate("frmPesquisarCnae", "Codigo", None))
        self.radBtnClasse.setToolTip(_translate("frmPesquisarCnae", "Mãe", None))
        self.radBtnClasse.setWhatsThis(_translate("frmPesquisarCnae", "Item de seleção para a pesquisa por mãe", None))
        self.radBtnClasse.setText(_translate("frmPesquisarCnae", "Classe", None))
        self.radBtnSubclasse.setToolTip(_translate("frmPesquisarCnae", "Mãe", None))
        self.radBtnSubclasse.setWhatsThis(_translate("frmPesquisarCnae", "Item de seleção para a pesquisa por mãe", None))
        self.radBtnSubclasse.setText(_translate("frmPesquisarCnae", "Subclasse", None))
        self.txtPesquisar.setToolTip(_translate("frmPesquisarCnae", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmPesquisarCnae", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmPesquisarCnae", "Pesquisa", None))
        self.btnPesquisar.setWhatsThis(_translate("frmPesquisarCnae", "Botão para pesquisar as informações", None))
        self.tabPesquisar.setWhatsThis(_translate("frmPesquisarCnae", "Tabela dos dados pesquisados", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmPesquisarCnae", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmPesquisarCnae", "Cod. SubClasse", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmPesquisarCnae", "Seção", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmPesquisarCnae", "Divisão", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmPesquisarCnae", "Grupo", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmPesquisarCnae", "Classe", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmPesquisarCnae", "Subclasse", None))


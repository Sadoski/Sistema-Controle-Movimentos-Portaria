# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarMotorista.ui'
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

class Ui_frmConsultarMotoristas(object):
    def setupUi(self, frmConsultarMotoristas):
        frmConsultarMotoristas.setObjectName(_fromUtf8("frmConsultarMotoristas"))
        frmConsultarMotoristas.resize(793, 502)
        frmConsultarMotoristas.setMinimumSize(QtCore.QSize(793, 502))
        frmConsultarMotoristas.setMaximumSize(QtCore.QSize(793, 502))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmConsultarMotoristas.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmConsultarMotoristas.setWindowIcon(icon)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmConsultarMotoristas)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 281, 81))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnNome = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnNome.setGeometry(QtCore.QRect(20, 20, 81, 23))
        self.radBtnNome.setObjectName(_fromUtf8("radBtnNome"))

        self.radBtnCpf = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCpf.setGeometry(QtCore.QRect(20, 50, 51, 23))
        self.radBtnCpf.setObjectName(_fromUtf8("radBtnCpf"))

        self.radBtnRg = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRg.setGeometry(QtCore.QRect(100, 20, 41, 23))
        self.radBtnRg.setObjectName(_fromUtf8("radBtnRg"))

        self.radBtnNumCarteira = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnNumCarteira.setGeometry(QtCore.QRect(100, 50, 161, 23))
        self.radBtnNumCarteira.setObjectName(_fromUtf8("radBtnNumCarteira"))

        self.txtPesquisar = QtGui.QLineEdit(frmConsultarMotoristas)
        self.txtPesquisar.setGeometry(QtCore.QRect(300, 60, 441, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.lblPesquisar = QtGui.QLabel(frmConsultarMotoristas)
        self.lblPesquisar.setGeometry(QtCore.QRect(300, 40, 71, 19))
        self.lblPesquisar.setObjectName(_fromUtf8("lblPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmConsultarMotoristas)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 60, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmConsultarMotoristas)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 100, 771, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.setColumnCount(13)
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
        self.tabPesquisar.setEditTriggers(self.tabPesquisar.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(self.tabPesquisar.SelectRows)
        self.tabPesquisar.setSelectionMode(self.tabPesquisar.SingleSelection)
        self.lblPesquisar.setBuddy(self.txtPesquisar)

        self.retranslateUi(frmConsultarMotoristas)
        QtCore.QMetaObject.connectSlotsByName(frmConsultarMotoristas)
        frmConsultarMotoristas.setTabOrder(self.radBtnNome, self.radBtnCpf)
        frmConsultarMotoristas.setTabOrder(self.radBtnCpf, self.radBtnRg)
        frmConsultarMotoristas.setTabOrder(self.radBtnRg, self.txtPesquisar)
        frmConsultarMotoristas.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmConsultarMotoristas.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmConsultarMotoristas):
        frmConsultarMotoristas.setWindowTitle(_translate("frmConsultarMotoristas", "Pesquisa Motoristas", None))
        self.grbTipoPesquisa.setTitle(_translate("frmConsultarMotoristas", "Tipo Pesquisa", None))
        self.radBtnNome.setToolTip(_translate("frmConsultarMotoristas", "Nome", None))
        self.radBtnNome.setText(_translate("frmConsultarMotoristas", "Nome", None))
        self.radBtnCpf.setToolTip(_translate("frmConsultarMotoristas", "CPF", None))
        self.radBtnCpf.setText(_translate("frmConsultarMotoristas", "CPF", None))
        self.radBtnRg.setToolTip(_translate("frmConsultarMotoristas", "RG", None))
        self.radBtnRg.setText(_translate("frmConsultarMotoristas", "RG", None))
        self.radBtnNumCarteira.setToolTip(_translate("frmConsultarMotoristas", "Nº Carteira", None))
        self.radBtnNumCarteira.setText(_translate("frmConsultarMotoristas", "Nº Carteira Motorista", None))
        self.txtPesquisar.setToolTip(_translate("frmConsultarMotoristas", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmConsultarMotoristas", "Campo de inserir os dados para pesquisar", None))
        self.lblPesquisar.setText(_translate("frmConsultarMotoristas", "Pesquisar", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmConsultarMotoristas", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmConsultarMotoristas", "Nome", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmConsultarMotoristas", "RG", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmConsultarMotoristas", "CPF", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmConsultarMotoristas", "Endereco", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmConsultarMotoristas", "Numero", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmConsultarMotoristas", "Bairro", None))
        item = self.tabPesquisar.horizontalHeaderItem(7)
        item.setText(_translate("frmConsultarMotoristas", "Cidade", None))
        item = self.tabPesquisar.horizontalHeaderItem(8)
        item.setText(_translate("frmConsultarMotoristas", "Estado", None))
        item = self.tabPesquisar.horizontalHeaderItem(9)
        item.setText(_translate("frmConsultarMotoristas", "CEP", None))
        item = self.tabPesquisar.horizontalHeaderItem(10)
        item.setText(_translate("frmConsultarMotoristas", "Marca Vei.", None))
        item = self.tabPesquisar.horizontalHeaderItem(11)
        item.setText(_translate("frmConsultarMotoristas", "Modelo Veic.", None))
        item = self.tabPesquisar.horizontalHeaderItem(12)
        item.setText(_translate("frmConsultarMotoristas", "Placa Veic.", None))


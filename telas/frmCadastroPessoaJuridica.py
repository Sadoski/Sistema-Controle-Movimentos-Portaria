# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCadastroPessoaJuridica.ui'
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

class Ui_frmCadastroPessoaJuridica(object):
    def setupUi(self, frmCadastroPessoaJuridica):
        frmCadastroPessoaJuridica.setObjectName(_fromUtf8("frmCadastroPessoaJuridica"))
        frmCadastroPessoaJuridica.resize(791, 439)
        frmCadastroPessoaJuridica.setMinimumSize(QtCore.QSize(791, 439))
        frmCadastroPessoaJuridica.setMaximumSize(QtCore.QSize(791, 439))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmCadastroPessoaJuridica.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/pessoa_juridica.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCadastroPessoaJuridica.setWindowIcon(icon5)
        frmCadastroPessoaJuridica.setSizeGripEnabled(True)
        frmCadastroPessoaJuridica.setModal(True)

        self.grbBotoes = QtGui.QGroupBox(frmCadastroPessoaJuridica)
        self.grbBotoes.setGeometry(QtCore.QRect(10, 380, 771, 51))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(260, 10, 88, 27))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNovo.setIcon(icon)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(360, 10, 88, 27))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))

        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(560, 10, 88, 27))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.btnDeletar = QtGui.QPushButton(self.grbBotoes)
        self.btnDeletar.setEnabled(False)
        self.btnDeletar.setGeometry(QtCore.QRect(660, 10, 88, 27))
        self.btnDeletar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/critical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeletar.setIcon(icon3)
        self.btnDeletar.setObjectName(_fromUtf8("btnDeletar"))

        self.btnEditar = QtGui.QPushButton(self.grbBotoes)
        self.btnEditar.setEnabled(False)
        self.btnEditar.setGeometry(QtCore.QRect(460, 10, 88, 27))
        self.btnEditar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/Save-as_37111.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditar.setIcon(icon4)
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))

        self.lblPesquisar = QtGui.QLabel(self.grbBotoes)
        self.lblPesquisar.setGeometry(QtCore.QRect(10, 20, 111, 19))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 116, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblPesquisar.setPalette(palette)
        self.lblPesquisar.setObjectName(_fromUtf8("lblPesquisar"))

        self.grbDados = QtGui.QGroupBox(frmCadastroPessoaJuridica)
        self.grbDados.setEnabled(False)
        self.grbDados.setGeometry(QtCore.QRect(10, 10, 771, 321))
        self.grbDados.setTitle(_fromUtf8(""))
        self.grbDados.setObjectName(_fromUtf8("grbDados"))

        self.txtComplemento = QtGui.QLineEdit(self.grbDados)
        self.txtComplemento.setGeometry(QtCore.QRect(140, 180, 261, 24))
        self.txtComplemento.setMaxLength(50)
        self.txtComplemento.setObjectName(_fromUtf8("txtComplemento"))

        self.txtEstado = QtGui.QLineEdit(self.grbDados)
        self.txtEstado.setEnabled(False)
        self.txtEstado.setGeometry(QtCore.QRect(540, 230, 221, 25))
        self.txtEstado.setMaxLength(50)
        self.txtEstado.setObjectName(_fromUtf8("txtEstado"))

        self.lblEstado = QtGui.QLabel(self.grbDados)
        self.lblEstado.setGeometry(QtCore.QRect(540, 210, 51, 19))
        self.lblEstado.setObjectName(_fromUtf8("lblEstado"))

        self.lblComplemento = QtGui.QLabel(self.grbDados)
        self.lblComplemento.setGeometry(QtCore.QRect(140, 160, 101, 16))
        self.lblComplemento.setObjectName(_fromUtf8("lblComplemento"))

        self.txtFantasia = QtGui.QLineEdit(self.grbDados)
        self.txtFantasia.setGeometry(QtCore.QRect(8, 80, 751, 25))
        self.txtFantasia.setMaxLength(75)
        self.txtFantasia.setObjectName(_fromUtf8("txtFantasia"))

        self.txtCidade = QtGui.QLineEdit(self.grbDados)
        self.txtCidade.setEnabled(False)
        self.txtCidade.setGeometry(QtCore.QRect(150, 230, 381, 25))
        self.txtCidade.setMaxLength(75)
        self.txtCidade.setObjectName(_fromUtf8("txtCidade"))

        self.lblCidade = QtGui.QLabel(self.grbDados)
        self.lblCidade.setGeometry(QtCore.QRect(150, 210, 51, 19))
        self.lblCidade.setObjectName(_fromUtf8("lblCidade"))

        self.txtCnpj = QtGui.QLineEdit(self.grbDados)
        self.txtCnpj.setGeometry(QtCore.QRect(10, 130, 161, 25))
        self.txtCnpj.setMaxLength(18)
        self.txtCnpj.setObjectName(_fromUtf8("txtCnpj"))

        self.lblInsEstadual = QtGui.QLabel(self.grbDados)
        self.lblInsEstadual.setGeometry(QtCore.QRect(180, 110, 91, 19))
        self.lblInsEstadual.setObjectName(_fromUtf8("lblInsEstadual"))

        self.txtCep = QtGui.QLineEdit(self.grbDados)
        self.txtCep.setGeometry(QtCore.QRect(10, 230, 131, 25))
        self.txtCep.setObjectName(_fromUtf8("txtCep"))

        self.txtNumero = QtGui.QLineEdit(self.grbDados)
        self.txtNumero.setGeometry(QtCore.QRect(10, 180, 121, 25))
        self.txtNumero.setMaxLength(11)
        self.txtNumero.setObjectName(_fromUtf8("txtNumero"))

        self.txtRazaoSocial = QtGui.QLineEdit(self.grbDados)
        self.txtRazaoSocial.setGeometry(QtCore.QRect(10, 30, 751, 25))
        self.txtRazaoSocial.setMaxLength(75)
        self.txtRazaoSocial.setObjectName(_fromUtf8("txtRazaoSocial"))

        self.lblBairro = QtGui.QLabel(self.grbDados)
        self.lblBairro.setGeometry(QtCore.QRect(410, 160, 51, 19))
        self.lblBairro.setObjectName(_fromUtf8("lblBairro"))

        self.txtEndereco = QtGui.QLineEdit(self.grbDados)
        self.txtEndereco.setGeometry(QtCore.QRect(330, 130, 431, 25))
        self.txtEndereco.setMaxLength(50)
        self.txtEndereco.setObjectName(_fromUtf8("txtEndereco"))

        self.lblEndereco = QtGui.QLabel(self.grbDados)
        self.lblEndereco.setGeometry(QtCore.QRect(330, 110, 66, 19))
        self.lblEndereco.setObjectName(_fromUtf8("lblEndereco"))

        self.txtInsEstadual = QtGui.QLineEdit(self.grbDados)
        self.txtInsEstadual.setGeometry(QtCore.QRect(180, 130, 141, 25))
        self.txtInsEstadual.setMaxLength(15)
        self.txtInsEstadual.setObjectName(_fromUtf8("txtInsEstadual"))

        self.lblRazaoSocial = QtGui.QLabel(self.grbDados)
        self.lblRazaoSocial.setGeometry(QtCore.QRect(10, 10, 141, 19))
        self.lblRazaoSocial.setObjectName(_fromUtf8("lblRazaoSocial"))

        self.lblFantasia = QtGui.QLabel(self.grbDados)
        self.lblFantasia.setGeometry(QtCore.QRect(10, 60, 111, 19))
        self.lblFantasia.setObjectName(_fromUtf8("lblFantasia"))

        self.txtBairro = QtGui.QLineEdit(self.grbDados)
        self.txtBairro.setGeometry(QtCore.QRect(410, 180, 351, 25))
        self.txtBairro.setMaxLength(50)
        self.txtBairro.setObjectName(_fromUtf8("txtBairro"))

        self.lblNumero = QtGui.QLabel(self.grbDados)
        self.lblNumero.setGeometry(QtCore.QRect(10, 160, 66, 19))
        self.lblNumero.setObjectName(_fromUtf8("lblNumero"))

        self.txtSite = QtGui.QLineEdit(self.grbDados)
        self.txtSite.setGeometry(QtCore.QRect(10, 280, 561, 25))
        self.txtSite.setMaxLength(75)
        self.txtSite.setObjectName(_fromUtf8("txtSite"))

        self.lblCep = QtGui.QLabel(self.grbDados)
        self.lblCep.setGeometry(QtCore.QRect(10, 210, 31, 19))
        self.lblCep.setObjectName(_fromUtf8("lblCep"))

        self.lblSite = QtGui.QLabel(self.grbDados)
        self.lblSite.setGeometry(QtCore.QRect(10, 260, 31, 19))
        self.lblSite.setObjectName(_fromUtf8("lblSite"))

        self.lblCnpj = QtGui.QLabel(self.grbDados)
        self.lblCnpj.setGeometry(QtCore.QRect(10, 110, 81, 19))
        self.lblCnpj.setObjectName(_fromUtf8("lblCnpj"))

        self.lblEstado.setBuddy(self.txtEstado)
        self.lblComplemento.setBuddy(self.txtComplemento)
        self.lblCidade.setBuddy(self.txtCidade)
        self.lblInsEstadual.setBuddy(self.txtInsEstadual)
        self.lblBairro.setBuddy(self.txtBairro)
        self.lblEndereco.setBuddy(self.txtEndereco)
        self.lblRazaoSocial.setBuddy(self.txtRazaoSocial)
        self.lblFantasia.setBuddy(self.txtFantasia)
        self.lblNumero.setBuddy(self.txtNumero)
        self.lblCep.setBuddy(self.txtCep)
        self.lblSite.setBuddy(self.txtSite)
        self.lblCnpj.setBuddy(self.txtCnpj)

        self.retranslateUi(frmCadastroPessoaJuridica)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroPessoaJuridica)
        frmCadastroPessoaJuridica.setTabOrder(self.txtRazaoSocial, self.txtFantasia)
        frmCadastroPessoaJuridica.setTabOrder(self.txtFantasia, self.txtCnpj)
        frmCadastroPessoaJuridica.setTabOrder(self.txtCnpj, self.txtInsEstadual)
        frmCadastroPessoaJuridica.setTabOrder(self.txtInsEstadual, self.txtEndereco)
        frmCadastroPessoaJuridica.setTabOrder(self.txtEndereco, self.txtNumero)
        frmCadastroPessoaJuridica.setTabOrder(self.txtNumero, self.txtComplemento)
        frmCadastroPessoaJuridica.setTabOrder(self.txtComplemento, self.txtBairro)
        frmCadastroPessoaJuridica.setTabOrder(self.txtBairro, self.txtCep)
        frmCadastroPessoaJuridica.setTabOrder(self.txtCep, self.txtSite)

    def retranslateUi(self, frmCadastroPessoaJuridica):
        frmCadastroPessoaJuridica.setWindowTitle(_translate("frmCadastroPessoaJuridica", "Cadastro Pessoa Jurídica", None))
        self.btnNovo.setToolTip(_translate("frmCadastroPessoaJuridica", "Novo", None))
        self.btnNovo.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Botão para cadastrar uma novo registro da pessoa jurídica</p></body></html>", None))
        self.btnNovo.setText(_translate("frmCadastroPessoaJuridica", "Novo", None))
        self.btnSalvar.setToolTip(_translate("frmCadastroPessoaJuridica", "Salvar", None))
        self.btnSalvar.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Botão para salvar um novo registro da pessoa jurídica</p></body></html>", None))
        self.btnSalvar.setText(_translate("frmCadastroPessoaJuridica", "Salvar", None))
        self.btnCancelar.setToolTip(_translate("frmCadastroPessoaJuridica", "Cancelar", None))
        self.btnCancelar.setWhatsThis(_translate("frmCadastroPessoaJuridica", "Botão para cancelar a operação ", None))
        self.btnCancelar.setText(_translate("frmCadastroPessoaJuridica", "Cancelar", None))
        self.btnDeletar.setToolTip(_translate("frmCadastroPessoaJuridica", "Deletar", None))
        self.btnDeletar.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Botão de deletar o registro da pessoa jurídica</p></body></html>", None))
        self.btnDeletar.setText(_translate("frmCadastroPessoaJuridica", "Deletar", None))
        self.btnEditar.setToolTip(_translate("frmCadastroPessoaJuridica", "Editar", None))
        self.btnEditar.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Botão para salvar o registo editado da pessoa jurídica</p></body></html>", None))
        self.btnEditar.setText(_translate("frmCadastroPessoaJuridica", "Editar", None))
        self.lblPesquisar.setText(_translate("frmCadastroPessoaJuridica", "[F12] Pesquisar", None))
        self.txtComplemento.setToolTip(_translate("frmCadastroPessoaJuridica", "Complemento", None))
        self.txtComplemento.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do complemento do endereço da pessoa jurídica</p></body></html>", None))
        self.txtEstado.setToolTip(_translate("frmCadastroPessoaJuridica", "Estado", None))
        self.txtEstado.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do nome do estado onde fica localizado a cidade a pessoa jurídica</p></body></html>", None))
        self.lblEstado.setText(_translate("frmCadastroPessoaJuridica", "Estado", None))
        self.lblComplemento.setText(_translate("frmCadastroPessoaJuridica", "Complemento", None))
        self.txtFantasia.setToolTip(_translate("frmCadastroPessoaJuridica", "Fantasia", None))
        self.txtFantasia.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do nome fantasia da pessoa jurídica</p></body></html>", None))
        self.txtCidade.setToolTip(_translate("frmCadastroPessoaJuridica", "Cidade", None))
        self.txtCidade.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do nome da cidade onde fica localizado a pessoa jurídica</p></body></html>", None))
        self.lblCidade.setText(_translate("frmCadastroPessoaJuridica", "Cidade", None))
        self.txtCnpj.setToolTip(_translate("frmCadastroPessoaJuridica", "CNPJ", None))
        self.txtCnpj.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do numero do CNPJ da pessoa jurídica</p></body></html>", None))
        self.txtCnpj.setInputMask(_translate("frmCadastroPessoaJuridica", "00.000.000/0000-00; ", None))
        self.lblInsEstadual.setText(_translate("frmCadastroPessoaJuridica", "Ins. Estadual", None))
        self.txtCep.setToolTip(_translate("frmCadastroPessoaJuridica", "CEP", None))
        self.txtCep.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do número do CEP da cidade onde fica localizada a pessoa jurídica</p></body></html>", None))
        self.txtCep.setInputMask(_translate("frmCadastroPessoaJuridica", "00000-000; ", None))
        self.txtNumero.setToolTip(_translate("frmCadastroPessoaJuridica", "Número", None))
        self.txtNumero.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do número do endereço da pessoa jurídica</p></body></html>", None))
        self.txtRazaoSocial.setToolTip(_translate("frmCadastroPessoaJuridica", "Razão Social", None))
        self.txtRazaoSocial.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do nome da razão social da pessoa jurídica</p></body></html>", None))
        self.lblBairro.setText(_translate("frmCadastroPessoaJuridica", "Bairro", None))
        self.txtEndereco.setToolTip(_translate("frmCadastroPessoaJuridica", "Endereço", None))
        self.txtEndereco.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do endereço da pessoa jurídica</p></body></html>", None))
        self.lblEndereco.setText(_translate("frmCadastroPessoaJuridica", "Endereço", None))
        self.txtInsEstadual.setToolTip(_translate("frmCadastroPessoaJuridica", "Inscrição Estadual", None))
        self.txtInsEstadual.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do número da incrição estadual da pessoa jurídica</p></body></html>", None))
        self.lblRazaoSocial.setText(_translate("frmCadastroPessoaJuridica", "Razão Social", None))
        self.lblFantasia.setText(_translate("frmCadastroPessoaJuridica", "Fantasia", None))
        self.txtBairro.setToolTip(_translate("frmCadastroPessoaJuridica", "Bairro", None))
        self.txtBairro.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do nome do bairro do endereço da pessoa jurídica</p></body></html>", None))
        self.lblNumero.setText(_translate("frmCadastroPessoaJuridica", "Numero", None))
        self.txtSite.setToolTip(_translate("frmCadastroPessoaJuridica", "Site", None))
        self.txtSite.setWhatsThis(_translate("frmCadastroPessoaJuridica", "<html><head/><body><p>Campo do endereço do site da pessoa jurídica</p></body></html>", None))
        self.lblCep.setText(_translate("frmCadastroPessoaJuridica", "CEP", None))
        self.lblSite.setText(_translate("frmCadastroPessoaJuridica", "Site", None))
        self.lblCnpj.setText(_translate("frmCadastroPessoaJuridica", "CNPJ", None))


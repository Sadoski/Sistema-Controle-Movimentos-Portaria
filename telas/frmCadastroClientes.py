# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCadastroClientes.ui'
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

class Ui_frmCadastroFornecedor(object):
    def setupUi(self, frmCadastroFornecedor):
        frmCadastroFornecedor.setObjectName(_fromUtf8("frmCadastroFornecedor"))
        frmCadastroFornecedor.resize(895, 480)
        font = QtGui.QFont()
        font.setPointSize(11)
        frmCadastroFornecedor.setFont(font)
        self.grbBotoes = QtGui.QGroupBox(frmCadastroFornecedor)
        self.grbBotoes.setGeometry(QtCore.QRect(7, 395, 881, 80))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))
        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(370, 10, 81, 61))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))
        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setGeometry(QtCore.QRect(670, 10, 81, 61))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnDeletar = QtGui.QPushButton(self.grbBotoes)
        self.btnDeletar.setGeometry(QtCore.QRect(770, 10, 81, 61))
        self.btnDeletar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnDeletar.setObjectName(_fromUtf8("btnDeletar"))
        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setGeometry(QtCore.QRect(470, 10, 81, 61))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        self.btnEditar = QtGui.QPushButton(self.grbBotoes)
        self.btnEditar.setGeometry(QtCore.QRect(570, 10, 81, 61))
        self.btnEditar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))
        self.grbDadosCliente = QtGui.QGroupBox(frmCadastroFornecedor)
        self.grbDadosCliente.setGeometry(QtCore.QRect(7, 120, 881, 271))
        self.grbDadosCliente.setObjectName(_fromUtf8("grbDadosCliente"))
        self.lblCepCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblCepCliente.setGeometry(QtCore.QRect(368, 166, 31, 19))
        self.lblCepCliente.setObjectName(_fromUtf8("lblCepCliente"))
        self.txtCidadesCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtCidadesCliente.setEnabled(False)
        self.txtCidadesCliente.setGeometry(QtCore.QRect(532, 186, 341, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtCidadesCliente.setPalette(palette)
        self.txtCidadesCliente.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCidadesCliente.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCidadesCliente.setMaxLength(70)
        self.txtCidadesCliente.setObjectName(_fromUtf8("txtCidadesCliente"))
        self.lblBairroCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblBairroCliente.setGeometry(QtCore.QRect(8, 166, 41, 19))
        self.lblBairroCliente.setObjectName(_fromUtf8("lblBairroCliente"))
        self.lblComplementoCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblComplementoCliente.setGeometry(QtCore.QRect(602, 118, 101, 16))
        self.lblComplementoCliente.setObjectName(_fromUtf8("lblComplementoCliente"))
        self.txtTelefoneCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtTelefoneCliente.setGeometry(QtCore.QRect(222, 236, 191, 25))
        self.txtTelefoneCliente.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtTelefoneCliente.setObjectName(_fromUtf8("txtTelefoneCliente"))
        self.txtCnpjCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtCnpjCliente.setGeometry(QtCore.QRect(188, 40, 201, 25))
        self.txtCnpjCliente.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCnpjCliente.setText(_fromUtf8("../-"))
        self.txtCnpjCliente.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCnpjCliente.setObjectName(_fromUtf8("txtCnpjCliente"))
        self.lblRazaoSocialCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblRazaoSocialCliente.setGeometry(QtCore.QRect(452, 68, 81, 19))
        self.lblRazaoSocialCliente.setObjectName(_fromUtf8("lblRazaoSocialCliente"))
        self.lblCnpjCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblCnpjCliente.setGeometry(QtCore.QRect(188, 20, 41, 19))
        self.lblCnpjCliente.setObjectName(_fromUtf8("lblCnpjCliente"))
        self.txtRazaoSocialCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtRazaoSocialCliente.setGeometry(QtCore.QRect(452, 88, 421, 25))
        self.txtRazaoSocialCliente.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtRazaoSocialCliente.setMaxLength(70)
        self.txtRazaoSocialCliente.setObjectName(_fromUtf8("txtRazaoSocialCliente"))
        self.txtCepCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtCepCliente.setGeometry(QtCore.QRect(368, 186, 151, 25))
        self.txtCepCliente.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCepCliente.setInputMask(_fromUtf8("00000-000; "))
        self.txtCepCliente.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCepCliente.setObjectName(_fromUtf8("txtCepCliente"))
        self.txtInscricaoMunicipalCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtInscricaoMunicipalCliente.setGeometry(QtCore.QRect(608, 40, 211, 25))
        self.txtInscricaoMunicipalCliente.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoMunicipalCliente.setMaxLength(8)
        self.txtInscricaoMunicipalCliente.setObjectName(_fromUtf8("txtInscricaoMunicipalCliente"))
        self.lblInscricaoMunicipalCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblInscricaoMunicipalCliente.setGeometry(QtCore.QRect(608, 20, 141, 19))
        self.lblInscricaoMunicipalCliente.setObjectName(_fromUtf8("lblInscricaoMunicipalCliente"))
        self.lblEnderecoCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblEnderecoCliente.setGeometry(QtCore.QRect(8, 118, 66, 19))
        self.lblEnderecoCliente.setObjectName(_fromUtf8("lblEnderecoCliente"))
        self.txtComplementoCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtComplementoCliente.setGeometry(QtCore.QRect(602, 138, 271, 25))
        self.txtComplementoCliente.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtComplementoCliente.setMaxLength(50)
        self.txtComplementoCliente.setObjectName(_fromUtf8("txtComplementoCliente"))
        self.txtEstadosCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtEstadosCliente.setEnabled(False)
        self.txtEstadosCliente.setGeometry(QtCore.QRect(8, 236, 201, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtEstadosCliente.setPalette(palette)
        self.txtEstadosCliente.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtEstadosCliente.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhUppercaseOnly)
        self.txtEstadosCliente.setMaxLength(50)
        self.txtEstadosCliente.setObjectName(_fromUtf8("txtEstadosCliente"))
        self.txtNumeroCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtNumeroCliente.setGeometry(QtCore.QRect(436, 138, 161, 25))
        self.txtNumeroCliente.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtNumeroCliente.setMaxLength(11)
        self.txtNumeroCliente.setObjectName(_fromUtf8("txtNumeroCliente"))
        self.lblNomeFantasiaCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblNomeFantasiaCliente.setGeometry(QtCore.QRect(8, 68, 101, 19))
        self.lblNomeFantasiaCliente.setObjectName(_fromUtf8("lblNomeFantasiaCliente"))
        self.txtBairroCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtBairroCliente.setGeometry(QtCore.QRect(8, 186, 351, 25))
        self.txtBairroCliente.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtBairroCliente.setMaxLength(50)
        self.txtBairroCliente.setObjectName(_fromUtf8("txtBairroCliente"))
        self.txtInscricaoEstadualCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtInscricaoEstadualCliente.setGeometry(QtCore.QRect(398, 40, 201, 25))
        self.txtInscricaoEstadualCliente.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoEstadualCliente.setMaxLength(8)
        self.txtInscricaoEstadualCliente.setObjectName(_fromUtf8("txtInscricaoEstadualCliente"))
        self.lblTelefoeneCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblTelefoeneCliente.setGeometry(QtCore.QRect(222, 216, 61, 19))
        self.lblTelefoeneCliente.setObjectName(_fromUtf8("lblTelefoeneCliente"))
        self.lblNumeroCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblNumeroCliente.setGeometry(QtCore.QRect(436, 118, 51, 19))
        self.lblNumeroCliente.setObjectName(_fromUtf8("lblNumeroCliente"))
        self.txtEnderecoCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtEnderecoCliente.setGeometry(QtCore.QRect(8, 138, 421, 25))
        self.txtEnderecoCliente.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtEnderecoCliente.setMaxLength(50)
        self.txtEnderecoCliente.setObjectName(_fromUtf8("txtEnderecoCliente"))
        self.txtFantasiaCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtFantasiaCliente.setGeometry(QtCore.QRect(8, 88, 431, 25))
        self.txtFantasiaCliente.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtFantasiaCliente.setMaxLength(70)
        self.txtFantasiaCliente.setObjectName(_fromUtf8("txtFantasiaCliente"))
        self.lblCidadesCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblCidadesCliente.setGeometry(QtCore.QRect(532, 166, 51, 19))
        self.lblCidadesCliente.setObjectName(_fromUtf8("lblCidadesCliente"))
        self.lblEstadosCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblEstadosCliente.setGeometry(QtCore.QRect(10, 216, 51, 19))
        self.lblEstadosCliente.setObjectName(_fromUtf8("lblEstadosCliente"))
        self.lblInscricaoEstadualCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblInscricaoEstadualCliente.setGeometry(QtCore.QRect(398, 20, 121, 19))
        self.lblInscricaoEstadualCliente.setObjectName(_fromUtf8("lblInscricaoEstadualCliente"))
        self.txtIdCliente = QtGui.QLineEdit(self.grbDadosCliente)
        self.txtIdCliente.setEnabled(False)
        self.txtIdCliente.setGeometry(QtCore.QRect(6, 40, 171, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtIdCliente.setPalette(palette)
        self.txtIdCliente.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtIdCliente.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtIdCliente.setMaxLength(11)
        self.txtIdCliente.setObjectName(_fromUtf8("txtIdCliente"))
        self.lblCodigoCliente = QtGui.QLabel(self.grbDadosCliente)
        self.lblCodigoCliente.setGeometry(QtCore.QRect(6, 20, 51, 19))
        self.lblCodigoCliente.setObjectName(_fromUtf8("lblCodigoCliente"))
        self.grbPesquisarEmpresa = QtGui.QGroupBox(frmCadastroFornecedor)
        self.grbPesquisarEmpresa.setGeometry(QtCore.QRect(8, 0, 880, 123))
        self.grbPesquisarEmpresa.setObjectName(_fromUtf8("grbPesquisarEmpresa"))
        self.txtCnpjEmpresa = QtGui.QLineEdit(self.grbPesquisarEmpresa)
        self.txtCnpjEmpresa.setEnabled(False)
        self.txtCnpjEmpresa.setGeometry(QtCore.QRect(501, 90, 182, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtCnpjEmpresa.setPalette(palette)
        self.txtCnpjEmpresa.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCnpjEmpresa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtCnpjEmpresa.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCnpjEmpresa.setText(_fromUtf8("../-"))
        self.txtCnpjEmpresa.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCnpjEmpresa.setObjectName(_fromUtf8("txtCnpjEmpresa"))
        self.lblCodigoEmpresa = QtGui.QLabel(self.grbPesquisarEmpresa)
        self.lblCodigoEmpresa.setGeometry(QtCore.QRect(13, 20, 51, 19))
        self.lblCodigoEmpresa.setObjectName(_fromUtf8("lblCodigoEmpresa"))
        self.lblNomeFantasiaEmpresa = QtGui.QLabel(self.grbPesquisarEmpresa)
        self.lblNomeFantasiaEmpresa.setGeometry(QtCore.QRect(197, 20, 101, 19))
        self.lblNomeFantasiaEmpresa.setObjectName(_fromUtf8("lblNomeFantasiaEmpresa"))
        self.lblCnpj_2 = QtGui.QLabel(self.grbPesquisarEmpresa)
        self.lblCnpj_2.setGeometry(QtCore.QRect(501, 70, 41, 19))
        self.lblCnpj_2.setObjectName(_fromUtf8("lblCnpj_2"))
        self.txtFantasiaEmpresa = QtGui.QLineEdit(self.grbPesquisarEmpresa)
        self.txtFantasiaEmpresa.setGeometry(QtCore.QRect(197, 40, 631, 25))
        self.txtFantasiaEmpresa.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtFantasiaEmpresa.setMaxLength(70)
        self.txtFantasiaEmpresa.setObjectName(_fromUtf8("txtFantasiaEmpresa"))
        self.txtRazaoSocialEmpresa = QtGui.QLineEdit(self.grbPesquisarEmpresa)
        self.txtRazaoSocialEmpresa.setEnabled(False)
        self.txtRazaoSocialEmpresa.setGeometry(QtCore.QRect(13, 90, 482, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtRazaoSocialEmpresa.setPalette(palette)
        self.txtRazaoSocialEmpresa.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtRazaoSocialEmpresa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtRazaoSocialEmpresa.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtRazaoSocialEmpresa.setMaxLength(70)
        self.txtRazaoSocialEmpresa.setObjectName(_fromUtf8("txtRazaoSocialEmpresa"))
        self.lblRazaoSocialEmpresa = QtGui.QLabel(self.grbPesquisarEmpresa)
        self.lblRazaoSocialEmpresa.setGeometry(QtCore.QRect(13, 70, 81, 19))
        self.lblRazaoSocialEmpresa.setObjectName(_fromUtf8("lblRazaoSocialEmpresa"))
        self.txtIdEmpresa = QtGui.QLineEdit(self.grbPesquisarEmpresa)
        self.txtIdEmpresa.setEnabled(False)
        self.txtIdEmpresa.setGeometry(QtCore.QRect(13, 40, 171, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtIdEmpresa.setPalette(palette)
        self.txtIdEmpresa.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtIdEmpresa.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtIdEmpresa.setMaxLength(11)
        self.txtIdEmpresa.setObjectName(_fromUtf8("txtIdEmpresa"))
        self.txtInscricaoEstaduaEmpresa = QtGui.QLineEdit(self.grbPesquisarEmpresa)
        self.txtInscricaoEstaduaEmpresa.setEnabled(False)
        self.txtInscricaoEstaduaEmpresa.setGeometry(QtCore.QRect(689, 90, 178, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtInscricaoEstaduaEmpresa.setPalette(palette)
        self.txtInscricaoEstaduaEmpresa.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtInscricaoEstaduaEmpresa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtInscricaoEstaduaEmpresa.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoEstaduaEmpresa.setMaxLength(8)
        self.txtInscricaoEstaduaEmpresa.setObjectName(_fromUtf8("txtInscricaoEstaduaEmpresa"))
        self.lblInscricaoEstadualEmpresa = QtGui.QLabel(self.grbPesquisarEmpresa)
        self.lblInscricaoEstadualEmpresa.setGeometry(QtCore.QRect(689, 70, 121, 19))
        self.lblInscricaoEstadualEmpresa.setObjectName(_fromUtf8("lblInscricaoEstadualEmpresa"))
        self.btnPesquisar = QtGui.QPushButton(self.grbPesquisarEmpresa)
        self.btnPesquisar.setGeometry(QtCore.QRect(837, 40, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))
        self.lblCepCliente.setBuddy(self.txtCepCliente)
        self.lblBairroCliente.setBuddy(self.txtBairroCliente)
        self.lblComplementoCliente.setBuddy(self.txtComplementoCliente)
        self.lblRazaoSocialCliente.setBuddy(self.txtRazaoSocialCliente)
        self.lblCnpjCliente.setBuddy(self.txtCnpjCliente)
        self.lblInscricaoMunicipalCliente.setBuddy(self.txtInscricaoMunicipalCliente)
        self.lblEnderecoCliente.setBuddy(self.txtEnderecoCliente)
        self.lblNomeFantasiaCliente.setBuddy(self.txtFantasiaCliente)
        self.lblTelefoeneCliente.setBuddy(self.txtTelefoneCliente)
        self.lblNumeroCliente.setBuddy(self.txtNumeroCliente)
        self.lblCidadesCliente.setBuddy(self.txtCidadesCliente)
        self.lblEstadosCliente.setBuddy(self.txtEstadosCliente)
        self.lblInscricaoEstadualCliente.setBuddy(self.txtInscricaoEstadualCliente)
        self.lblCodigoCliente.setBuddy(self.txtIdCliente)
        self.lblCodigoEmpresa.setBuddy(self.txtIdEmpresa)
        self.lblNomeFantasiaEmpresa.setBuddy(self.txtFantasiaEmpresa)
        self.lblCnpj_2.setBuddy(self.txtCnpjEmpresa)
        self.lblRazaoSocialEmpresa.setBuddy(self.txtRazaoSocialEmpresa)
        self.lblInscricaoEstadualEmpresa.setBuddy(self.txtInscricaoEstaduaEmpresa)

        self.retranslateUi(frmCadastroFornecedor)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtIdCliente, self.txtCnpjCliente)
        frmCadastroFornecedor.setTabOrder(self.txtCnpjCliente, self.txtInscricaoEstadualCliente)
        frmCadastroFornecedor.setTabOrder(self.txtInscricaoEstadualCliente, self.txtInscricaoMunicipalCliente)
        frmCadastroFornecedor.setTabOrder(self.txtInscricaoMunicipalCliente, self.txtFantasiaCliente)
        frmCadastroFornecedor.setTabOrder(self.txtFantasiaCliente, self.txtRazaoSocialCliente)
        frmCadastroFornecedor.setTabOrder(self.txtRazaoSocialCliente, self.txtEnderecoCliente)
        frmCadastroFornecedor.setTabOrder(self.txtEnderecoCliente, self.txtNumeroCliente)
        frmCadastroFornecedor.setTabOrder(self.txtNumeroCliente, self.txtComplementoCliente)
        frmCadastroFornecedor.setTabOrder(self.txtComplementoCliente, self.txtBairroCliente)
        frmCadastroFornecedor.setTabOrder(self.txtBairroCliente, self.txtCepCliente)
        frmCadastroFornecedor.setTabOrder(self.txtCepCliente, self.txtCidadesCliente)
        frmCadastroFornecedor.setTabOrder(self.txtCidadesCliente, self.txtEstadosCliente)
        frmCadastroFornecedor.setTabOrder(self.txtEstadosCliente, self.txtTelefoneCliente)
        frmCadastroFornecedor.setTabOrder(self.txtTelefoneCliente, self.btnNovo)
        frmCadastroFornecedor.setTabOrder(self.btnNovo, self.btnSalvar)
        frmCadastroFornecedor.setTabOrder(self.btnSalvar, self.btnEditar)
        frmCadastroFornecedor.setTabOrder(self.btnEditar, self.btnCancelar)
        frmCadastroFornecedor.setTabOrder(self.btnCancelar, self.btnDeletar)

    def retranslateUi(self, frmCadastroFornecedor):
        frmCadastroFornecedor.setWindowTitle(_translate("frmCadastroFornecedor", "Cadastro Clientes", None))
        self.grbBotoes.setWhatsThis(_translate("frmCadastroFornecedor", "Grupo de botões referente as suas funções", None))
        self.btnNovo.setWhatsThis(_translate("frmCadastroFornecedor", "Botão de Criação de um novo registro", None))
        self.btnNovo.setText(_translate("frmCadastroFornecedor", "Novo", None))
        self.btnCancelar.setWhatsThis(_translate("frmCadastroFornecedor", "Botão de cancelar a operação iniciada", None))
        self.btnCancelar.setText(_translate("frmCadastroFornecedor", "Cancelar", None))
        self.btnDeletar.setWhatsThis(_translate("frmCadastroFornecedor", "Botão de deleção de um registro existente", None))
        self.btnDeletar.setText(_translate("frmCadastroFornecedor", "Deletar", None))
        self.btnSalvar.setWhatsThis(_translate("frmCadastroFornecedor", "Botão para salvar um novo registro", None))
        self.btnSalvar.setText(_translate("frmCadastroFornecedor", "Salvar", None))
        self.btnEditar.setWhatsThis(_translate("frmCadastroFornecedor", "Botão para salvar edição de um registro existente", None))
        self.btnEditar.setText(_translate("frmCadastroFornecedor", "Editar", None))
        self.grbDadosCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Grupo de Dados para cadastro e edição de cliente", None))
        self.grbDadosCliente.setTitle(_translate("frmCadastroFornecedor", "Dados Cliente", None))
        self.lblCepCliente.setText(_translate("frmCadastroFornecedor", "CEP", None))
        self.txtCidadesCliente.setToolTip(_translate("frmCadastroFornecedor", "Cidade Cliente", None))
        self.txtCidadesCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome da cidade referente a localização do endereço dentro do estado", None))
        self.lblBairroCliente.setText(_translate("frmCadastroFornecedor", "Bairro", None))
        self.lblComplementoCliente.setText(_translate("frmCadastroFornecedor", "Complemento", None))
        self.txtTelefoneCliente.setToolTip(_translate("frmCadastroFornecedor", "Telefone Cliente", None))
        self.txtTelefoneCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero de cantato de telefone da Cliente", None))
        self.txtTelefoneCliente.setInputMask(_translate("frmCadastroFornecedor", "(00) 00000-0000; ", None))
        self.txtCnpjCliente.setToolTip(_translate("frmCadastroFornecedor", "CNPJ Cliente", None))
        self.txtCnpjCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero do CNPJ da Cliente", None))
        self.txtCnpjCliente.setInputMask(_translate("frmCadastroFornecedor", "00.000.000/0000-00; ", None))
        self.lblRazaoSocialCliente.setText(_translate("frmCadastroFornecedor", "Razão Social", None))
        self.lblCnpjCliente.setText(_translate("frmCadastroFornecedor", "CNPJ", None))
        self.txtRazaoSocialCliente.setToolTip(_translate("frmCadastroFornecedor", "Razão Social Cliente", None))
        self.txtRazaoSocialCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome da razão social da Cliente", None))
        self.txtCepCliente.setToolTip(_translate("frmCadastroFornecedor", "CEP Cliente", None))
        self.txtCepCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo de CEP referente a identificação da cidade e qual estado pertence", None))
        self.txtInscricaoMunicipalCliente.setToolTip(_translate("frmCadastroFornecedor", "Inscrição Municipal Cliente", None))
        self.txtInscricaoMunicipalCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero do inscrição municipal da Cliente", None))
        self.lblInscricaoMunicipalCliente.setText(_translate("frmCadastroFornecedor", "Inscrição Municipal", None))
        self.lblEnderecoCliente.setText(_translate("frmCadastroFornecedor", "Endereço", None))
        self.txtComplementoCliente.setToolTip(_translate("frmCadastroFornecedor", "Complemento Cliente", None))
        self.txtComplementoCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo complementar do endereço", None))
        self.txtEstadosCliente.setToolTip(_translate("frmCadastroFornecedor", "Estado Cliente", None))
        self.txtEstadosCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome do estado de localização do endereço", None))
        self.txtNumeroCliente.setToolTip(_translate("frmCadastroFornecedor", "Numero Cliente", None))
        self.txtNumeroCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo de numero referente ao numero do endereço", None))
        self.lblNomeFantasiaCliente.setText(_translate("frmCadastroFornecedor", "Nome Fantasia", None))
        self.txtBairroCliente.setToolTip(_translate("frmCadastroFornecedor", "Bairro Cliente", None))
        self.txtBairroCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome do bairro referente ao endereço", None))
        self.txtInscricaoEstadualCliente.setToolTip(_translate("frmCadastroFornecedor", "Inscrição Estadual Cliente", None))
        self.txtInscricaoEstadualCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero do inscrição estadual da Cliente", None))
        self.lblTelefoeneCliente.setText(_translate("frmCadastroFornecedor", "Telefone", None))
        self.lblNumeroCliente.setText(_translate("frmCadastroFornecedor", "Numero", None))
        self.txtEnderecoCliente.setToolTip(_translate("frmCadastroFornecedor", "Endereço Cliente", None))
        self.txtEnderecoCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo de descrição do endereço", None))
        self.txtFantasiaCliente.setToolTip(_translate("frmCadastroFornecedor", "Nome Fantasia Cliente", None))
        self.txtFantasiaCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome fantasia da Cliente", None))
        self.lblCidadesCliente.setText(_translate("frmCadastroFornecedor", "Cidade", None))
        self.lblEstadosCliente.setText(_translate("frmCadastroFornecedor", "Estado", None))
        self.lblInscricaoEstadualCliente.setText(_translate("frmCadastroFornecedor", "Incrição Estadual", None))
        self.txtIdCliente.setToolTip(_translate("frmCadastroFornecedor", "Codigo Cliente", None))
        self.txtIdCliente.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do codigo de identificação da Cliente", None))
        self.lblCodigoCliente.setText(_translate("frmCadastroFornecedor", "Codigo", None))
        self.grbPesquisarEmpresa.setTitle(_translate("frmCadastroFornecedor", "Pesquisar Empresa", None))
        self.txtCnpjEmpresa.setToolTip(_translate("frmCadastroFornecedor", "CNPJ Empresa", None))
        self.txtCnpjEmpresa.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero do CNPJ da empresa", None))
        self.txtCnpjEmpresa.setInputMask(_translate("frmCadastroFornecedor", "00.000.000/0000-00; ", None))
        self.lblCodigoEmpresa.setText(_translate("frmCadastroFornecedor", "Codigo", None))
        self.lblNomeFantasiaEmpresa.setText(_translate("frmCadastroFornecedor", "Nome Fantasia", None))
        self.lblCnpj_2.setText(_translate("frmCadastroFornecedor", "CNPJ", None))
        self.txtFantasiaEmpresa.setToolTip(_translate("frmCadastroFornecedor", "Nome Fantasia Empresa", None))
        self.txtFantasiaEmpresa.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome fantasia da empresa", None))
        self.txtRazaoSocialEmpresa.setToolTip(_translate("frmCadastroFornecedor", "Razão Social Empresa", None))
        self.txtRazaoSocialEmpresa.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome da razão social da empresa", None))
        self.lblRazaoSocialEmpresa.setText(_translate("frmCadastroFornecedor", "Razão Social", None))
        self.txtIdEmpresa.setToolTip(_translate("frmCadastroFornecedor", "Codigo Empresa", None))
        self.txtIdEmpresa.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do codigo de identificação da empresa", None))
        self.txtInscricaoEstaduaEmpresa.setToolTip(_translate("frmCadastroFornecedor", "Inscrição Estadual Empresa", None))
        self.txtInscricaoEstaduaEmpresa.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero do inscrição estadual da empresa", None))
        self.lblInscricaoEstadualEmpresa.setText(_translate("frmCadastroFornecedor", "Incrição Estadual", None))


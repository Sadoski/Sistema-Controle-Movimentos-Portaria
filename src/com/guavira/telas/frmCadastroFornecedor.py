# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCadastroFornecedor.ui'
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
        self.grbDadosFornecedor = QtGui.QGroupBox(frmCadastroFornecedor)
        self.grbDadosFornecedor.setGeometry(QtCore.QRect(7, 120, 881, 271))
        self.grbDadosFornecedor.setObjectName(_fromUtf8("grbDadosFornecedor"))
        self.lblCepFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblCepFornecedor.setGeometry(QtCore.QRect(368, 166, 31, 19))
        self.lblCepFornecedor.setObjectName(_fromUtf8("lblCepFornecedor"))
        self.txtCidadesFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtCidadesFornecedor.setEnabled(False)
        self.txtCidadesFornecedor.setGeometry(QtCore.QRect(532, 186, 341, 25))
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
        self.txtCidadesFornecedor.setPalette(palette)
        self.txtCidadesFornecedor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCidadesFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCidadesFornecedor.setMaxLength(70)
        self.txtCidadesFornecedor.setObjectName(_fromUtf8("txtCidadesFornecedor"))
        self.lblBairroFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblBairroFornecedor.setGeometry(QtCore.QRect(8, 166, 41, 19))
        self.lblBairroFornecedor.setObjectName(_fromUtf8("lblBairroFornecedor"))
        self.lblComplementoFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblComplementoFornecedor.setGeometry(QtCore.QRect(602, 118, 101, 16))
        self.lblComplementoFornecedor.setObjectName(_fromUtf8("lblComplementoFornecedor"))
        self.txtTelefoneFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtTelefoneFornecedor.setGeometry(QtCore.QRect(222, 236, 191, 25))
        self.txtTelefoneFornecedor.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtTelefoneFornecedor.setObjectName(_fromUtf8("txtTelefoneFornecedor"))
        self.txtCnpjFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtCnpjFornecedor.setGeometry(QtCore.QRect(188, 40, 201, 25))
        self.txtCnpjFornecedor.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCnpjFornecedor.setText(_fromUtf8("../-"))
        self.txtCnpjFornecedor.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCnpjFornecedor.setObjectName(_fromUtf8("txtCnpjFornecedor"))
        self.lblRazaoSocialFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblRazaoSocialFornecedor.setGeometry(QtCore.QRect(452, 68, 81, 19))
        self.lblRazaoSocialFornecedor.setObjectName(_fromUtf8("lblRazaoSocialFornecedor"))
        self.lblCnpjFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblCnpjFornecedor.setGeometry(QtCore.QRect(188, 20, 41, 19))
        self.lblCnpjFornecedor.setObjectName(_fromUtf8("lblCnpjFornecedor"))
        self.txtRazaoSocialFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtRazaoSocialFornecedor.setGeometry(QtCore.QRect(452, 88, 421, 25))
        self.txtRazaoSocialFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtRazaoSocialFornecedor.setMaxLength(70)
        self.txtRazaoSocialFornecedor.setObjectName(_fromUtf8("txtRazaoSocialFornecedor"))
        self.txtCepFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtCepFornecedor.setGeometry(QtCore.QRect(368, 186, 151, 25))
        self.txtCepFornecedor.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCepFornecedor.setInputMask(_fromUtf8("00000-000; "))
        self.txtCepFornecedor.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCepFornecedor.setObjectName(_fromUtf8("txtCepFornecedor"))
        self.txtInscricaoMunicipalFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtInscricaoMunicipalFornecedor.setGeometry(QtCore.QRect(608, 40, 211, 25))
        self.txtInscricaoMunicipalFornecedor.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoMunicipalFornecedor.setMaxLength(8)
        self.txtInscricaoMunicipalFornecedor.setObjectName(_fromUtf8("txtInscricaoMunicipalFornecedor"))
        self.lblInscricaoMunicipalFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblInscricaoMunicipalFornecedor.setGeometry(QtCore.QRect(608, 20, 141, 19))
        self.lblInscricaoMunicipalFornecedor.setObjectName(_fromUtf8("lblInscricaoMunicipalFornecedor"))
        self.lblEnderecoFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblEnderecoFornecedor.setGeometry(QtCore.QRect(8, 118, 66, 19))
        self.lblEnderecoFornecedor.setObjectName(_fromUtf8("lblEnderecoFornecedor"))
        self.txtComplementoFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtComplementoFornecedor.setGeometry(QtCore.QRect(602, 138, 271, 25))
        self.txtComplementoFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtComplementoFornecedor.setMaxLength(50)
        self.txtComplementoFornecedor.setObjectName(_fromUtf8("txtComplementoFornecedor"))
        self.txtEstadosFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtEstadosFornecedor.setEnabled(False)
        self.txtEstadosFornecedor.setGeometry(QtCore.QRect(8, 236, 201, 25))
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
        self.txtEstadosFornecedor.setPalette(palette)
        self.txtEstadosFornecedor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtEstadosFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhUppercaseOnly)
        self.txtEstadosFornecedor.setMaxLength(50)
        self.txtEstadosFornecedor.setObjectName(_fromUtf8("txtEstadosFornecedor"))
        self.txtNumeroFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtNumeroFornecedor.setGeometry(QtCore.QRect(436, 138, 161, 25))
        self.txtNumeroFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtNumeroFornecedor.setMaxLength(11)
        self.txtNumeroFornecedor.setObjectName(_fromUtf8("txtNumeroFornecedor"))
        self.lblNomeFantasiaFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblNomeFantasiaFornecedor.setGeometry(QtCore.QRect(8, 68, 101, 19))
        self.lblNomeFantasiaFornecedor.setObjectName(_fromUtf8("lblNomeFantasiaFornecedor"))
        self.txtBairroFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtBairroFornecedor.setGeometry(QtCore.QRect(8, 186, 351, 25))
        self.txtBairroFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtBairroFornecedor.setMaxLength(50)
        self.txtBairroFornecedor.setObjectName(_fromUtf8("txtBairroFornecedor"))
        self.txtInscricaoEstadualFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtInscricaoEstadualFornecedor.setGeometry(QtCore.QRect(398, 40, 201, 25))
        self.txtInscricaoEstadualFornecedor.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoEstadualFornecedor.setMaxLength(8)
        self.txtInscricaoEstadualFornecedor.setObjectName(_fromUtf8("txtInscricaoEstadualFornecedor"))
        self.lblTelefoeneFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblTelefoeneFornecedor.setGeometry(QtCore.QRect(222, 216, 61, 19))
        self.lblTelefoeneFornecedor.setObjectName(_fromUtf8("lblTelefoeneFornecedor"))
        self.lblNumeroFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblNumeroFornecedor.setGeometry(QtCore.QRect(436, 118, 51, 19))
        self.lblNumeroFornecedor.setObjectName(_fromUtf8("lblNumeroFornecedor"))
        self.txtEnderecoFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtEnderecoFornecedor.setGeometry(QtCore.QRect(8, 138, 421, 25))
        self.txtEnderecoFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtEnderecoFornecedor.setMaxLength(50)
        self.txtEnderecoFornecedor.setObjectName(_fromUtf8("txtEnderecoFornecedor"))
        self.txtFantasiaFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtFantasiaFornecedor.setGeometry(QtCore.QRect(8, 88, 431, 25))
        self.txtFantasiaFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtFantasiaFornecedor.setMaxLength(70)
        self.txtFantasiaFornecedor.setObjectName(_fromUtf8("txtFantasiaFornecedor"))
        self.lblCidadesFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblCidadesFornecedor.setGeometry(QtCore.QRect(532, 166, 51, 19))
        self.lblCidadesFornecedor.setObjectName(_fromUtf8("lblCidadesFornecedor"))
        self.lblEstadosFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblEstadosFornecedor.setGeometry(QtCore.QRect(10, 216, 51, 19))
        self.lblEstadosFornecedor.setObjectName(_fromUtf8("lblEstadosFornecedor"))
        self.lblInscricaoEstadualFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblInscricaoEstadualFornecedor.setGeometry(QtCore.QRect(398, 20, 121, 19))
        self.lblInscricaoEstadualFornecedor.setObjectName(_fromUtf8("lblInscricaoEstadualFornecedor"))
        self.txtIdFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtIdFornecedor.setEnabled(False)
        self.txtIdFornecedor.setGeometry(QtCore.QRect(6, 40, 171, 25))
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
        self.txtIdFornecedor.setPalette(palette)
        self.txtIdFornecedor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtIdFornecedor.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtIdFornecedor.setMaxLength(11)
        self.txtIdFornecedor.setObjectName(_fromUtf8("txtIdFornecedor"))
        self.lblCodigoFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblCodigoFornecedor.setGeometry(QtCore.QRect(6, 20, 51, 19))
        self.lblCodigoFornecedor.setObjectName(_fromUtf8("lblCodigoFornecedor"))
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
        self.lblCepFornecedor.setBuddy(self.txtCepFornecedor)
        self.lblBairroFornecedor.setBuddy(self.txtBairroFornecedor)
        self.lblComplementoFornecedor.setBuddy(self.txtComplementoFornecedor)
        self.lblRazaoSocialFornecedor.setBuddy(self.txtRazaoSocialFornecedor)
        self.lblCnpjFornecedor.setBuddy(self.txtCnpjFornecedor)
        self.lblInscricaoMunicipalFornecedor.setBuddy(self.txtInscricaoMunicipalFornecedor)
        self.lblEnderecoFornecedor.setBuddy(self.txtEnderecoFornecedor)
        self.lblNomeFantasiaFornecedor.setBuddy(self.txtFantasiaFornecedor)
        self.lblTelefoeneFornecedor.setBuddy(self.txtTelefoneFornecedor)
        self.lblNumeroFornecedor.setBuddy(self.txtNumeroFornecedor)
        self.lblCidadesFornecedor.setBuddy(self.txtCidadesFornecedor)
        self.lblEstadosFornecedor.setBuddy(self.txtEstadosFornecedor)
        self.lblInscricaoEstadualFornecedor.setBuddy(self.txtInscricaoEstadualFornecedor)
        self.lblCodigoFornecedor.setBuddy(self.txtIdFornecedor)
        self.lblCodigoEmpresa.setBuddy(self.txtIdEmpresa)
        self.lblNomeFantasiaEmpresa.setBuddy(self.txtFantasiaEmpresa)
        self.lblCnpj_2.setBuddy(self.txtCnpjEmpresa)
        self.lblRazaoSocialEmpresa.setBuddy(self.txtRazaoSocialEmpresa)
        self.lblInscricaoEstadualEmpresa.setBuddy(self.txtInscricaoEstaduaEmpresa)

        self.retranslateUi(frmCadastroFornecedor)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtIdFornecedor, self.txtCnpjFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtCnpjFornecedor, self.txtInscricaoEstadualFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtInscricaoEstadualFornecedor, self.txtInscricaoMunicipalFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtInscricaoMunicipalFornecedor, self.txtFantasiaFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtFantasiaFornecedor, self.txtRazaoSocialFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtRazaoSocialFornecedor, self.txtEnderecoFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtEnderecoFornecedor, self.txtNumeroFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtNumeroFornecedor, self.txtComplementoFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtComplementoFornecedor, self.txtBairroFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtBairroFornecedor, self.txtCepFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtCepFornecedor, self.txtCidadesFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtCidadesFornecedor, self.txtEstadosFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtEstadosFornecedor, self.txtTelefoneFornecedor)
        frmCadastroFornecedor.setTabOrder(self.txtTelefoneFornecedor, self.btnNovo)
        frmCadastroFornecedor.setTabOrder(self.btnNovo, self.btnSalvar)
        frmCadastroFornecedor.setTabOrder(self.btnSalvar, self.btnEditar)
        frmCadastroFornecedor.setTabOrder(self.btnEditar, self.btnCancelar)
        frmCadastroFornecedor.setTabOrder(self.btnCancelar, self.btnDeletar)

    def retranslateUi(self, frmCadastroFornecedor):
        frmCadastroFornecedor.setWindowTitle(_translate("frmCadastroFornecedor", "Cadastro Fornecedor", None))
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
        self.grbDadosFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Grupo de Dados para cadastro e edição de empresas", None))
        self.grbDadosFornecedor.setTitle(_translate("frmCadastroFornecedor", "Dados Fornecedor", None))
        self.lblCepFornecedor.setText(_translate("frmCadastroFornecedor", "CEP", None))
        self.txtCidadesFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Cidade fornecedor", None))
        self.txtCidadesFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome da cidade referente a localização do endereço dentro do estado", None))
        self.lblBairroFornecedor.setText(_translate("frmCadastroFornecedor", "Bairro", None))
        self.lblComplementoFornecedor.setText(_translate("frmCadastroFornecedor", "Complemento", None))
        self.txtTelefoneFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Telefone fornecedor", None))
        self.txtTelefoneFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero de cantato de telefone da fornecedor", None))
        self.txtTelefoneFornecedor.setInputMask(_translate("frmCadastroFornecedor", "(00) 00000-0000; ", None))
        self.txtCnpjFornecedor.setToolTip(_translate("frmCadastroFornecedor", "CNPJ fornecedor", None))
        self.txtCnpjFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero do CNPJ da fornecedor", None))
        self.txtCnpjFornecedor.setInputMask(_translate("frmCadastroFornecedor", "00.000.000/0000-00; ", None))
        self.lblRazaoSocialFornecedor.setText(_translate("frmCadastroFornecedor", "Razão Social", None))
        self.lblCnpjFornecedor.setText(_translate("frmCadastroFornecedor", "CNPJ", None))
        self.txtRazaoSocialFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Razão Social fornecedor", None))
        self.txtRazaoSocialFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome da razão social da fornecedor", None))
        self.txtCepFornecedor.setToolTip(_translate("frmCadastroFornecedor", "CEP fornecedor", None))
        self.txtCepFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo de CEP referente a identificação da cidade e qual estado pertence", None))
        self.txtInscricaoMunicipalFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Inscrição Municipal fornecedor", None))
        self.txtInscricaoMunicipalFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero do inscrição municipal da fornecedor", None))
        self.lblInscricaoMunicipalFornecedor.setText(_translate("frmCadastroFornecedor", "Inscrição Municipal", None))
        self.lblEnderecoFornecedor.setText(_translate("frmCadastroFornecedor", "Endereço", None))
        self.txtComplementoFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Complemento fornecedor", None))
        self.txtComplementoFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo complementar do endereço", None))
        self.txtEstadosFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Estado fornecedor", None))
        self.txtEstadosFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome do estado de localização do endereço", None))
        self.txtNumeroFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Numero fornecedor", None))
        self.txtNumeroFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo de numero referente ao numero do endereço", None))
        self.lblNomeFantasiaFornecedor.setText(_translate("frmCadastroFornecedor", "Nome Fantasia", None))
        self.txtBairroFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Bairro fornecedor", None))
        self.txtBairroFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome do bairro referente ao endereço", None))
        self.txtInscricaoEstadualFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Inscrição Estadual fornecedor", None))
        self.txtInscricaoEstadualFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do numero do inscrição estadual da fornecedor", None))
        self.lblTelefoeneFornecedor.setText(_translate("frmCadastroFornecedor", "Telefone", None))
        self.lblNumeroFornecedor.setText(_translate("frmCadastroFornecedor", "Numero", None))
        self.txtEnderecoFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Endereço fornecedor", None))
        self.txtEnderecoFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo de descrição do endereço", None))
        self.txtFantasiaFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Nome Fantasia fornecedor", None))
        self.txtFantasiaFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do nome fantasia da fornecedor", None))
        self.lblCidadesFornecedor.setText(_translate("frmCadastroFornecedor", "Cidade", None))
        self.lblEstadosFornecedor.setText(_translate("frmCadastroFornecedor", "Estado", None))
        self.lblInscricaoEstadualFornecedor.setText(_translate("frmCadastroFornecedor", "Incrição Estadual", None))
        self.txtIdFornecedor.setToolTip(_translate("frmCadastroFornecedor", "Codigo fornecedor", None))
        self.txtIdFornecedor.setWhatsThis(_translate("frmCadastroFornecedor", "Campo do codigo de identificação da fornecedor", None))
        self.lblCodigoFornecedor.setText(_translate("frmCadastroFornecedor", "Codigo", None))
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


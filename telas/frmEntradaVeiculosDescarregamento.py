# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEntradaVeiculosDescarregamento.ui'
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

class Ui_frmEntradaVeiculosDescarregamento(object):
    def setupUi(self, frmEntradaVeiculosDescarregamento):
        frmEntradaVeiculosDescarregamento.setObjectName(_fromUtf8("frmEntradaVeiculosDescarregamento"))
        frmEntradaVeiculosDescarregamento.resize(743, 558)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        frmEntradaVeiculosDescarregamento.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/descarregamento.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmEntradaVeiculosDescarregamento.setWindowIcon(icon)
        frmEntradaVeiculosDescarregamento.setSizeGripEnabled(True)
        frmEntradaVeiculosDescarregamento.setModal(True)

        self.txtData = QtGui.QDateEdit(frmEntradaVeiculosDescarregamento)
        self.txtData.setDate(QtCore.QDate.currentDate())
        self.txtData.setEnabled(False)
        self.txtData.setGeometry(QtCore.QRect(15, 30, 110, 22))
        self.txtData.setCalendarPopup(True)
        self.txtData.setObjectName(_fromUtf8("txtData"))

        self.txtHora = QtGui.QTimeEdit(frmEntradaVeiculosDescarregamento)
        self.txtHora.setTime(QtCore.QTime.currentTime())
        self.txtHora.setEnabled(False)
        self.txtHora.setGeometry(QtCore.QRect(139, 30, 118, 22))
        self.txtHora.setObjectName(_fromUtf8("txtHora"))

        self.lblDataEntrada = QtGui.QLabel(frmEntradaVeiculosDescarregamento)
        self.lblDataEntrada.setGeometry(QtCore.QRect(15, 10, 101, 16))
        self.lblDataEntrada.setObjectName(_fromUtf8("lblDataEntrada"))

        self.lblHoraEntrada = QtGui.QLabel(frmEntradaVeiculosDescarregamento)
        self.lblHoraEntrada.setGeometry(QtCore.QRect(139, 10, 91, 16))
        self.lblHoraEntrada.setObjectName(_fromUtf8("lblHoraEntrada"))

        self.grbDadosFornecedor = QtGui.QGroupBox(frmEntradaVeiculosDescarregamento)
        self.grbDadosFornecedor.setEnabled(False)
        self.grbDadosFornecedor.setGeometry(QtCore.QRect(5, 119, 731, 261))
        self.grbDadosFornecedor.setObjectName(_fromUtf8("grbDadosFornecedor"))

        self.txtIdFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtIdFornecedor.setGeometry(QtCore.QRect(10, 33, 181, 25))
        self.txtIdFornecedor.setMaxLength(11)
        self.txtIdFornecedor.setObjectName(_fromUtf8("txtIdFornecedor"))

        self.txtNomeFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtNomeFornecedor.setEnabled(False)
        self.txtNomeFornecedor.setGeometry(QtCore.QRect(195, 33, 521, 25))
        self.txtNomeFornecedor.setMaxLength(70)
        self.txtNomeFornecedor.setObjectName(_fromUtf8("txtNomeFornecedor"))

        self.lblCodigoFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblCodigoFornecedor.setGeometry(QtCore.QRect(10, 13, 131, 21))
        self.lblCodigoFornecedor.setObjectName(_fromUtf8("lblCodigoFornecedor"))

        self.lblNomeFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblNomeFornecedor.setGeometry(QtCore.QRect(195, 13, 151, 16))
        self.lblNomeFornecedor.setObjectName(_fromUtf8("lblNomeFornecedor"))

        self.txtEnderecoFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtEnderecoFornecedor.setEnabled(False)
        self.txtEnderecoFornecedor.setGeometry(QtCore.QRect(8, 128, 311, 25))
        self.txtEnderecoFornecedor.setMaxLength(50)
        self.txtEnderecoFornecedor.setObjectName(_fromUtf8("txtEnderecoFornecedor"))

        self.txtNumeroFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtNumeroFornecedor.setEnabled(False)
        self.txtNumeroFornecedor.setGeometry(QtCore.QRect(330, 128, 141, 25))
        self.txtNumeroFornecedor.setMaxLength(11)
        self.txtNumeroFornecedor.setObjectName(_fromUtf8("txtNumeroFornecedor"))

        self.txtComplementoFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtComplementoFornecedor.setEnabled(False)
        self.txtComplementoFornecedor.setGeometry(QtCore.QRect(480, 128, 241, 25))
        self.txtComplementoFornecedor.setMaxLength(50)
        self.txtComplementoFornecedor.setObjectName(_fromUtf8("txtComplementoFornecedor"))

        self.txtCidadeFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtCidadeFornecedor.setEnabled(False)
        self.txtCidadeFornecedor.setGeometry(QtCore.QRect(290, 172, 431, 25))
        self.txtCidadeFornecedor.setMaxLength(70)
        self.txtCidadeFornecedor.setObjectName(_fromUtf8("txtCidadeFornecedor"))

        self.txtEstadoFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtEstadoFornecedor.setEnabled(False)
        self.txtEstadoFornecedor.setGeometry(QtCore.QRect(10, 220, 201, 25))
        self.txtEstadoFornecedor.setMaxLength(50)
        self.txtEstadoFornecedor.setObjectName(_fromUtf8("txtEstadoFornecedor"))

        self.txtCepFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtCepFornecedor.setEnabled(False)
        self.txtCepFornecedor.setGeometry(QtCore.QRect(220, 220, 161, 25))
        self.txtCepFornecedor.setObjectName(_fromUtf8("txtCepFornecedor"))

        self.txtBairroFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtBairroFornecedor.setEnabled(False)
        self.txtBairroFornecedor.setGeometry(QtCore.QRect(8, 172, 271, 25))
        self.txtBairroFornecedor.setMaxLength(50)
        self.txtBairroFornecedor.setObjectName(_fromUtf8("txtBairroFornecedor"))

        self.lblEnderecoEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblEnderecoEmitente.setGeometry(QtCore.QRect(10, 108, 61, 16))
        self.lblEnderecoEmitente.setObjectName(_fromUtf8("lblEnderecoEmitente"))

        self.lblNumeroEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblNumeroEmitente.setGeometry(QtCore.QRect(330, 108, 61, 16))
        self.lblNumeroEmitente.setObjectName(_fromUtf8("lblNumeroEmitente"))

        self.lblComplementoEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblComplementoEmitente.setGeometry(QtCore.QRect(480, 108, 91, 16))
        self.lblComplementoEmitente.setObjectName(_fromUtf8("lblComplementoEmitente"))

        self.lblBairroEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblBairroEmitente.setGeometry(QtCore.QRect(10, 152, 61, 16))
        self.lblBairroEmitente.setObjectName(_fromUtf8("lblBairroEmitente"))

        self.lblCidadeEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblCidadeEmitente.setGeometry(QtCore.QRect(288, 152, 61, 16))
        self.lblCidadeEmitente.setObjectName(_fromUtf8("lblCidadeEmitente"))

        self.lblEstadoEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblEstadoEmitente.setGeometry(QtCore.QRect(10, 200, 61, 16))
        self.lblEstadoEmitente.setObjectName(_fromUtf8("lblEstadoEmitente"))

        self.lblCepEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblCepEmitente.setGeometry(QtCore.QRect(220, 200, 61, 16))
        self.lblCepEmitente.setObjectName(_fromUtf8("lblCepEmitente"))

        self.txtInscricaoEstaduaFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtInscricaoEstaduaFornecedor.setEnabled(False)
        self.txtInscricaoEstaduaFornecedor.setGeometry(QtCore.QRect(554, 80, 161, 25))
        self.txtInscricaoEstaduaFornecedor.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoEstaduaFornecedor.setMaxLength(8)
        self.txtInscricaoEstaduaFornecedor.setObjectName(_fromUtf8("txtInscricaoEstaduaFornecedor"))

        self.txtRazaoSocialFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtRazaoSocialFornecedor.setEnabled(False)
        self.txtRazaoSocialFornecedor.setGeometry(QtCore.QRect(7, 80, 361, 25))
        self.txtRazaoSocialFornecedor.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtRazaoSocialFornecedor.setMaxLength(70)
        self.txtRazaoSocialFornecedor.setObjectName(_fromUtf8("txtRazaoSocialFornecedor"))

        self.lblRazaoSociaFornecedor = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblRazaoSociaFornecedor.setGeometry(QtCore.QRect(7, 60, 81, 19))
        self.lblRazaoSociaFornecedor.setObjectName(_fromUtf8("lblRazaoSociaFornecedor"))

        self.lblCnpjEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblCnpjEmitente.setGeometry(QtCore.QRect(378, 60, 41, 19))
        self.lblCnpjEmitente.setObjectName(_fromUtf8("lblCnpjEmitente"))

        self.lblInscricaoEstadualEmitente = QtGui.QLabel(self.grbDadosFornecedor)
        self.lblInscricaoEstadualEmitente.setGeometry(QtCore.QRect(554, 60, 121, 19))
        self.lblInscricaoEstadualEmitente.setObjectName(_fromUtf8("lblInscricaoEstadualEmitente"))

        self.txtCnpjFornecedor = QtGui.QLineEdit(self.grbDadosFornecedor)
        self.txtCnpjFornecedor.setEnabled(False)
        self.txtCnpjFornecedor.setGeometry(QtCore.QRect(378, 80, 171, 25))
        self.txtCnpjFornecedor.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCnpjFornecedor.setText(_fromUtf8("../-"))
        self.txtCnpjFornecedor.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCnpjFornecedor.setObjectName(_fromUtf8("txtCnpjFornecedor"))

        self.btnPesquisarFornecedor = QtGui.QPushButton(self.grbDadosFornecedor)
        self.btnPesquisarFornecedor.setGeometry(QtCore.QRect(390, 220, 31, 26))
        self.btnPesquisarFornecedor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPesquisarFornecedor.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisarFornecedor.setIcon(icon1)
        self.btnPesquisarFornecedor.setObjectName(_fromUtf8("btnPesquisarFornecedor"))

        self.grbNotaFiscal = QtGui.QGroupBox(frmEntradaVeiculosDescarregamento)
        self.grbNotaFiscal.setEnabled(False)
        self.grbNotaFiscal.setGeometry(QtCore.QRect(5, 58, 731, 63))
        self.grbNotaFiscal.setObjectName(_fromUtf8("grbNotaFiscal"))

        self.txtNumeroNotaFiscal = QtGui.QLineEdit(self.grbNotaFiscal)
        self.txtNumeroNotaFiscal.setEnabled(False)
        self.txtNumeroNotaFiscal.setGeometry(QtCore.QRect(110, 33, 171, 25))
        self.txtNumeroNotaFiscal.setMaxLength(11)
        self.txtNumeroNotaFiscal.setObjectName(_fromUtf8("txtNumeroNotaFiscal"))

        self.lblTipoProduto = QtGui.QLabel(self.grbNotaFiscal)
        self.lblTipoProduto.setGeometry(QtCore.QRect(298, 13, 111, 16))
        self.lblTipoProduto.setObjectName(_fromUtf8("lblTipoProduto"))

        self.txtProduto = QtGui.QLineEdit(self.grbNotaFiscal)
        self.txtProduto.setEnabled(False)
        self.txtProduto.setGeometry(QtCore.QRect(294, 33, 361, 25))
        self.txtProduto.setMaxLength(50)
        self.txtProduto.setObjectName(_fromUtf8("txtProduto"))

        self.lblNumeroNotaFiscal = QtGui.QLabel(self.grbNotaFiscal)
        self.lblNumeroNotaFiscal.setGeometry(QtCore.QRect(110, 13, 131, 16))
        self.lblNumeroNotaFiscal.setObjectName(_fromUtf8("lblNumeroNotaFiscal"))

        self.btnPesquisarNotaFiscal = QtGui.QPushButton(self.grbNotaFiscal)
        self.btnPesquisarNotaFiscal.setGeometry(QtCore.QRect(690, 30, 31, 27))
        self.btnPesquisarNotaFiscal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPesquisarNotaFiscal.setText(_fromUtf8(""))
        self.btnPesquisarNotaFiscal.setIcon(icon1)
        self.btnPesquisarNotaFiscal.setObjectName(_fromUtf8("btnPesquisarNotaFiscal"))

        self.lblCodigo = QtGui.QLabel(self.grbNotaFiscal)
        self.lblCodigo.setGeometry(QtCore.QRect(10, 15, 81, 16))
        self.lblCodigo.setObjectName(_fromUtf8("lblCodigo"))

        self.txtCodigo = QtGui.QLineEdit(self.grbNotaFiscal)
        self.txtCodigo.setGeometry(QtCore.QRect(10, 33, 91, 25))
        self.txtCodigo.setMaxLength(11)
        self.txtCodigo.setObjectName(_fromUtf8("txtCodigo"))

        self.grbDadosMotorista = QtGui.QGroupBox(frmEntradaVeiculosDescarregamento)
        self.grbDadosMotorista.setEnabled(False)
        self.grbDadosMotorista.setGeometry(QtCore.QRect(5, 380, 731, 109))
        self.grbDadosMotorista.setObjectName(_fromUtf8("grbDadosMotorista"))

        self.txtModeloMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtModeloMotorista.setEnabled(False)
        self.txtModeloMotorista.setGeometry(QtCore.QRect(7, 78, 205, 25))
        self.txtModeloMotorista.setMaxLength(50)
        self.txtModeloMotorista.setObjectName(_fromUtf8("txtModeloMotorista"))

        self.lblMarca = QtGui.QLabel(self.grbDadosMotorista)
        self.lblMarca.setGeometry(QtCore.QRect(220, 58, 51, 19))
        self.lblMarca.setObjectName(_fromUtf8("lblMarca"))

        self.txtMarcaMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtMarcaMotorista.setEnabled(False)
        self.txtMarcaMotorista.setGeometry(QtCore.QRect(220, 78, 231, 25))
        self.txtMarcaMotorista.setMaxLength(50)
        self.txtMarcaMotorista.setObjectName(_fromUtf8("txtMarcaMotorista"))

        self.txtNomeMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtNomeMotorista.setEnabled(False)
        self.txtNomeMotorista.setGeometry(QtCore.QRect(174, 34, 521, 25))
        self.txtNomeMotorista.setMaxLength(70)
        self.txtNomeMotorista.setObjectName(_fromUtf8("txtNomeMotorista"))

        self.lblNomeMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblNomeMotorista.setGeometry(QtCore.QRect(174, 14, 171, 19))
        self.lblNomeMotorista.setObjectName(_fromUtf8("lblNomeMotorista"))

        self.txtPlacaMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtPlacaMotorista.setEnabled(False)
        self.txtPlacaMotorista.setGeometry(QtCore.QRect(460, 78, 211, 25))
        self.txtPlacaMotorista.setObjectName(_fromUtf8("txtPlacaMotorista"))

        self.lblModelo = QtGui.QLabel(self.grbDadosMotorista)
        self.lblModelo.setGeometry(QtCore.QRect(7, 58, 51, 19))
        self.lblModelo.setObjectName(_fromUtf8("lblModelo"))

        self.txtidMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtidMotorista.setGeometry(QtCore.QRect(5, 34, 161, 25))
        self.txtidMotorista.setMaxLength(11)
        self.txtidMotorista.setObjectName(_fromUtf8("txtidMotorista"))

        self.lblCodigoMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblCodigoMotorista.setGeometry(QtCore.QRect(4, 14, 121, 19))
        self.lblCodigoMotorista.setObjectName(_fromUtf8("lblCodigoMotorista"))

        self.lblPlaca = QtGui.QLabel(self.grbDadosMotorista)
        self.lblPlaca.setGeometry(QtCore.QRect(460, 58, 51, 19))
        self.lblPlaca.setObjectName(_fromUtf8("lblPlaca"))

        self.btnPesquisarMotorista = QtGui.QPushButton(self.grbDadosMotorista)
        self.btnPesquisarMotorista.setGeometry(QtCore.QRect(690, 76, 31, 26))
        self.btnPesquisarMotorista.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPesquisarMotorista.setText(_fromUtf8(""))
        self.btnPesquisarMotorista.setIcon(icon1)
        self.btnPesquisarMotorista.setObjectName(_fromUtf8("btnPesquisarMotorista"))

        self.grbBotoes = QtGui.QGroupBox(frmEntradaVeiculosDescarregamento)
        self.grbBotoes.setGeometry(QtCore.QRect(20, 500, 718, 51))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(400, 12, 88, 27))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNovo.setIcon(icon2)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(500, 12, 88, 27))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon3)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))

        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(600, 12, 88, 27))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon4)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.lblDataEntrada.setBuddy(self.txtData)
        self.lblHoraEntrada.setBuddy(self.txtHora)
        self.lblCodigoFornecedor.setBuddy(self.txtIdFornecedor)
        self.lblNomeFornecedor.setBuddy(self.txtNomeFornecedor)
        self.lblEnderecoEmitente.setBuddy(self.txtEnderecoFornecedor)
        self.lblNumeroEmitente.setBuddy(self.txtNumeroFornecedor)
        self.lblComplementoEmitente.setBuddy(self.txtComplementoFornecedor)
        self.lblBairroEmitente.setBuddy(self.txtBairroFornecedor)
        self.lblCidadeEmitente.setBuddy(self.txtCidadeFornecedor)
        self.lblEstadoEmitente.setBuddy(self.txtEstadoFornecedor)
        self.lblCepEmitente.setBuddy(self.txtCepFornecedor)
        self.lblRazaoSociaFornecedor.setBuddy(self.txtRazaoSocialFornecedor)
        self.lblCnpjEmitente.setBuddy(self.txtCnpjFornecedor)
        self.lblInscricaoEstadualEmitente.setBuddy(self.txtInscricaoEstaduaFornecedor)
        self.lblTipoProduto.setBuddy(self.txtProduto)
        self.lblNumeroNotaFiscal.setBuddy(self.txtNumeroNotaFiscal)
        self.lblCodigo.setBuddy(self.txtNumeroNotaFiscal)
        self.lblMarca.setBuddy(self.txtMarcaMotorista)
        self.lblNomeMotorista.setBuddy(self.txtNomeMotorista)
        self.lblModelo.setBuddy(self.txtModeloMotorista)
        self.lblCodigoMotorista.setBuddy(self.txtidMotorista)
        self.lblPlaca.setBuddy(self.txtPlacaMotorista)

        self.retranslateUi(frmEntradaVeiculosDescarregamento)
        QtCore.QMetaObject.connectSlotsByName(frmEntradaVeiculosDescarregamento)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtData, self.txtHora)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtHora, self.txtNumeroNotaFiscal)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtNumeroNotaFiscal, self.txtProduto)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtProduto, self.txtIdFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtIdFornecedor, self.txtNomeFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtNomeFornecedor, self.txtRazaoSocialFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtRazaoSocialFornecedor, self.txtCnpjFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtCnpjFornecedor, self.txtInscricaoEstaduaFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtInscricaoEstaduaFornecedor, self.txtEnderecoFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtEnderecoFornecedor, self.txtNumeroFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtNumeroFornecedor, self.txtComplementoFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtComplementoFornecedor, self.txtBairroFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtBairroFornecedor, self.txtCidadeFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtCidadeFornecedor, self.txtEstadoFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtEstadoFornecedor, self.txtCepFornecedor)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtCepFornecedor, self.txtidMotorista)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtidMotorista, self.txtNomeMotorista)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtNomeMotorista, self.txtModeloMotorista)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtModeloMotorista, self.txtMarcaMotorista)
        frmEntradaVeiculosDescarregamento.setTabOrder(self.txtMarcaMotorista, self.txtPlacaMotorista)

    def retranslateUi(self, frmEntradaVeiculosDescarregamento):
        frmEntradaVeiculosDescarregamento.setWindowTitle(_translate("frmEntradaVeiculosDescarregamento", "Entrada de Veiculos Descarregamento", None))
        self.txtData.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Data Entrada", None))
        self.txtHora.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Hora Entrada", None))
        self.lblDataEntrada.setText(_translate("frmEntradaVeiculosDescarregamento", "Data Entrada", None))
        self.lblHoraEntrada.setText(_translate("frmEntradaVeiculosDescarregamento", "Hora Entrada", None))
        self.grbDadosFornecedor.setTitle(_translate("frmEntradaVeiculosDescarregamento", "Fornecedor", None))
        self.txtIdFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Codigo Emitente", None))
        self.txtIdFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do codigo de identificação do emitente", None))
        self.txtNomeFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Nome Fantasia Emitente", None))
        self.txtNomeFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do nome fantasia do emitente", None))
        self.lblCodigoFornecedor.setText(_translate("frmEntradaVeiculosDescarregamento", "Codigo", None))
        self.lblNomeFornecedor.setText(_translate("frmEntradaVeiculosDescarregamento", "Nome Fatasia", None))
        self.txtEnderecoFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Endereço ", None))
        self.txtEnderecoFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Endereço do emitente", None))
        self.txtNumeroFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Numero ", None))
        self.txtNumeroFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Numero referente ao endereço do emitente", None))
        self.txtComplementoFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Complemento", None))
        self.txtComplementoFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Complemento do endereço do emitente", None))
        self.txtCidadeFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Cidade", None))
        self.txtCidadeFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Nome da cidade onde o emitente reside", None))
        self.txtEstadoFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Estado", None))
        self.txtEstadoFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Nome do estado onde fica localizado a cidade do emitente", None))
        self.txtCepFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "CEP ", None))
        self.txtCepFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Codigo do CEP referente a cidade do emitente", None))
        self.txtCepFornecedor.setInputMask(_translate("frmEntradaVeiculosDescarregamento", "00000-000; ", None))
        self.txtBairroFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Bairro", None))
        self.txtBairroFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Nome do bairro localizado o endereço do emitente", None))
        self.lblEnderecoEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "Endereço", None))
        self.lblNumeroEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "Numero", None))
        self.lblComplementoEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "Complemento", None))
        self.lblBairroEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "Bairro", None))
        self.lblCidadeEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "Cidade", None))
        self.lblEstadoEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "Estado", None))
        self.lblCepEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "CEP", None))
        self.txtInscricaoEstaduaFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Inscrição Estadual ", None))
        self.txtInscricaoEstaduaFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do numero do inscrição estadual do emitente", None))
        self.txtRazaoSocialFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Razão Social ", None))
        self.txtRazaoSocialFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do nome da razão social do emitente", None))
        self.lblRazaoSociaFornecedor.setText(_translate("frmEntradaVeiculosDescarregamento", "Razão Social", None))
        self.lblCnpjEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "CNPJ", None))
        self.lblInscricaoEstadualEmitente.setText(_translate("frmEntradaVeiculosDescarregamento", "Incrição Estadual", None))
        self.txtCnpjFornecedor.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "CNPJ ", None))
        self.txtCnpjFornecedor.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do numero do CNPJ do emitente", None))
        self.txtCnpjFornecedor.setInputMask(_translate("frmEntradaVeiculosDescarregamento", "00.000.000/0000-00; ", None))
        self.grbNotaFiscal.setTitle(_translate("frmEntradaVeiculosDescarregamento", "Nota Fiscal", None))
        self.txtNumeroNotaFiscal.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Numero Nota Fiscal", None))
        self.txtNumeroNotaFiscal.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do numero da nota fiscal", None))
        self.lblTipoProduto.setText(_translate("frmEntradaVeiculosDescarregamento", "Produto", None))
        self.txtProduto.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Tipo de Produto", None))
        self.txtProduto.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo de descrição do tipo de produto", None))
        self.lblNumeroNotaFiscal.setText(_translate("frmEntradaVeiculosDescarregamento", "Numero Nota Fiscal", None))
        self.lblCodigo.setText(_translate("frmEntradaVeiculosDescarregamento", "Codigo", None))
        self.txtCodigo.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Codigo", None))
        self.txtCodigo.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "<html><head/><body><p>Campo do codigo da NF</p></body></html>", None))
        self.grbDadosMotorista.setTitle(_translate("frmEntradaVeiculosDescarregamento", "Motorista", None))
        self.txtModeloMotorista.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Marca do Veiculo", None))
        self.txtModeloMotorista.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do nome do modelo do veiculo", None))
        self.lblMarca.setText(_translate("frmEntradaVeiculosDescarregamento", "Marca", None))
        self.txtMarcaMotorista.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Marca do Veiculo", None))
        self.txtMarcaMotorista.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do nome da marca do veiculo", None))
        self.txtNomeMotorista.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Nome Fantasia Motorista", None))
        self.txtNomeMotorista.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do nome fantasia do motorista", None))
        self.lblNomeMotorista.setText(_translate("frmEntradaVeiculosDescarregamento", "Nome Fantasia Motorista", None))
        self.txtPlacaMotorista.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Placa do Veiculo", None))
        self.txtPlacaMotorista.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo de identificação da placa do veiculo", None))
        self.txtPlacaMotorista.setInputMask(_translate("frmEntradaVeiculosDescarregamento", "nnn-0000; ", None))
        self.txtPlacaMotorista.setText(_translate("frmEntradaVeiculosDescarregamento", "-", None))
        self.lblModelo.setText(_translate("frmEntradaVeiculosDescarregamento", "Modelo", None))
        self.txtidMotorista.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Codigo Motorista", None))
        self.txtidMotorista.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Campo do Codigo de identificação do motorista", None))
        self.lblCodigoMotorista.setText(_translate("frmEntradaVeiculosDescarregamento", "Codigo Motorista", None))
        self.lblPlaca.setText(_translate("frmEntradaVeiculosDescarregamento", "Placa", None))
        self.btnNovo.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Novo", None))
        self.btnNovo.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "<html><head/><body><p>Botão para cadastrar uma novo registro da pessoa jurídica</p></body></html>", None))
        self.btnNovo.setText(_translate("frmEntradaVeiculosDescarregamento", "Novo", None))
        self.btnSalvar.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Salvar", None))
        self.btnSalvar.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "<html><head/><body><p>Botão para salvar um novo registro da pessoa jurídica</p></body></html>", None))
        self.btnSalvar.setText(_translate("frmEntradaVeiculosDescarregamento", "Salvar", None))
        self.btnCancelar.setToolTip(_translate("frmEntradaVeiculosDescarregamento", "Cancelar", None))
        self.btnCancelar.setWhatsThis(_translate("frmEntradaVeiculosDescarregamento", "Botão para cancelar a operação ", None))
        self.btnCancelar.setText(_translate("frmEntradaVeiculosDescarregamento", "Cancelar", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEntradaCaminhaoEmpresa.ui'
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

class Ui_frmEntradaCaminhoaEmpresa(object):
    def setupUi(self, frmEntradaCaminhoaEmpresa):
        frmEntradaCaminhoaEmpresa.setObjectName(_fromUtf8("frmEntradaCaminhoaEmpresa"))
        frmEntradaCaminhoaEmpresa.resize(890, 500)
        frmEntradaCaminhoaEmpresa.setMinimumSize(QtCore.QSize(890, 500))
        frmEntradaCaminhoaEmpresa.setMaximumSize(QtCore.QSize(890, 500))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        frmEntradaCaminhoaEmpresa.setFont(font)
        self.grbDadosMotorista = QtGui.QGroupBox(frmEntradaCaminhoaEmpresa)
        self.grbDadosMotorista.setEnabled(False)
        self.grbDadosMotorista.setGeometry(QtCore.QRect(10, 10, 871, 114))
        self.grbDadosMotorista.setObjectName(_fromUtf8("grbDadosMotorista"))
        self.txtModeloMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtModeloMotorista.setEnabled(False)
        self.txtModeloMotorista.setGeometry(QtCore.QRect(10, 80, 291, 25))
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
        self.txtModeloMotorista.setPalette(palette)
        self.txtModeloMotorista.setMaxLength(50)
        self.txtModeloMotorista.setObjectName(_fromUtf8("txtModeloMotorista"))
        self.lblMarcaMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblMarcaMotorista.setGeometry(QtCore.QRect(310, 62, 51, 19))
        self.lblMarcaMotorista.setObjectName(_fromUtf8("lblMarcaMotorista"))
        self.txtMarcaMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtMarcaMotorista.setEnabled(False)
        self.txtMarcaMotorista.setGeometry(QtCore.QRect(310, 82, 331, 25))
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
        self.txtMarcaMotorista.setPalette(palette)
        self.txtMarcaMotorista.setMaxLength(50)
        self.txtMarcaMotorista.setObjectName(_fromUtf8("txtMarcaMotorista"))
        self.txtNomeMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtNomeMotorista.setGeometry(QtCore.QRect(180, 36, 621, 25))
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
        self.txtNomeMotorista.setPalette(palette)
        self.txtNomeMotorista.setMaxLength(70)
        self.txtNomeMotorista.setObjectName(_fromUtf8("txtNomeMotorista"))
        self.lblNomeMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblNomeMotorista.setGeometry(QtCore.QRect(180, 16, 151, 19))
        self.lblNomeMotorista.setObjectName(_fromUtf8("lblNomeMotorista"))
        self.txtPlacaMotorista = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtPlacaMotorista.setEnabled(False)
        self.txtPlacaMotorista.setGeometry(QtCore.QRect(650, 82, 211, 25))
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
        self.txtPlacaMotorista.setPalette(palette)
        self.txtPlacaMotorista.setObjectName(_fromUtf8("txtPlacaMotorista"))
        self.lblModeloMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblModeloMotorista.setGeometry(QtCore.QRect(10, 60, 51, 19))
        self.lblModeloMotorista.setObjectName(_fromUtf8("lblModeloMotorista"))
        self.txtidFuncionario = QtGui.QLineEdit(self.grbDadosMotorista)
        self.txtidFuncionario.setEnabled(False)
        self.txtidFuncionario.setGeometry(QtCore.QRect(10, 36, 161, 25))
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
        self.txtidFuncionario.setPalette(palette)
        self.txtidFuncionario.setMaxLength(11)
        self.txtidFuncionario.setObjectName(_fromUtf8("txtidFuncionario"))
        self.lblCodigoMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblCodigoMotorista.setGeometry(QtCore.QRect(10, 16, 121, 19))
        self.lblCodigoMotorista.setObjectName(_fromUtf8("lblCodigoMotorista"))
        self.lblPlacaMotorista = QtGui.QLabel(self.grbDadosMotorista)
        self.lblPlacaMotorista.setGeometry(QtCore.QRect(650, 62, 51, 19))
        self.lblPlacaMotorista.setObjectName(_fromUtf8("lblPlacaMotorista"))
        self.btnPesquisarMotorista = QtGui.QPushButton(self.grbDadosMotorista)
        self.btnPesquisarMotorista.setGeometry(QtCore.QRect(820, 35, 31, 26))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnPesquisarMotorista.setFont(font)
        self.btnPesquisarMotorista.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisarMotorista.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Sistema Contorle Movimentos Portaria/imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisarMotorista.setIcon(icon)
        self.btnPesquisarMotorista.setObjectName(_fromUtf8("btnPesquisarMotorista"))
        self.grbBotoes = QtGui.QGroupBox(frmEntradaCaminhoaEmpresa)
        self.grbBotoes.setGeometry(QtCore.QRect(10, 410, 871, 80))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))
        self.btnDeletar = QtGui.QPushButton(self.grbBotoes)
        self.btnDeletar.setEnabled(False)
        self.btnDeletar.setGeometry(QtCore.QRect(780, 10, 81, 61))
        self.btnDeletar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnDeletar.setObjectName(_fromUtf8("btnDeletar"))
        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(680, 10, 81, 61))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(480, 10, 81, 61))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(380, 10, 81, 61))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))
        self.btnEditar = QtGui.QPushButton(self.grbBotoes)
        self.btnEditar.setEnabled(False)
        self.btnEditar.setGeometry(QtCore.QRect(580, 10, 81, 61))
        self.btnEditar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))
        self.grbDadosOrigem = QtGui.QGroupBox(frmEntradaCaminhoaEmpresa)
        self.grbDadosOrigem.setEnabled(False)
        self.grbDadosOrigem.setGeometry(QtCore.QRect(10, 130, 871, 121))
        self.grbDadosOrigem.setObjectName(_fromUtf8("grbDadosOrigem"))
        self.lblEstadosCliente = QtGui.QLabel(self.grbDadosOrigem)
        self.lblEstadosCliente.setGeometry(QtCore.QRect(12, 69, 51, 19))
        self.lblEstadosCliente.setObjectName(_fromUtf8("lblEstadosCliente"))
        self.txtEstadosCliente = QtGui.QLineEdit(self.grbDadosOrigem)
        self.txtEstadosCliente.setEnabled(False)
        self.txtEstadosCliente.setGeometry(QtCore.QRect(10, 90, 201, 25))
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
        self.lblCepCliente = QtGui.QLabel(self.grbDadosOrigem)
        self.lblCepCliente.setGeometry(QtCore.QRect(6, 20, 31, 19))
        self.lblCepCliente.setObjectName(_fromUtf8("lblCepCliente"))
        self.txtCidadesCliente = QtGui.QLineEdit(self.grbDadosOrigem)
        self.txtCidadesCliente.setEnabled(False)
        self.txtCidadesCliente.setGeometry(QtCore.QRect(180, 40, 621, 25))
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
        self.lblCidadesCliente = QtGui.QLabel(self.grbDadosOrigem)
        self.lblCidadesCliente.setGeometry(QtCore.QRect(180, 20, 51, 19))
        self.lblCidadesCliente.setObjectName(_fromUtf8("lblCidadesCliente"))
        self.txtCepCliente = QtGui.QLineEdit(self.grbDadosOrigem)
        self.txtCepCliente.setEnabled(False)
        self.txtCepCliente.setGeometry(QtCore.QRect(10, 40, 161, 25))
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
        self.txtCepCliente.setPalette(palette)
        self.txtCepCliente.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCepCliente.setInputMask(_fromUtf8("00000-000; "))
        self.txtCepCliente.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCepCliente.setObjectName(_fromUtf8("txtCepCliente"))
        self.btnPesquisarCidade = QtGui.QPushButton(self.grbDadosOrigem)
        self.btnPesquisarCidade.setEnabled(False)
        self.btnPesquisarCidade.setGeometry(QtCore.QRect(820, 40, 31, 26))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnPesquisarCidade.setFont(font)
        self.btnPesquisarCidade.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisarCidade.setText(_fromUtf8(""))
        self.btnPesquisarCidade.setIcon(icon)
        self.btnPesquisarCidade.setObjectName(_fromUtf8("btnPesquisarCidade"))
        self.grbDadosDestino = QtGui.QGroupBox(frmEntradaCaminhoaEmpresa)
        self.grbDadosDestino.setEnabled(False)
        self.grbDadosDestino.setGeometry(QtCore.QRect(10, 250, 871, 71))
        self.grbDadosDestino.setObjectName(_fromUtf8("grbDadosDestino"))
        self.txtSetor = QtGui.QComboBox(self.grbDadosDestino)
        self.txtSetor.setEnabled(False)
        self.txtSetor.setGeometry(QtCore.QRect(300, 40, 281, 22))
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
        self.txtSetor.setPalette(palette)
        self.txtSetor.setObjectName(_fromUtf8("txtSetor"))
        self.lblSetor = QtGui.QLabel(self.grbDadosDestino)
        self.lblSetor.setGeometry(QtCore.QRect(300, 20, 46, 13))
        self.lblSetor.setObjectName(_fromUtf8("lblSetor"))
        self.txtTipoAfazer = QtGui.QComboBox(self.grbDadosDestino)
        self.txtTipoAfazer.setEnabled(False)
        self.txtTipoAfazer.setGeometry(QtCore.QRect(10, 40, 281, 22))
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
        self.txtTipoAfazer.setPalette(palette)
        self.txtTipoAfazer.setObjectName(_fromUtf8("txtTipoAfazer"))
        self.lblTipoAfazer = QtGui.QLabel(self.grbDadosDestino)
        self.lblTipoAfazer.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.lblTipoAfazer.setObjectName(_fromUtf8("lblTipoAfazer"))
        self.grbDadosExtra = QtGui.QGroupBox(frmEntradaCaminhoaEmpresa)
        self.grbDadosExtra.setEnabled(False)
        self.grbDadosExtra.setGeometry(QtCore.QRect(10, 320, 871, 81))
        self.grbDadosExtra.setObjectName(_fromUtf8("grbDadosExtra"))
        self.txtTipoCarga = QtGui.QComboBox(self.grbDadosExtra)
        self.txtTipoCarga.setEnabled(False)
        self.txtTipoCarga.setGeometry(QtCore.QRect(280, 42, 241, 25))
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
        self.txtTipoCarga.setPalette(palette)
        self.txtTipoCarga.setObjectName(_fromUtf8("txtTipoCarga"))
        self.lblDataEntrada = QtGui.QLabel(self.grbDadosExtra)
        self.lblDataEntrada.setGeometry(QtCore.QRect(10, 22, 101, 16))
        self.lblDataEntrada.setObjectName(_fromUtf8("lblDataEntrada"))
        self.lblHoraEntrada = QtGui.QLabel(self.grbDadosExtra)
        self.lblHoraEntrada.setGeometry(QtCore.QRect(140, 22, 91, 16))
        self.lblHoraEntrada.setObjectName(_fromUtf8("lblHoraEntrada"))
        self.txtHora = QtGui.QTimeEdit(self.grbDadosExtra)
        self.txtHora.setEnabled(False)
        self.txtHora.setGeometry(QtCore.QRect(140, 42, 118, 25))
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
        self.txtHora.setPalette(palette)
        self.txtHora.setObjectName(_fromUtf8("txtHora"))
        self.txtProduto = QtGui.QComboBox(self.grbDadosExtra)
        self.txtProduto.setEnabled(False)
        self.txtProduto.setGeometry(QtCore.QRect(530, 42, 241, 25))
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
        self.txtProduto.setPalette(palette)
        self.txtProduto.setObjectName(_fromUtf8("txtProduto"))
        self.txtData = QtGui.QDateEdit(self.grbDadosExtra)
        self.txtData.setEnabled(False)
        self.txtData.setGeometry(QtCore.QRect(10, 42, 110, 25))
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
        self.txtData.setPalette(palette)
        self.txtData.setCalendarPopup(True)
        self.txtData.setObjectName(_fromUtf8("txtData"))
        self.lblTipoCarga = QtGui.QLabel(self.grbDadosExtra)
        self.lblTipoCarga.setGeometry(QtCore.QRect(280, 20, 101, 16))
        self.lblTipoCarga.setObjectName(_fromUtf8("lblTipoCarga"))
        self.lblProduto = QtGui.QLabel(self.grbDadosExtra)
        self.lblProduto.setGeometry(QtCore.QRect(530, 20, 51, 16))
        self.lblProduto.setObjectName(_fromUtf8("lblProduto"))
        self.lblMarcaMotorista.setBuddy(self.txtMarcaMotorista)
        self.lblNomeMotorista.setBuddy(self.txtNomeMotorista)
        self.lblModeloMotorista.setBuddy(self.txtModeloMotorista)
        self.lblCodigoMotorista.setBuddy(self.txtidFuncionario)
        self.lblPlacaMotorista.setBuddy(self.txtPlacaMotorista)
        self.lblEstadosCliente.setBuddy(self.txtEstadosCliente)
        self.lblCepCliente.setBuddy(self.txtCepCliente)
        self.lblCidadesCliente.setBuddy(self.txtCidadesCliente)
        self.lblDataEntrada.setBuddy(self.txtData)
        self.lblHoraEntrada.setBuddy(self.txtHora)
        self.lblTipoCarga.setBuddy(self.txtTipoCarga)
        self.lblProduto.setBuddy(self.txtTipoCarga)

        self.retranslateUi(frmEntradaCaminhoaEmpresa)
        QtCore.QMetaObject.connectSlotsByName(frmEntradaCaminhoaEmpresa)

    def retranslateUi(self, frmEntradaCaminhoaEmpresa):
        frmEntradaCaminhoaEmpresa.setWindowTitle(_translate("frmEntradaCaminhoaEmpresa", "Entrada de Caminhões Empresa", None))
        self.grbDadosMotorista.setTitle(_translate("frmEntradaCaminhoaEmpresa", "Motorista", None))
        self.txtModeloMotorista.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Marca do Veiculo", None))
        self.txtModeloMotorista.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Campo de identicação do modelo do veiculo", None))
        self.lblMarcaMotorista.setText(_translate("frmEntradaCaminhoaEmpresa", "Marca", None))
        self.txtMarcaMotorista.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Marca do Veiculo", None))
        self.txtMarcaMotorista.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Campo do nome da marca do veiculo", None))
        self.txtNomeMotorista.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Nome Motorista", None))
        self.txtNomeMotorista.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Campo do nome do Motorista", None))
        self.lblNomeMotorista.setText(_translate("frmEntradaCaminhoaEmpresa", "Nome Motorista", None))
        self.txtPlacaMotorista.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Placa do Veiculo", None))
        self.txtPlacaMotorista.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Campo de identificação da placa do veiculo", None))
        self.txtPlacaMotorista.setInputMask(_translate("frmEntradaCaminhoaEmpresa", "nnn-0000; ", None))
        self.txtPlacaMotorista.setText(_translate("frmEntradaCaminhoaEmpresa", "-", None))
        self.lblModeloMotorista.setText(_translate("frmEntradaCaminhoaEmpresa", "Modelo", None))
        self.txtidFuncionario.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Codigo Motorista", None))
        self.txtidFuncionario.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Campo do Codigo de identificação do Motorista", None))
        self.lblCodigoMotorista.setText(_translate("frmEntradaCaminhoaEmpresa", "Codigo Motorista", None))
        self.lblPlacaMotorista.setText(_translate("frmEntradaCaminhoaEmpresa", "Placa", None))
        self.grbBotoes.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Grupo de botões referente as suas funções", None))
        self.btnDeletar.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Botão de cancelar a operação iniciada", None))
        self.btnDeletar.setText(_translate("frmEntradaCaminhoaEmpresa", "Deletar", None))
        self.btnCancelar.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Botão de cancelar a operação iniciada", None))
        self.btnCancelar.setText(_translate("frmEntradaCaminhoaEmpresa", "Cancelar", None))
        self.btnSalvar.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Botão para salvar um novo registro", None))
        self.btnSalvar.setText(_translate("frmEntradaCaminhoaEmpresa", "Salvar", None))
        self.btnNovo.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Botão de Criação de um novo registro", None))
        self.btnNovo.setText(_translate("frmEntradaCaminhoaEmpresa", "Novo", None))
        self.btnEditar.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Botão para salvar um novo registro", None))
        self.btnEditar.setText(_translate("frmEntradaCaminhoaEmpresa", "Editar", None))
        self.grbDadosOrigem.setTitle(_translate("frmEntradaCaminhoaEmpresa", "Dados Origem", None))
        self.lblEstadosCliente.setText(_translate("frmEntradaCaminhoaEmpresa", "Estado", None))
        self.txtEstadosCliente.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Estado Cliente", None))
        self.txtEstadosCliente.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Campo do nome do estado de localização do endereço", None))
        self.lblCepCliente.setText(_translate("frmEntradaCaminhoaEmpresa", "CEP", None))
        self.txtCidadesCliente.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Cidade Cliente", None))
        self.txtCidadesCliente.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Campo do nome da cidade referente a localização do endereço dentro do estado", None))
        self.lblCidadesCliente.setText(_translate("frmEntradaCaminhoaEmpresa", "Cidade", None))
        self.txtCepCliente.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "CEP Cliente", None))
        self.txtCepCliente.setWhatsThis(_translate("frmEntradaCaminhoaEmpresa", "Campo de CEP referente a identificação da cidade e qual estado pertence", None))
        self.grbDadosDestino.setTitle(_translate("frmEntradaCaminhoaEmpresa", "Dados Destino", None))
        self.lblSetor.setText(_translate("frmEntradaCaminhoaEmpresa", "Setor", None))
        self.lblTipoAfazer.setText(_translate("frmEntradaCaminhoaEmpresa", "Tipo de Afazer", None))
        self.grbDadosExtra.setTitle(_translate("frmEntradaCaminhoaEmpresa", "Dados Extra", None))
        self.txtTipoCarga.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Tipo de Carga", None))
        self.lblDataEntrada.setText(_translate("frmEntradaCaminhoaEmpresa", "Data Entrada", None))
        self.lblHoraEntrada.setText(_translate("frmEntradaCaminhoaEmpresa", "Hora Entrada", None))
        self.txtHora.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Hora Entrada", None))
        self.txtProduto.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Tipo de Carga", None))
        self.txtData.setToolTip(_translate("frmEntradaCaminhoaEmpresa", "Data Entrada", None))
        self.lblTipoCarga.setText(_translate("frmEntradaCaminhoaEmpresa", "Tipo de Carga", None))
        self.lblProduto.setText(_translate("frmEntradaCaminhoaEmpresa", "Produto", None))


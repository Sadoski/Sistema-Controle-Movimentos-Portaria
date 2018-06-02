# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmSaidaFuncionario.ui'
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

class Ui_frmSaidaFuncionario(object):
    def setupUi(self, frmSaidaFuncionario):
        frmSaidaFuncionario.setObjectName(_fromUtf8("frmSaidaFuncionario"))
        frmSaidaFuncionario.resize(667, 247)
        font = QtGui.QFont()
        font.setPointSize(11)
        frmSaidaFuncionario.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/carregamento.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSaidaFuncionario.setWindowIcon(icon)
        frmSaidaFuncionario.setSizeGripEnabled(True)
        frmSaidaFuncionario.setModal(True)

        self.grbDadosSaidaFuncionario = QtGui.QGroupBox(frmSaidaFuncionario)
        self.grbDadosSaidaFuncionario.setEnabled(False)
        self.grbDadosSaidaFuncionario.setGeometry(QtCore.QRect(5, 10, 657, 171))
        self.grbDadosSaidaFuncionario.setTitle(_fromUtf8(""))
        self.grbDadosSaidaFuncionario.setObjectName(_fromUtf8("grbDadosSaidaFuncionario"))

        self.lblDataSaida = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblDataSaida.setGeometry(QtCore.QRect(10, 10, 81, 19))
        self.lblDataSaida.setObjectName(_fromUtf8("lblDataSaida"))

        self.lblCargo = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblCargo.setGeometry(QtCore.QRect(227, 110, 66, 19))
        self.lblCargo.setObjectName(_fromUtf8("lblCargo"))

        self.lblNomeFuncionario = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblNomeFuncionario.setGeometry(QtCore.QRect(179, 64, 151, 19))
        self.lblNomeFuncionario.setObjectName(_fromUtf8("lblNomeFuncionario"))

        self.lblCodigoFuncionario = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblCodigoFuncionario.setGeometry(QtCore.QRect(7, 64, 121, 19))
        self.lblCodigoFuncionario.setObjectName(_fromUtf8("lblCodigoFuncionario"))

        self.txtidFuncionario = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtidFuncionario.setGeometry(QtCore.QRect(7, 84, 161, 25))
        self.txtidFuncionario.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtidFuncionario.setMaxLength(11)
        self.txtidFuncionario.setObjectName(_fromUtf8("txtidFuncionario"))

        self.txtNomeFuncionario = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtNomeFuncionario.setEnabled(False)
        self.txtNomeFuncionario.setGeometry(QtCore.QRect(179, 84, 421, 25))
        self.txtNomeFuncionario.setMaxLength(70)
        self.txtNomeFuncionario.setObjectName(_fromUtf8("txtNomeFuncionario"))

        self.lblSetor = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblSetor.setGeometry(QtCore.QRect(7, 110, 66, 19))
        self.lblSetor.setObjectName(_fromUtf8("lblSetor"))

        self.txtCargos = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtCargos.setEnabled(False)
        self.txtCargos.setGeometry(QtCore.QRect(227, 130, 211, 25))
        self.txtCargos.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCargos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtCargos.setMaxLength(50)
        self.txtCargos.setObjectName(_fromUtf8("txtCargos"))

        self.btnPesquisar = QtGui.QPushButton(self.grbDadosSaidaFuncionario)
        self.btnPesquisar.setGeometry(QtCore.QRect(613, 82, 31, 28))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.lblHoraSaida = QtGui.QLabel(self.grbDadosSaidaFuncionario)
        self.lblHoraSaida.setGeometry(QtCore.QRect(150, 10, 81, 19))
        self.lblHoraSaida.setObjectName(_fromUtf8("lblHoraSaida"))

        self.txtHoraSaida = QtGui.QTimeEdit(self.grbDadosSaidaFuncionario)
        self.txtHoraSaida.setTime(QtCore.QTime.currentTime())
        self.txtHoraSaida.setGeometry(QtCore.QRect(150, 30, 118, 25))
        self.txtHoraSaida.setObjectName(_fromUtf8("txtHoraSaida"))

        self.txtDataSaida = QtGui.QDateEdit(self.grbDadosSaidaFuncionario)
        self.txtDataSaida.setDate(QtCore.QDate.currentDate())
        self.txtDataSaida.setGeometry(QtCore.QRect(10, 30, 110, 25))
        self.txtDataSaida.setCalendarPopup(True)
        self.txtDataSaida.setObjectName(_fromUtf8("txtDataSaida"))

        self.txtSetor = QtGui.QLineEdit(self.grbDadosSaidaFuncionario)
        self.txtSetor.setEnabled(False)
        self.txtSetor.setGeometry(QtCore.QRect(7, 130, 211, 25))
        self.txtSetor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtSetor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtSetor.setMaxLength(50)
        self.txtSetor.setObjectName(_fromUtf8("txtSetor"))

        self.grbBotoes = QtGui.QGroupBox(frmSaidaFuncionario)
        self.grbBotoes.setGeometry(QtCore.QRect(5, 190, 656, 51))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(320, 12, 88, 27))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNovo.setIcon(icon1)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(420, 12, 88, 27))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon2)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))

        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(520, 12, 88, 27))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon3)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.lblDataSaida.setBuddy(self.txtDataSaida)
        self.lblCargo.setBuddy(self.txtCargos)
        self.lblNomeFuncionario.setBuddy(self.txtNomeFuncionario)
        self.lblCodigoFuncionario.setBuddy(self.txtidFuncionario)
        self.lblSetor.setBuddy(self.txtSetor)
        self.lblHoraSaida.setBuddy(self.txtHoraSaida)

        self.retranslateUi(frmSaidaFuncionario)
        QtCore.QMetaObject.connectSlotsByName(frmSaidaFuncionario)
        frmSaidaFuncionario.setTabOrder(self.txtidFuncionario, self.txtNomeFuncionario)
        frmSaidaFuncionario.setTabOrder(self.txtNomeFuncionario, self.btnPesquisar)
        frmSaidaFuncionario.setTabOrder(self.btnPesquisar, self.txtDataSaida)
        frmSaidaFuncionario.setTabOrder(self.txtDataSaida, self.txtHoraSaida)

    def retranslateUi(self, frmSaidaFuncionario):
        frmSaidaFuncionario.setWindowTitle(_translate("frmSaidaFuncionario", "Saida de Funcionarios em Horario de Serviço", None))
        self.lblDataSaida.setText(_translate("frmSaidaFuncionario", "Data Saida", None))
        self.lblCargo.setText(_translate("frmSaidaFuncionario", "Cargo", None))
        self.lblNomeFuncionario.setText(_translate("frmSaidaFuncionario", "Nome Funcionario", None))
        self.lblCodigoFuncionario.setText(_translate("frmSaidaFuncionario", "Codigo Funcionario", None))
        self.txtidFuncionario.setToolTip(_translate("frmSaidaFuncionario", "Codigo Funcionario", None))
        self.txtidFuncionario.setWhatsThis(_translate("frmSaidaFuncionario", "Campo do Codigo de identificação do Funcionario", None))
        self.txtNomeFuncionario.setToolTip(_translate("frmSaidaFuncionario", "Nome Funcionario", None))
        self.txtNomeFuncionario.setWhatsThis(_translate("frmSaidaFuncionario", "Campo do nome do funcionario", None))
        self.lblSetor.setText(_translate("frmSaidaFuncionario", "Setor", None))
        self.txtCargos.setToolTip(_translate("frmSaidaFuncionario", "Cargo", None))
        self.txtCargos.setWhatsThis(_translate("frmSaidaFuncionario", "Campo de descrição do cargo de trabalho do funcionario", None))
        self.lblHoraSaida.setText(_translate("frmSaidaFuncionario", "Hora Saida", None))
        self.txtHoraSaida.setToolTip(_translate("frmSaidaFuncionario", "Hora Saida", None))
        self.txtHoraSaida.setWhatsThis(_translate("frmSaidaFuncionario", "Campo de hora de saida", None))
        self.txtDataSaida.setToolTip(_translate("frmSaidaFuncionario", "Data Saida", None))
        self.txtDataSaida.setWhatsThis(_translate("frmSaidaFuncionario", "Campo de data da saida", None))
        self.txtSetor.setToolTip(_translate("frmSaidaFuncionario", "Setor", None))
        self.txtSetor.setWhatsThis(_translate("frmSaidaFuncionario", "Campo de descrição do setor de trabalho do funcionario", None))
        self.btnNovo.setToolTip(_translate("frmSaidaFuncionario", "Novo", None))
        self.btnNovo.setWhatsThis(_translate("frmSaidaFuncionario", "<html><head/><body><p>Botão para cadastrar uma novo registro da pessoa jurídica</p></body></html>", None))
        self.btnNovo.setText(_translate("frmSaidaFuncionario", "Novo", None))
        self.btnSalvar.setToolTip(_translate("frmSaidaFuncionario", "Salvar", None))
        self.btnSalvar.setWhatsThis(_translate("frmSaidaFuncionario", "<html><head/><body><p>Botão para salvar um novo registro da pessoa jurídica</p></body></html>", None))
        self.btnSalvar.setText(_translate("frmSaidaFuncionario", "Salvar", None))
        self.btnCancelar.setToolTip(_translate("frmSaidaFuncionario", "Cancelar", None))
        self.btnCancelar.setWhatsThis(_translate("frmSaidaFuncionario", "Botão para cancelar a operação ", None))
        self.btnCancelar.setText(_translate("frmSaidaFuncionario", "Cancelar", None))


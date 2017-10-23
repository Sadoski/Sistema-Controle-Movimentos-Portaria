# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmSobre.ui'
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

class Ui_frmSobre(object):
    def setupUi(self, frmSobre):
        frmSobre.setObjectName(_fromUtf8("frmSobre"))
        frmSobre.resize(462, 389)
        frmSobre.setSizeGripEnabled(False)
        frmSobre.setModal(True)

        self.btnOk = QtGui.QPushButton(frmSobre)
        self.btnOk.setGeometry(QtCore.QRect(370, 350, 75, 23))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))

        self.lblScmp = QtGui.QLabel(frmSobre)
        self.lblScmp.setGeometry(QtCore.QRect(150, 30, 171, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(8, 4, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 4, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblScmp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tw Cen MT Condensed"))

        font.setPointSize(80)
        self.lblScmp.setFont(font)
        self.lblScmp.setObjectName(_fromUtf8("lblScmp"))

        self.scrollInformacoes = QtGui.QScrollArea(frmSobre)
        self.scrollInformacoes.setGeometry(QtCore.QRect(10, 130, 441, 211))
        self.scrollInformacoes.setWidgetResizable(True)
        self.scrollInformacoes.setObjectName(_fromUtf8("scrollInformacoes"))

        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 209))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))

        self.lblMotivo1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblMotivo1.setGeometry(QtCore.QRect(10, 10, 421, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblMotivo1.setFont(font)
        self.lblMotivo1.setObjectName(_fromUtf8("lblMotivo1"))

        self.lblMotivo2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblMotivo2.setGeometry(QtCore.QRect(10, 30, 421, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblMotivo2.setFont(font)
        self.lblMotivo2.setObjectName(_fromUtf8("lblMotivo2"))

        self.lblMotivo3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblMotivo3.setGeometry(QtCore.QRect(10, 50, 421, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblMotivo3.setFont(font)
        self.lblMotivo3.setObjectName(_fromUtf8("lblMotivo3"))

        self.lblDesenvolvido = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblDesenvolvido.setGeometry(QtCore.QRect(10, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblDesenvolvido.setFont(font)
        self.lblDesenvolvido.setObjectName(_fromUtf8("lblDesenvolvido"))

        self.lblOrientador = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblOrientador.setGeometry(QtCore.QRect(10, 160, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblOrientador.setFont(font)
        self.lblOrientador.setObjectName(_fromUtf8("lblOrientador"))

        self.lblSupervisorEstagio = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblSupervisorEstagio.setGeometry(QtCore.QRect(10, 180, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblSupervisorEstagio.setFont(font)
        self.lblSupervisorEstagio.setObjectName(_fromUtf8("lblSupervisorEstagio"))

        self.lblEmail = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblEmail.setGeometry(QtCore.QRect(10, 120, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName(_fromUtf8("lblEmail"))

        self.lblCelular = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblCelular.setGeometry(QtCore.QRect(10, 100, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCelular.setFont(font)
        self.lblCelular.setObjectName(_fromUtf8("lblCelular"))

        self.lblJeffersonAparecidoSadoski = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblJeffersonAparecidoSadoski.setGeometry(QtCore.QRect(110, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblJeffersonAparecidoSadoski.setFont(font)
        self.lblJeffersonAparecidoSadoski.setObjectName(_fromUtf8("lblJeffersonAparecidoSadoski"))

        self.lblRodneyGasparPereira = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblRodneyGasparPereira.setGeometry(QtCore.QRect(77, 160, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblRodneyGasparPereira.setFont(font)
        self.lblRodneyGasparPereira.setObjectName(_fromUtf8("lblRodneyGasparPereira"))

        self.lblEmanoelFranciscoDosSantos = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblEmanoelFranciscoDosSantos.setGeometry(QtCore.QRect(118, 180, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblEmanoelFranciscoDosSantos.setFont(font)
        self.lblEmanoelFranciscoDosSantos.setObjectName(_fromUtf8("lblEmanoelFranciscoDosSantos"))

        self.lblJeffersonSadoskiHotmailCom = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblJeffersonSadoskiHotmailCom.setGeometry(QtCore.QRect(50, 120, 201, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 17, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 17, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblJeffersonSadoskiHotmailCom.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lblJeffersonSadoskiHotmailCom.setFont(font)
        self.lblJeffersonSadoskiHotmailCom.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lblJeffersonSadoskiHotmailCom.setMouseTracking(True)
        self.lblJeffersonSadoskiHotmailCom.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lblJeffersonSadoskiHotmailCom.setAcceptDrops(True)
        self.lblJeffersonSadoskiHotmailCom.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.lblJeffersonSadoskiHotmailCom.setObjectName(_fromUtf8("lblJeffersonSadoskiHotmailCom"))

        self.lbl5565996977055 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl5565996977055.setGeometry(QtCore.QRect(50, 100, 131, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl5565996977055.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl5565996977055.setFont(font)
        self.lbl5565996977055.setObjectName(_fromUtf8("lbl5565996977055"))

        self.scrollInformacoes.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(frmSobre)
        QtCore.QMetaObject.connectSlotsByName(frmSobre)

    def retranslateUi(self, frmSobre):
        frmSobre.setWindowTitle(_translate("frmSobre", "Sobre", None))
        self.btnOk.setText(_translate("frmSobre", "OK", None))
        self.lblScmp.setText(_translate("frmSobre", "SCMP", None))
        self.lblMotivo1.setText(_translate("frmSobre", "Sistema desenvolvido por  motivo de estagio na  empresa Apasa", None))
        self.lblMotivo2.setText(_translate("frmSobre", "Insdutrial e Agroflorestal LTDA para controle de movimento portaria", None))
        self.lblMotivo3.setText(_translate("frmSobre", "e obtenção de nota na Faculdade Integradas de Diamantino FID.", None))
        self.lblDesenvolvido.setText(_translate("frmSobre", "Desenvolvido por: ", None))
        self.lblOrientador.setText(_translate("frmSobre", "Orientador:", None))
        self.lblSupervisorEstagio.setText(_translate("frmSobre", "Supervisor Estagio: ", None))
        self.lblEmail.setText(_translate("frmSobre", "E-mail:", None))
        self.lblCelular.setText(_translate("frmSobre", "Celular:", None))
        self.lblJeffersonAparecidoSadoski.setText(_translate("frmSobre", "Jefferson Aparecido Sadoski", None))
        self.lblRodneyGasparPereira.setText(_translate("frmSobre", "Rodney Gaspar Pereira", None))
        self.lblEmanoelFranciscoDosSantos.setText(_translate("frmSobre", "Manoel Francisco dos Santos", None))
        self.lblJeffersonSadoskiHotmailCom.setText(_translate("frmSobre", "jefferson_sadoski@hotmail.com", None))
        self.lbl5565996977055.setText(_translate("frmSobre", "+55 65 99697-7055", None))


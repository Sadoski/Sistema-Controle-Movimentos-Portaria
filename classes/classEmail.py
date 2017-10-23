import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from telas.email import Ui_Email

class Email(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Email()
        self.ui.setupUi(self)

        self.ui.btnAnexo.clicked.connect(self.file_open)
        self.ui.txtNome.currentIndexChanged.connect(self.servidor)

    def servidor(self):
        if self.ui.txtNome.currentIndex() == 0:
            self.desativarSevidor()
            self.limparServidor()
            self.ui.txtServidor.setText("smtp.gmail.com")
            self.ui.txtAutenticacao.setText("SSL")
            self.ui.txtPorta.setText("465")

        elif self.ui.txtNome.currentIndex() == 1:
            self.desativarSevidor()
            self.limparServidor()
            self.ui.txtServidor.setText("smtp.gmail.com")
            self.ui.txtAutenticacao.setText("StartTLS")
            self.ui.txtPorta.setText("587")

        elif self.ui.txtNome.currentIndex() == 2:
            self.desativarSevidor()
            self.limparServidor()
            self.ui.txtServidor.setText("smtp.live.com")
            self.ui.txtAutenticacao.setText("SSL")
            self.ui.txtPorta.setText("465")

        elif self.ui.txtNome.currentIndex() == 3:
            self.desativarSevidor()
            self.limparServidor()
            self.ui.txtServidor.setText("smtp.mail.com")
            self.ui.txtAutenticacao.setText("SSL")
            self.ui.txtPorta.setText("465")

        elif self.ui.txtNome.currentIndex() == 4:
            self.desativarSevidor()
            self.ui.txtServidor.setText("smtp.live.com")
            self.ui.txtAutenticacao.setText("StartTLS")
            self.ui.txtPorta.setText("587")

        elif self.ui.txtNome.currentIndex() == 5:
            self.desativarSevidor()
            self.limparServidor()
            self.ui.txtServidor.setText("smtp.office365.com")
            self.ui.txtAutenticacao.setText("StartTLS")
            self.ui.txtPorta.setText("587")

        elif self.ui.txtNome.currentIndex() == 6:
            self.desativarSevidor()
            self.limparServidor()
            self.ui.txtServidor.setText("smtp.mail.yahoo.com")
            self.ui.txtAutenticacao.setText("SSL")
            self.ui.txtPorta.setText("465")

        elif self.ui.txtNome.currentIndex() == 7:
            self.limparServidor()
            self.ui.txtServidor.setEnabled(True)
            self.ui.txtAutenticacao.setEnabled(True)
            self.ui.txtPorta.setEnabled(True)
            self.ui.txtServidor.setFocus()

    def desativarSevidor(self):
        self.ui.txtServidor.setEnabled(False)
        self.ui.txtAutenticacao.setEnabled(False)
        self.ui.txtPorta.setEnabled(False)

    def limparServidor(self):
        self.ui.txtServidor.clear()
        self.ui.txtAutenticacao.clear()
        self.ui.txtPorta.clear()

    def enviar(self):
        servidor = self.ui.txtServidor.text()
        autenticacao = self.ui.txtAutenticacao.text()
        porta = self.ui.txtPorta.text()

        remetente = self.ui.txtRemetente.text()
        senha = self.ui.txtSenhaRemetente.text()
        destinatario = self.ui.txtDestinatario.text()

        assunto = self.ui.txtAssunto.text()
        texto = self.ui.txtTexto.textCursor()

        # Configura o servidor de envio (SMTP)
        server = smtplib.SMTP(servidor, porta)
        server.starttls()
        server.login(remetente, senha)

        # Cria o documento com várias partes
        msg = MIMEMultipart()
        msg["From"] = remetente
        msg["To"] = destinatario
        msg["Subject"] = assunto

        with open('img.jpg', 'rb') as f:
            msgImg = MIMEImage(f.read(), name=self.name)
        msg.attach(msgImg)

        # Anexa o corpo do texto
        msgText = MIMEText('<b>{}</b><br><img src="cid:{}"><br>'.format(texto, self.name), 'html')
        msg.attach(msgText)

        # Envia!
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        if name != '':
            link = open(name, 'rb')
            print(link)


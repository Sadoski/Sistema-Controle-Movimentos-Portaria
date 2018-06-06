import csv
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class UsuarioCSV():

    lista = []

    def __init__(self, dados):
        self.findAll(dados)
        self.dir = self.salvar()
        self.gerarCsv()


    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Nome': pessoa[1], 'Sobrenome': pessoa[2], 'Setor': pessoa[3], 'Cargo': pessoa[4], 'Login': pessoa[5]}
            self.lista.append(dados)
        return self.lista

    def gerarCsv(self):

        listaParaGerarCsv = []
        for dad in self.lista:

            listaInterna = []
            listaInterna.append(dad['Codigo'])
            listaInterna.append(dad['Nome'] + ' ' + dad['Sobrenome'])
            listaInterna.append(dad['Setor'])
            listaInterna.append(dad['Cargo'])
            listaInterna.append(dad['Login'])

            listaParaGerarCsv.append(listaInterna)

        if self.dir:
            with open(self.dir, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Relatório Usuario'])
                spamwriter.writerow(['Codigo', 'Nome', 'Setor', 'Cargo', 'Login'])
                for linha in listaParaGerarCsv:
                    spamwriter.writerow(linha)

    def salvar(self):

        diretorioBase = ''

        if os.name == 'nt':
            diretorioBase = 'C' + ':'
        else:
            diretorioBase = os.getenv("HOME")

        caminhoAbsoluto = diretorioBase + os.sep + 'SCMP' + os.sep + 'Relatório' + os.sep + 'csv' + os.sep

        if not os.path.exists(caminhoAbsoluto):
            os.makedirs(caminhoAbsoluto)

        name = QFileDialog.getSaveFileName(None, 'Salvar', caminhoAbsoluto, 'CSV (*.csv)')

        return name
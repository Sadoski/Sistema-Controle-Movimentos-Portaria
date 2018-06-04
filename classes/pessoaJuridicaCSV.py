import csv
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class RelatorioPessoaJuridicaCSV():

    lista = []

    def __init__(self, dados):
        self.findAll(dados)
        self.dir = self.salvar()
        self.gerarCsv()


    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Razão Social': pessoa[1], 'Fantasia': pessoa[2], 'CNPJ': pessoa[3], 'Ins. Estadual': pessoa[4], 'Endereco': pessoa[5], 'Numero': pessoa[6], 'Complemento': pessoa[7], 'Bairro': pessoa[8], 'Cidade': pessoa[9], 'Estado': pessoa[10], 'CEP': pessoa[11], 'Site': pessoa[12]}
            self.lista.append(dados)
        return self.lista

    def gerarCsv(self):

        listaParaGerarCsv = []
        for dad in self.lista:

            listaInterna = []
            listaInterna.append(dad['Codigo'])
            listaInterna.append(dad['Razão Social'])
            listaInterna.append(dad['Fantasia'])
            listaInterna.append(dad['CNPJ'])
            listaInterna.append(dad['Ins. Estadual'])
            listaInterna.append(dad['Endereco'])
            listaInterna.append(dad['Numero'])
            listaInterna.append(dad['Complemento'])
            listaInterna.append(dad['Bairro'])
            listaInterna.append(dad['Cidade'])
            listaInterna.append(dad['Estado'])
            listaInterna.append(dad['CEP'])
            listaInterna.append(dad['Site'])
            
            listaParaGerarCsv.append(listaInterna)

        if self.dir:
            with open(self.dir, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Relatório Pessoa Juridica'])
                spamwriter.writerow(['Codigo', 'Razão Social', 'Fantasia', 'CNPJ', 'Ins. Estadual', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP', 'Site'])
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
import csv
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class FornecedorCSV():

    lista = []

    def __init__(self, dados):
        self.findAll(dados)
        self.dir = self.salvar()
        self.gerarCsv()


    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Pessoa': pessoa[1], 'Razão Social': pessoa[2], 'Fantasia': pessoa[3], 'CNPJ': pessoa[4], 'Ins. Estadual': pessoa[5], 'Expeditor': pessoa[6], 'UF': pessoa[7], 'Aniversario': pessoa[8], 'Endereco': pessoa[9], 'Numero': pessoa[10], 'Complemento': pessoa[11], 'Bairro': pessoa[12], 'Cidade': pessoa[13], 'Estado': pessoa[14], 'CEP': pessoa[15], 'Site': pessoa[16], 'Obs.': pessoa[17], 'Situação': pessoa[18]}
            self.lista.append(dados)
        return self.lista

    def gerarCsv(self):

        listaParaGerarCsv = []
        for dad in self.lista:

            listaInterna = []
            listaInterna.append(dad['Codigo'])
            listaInterna.append(dad['Pessoa'])
            listaInterna.append(dad['Razão Social'])
            listaInterna.append(dad['Fantasia'])
            listaInterna.append(str(dad['CNPJ']))
            listaInterna.append(dad['Ins. Estadual'])
            listaInterna.append(dad['Expeditor'])
            listaInterna.append(dad['UF'])
            listaInterna.append(dad['Aniversario'])
            listaInterna.append(dad['Endereco'])
            listaInterna.append(dad['Numero'])
            listaInterna.append(dad['Complemento'])
            listaInterna.append(dad['Bairro'])
            listaInterna.append(dad['Cidade'])
            listaInterna.append(dad['Estado'])
            listaInterna.append(dad['CEP'])
            listaInterna.append(dad['Site'])
            listaInterna.append(dad['Obs.'])
            if dad['Situação'] == 1 :
                da = 'Ativo'
            else:
                da = 'Inativo'
            listaInterna.append(da)
            
            listaParaGerarCsv.append(listaInterna)

        if self.dir:
            with open(self.dir, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Relatório Fornecedor'])
                spamwriter.writerow(['Codigo', 'Pessoa', 'Nome/Razão Social', 'Sobrenome/Fantasia', 'CPF/CNPJ', 'RG/Ins. Estadual', 'Expeditor', 'UF', 'Aniversario', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP', 'Site', 'Obs.' 'Situação'])
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
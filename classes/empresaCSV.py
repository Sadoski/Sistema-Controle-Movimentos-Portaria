import csv
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class EmpresaCSV():

    lista = []

    def __init__(self, dados):
        self.findAll(dados)
        self.dir = self.salvar()
        self.gerarCsv()


    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Razão Social': pessoa[1], 'Fantasia': pessoa[2], 'CNPJ': pessoa[3], 'Ins. Estadual': pessoa[4], 'Ins. Municipal': pessoa[5], 'Tipo Empresa': pessoa[6], 'Endereco': pessoa[7], 'Numero': pessoa[8], 'Complemento': pessoa[9], 'Bairro': pessoa[10], 'Cidade': pessoa[11], 'Estado': pessoa[12], 'CEP': pessoa[13], 'Situação': pessoa[14], 'CNAE': pessoa[15]}
            self.lista.append(dados)
        return self.lista

    def gerarCsv(self):

        listaParaGerarCsv = []
        for dad in self.lista:

            listaInterna = []
            listaInterna.append(dad['Codigo'])
            listaInterna.append(dad['Razão Social'])
            listaInterna.append(dad['Fantasia'])
            listaInterna.append(str(dad['CNPJ']))
            listaInterna.append(dad['Ins. Estadual'])
            listaInterna.append(dad['Ins. Municipal'])
            listaInterna.append(dad['Tipo Empresa'])
            listaInterna.append(dad['Endereco'])
            listaInterna.append(dad['Numero'])
            listaInterna.append(dad['Complemento'])
            listaInterna.append(dad['Bairro'])
            listaInterna.append(dad['Cidade'])
            listaInterna.append(dad['Estado'])
            listaInterna.append(dad['CEP'])
            if dad['Situação'] == 1 :
                da = 'Ativo'
            else:
                da = 'Inativo'
            listaInterna.append(da)
            listaInterna.append(dad['CNAE'])
            
            listaParaGerarCsv.append(listaInterna)

        if self.dir:
            with open(self.dir, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Relatório Empresa'])
                spamwriter.writerow(['Codigo', 'Razão Social', 'Fantasia', 'CNPJ', 'Ins. Estadual', 'Ins. Municipal', 'Tipo Empresa', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP', 'Situação', 'CNAE'])
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
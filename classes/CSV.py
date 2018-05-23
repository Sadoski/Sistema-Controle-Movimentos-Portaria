import csv
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao


class RelatorioPessoaFisicaCSV():

    lista = []

    def __init__(self, dados):
        self.findAll(dados)
        self.dir = self.salvar()
        self.gerarCsv()


    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Nome': pessoa[1], 'Sobrenome': pessoa[2], 'CPF': pessoa[3], 'RG': pessoa[4], 'Expeditor': pessoa[5], 'UF': pessoa[6], 'Aniversario': pessoa[7], 'Genero' : pessoa[8], 'Mae': pessoa[9], 'Pai': pessoa[10], 'Endereco': pessoa[11], 'Numero': pessoa[12], 'Complemento': pessoa[13], 'Bairro': pessoa[14], 'Cidade': pessoa[15], 'Estado': pessoa[16], 'CEP': pessoa[17]}
            self.lista.append(dados)
        return self.lista

    def gerarCsv(self):

        listaParaGerarCsv = []
        for dad in self.lista:

            listaInterna = []
            listaInterna.append(dad['Codigo'])
            listaInterna.append(dad['Nome'])
            listaInterna.append(dad['Sobrenome'])
            listaInterna.append(dad['CPF'])
            listaInterna.append(dad['RG'])
            listaInterna.append(dad['Expeditor'])
            listaInterna.append(dad['UF'])
            listaInterna.append(dad['Aniversario'])
            listaInterna.append(dad['Genero'])
            listaInterna.append(dad['Mae'])
            listaInterna.append(dad['Pai'])
            listaInterna.append(dad['Endereco'])
            listaInterna.append(dad['Numero'])
            listaInterna.append(dad['Complemento'])
            listaInterna.append(dad['Bairro'])
            listaInterna.append(dad['Cidade'])
            listaInterna.append(dad['Estado'])
            listaInterna.append(dad['CEP'])
            
            listaParaGerarCsv.append(listaInterna)

        if self.dir:
            with open(self.dir, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Relatório Pessoa Fisica'])
                spamwriter.writerow(['Codigo', 'Nome', 'Sobrenome', 'CPF', 'RG', 'Expeditor', 'UF', 'Aniversario', 'Gênero', 'Mãe', 'Pai', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP'])
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
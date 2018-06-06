import csv
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo


class NotasFiscaisCSV():

    lista = []

    def __init__(self, dados):
        self.findAll(dados)
        self.dir = self.salvar()
        self.gerarCsv()


    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Tipo': pessoa[1], 'Serie': pessoa[2], 'Nº NF': pessoa[3], 'Fornecedor': pessoa[4], 'Motorista': pessoa[5], 'Data Emissão': pessoa[6], 'Data Entrada': pessoa[7], 'Valor Total': pessoa[8], 'Valor ICMS': pessoa[9], 'Valor IPI': pessoa[10], 'Alicota ICMS': pessoa[11], 'Alicota IPI': pessoa[12]}
            self.lista.append(dados)
        return self.lista

    def gerarCsv(self):
        nf = NotaFiscalRomanieo()
        listaParaGerarCsv = []
        for dad in self.lista:

            listaInterna = []
            listaInterna.append(dad['Codigo'])
            listaInterna.append(dad['Tipo'])
            listaInterna.append(dad['Serie'])
            listaInterna.append(dad['Nº NF'])
            listaInterna.append(nf.pesquisarForneRel(dad['Fornecedor']))
            listaInterna.append(nf.pesquisarMotoRel(dad['Motorista']))
            listaInterna.append(dad['Data Emissão'])
            listaInterna.append(dad['Data Entrada'])
            listaInterna.append(dad['Valor Total'])
            listaInterna.append(dad['Valor ICMS'])
            listaInterna.append(dad['Valor IPI'])
            listaInterna.append(dad['Alicota ICMS'])
            listaInterna.append(dad['Alicota IPI'])
            listaInterna.append(nf.pesquisarProdRel(dad['Codigo']))

            listaParaGerarCsv.append(listaInterna)

        if self.dir:
            with open(self.dir, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Relatório Notas Fiscais'])
                spamwriter.writerow(['Codigo', 'Tipo', 'Serie', 'Nº NF', 'Fornecedor', 'Motorista', 'Data Emissão', 'Data Entrada', 'Valor Total', 'Valor ICMS', 'Valor IPI', 'Alicota ICMS', 'Alicota IPI', 'Produto'])
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
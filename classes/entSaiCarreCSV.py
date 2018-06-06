import csv
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from dao.carregamentoSaidaDao import CarregamentoSaidaDao
from dao.notaFiscalRomaneioDao import NotaFiscalRomanieo


class EntSaiCarreCSV():

    lista = []

    def __init__(self, dados):
        self.findAll(dados)
        self.dir = self.salvar()
        self.gerarCsv()


    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Data Entrada': pessoa[1], 'Hora Entrada': pessoa[2], 'Data Saida': pessoa[3], 'Hora Saida': pessoa[4], 'Carga': pessoa[5], 'Produto': pessoa[6], 'Motorista': pessoa[7], 'Modelo': pessoa[8], 'Marca': pessoa[9], 'Placa': pessoa[10],  'Cliente': pessoa[11]}
            self.lista.append(dados)
        return self.lista

    def gerarCsv(self):
        entSaiDao = CarregamentoSaidaDao()
        listaParaGerarCsv = []
        for dad in self.lista:

            listaInterna = []
            listaInterna.append(dad['Codigo'])
            listaInterna.append(dad['Data Entrada'])
            listaInterna.append(dad['Hora Entrada'])
            listaInterna.append(dad['Data Saida'])
            listaInterna.append(dad['Hora Saida'])
            listaInterna.append(dad['Carga'])
            listaInterna.append(dad['Produto'])
            listaInterna.append(entSaiDao.pesquisarMotoristaCarreRel(dad['Motorista']))
            listaInterna.append(dad['Marca'])
            listaInterna.append(dad['Modelo'])
            listaInterna.append(dad['Placa'])
            listaInterna.append(entSaiDao.pesquisarClienteCarreRel(dad['Cliente']))

            listaParaGerarCsv.append(listaInterna)

        if self.dir:
            with open(self.dir, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Relatório Notas Fiscais'])
                spamwriter.writerow(['Codigo', 'Data Entrada', 'Hora Entrada', 'Data Saida', 'Hora Saida', 'Carga', 'Produto', 'Motorista', 'Marca', 'Modelo', 'Placa', 'Cliente'])
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
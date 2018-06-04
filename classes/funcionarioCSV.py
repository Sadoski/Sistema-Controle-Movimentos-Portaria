import csv
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class FuncionarioCSV():

    lista = []

    def __init__(self, dados):
        self.findAll(dados)
        self.dir = self.salvar()
        self.gerarCsv()


    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Nome': pessoa[1], 'Sobrenome': pessoa[2], 'CPF': pessoa[3], 'RG': pessoa[4], 'Expeditor': pessoa[5], 'UF': pessoa[6], 'Aniversario': pessoa[7], 'Endereco': pessoa[8], 'Numero': pessoa[9], 'Complemento': pessoa[10], 'Bairro': pessoa[11], 'Cidade': pessoa[12], 'Estado': pessoa[13], 'CEP': pessoa[14], 'Genero' : pessoa[15], 'Mae': pessoa[16], 'Pai': pessoa[17], 'Admissão': pessoa[18], 'Demissão': pessoa[19], 'Nº Carteira': pessoa[20], 'Serie': pessoa[21], 'UFF': pessoa[22], 'Emissão': pessoa[23], 'PIS/PASEP': pessoa[24], 'Estado Civil': pessoa[25], 'Deficiencia': pessoa[26], 'Categoria': pessoa[27], 'Cargo': pessoa[28], 'Setor': pessoa[29], 'Obs.': pessoa[30], 'Jornada': pessoa[31], 'Situação': pessoa[32]}
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
            listaInterna.append(dad['Endereco'])
            listaInterna.append(dad['Numero'])
            listaInterna.append(dad['Complemento'])
            listaInterna.append(dad['Bairro'])
            listaInterna.append(dad['Cidade'])
            listaInterna.append(dad['Estado'])
            listaInterna.append(dad['CEP'])
            listaInterna.append(dad['Genero'])
            listaInterna.append(dad['Mae'])
            listaInterna.append(dad['Pai'])
            listaInterna.append(dad['Admissão'])
            listaInterna.append(dad['Demissão'])
            listaInterna.append(dad['Nº Carteira'])
            listaInterna.append(dad['Serie'])
            listaInterna.append(dad['UFF'])
            listaInterna.append(dad['Emissão'])
            listaInterna.append(dad['PIS/PASEP'])
            listaInterna.append(dad['Estado Civil'])
            listaInterna.append(dad['Deficiencia'])
            listaInterna.append(dad['Categoria'])
            listaInterna.append(dad['Cargo'])
            listaInterna.append(dad['Setor'])
            listaInterna.append(dad['Obs.'])
            listaInterna.append(dad['Jornada'])
            if dad['Situação'] == 1 :
                da = 'Ativo'
            else:
                da = 'Inativo'
            listaInterna.append(da)

            listaParaGerarCsv.append(listaInterna)

        if self.dir:
            with open(self.dir, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Relatório Funcionario'])
                spamwriter.writerow(['Codigo', 'Nome', 'Sobrenome', 'CPF', 'RG', 'Expeditor', 'UF', 'Aniversario', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP', 'Gênero', 'Mãe', 'Pai', 'Admissão', 'Demissão', 'Nº Carteira', 'Serie', 'UF', 'Emissão', 'PIS/PASEP', 'Estado Civil', 'Deficiencia', 'Categoria', 'Cargo', 'Setor', 'Obs.', 'Jornada', 'Situação'])
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
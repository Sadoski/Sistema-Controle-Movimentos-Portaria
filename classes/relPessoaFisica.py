class RelPessoaFisica:
    lista = []
    def findAll(self, pessoaFisica):
        for pessoa in pessoaFisica:
            dados = {'Codigo': pessoa[0], 'Nome': pessoa[1], 'Sobrenome': pessoa[2], 'CPF': pessoa[3], 'RG': pessoa[4], 'Expeditor': pessoa[5], 'UF': pessoa[6], 'Mãe': pessoa[7], 'Pai': pessoa[8], 'Endereço': pessoa[9], 'Número': pessoa[10], 'Bairro': pessoa[11], 'Cidade': pessoa[12], 'CEP': pessoa[13], 'Estado': pessoa[14]}]
            lista.append(dados)
        return lista

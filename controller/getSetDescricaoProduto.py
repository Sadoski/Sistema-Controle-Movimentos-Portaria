class DescricaoProduto():
    def __init__(self, idDescricao, cargaProduto, notaFiscal, unidade, quantidade, valor):
        self.__idDescricao = idDescricao
        self.__cargaProduto = cargaProduto
        self.__notaFiscal = notaFiscal
        self.__unidade = unidade
        self.__quantidade = quantidade
        self.__valor = valor

    @property
    def getIdDescricao(self):
        return self.__idDescricao

    @getIdDescricao.setter
    def setIdDescricao(self, idDescricao):
        self.__idDescricao = idDescricao

    @property
    def getCargaProduto(self):
        return self.__cargaProduto

    @getCargaProduto.setter
    def setCargaProduto(self, cargaProduto):
        self.__cargaProduto = cargaProduto

    @property
    def getNotaFiscal(self):
        return self.__notaFiscal

    @getNotaFiscal.setter
    def setNotaFiscal(self, notaFiscal):
        self.__notaFiscalo = notaFiscal

    @property
    def getUnidade(self):
        return self.__unidade

    @getUnidade.setter
    def setUnidade(self, unidade):
        self.__unidade = unidade

    @property
    def getQuantidade(self):
        return self.__quantidade

    @getQuantidade.setter
    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def getValor(self):
        return self.__valor

    @getValor.setter
    def setValor(self, valor):
        self.__valor = valor
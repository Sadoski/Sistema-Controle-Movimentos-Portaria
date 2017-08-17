class NotaFiscal():
    def __init__(self, idNotaFiscal, idFornecedor, idEmpresa, idMotorista, numNotaFiscal, dataEmissao, valorTotal):
        self.__idNotaFiscal = idNotaFiscal
        self.__idFornecedor = idFornecedor
        self.__idEmpresa = idEmpresa
        self.__idMotorista = idMotorista
        self.__numNotaFiscal = numNotaFiscal
        self.__dataEmissao = dataEmissao
        self.__valorTotal = valorTotal

    @property
    def getIdFornecedor(self):
        return self.__idFornecedor

    @getIdFornecedor.setter
    def setIdFornecedor(self, idFornecedor):
        self.__idFornecedor = idFornecedor

    @property
    def getIdEmpresa(self):
        return self.__idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self.__idEmpresa = idEmpresa

    @property
    def getIdMotorista(self):
        return self.__idMotorista

    @getIdMotorista.setter
    def setIdMotorista(self, idMotorista):
        self.__idMotorista = idMotorista

    @property
    def getNumNotaFiscal(self):
        return self.__numNotaFiscal

    @getNumNotaFiscal.setter
    def setNumNotaFiscal(self, numNotaFiscal):
        self.__numNotaFiscal = numNotaFiscal

    @property
    def getDataEmissao(self):
        return self.__dataEmissao

    @getDataEmissao.setter
    def setDataEmissao(self, dataEmissao):
        self.__dataEmissao = dataEmissao

    @property
    def getValorTotal(self):
        return self.__valorTotal

    @getValorTotal.setter
    def setValorTotal(self, valorTotal):
        self.__valorTotal = valorTotal
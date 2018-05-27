class NotaFiscal():
    def __init__(self, idNotaFiscal, idFornecedor, idTipoNf, idMotorista, serie, modelo, numNotaFiscal, dataEmissao, dataEntrada, valorTotal):
        self.__idNotaFiscal = idNotaFiscal
        self.__idFornecedor = idFornecedor
        self.__idTipoNf = idTipoNf
        self.__idMotorista = idMotorista
        self.__serie = serie
        self.__modelo = modelo
        self.__numNotaFiscal = numNotaFiscal
        self.__dataEmissao = dataEmissao
        self.__dataEntrada = dataEntrada
        self.__valorTotal = valorTotal

    @property
    def getIdFornecedor(self):
        return self.__idFornecedor

    @getIdFornecedor.setter
    def setIdFornecedor(self, idFornecedor):
        self.__idFornecedor = idFornecedor

    @property
    def getIdTipoNf(self):
        return self.__idTipoNf

    @getIdTipoNf.setter
    def setIdTipoNf(self, tipoNf):
        self.__idTipoNf = tipoNf

    @property
    def getIdMotorista(self):
        return self.__idMotorista

    @getIdMotorista.setter
    def setIdMotorista(self, idMotorista):
        self.__idMotorista = idMotorista

    @property
    def getSerie(self):
        return self.__serie

    @getSerie.setter
    def setSerie(self, serie):
        self.__serie = serie

    @property
    def getModelo(self):
        return self.__modelo

    @getModelo.setter
    def setModelo(self, modelo):
        self.__modelo = modelo

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
    def getDataEntrada(self):
        return self.__dataEntrada

    @getDataEntrada.setter
    def setDataEntrada(self, dataEntrada):
        self.__dataEntrada = dataEntrada

    @property
    def getValorTotal(self):
        return self.__valorTotal

    @getValorTotal.setter
    def setValorTotal(self, valorTotal):
        self.__valorTotal = valorTotal
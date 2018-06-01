class NotaFiscal():
    def __init__(self, idNotaFiscal, idFornecedor, fornecedor, idTipoNf, idMotorista, motorista, serie, numNotaFiscal, dataEmissao, dataEntrada, valorTotal, valorIcms, valorIpi, alicotaIcms, alicotaIpi):
        self.__idNotaFiscal = idNotaFiscal
        self.__idFornecedor = idFornecedor
        self.__fornecedor = fornecedor
        self.__idTipoNf = idTipoNf
        self.__idMotorista = idMotorista
        self.__motorista = motorista
        self.__serie = serie
        self.__numNotaFiscal = numNotaFiscal
        self.__dataEmissao = dataEmissao
        self.__dataEntrada = dataEntrada
        self.__valorTotal = valorTotal
        self.__valorIcms = valorIcms
        self.__valorIpi = valorIpi
        self.__alicotaIcms = alicotaIcms
        self.__alicotaIpi = alicotaIpi

    @property
    def getIdNotaFiscal(self):
        return self.__idNotaFiscal

    @getIdNotaFiscal.setter
    def setIdNotaFiscal(self, idNotaFiscal):
        self.__idNotaFiscal = idNotaFiscal

    @property
    def getIdFornecedor(self):
        return self.__idFornecedor

    @getIdFornecedor.setter
    def setIdFornecedor(self, idFornecedor):
        self.__idFornecedor = idFornecedor

    @property
    def getFornecedor(self):
        return self.__fornecedor

    @getFornecedor.setter
    def setFornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

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
    def getMotorista(self):
        return self.__motorista

    @getMotorista.setter
    def setMotorista(self, motorista):
        self.__motorista = motorista

    @property
    def getSerie(self):
        return self.__serie

    @getSerie.setter
    def setSerie(self, serie):
        self.__serie = serie

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

    @property
    def getValorIcms(self):
        return self.__valorIcms

    @getValorIcms.setter
    def setValorIcms(self, valorIcms):
        self.__valorIcms = valorIcms

    @property
    def getValorIpi(self):
        return self.__valorIpi

    @getValorIpi.setter
    def setValorIpi(self, valorIpi):
        self.__valorIpi = valorIpi

    @property
    def getAlicotaIcms(self):
        return self.__alicotaIcms

    @getAlicotaIcms.setter
    def setAlicotaIcms(self, alicotaIcms):
        self.__alicotaIcms = alicotaIcms

    @property
    def getAlicotaIpi(self):
        return self.__alicotaIpi

    @getAlicotaIpi.setter
    def setAlicotaIpi(self, alicotaIpi):
        self.__alicotaIpi = alicotaIpi
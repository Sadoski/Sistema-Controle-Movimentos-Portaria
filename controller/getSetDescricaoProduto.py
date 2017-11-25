class DescricaoProduto():
    def __init__(self, idDescricao, notaFiscal, codigoNosso, codigoProduto, produto, ncm, cst, cfop, un, qtd, valorUnitario, valorTotal, valorIcms, valorIpi, alicotaIcms, alicotaIpi):
        self.__idDescricao = idDescricao
        self.__notaFiscal = notaFiscal
        self.__codigoNosso = codigoNosso
        self.__codigoProduto = codigoProduto
        self.__produto = produto
        self.__ncm = ncm
        self.__cst = cst
        self.__cfop = cfop
        self.__un = un
        self.__qtd = qtd
        self.__valorUnitario = valorUnitario
        self.__valorTotal = valorTotal
        self.__valorIcms = valorIcms
        self.__valorIpi = valorIpi
        self.__alicotaIcms = alicotaIcms
        self.__alicotaIpi = alicotaIpi


    @property
    def getIdDescricao(self):
        return self.__idDescricao

    @getIdDescricao.setter
    def setIdDescricao(self, idDescricao):
        self.__idDescricao = idDescricao

    @property
    def getNotaFiscal(self):
        return self.__notaFiscal

    @getNotaFiscal.setter
    def setNotaFiscal(self, notaFiscal):
        self.__notaFiscal = notaFiscal

    @property
    def getCodigoNosso(self):
        return self.__codigoNosso

    @getCodigoNosso.setter
    def setCodigoNosso(self, codigoNosso):
        self.__codigoNosso = codigoNosso

    @property
    def getCodigoProduto(self):
        return self.__codigoProduto

    @getCodigoProduto.setter
    def setCodigoProduto(self, codigoProduto):
        self.__codigoProduto = codigoProduto

    @property
    def getProduto(self):
        return self.__produto

    @getProduto.setter
    def setProduto(self, produto):
        self.__produto = produto

    @property
    def getCst(self):
        return self.__cst

    @getCst.setter
    def setCst(self, cst):
        self.__cst = cst

    @property
    def getCfop(self):
        return self.__cfop

    @getCfop.setter
    def setCfop(self, cfop):
        self.__cfop = cfop

    @property
    def getUn(self):
        return self.__un

    @getUn.setter
    def setUn(self, un):
        self.__un = un

    @property
    def getQtd(self):
        return self.__qtd

    @getQtd.setter
    def setQtd(self, qtd):
        self.__qtd = qtd

    @property
    def getValorUnitario(self):
        return self.__valorUnitario

    @getValorUnitario.setter
    def setValorUnitario(self, valorUnitario):
        self.__valorUnitario = valorUnitario

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
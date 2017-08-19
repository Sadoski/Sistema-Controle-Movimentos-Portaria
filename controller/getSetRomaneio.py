class Romaneio():
    def __init__(self, idRomaneio, idNotaFiscal, numRomaneio, idMetragem,  certificada):
        self.__idRomaneio = idRomaneio
        self.__idNotaFiscal = idNotaFiscal
        self.__numRomaneio = numRomaneio
        self.__idMetragem = idMetragem
        self.__certificada = certificada
        print(self.__certificada)

    @property
    def getIdRomaneio(self):
        return self.__idRomaneio

    @getIdRomaneio.setter
    def setIdRomaneio(self, idRomaneio):
        self.__idRomaneio =idRomaneio

    @property
    def getIdNotaFiscal(self):
        return self.__idNotaFiscal

    @getIdNotaFiscal.setter
    def setIdNotaFiscal(self, idNotaFiscal):
        self.__idNotaFiscal = idNotaFiscal

    @property
    def getIdMetragem(self):
        return self.__idMetragem

    @getIdMetragem.setter
    def setIdMetragem(self, idMetragem):
        self.__idMetragem = idMetragem

    @property
    def getNumRomaneio(self):
        return self.__numRomaneio

    @getNumRomaneio.setter
    def setNumRomaneio(self, numRomaneio):
        self.__numRomaneio = numRomaneio

    @property
    def getCertifica(self):
        return self.__certificada

    @getCertifica.setter
    def setCertificada(self, certificada):
        self.__certificada = certificada
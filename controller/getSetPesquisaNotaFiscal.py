class PesquisaNotaFiscal():
    def __init__(self, idNotaFiscal, numNotaFiscal, dataEmissao, valorTotal, codEmitente, fantasiaEmitente, razaoSocialEmitente, cnpjEmitente, insEstadualEmitente, codDestinatario, fantasiaDestinatario, razaoSocialDestinatario, cnpjDestinatario, insEstadualDestinatario, codMotorista, nomeMotorista, rg, cpf, codRomaneio, numRomaneio, certificada, metragem):
        self.__idNotaFiscal = idNotaFiscal
        self.__numNotaFiscal = numNotaFiscal
        self.__dataEmissao = dataEmissao
        self.__valorTotal = valorTotal
        self.__codEmitente = codEmitente
        self.__fantasiaEmitente = fantasiaEmitente
        self.__razaoSocialEmitente = razaoSocialEmitente
        self.__cnpjEmitente = cnpjEmitente
        self.__insEstadualEmitente = insEstadualEmitente
        self.__codDestinatario = codDestinatario
        self.__fantasiaDestinatario = fantasiaDestinatario
        self.__razaoSocialDestinatario = razaoSocialDestinatario
        self.__cnpjDestinatario = cnpjDestinatario
        self.__insEstadualDestinatario= insEstadualDestinatario
        self.__codMotorista = codMotorista
        self.__nomeMotorista = nomeMotorista
        self.__rg = rg
        self.__cpf = cpf
        self.__codRomaneio = codRomaneio
        self.__numRomaneio = numRomaneio
        self.__certificada = certificada
        self.__metragem = metragem


    @property
    def getIdNotaFiscal(self):
        return self.__idNotaFiscal

    @getIdNotaFiscal.setter
    def setIdNotaFiscal(self, idNotaFiscal):
        self.__idNotaFiscal = idNotaFiscal

    @property
    def getNumNotaFiscal(self):
        return self.__numNotaFiscal

    @getNumNotaFiscal.setter
    def setNumNotaFiscal(self, numNotaFiscal):
        self.__numNotaFiscal = numNotaFiscal

    @property
    def getData(self):
        return self.__dataEmissao

    @getData.setter
    def setData(self, data):
        self.__dataEmissao = data

    @property
    def getValorTotal(self):
        return self.__valorTotal

    @getValorTotal.setter
    def setValorTotal(self, valorTotal):
        self.__valorTotal = valorTotal

    @property
    def getCodEmitente(self):
        return self.__codEmitente

    @getCodEmitente.setter
    def setCodEmitente(self, codEmitente):
        self.__codEmitente = codEmitente

    @property
    def getFantasiaEmitente(self):
        return self.__fantasiaEmitente

    @getFantasiaEmitente.setter
    def setFantasiaEmitente(self, fantasiaEmitente):
        self.__fantasiaEmitente = fantasiaEmitente

    @property
    def getRazaoSocialEmitente(self):
        return self.__razaoSocialEmitente

    @getRazaoSocialEmitente.setter
    def setRazaoSocialEmitente(self, razaoSocialEmitente):
        self.__razaoSocialEmitente = razaoSocialEmitente

    @property
    def getCnpjEmitente(self):
        return self.__cnpjEmitente

    @getCnpjEmitente.setter
    def setCnpjEmitente(self, cnpjEmitente):
        self.__cnpjEmitente = cnpjEmitente

    @property
    def getInsEstadualEmitente(self):
        return self.__insEstadualEmitente

    @getInsEstadualEmitente.setter
    def setInsEstadualEmitente(self, insEstadualEmitente):
        self.__insEstadualEmitente = insEstadualEmitente

    @property
    def getCodDestinatario(self):
        return self.__codDestinatario

    @getCodDestinatario.setter
    def setCodEmitente(self, codDestinatario):
        self.__codDestinatario = codDestinatario

    @property
    def getFantasiaDestinatario(self):
        return self.__fantasiaDestinatario

    @getFantasiaDestinatario.setter
    def setFantasiaDestinatario(self, fantasiaDestinatario):
        self.__fantasiaDestinatario = fantasiaDestinatario

    @property
    def getRazaoSocialDestinatario(self):
        return self.__razaoSocialDestinatario

    @getRazaoSocialDestinatario.setter
    def setRazaoSocialDestinatario(self, razaoSocialDestinatario):
        self.__razaoSocialDestinatario = razaoSocialDestinatario

    @property
    def getCnpjDestinatario(self):
        return self.__cnpjDestinatario

    @getCnpjDestinatario.setter
    def setCnpjDestinatario(self, cnpjDestinatario):
        self.__cnpjDestinatario = cnpjDestinatario

    @property
    def getInsEstadualDestinatario(self):
        return self.__insEstadualDestinatario

    @getInsEstadualDestinatario.setter
    def setInsEstadualDestinatario(self, insEstadualDestinatario):
        self.__insEstadualDestinatario = insEstadualDestinatario

    @property
    def getCodMotorista(self):
        return self.__codMotorista

    @getCodMotorista.setter
    def setCodMotorista(self, codMotorista):
        self.__codMotorista = codMotorista

    @property
    def getNomeMotorista(self):
        return self.__nomeMotorista

    @getNomeMotorista.setter
    def setNomeMotorista(self, nomeMotorista):
        self.__nomeMotorista = nomeMotorista

    @property
    def getRg(self):
        return self.__rg

    @getRg.setter
    def setRg(self, rg):
        self.__rg = rg

    @property
    def getCpf(self):
        return self.__cpf

    @getCpf.setter
    def setCpf(self, cpf):
        self.__cpf = cpf

    @property
    def getCodRomaneio(self):
        return self.__codRomaneio

    @getCodRomaneio.setter
    def setCodRomaneio(self, codRomaneio):
        self.__codRomaneio = codRomaneio

    @property
    def getNumRomaneio(self):
        return self.__numRomaneio

    @getNumRomaneio.setter
    def setNumRomaneio(self, numRomaneio):
        self.__numRomaneio = numRomaneio

    @property
    def getCetificada(self):
        return self.__certificada

    @getCetificada.setter
    def setCertificada(self, certificada):
        self.__certificada = certificada

    @property
    def getMetragem(self):
        return self.__metragem

    @getMetragem.setter
    def setMetragem(self, metragem):
        self.__metragem = metragem
class Cliente():
    def __init__(self, idCliente, idPessoa, cnpj, inscricaoEstadual, fantasia, razaoSocial, observacao, situacao):
        self.__idCliente = idCliente
        self.__idPessoa = idPessoa
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.__fantasia = fantasia
        self.__razaoSocial = razaoSocial
        self.__observacao = observacao
        self.__situacao = situacao


    @property
    def getIdCliente(self):
        return self.__idCliente

    @getIdCliente.setter
    def setIdCliente(self, idCliente):
        self.__idCliente = idCliente

    @property
    def getIdPessoa(self):
        return self.__idPessoa

    @getIdPessoa.setter
    def setIdPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    @property
    def getCnpj(self):
        return self.__cnpj

    @getCnpj.setter
    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def getInscricaoEstadual(self):
        return self.__inscricaoEstadual

    @getInscricaoEstadual.setter
    def setInscricaoEstadual(self, inscricaoEstadual):
        self.__inscricaoEstadual = inscricaoEstadual

    @property
    def getFantasia(self):
        return self.__fantasia

    @getFantasia.setter
    def setFantasia(self, fantasia):
        self.__fantasia = fantasia

    @property
    def getRazaoSocial(self):
        return self.__razaoSocial

    @getRazaoSocial.setter
    def setRazaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial

    @property
    def getObservacao(self):
        return self.__observacao

    @getObservacao.setter
    def setObservcao(self, observacao):
        self.__observacao = observacao

    @property
    def getSituacao(self):
        return self.__situacao

    @getSituacao.setter
    def setSituacao(self, situacao):
        self.__situcao = situacao


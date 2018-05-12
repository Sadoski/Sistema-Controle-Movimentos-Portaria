class Fornecedor():
    def __init__(self, idFornecedor, idPessoa, idPessoaFisica, idPessoaJuridica,  cnpj, inscricaoEstadual, fantasia, razaoSocial, observacao, situacao, tipo):
        self.__idFornecedor = idFornecedor
        self.__idPessoa = idPessoa
        self.__idPessoaFisica = idPessoaFisica
        self.__idPessoaJuridica = idPessoaJuridica
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.__fantasia = fantasia
        self.__razaoSocial = razaoSocial
        self.__observacao = observacao
        self.__situacao = situacao
        self.__tipo = tipo


    @property
    def getIdFornecedor(self):
        return self.__idFornecedor

    @getIdFornecedor.setter
    def setIdFornecedor(self, idFornecedor):
        self.__idFornecedor = idFornecedor

    @property
    def getIdPessoa(self):
        return self.__idPessoa

    @getIdPessoa.setter
    def setIdPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    @property
    def getIdPessoaFisica(self):
        return self.__idPessoaFisica

    @getIdPessoaFisica.setter
    def setIdPessoaFisica(self, idPessoaFisica):
        self.__idPessoaFisica = idPessoaFisica

    @property
    def getIdPessoaJuridica(self):
        return self.__idPessoaJuridica

    @getIdPessoaJuridica.setter
    def setIdPessoaJuridica(self, idPessoaJuridica):
        self.__idPessoaJuridica = idPessoaJuridica

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

    @property
    def getTipo(self):
        return self.__tipo

    @getTipo.setter
    def setTipo(self, tipo):
        self.__Tipo = tipo
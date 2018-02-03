class PessoaJuridica():
    def __init__(self, idPessoa, idPesJuridica, idTipoPessoa, razao, fantasia, cnpj, inscricao, endereco, numero, complemento, bairro, idCidade, cidade, estado, cep, site):
        self.__idPessoa = idPessoa
        self.__idPesJuridica = idPesJuridica
        self.__idTipoPessoa = idTipoPessoa
        self.__razao = razao
        self.__fantasia = fantasia
        self.__cnpj = cnpj
        self.__inscricao = inscricao
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__idCidade = idCidade
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep
        self.__site = site

    @property
    def getIdPessoa(self):
        return self.__idPessoa

    @getIdPessoa.setter
    def setIdPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    @property
    def getIdPesJuridica(self):
        return self.__idPesJuridica

    @getIdPesJuridica.setter
    def setIdJuridica(self, idPesJuridica):
        self.__idPesJuridica = idPesJuridica

    @property
    def getIdTipoPessoa(self):
        return self.__idTipoPessoa

    @getIdTipoPessoa.setter
    def setIdTipoPessoa(self, idTipoPessoa):
        self.__idTipoPessoa = idTipoPessoa

    @property
    def getRazao(self):
        return self.__razao

    @getRazao.setter
    def setRazao(self, razao):
        self.__razao = razao

    @property
    def getFantasia(self):
        return self.__fantasia

    @getFantasia.setter
    def setFantasia(self, fantasia):
        self.__fantasia = fantasia

    @property
    def getCnpj(self):
        return self.__cnpj

    @getCnpj.setter
    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def getInscricao(self):
        return self.__inscricao

    @getInscricao.setter
    def setInscricao(self, inscricao):
        self.__inscricao = inscricao

    @property
    def getEndereco(self):
        return self.__endereco

    @getEndereco.setter
    def setEndereco(self, endereco):
        self.__endereco = endereco

    @property
    def getNumero(self):
        return self.__numero

    @getNumero.setter
    def setNumero(self, numero):
        self.__numero = numero

    @property
    def getComplemento(self):
        return self.__complemento

    @getComplemento.setter
    def setComplemento(self, complemento):
        self.__complemento = complemento

    @property
    def getBairro(self):
        return self.__bairro

    @getBairro.setter
    def setBairro(self, bairro):
        self.__bairro = bairro

    @property
    def getIdCidade(self):
        return self.__idCidade

    @getIdCidade.setter
    def setIdCidade(self, idCidade):
        self.__idCidade = idCidade

    @property
    def getCidade(self):
        return self.__cidade

    @getCidade.setter
    def setCidade(self, cidade):
        self.__cidade = cidade

    @property
    def getEstado(self):
        return self.__estado

    @getEstado.setter
    def setEstado(self, estado):
        self.__estado = estado

    @property
    def getCep(self):
        return self.__cep

    @getCep.setter
    def setCep(self, cep):
        self.__cep = cep

    @property
    def getSite(self):
        return self.__site

    @getSite.setter
    def setSite(self, site):
        self.__site = site
class PessoaFisica():
    def __init__(self, idPessoa, idPesFisica, idTipoPessoa, nome, apelido, cpf, rg, expeditor, uf, data, sexo, endereco, numero, complemento, bairro, mae, pai, idCidade, cidade, estado, cep):
        self.__idPessoa = idPessoa
        self.__idPesFisica = idPesFisica
        self.__idTipoPessoa = idTipoPessoa
        self.__nome = nome
        self.__apelido = apelido
        self.__cpf = cpf
        self.__rg = rg
        self.__expeditor = expeditor
        self.__uf = uf
        self.__data = data
        self.__sexo = sexo
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__mae = mae
        self.__pai = pai
        self.__idCidade = idCidade
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    @property
    def getIdPessoa(self):
        return self.__idPessoa

    @getIdPessoa.setter
    def setIdPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    @property
    def getIdPesFisica(self):
        return self.__idPesFisica

    @getIdPesFisica.setter
    def setIdPesFisica(self, idPesFisica):
        self.__idPesFisica = idPesFisica

    @property
    def getIdTipoPessoa(self):
        return self.__idTipoPessoa

    @getIdTipoPessoa.setter
    def setIdTipoPessoa(self, idTipoPessoa):
        self.__idTipoPessoa = idTipoPessoa

    @property
    def getNome(self):
        return self.__nome

    @getNome.setter
    def setNome(self, Nome):
        self.__nome = Nome

    @property
    def getApelido(self):
        return self.__apelido

    @getApelido.setter
    def setApelido(self, apelido):
        self.__apelido = apelido

    @property
    def getCpf(self):
        return self.__cpf

    @getCpf.setter
    def setCpf(self, cpf):
        self.__Cpf = cpf

    @property
    def getRg(self):
        return self.__rg

    @getRg.setter
    def setRg(self, rg):
        self.__rg = rg

    @property
    def getExpeditor(self):
        return self.__expeditor

    @getExpeditor.setter
    def setExpeditor(self, expeditor):
        self.__expeditor = expeditor

    @property
    def getUf(self):
        return self.__uf

    @getUf.setter
    def setUf(self, uf):
        self.__uf = uf

    @property
    def getData(self):
        return self.__data

    @getData.setter
    def setData(self, data):
        self.__data = data

    @property
    def getSexo(self):
        return self.__sexo

    @getSexo.setter
    def setSexo(self, sexo):
        self.__sexo = sexo

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
    def getBairro(self):
        return self.__bairro

    @getBairro.setter
    def setBairro(self, bairro):
        self.__bairro = bairro

    @property
    def getMae(self):
        return self.__mae

    @getMae.setter
    def setMae(self, mae):
        self.__mae = mae

    @property
    def getPai(self):
        return self.__pai

    @getPai.setter
    def setPai(self, pai):
        self.__pai = pai

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
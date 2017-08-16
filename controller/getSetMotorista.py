class Motorista():

    def __init__(self, idMotorista, nome, nascimento, rg, expeditor, cpf, pis, sexo, cnh, categoria, endereco, numero, complemento, bairro, cidade, telefone, celular):
        self.__idMotorista = idMotorista
        self.__nome = nome
        self.__nascimento = nascimento
        self.__rg = rg
        self.__expeditor = expeditor
        self.__cpf = cpf
        self.__pis = pis
        self.__cnh = cnh
        self.__categoria = categoria
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__telefone = telefone
        self.__celular = celular
        self.__sexo = sexo

    @property
    def getIdMotorista(self):
        return self.__idMotorista

    @getIdMotorista.setter
    def setIdFuncionario(self, idMotorista):
        self.__idMotorista = idMotorista

    @property
    def getNome(self):
        return self.__nome

    @getNome.setter
    def setNome(self, nome):
        self.__nome = nome

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
    def getCpf(self):
        return self.__cpf

    @getCpf.setter
    def setCpf(self, cpf):
        self.__cpf = cpf

    @property
    def getPis(self):
        return self.__pis

    @getPis.setter
    def setCnh(self, pis):
        self.__pis = pis

    @property
    def getNascimento(self):
        return self.__nascimento

    @getNascimento.setter
    def setNacimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def getSexo(self):
        return self.__sexo

    @getSexo.setter
    def setSexo(self, sexo):
        self.__sexo = sexo

    @property
    def getCnh(self):
        return self.__cnh

    @getCnh.setter
    def setCnh(self, cnh):
        self.__cnh = cnh

    @property
    def getCategoria(self):
        return self.__categoria

    @getCategoria.setter
    def setPai(self, categoria):
        self.__categoria = categoria

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
    def getCidade(self):
        return self.__cidade

    @getCidade.setter
    def setCidade(self, cidade):
        self.__cidade = cidade

    @property
    def getTelefone(self):
        return self.__telefone

    @getTelefone.setter
    def setTelefone(self, telefone):
        self.__telefone = telefone

    @property
    def getCelular(self):
        return self.__celular

    @getCelular.setter
    def setCelular(self, celular):
        self.__celular = celular



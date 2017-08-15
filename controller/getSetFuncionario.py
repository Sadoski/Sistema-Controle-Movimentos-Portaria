class Funcionario():

    def __init__(self, idFuncionario, nome, rg, expeditor, cpf, nascimento, sexo, mae, pai, endereco, numero, complemento, bairro, cidade, telefone, celular, funcao, empresa):
        self.__idFuncionario = idFuncionario
        self.__nome = nome
        self.__rg = rg
        self.__expeditor = expeditor
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__sexo = sexo
        self.__mae = mae
        self.__pai = pai
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__telefone = telefone
        self.__celular = celular
        self.__funcao = funcao
        self.__empresa = empresa

    @property
    def getIdFuncionario(self):
        return self.__idFuncionario

    @getIdFuncionario.setter
    def setIdFuncionario(self, idFuncionario):
        self.__idFuncionario = idFuncionario

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
    def getMae(self):
        return  self.__mae

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

    @property
    def getFuncao(self):
        return self.__funcao

    @getFuncao.setter
    def setFuncao(self, funcao):
        self.__funcao = funcao

    @property
    def getEmpresa(self):
        return self.__empresa

    @getEmpresa.setter
    def setEmpresa(self, empresa):
        self.__empresa = empresa

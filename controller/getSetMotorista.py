class Motorista():

    def __init__(self, idMotorista, idPessoa, idPessoaFisica, nome, sobrenome, rg, cpf, pis, cnh, categoria, marca, modelo, placa, obs, situacao):
        self.__idMotorista = idMotorista
        self.__idPessoa = idPessoa
        self.__idPessoaFisica = idPessoaFisica
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__rg = rg
        self.__cpf = cpf
        self.__pis = pis
        self.__cnh = cnh
        self.__categoria = categoria
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__obs = obs
        self.__situacao = situacao


    @property
    def getIdMotorista(self):
        return self.__idMotorista

    @getIdMotorista.setter
    def setIdMotorista(self, idMotorista):
        self.__idMotorista = idMotorista

    @property
    def getIdPessoa(self):
        return self.__idPessoa

    @getIdPessoa.setter
    def setIdPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    @property
    def getIdPessoaFisica(self):
        return self.__idPessoa

    @getIdPessoaFisica.setter
    def setIdPessoaFisica(self, idPessoaFisica):
        self.__idPessoaFisica = idPessoaFisica

    @property
    def getNome(self):
        return self.__nome

    @getNome.setter
    def setNome(self, nome):
        self.__nome = nome

    @property
    def getSobrenome(self):
        return self.__sobrenome

    @getSobrenome.setter
    def setSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

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
    def getPis(self):
        return self.__pis

    @getPis.setter
    def setPis(self, pis):
        self.__pis = pis

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
    def setCategoria(self, categoria):
        self.__categoria = categoria

    @property
    def getMarca(self):
        return self.__marca

    @getMarca.setter
    def setMarca(self, marca):
        self.__marca = marca

    @property
    def getModelo(self):
        return self.__modelo

    @getModelo.setter
    def setModelo(self, modelo):
        self.__modelo = modelo

    @property
    def getPlaca(self):
        return self.__placa

    @getPlaca.setter
    def setPlaca(self, placa):
        self.__placa = placa

    @property
    def getObservacao(self):
        return self.__obs

    @getObservacao.setter
    def setObservacao(self, obs):
        self.__obs = obs

    @property
    def getSituacao(self):
        return self.__situacao

    @getSituacao.setter
    def setSituacao(self, situacao):
        self.__situacao = situacao
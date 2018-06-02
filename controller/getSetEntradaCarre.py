class EntradaCarre():
    def __init__(self, data, hora, cargaProduto, produto, idMotorista, idVeiculo, idCliente):
        self.__data = data
        self.__hora = hora
        self.__cargaProduto = cargaProduto
        self.__produto = produto
        self.__idMotorista = idMotorista
        self.__idVeiculo = idVeiculo
        self.__idCliente = idCliente


    @property
    def getData(self):
        return self.__data

    @getData.setter
    def setData(self, data):
        self.__data = data

    @property
    def getHora(self):
        return self.__hora

    @getHora.setter
    def setHora(self, hora):
        self.__hora = hora

    @property
    def getCarga(self):
        return self.__cargaProduto

    @getCarga.setter
    def setCarga(self, carga):
        self.__cargaProduto = carga

    @property
    def getIdMotorista(self):
        return self.__idMotorista

    @getIdMotorista.setter
    def setIdMotorista(self, idMotorista):
        self.__idMotorista = idMotorista

    @property
    def getIdVeiculo(self):
        return self.__idVeiculo

    @getIdVeiculo.setter
    def setIdVeiculo(self, idVeiculo):
        self.__idVeiculo = idVeiculo

    @property
    def getIdCliente(self):
        return self.__idCliente

    @getIdCliente.setter
    def setIdCliente(self, idCliente):
        self.__idCliente = idCliente

    @property
    def getProduto(self):
        return self.__produto

    @getProduto.setter
    def setProduto(self, produto):
        self.__produto = produto
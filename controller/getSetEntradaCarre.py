class EntradaCarre():
    def __init__(self, data, hora, cargaProduto, idMotorista, idCliente, idEmpresa, ):
        self.__data = data
        self.__hora = hora
        self.__cargaProduto = cargaProduto
        self.__idMotorista = idMotorista
        self.__idCliente = idCliente
        self.__idEmpresa = idEmpresa

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
    def getCargaProduto(self):
        return self.__cargaProduto

    @getCargaProduto.setter
    def setCargaProduto(self, cargaProduto):
        self.__cargaProduto = cargaProduto

    @property
    def getIdMotorista(self):
        return self.__idMotorista

    @getIdMotorista.setter
    def setIdMotorista(self, idMotorista):
        self.__idMotorista = idMotorista

    @property
    def getIdCliente(self):
        return self.__idCliente

    @getIdCliente.setter
    def setIdCliente(self, idCliente):
        self.__idCliente = idCliente

    @property
    def getIdEmpresa(self):
        return self.__idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self.__idEmpresa = idEmpresa
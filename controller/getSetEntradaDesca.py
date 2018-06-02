class EntradaDesca():
    def __init__(self, data, hora, idNf, idMotorista, idFornecedor):
        self.__data = data
        self.__hora = hora
        self.__idNf = idNf
        self.__idMotorista = idMotorista
        self.__idFornecedor = idFornecedor


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
    def getIdNf(self):
        return self.__idNf

    @getIdNf.setter
    def setIdNf(self, idNf):
        self.__idNf = idNf

    @property
    def getIdMotorista(self):
        return self.__idMotorista

    @getIdMotorista.setter
    def setIdMotorista(self, idMotorista):
        self.__idMotorista = idMotorista

    @property
    def getIdFornecedor(self):
        return self.__idFornecedor

    @getIdFornecedor.setter
    def setIdFornecedor(self, idFornecedor):
        self.__idFornecedor = idFornecedor
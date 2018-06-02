class FuncionarioSaida():
    def __init__(self, idSaida, idFuncionario, data, hora):
        self.__idSaida = idSaida
        self.__idFuncionario = idFuncionario
        self.__data = data
        self.__hora = hora

    @property
    def getIdSaida(self):
        return self.__idSaida

    @getIdSaida.setter
    def setIdSaida(self, idSaida):
        self.__idSaida = idSaida

    @property
    def getIdFuncionario(self):
        return self.__idFuncionario

    @getIdFuncionario.setter
    def setIdFuncionario(self, idFuncionario):
        self.__idFuncionario = idFuncionario

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
class EntradaFuncionario():
    def __init__(self, idSaida, data, hora):
        self.__idSaida = idSaida
        self.__data = data
        self.__hora = hora

    @property
    def getIdSaida(self):
        return self.__idSaida

    @getIdSaida.setter
    def setIdSaida(self, idSaida):
        self.__idSaida = idSaida

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
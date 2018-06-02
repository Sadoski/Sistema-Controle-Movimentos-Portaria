class SaidaDesca():
    def __init__(self, idEntrada, data, hora):
        self.__data = data
        self.__hora = hora
        self.__idEntrada = idEntrada


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
    def getIdEntrada(self):
        return self.__idEntrada

    @getIdEntrada.setter
    def setIdEntrada(self, idEntrada):
        self.__idEntrada = idEntrada
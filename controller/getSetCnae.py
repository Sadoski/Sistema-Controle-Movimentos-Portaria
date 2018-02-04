class Cnae():
    def __init__(self, codSubclasse, subclasse):
        self.__codSubclasse = codSubclasse
        self.__subclasse = subclasse

    @property
    def getCodSubclasse(self):
        return self.__codSubclasse

    @getCodSubclasse.setter
    def setCodSubclasse(self, codSubclasse):
        self.__codSubclasse = codSubclasse

    @property
    def getSubclasse(self):
        return self.__subclasse

    @getSubclasse.setter
    def setSubclasse(self, subclasse):
        self.__subclasse = subclasse
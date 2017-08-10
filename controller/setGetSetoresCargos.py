class Setor():

    def __init__(self, idEmpresa, setor):
       self.__idEmpresa = idEmpresa
       self.__setor = setor

    @property
    def getIdEmpresa(self):
        return self.__idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self.__idEmpresa = idEmpresa

    @property
    def getSetor(self):
        return self.__setor

    @getSetor.setter
    def setSetor(self, setor):
        self.__setor = setor
class Setor():
    def __init__(self, idSetor, setor, idEmpresa):
        self.__idSetor = idSetor
        self.__idEmpresa = idEmpresa
        self.__setor = setor

    @property
    def getIdSetor(self):
        return self.__idSetor

    @getIdSetor.setter
    def setIdSetor(self, idSetor):
        self.__idSetor = idSetor

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



class Relacao():
    def __init__(self, idEmpresa, setor, cargo):
        self.__idEmpresa = idEmpresa
        self.__setor = setor
        self.__cargo = setor


    @property
    def getIdEmpresa(self):
        return self.__idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self.__idEmpresa = idEmpresa

    @property
    def getIdSetor(self):
        return self.__setor

    @getIdSetor.setter
    def setIdSetor(self, setor):
        self.__setor = setor

    @property
    def getIdCargo(self):
        return self.__cargo

    @getIdCargo.setter
    def setIdCargo(self, cargo):
        self.__cargo = cargo
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

class Cargo():
    def __init__(self, idEmpresa, cargo):
        self.__idEmpresa = idEmpresa
        self.__cargo = cargo


    @property
    def getIdEmpresa(self):
        return self.__idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self.__idEmpresa = idEmpresa

    @property
    def getCargo(self):
        return self.__cargo

    @getCargo.setter
    def setCargo(self, cargo):
        self.__cargo = cargo

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
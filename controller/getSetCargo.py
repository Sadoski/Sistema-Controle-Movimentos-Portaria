class Cargo():
    def __init__(self, idcargo, cargo, idEmpresa):
        self.__idCargo = idcargo
        self.__idEmpresa = idEmpresa
        self.__cargo = cargo

    @property
    def getIdCargo(self):
        return self.__idCargo

    @getIdCargo.setter
    def setIdCargo(self, idCargo):
        self.__idCargo = idCargo

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
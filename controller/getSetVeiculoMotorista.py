class VeiculoMotorista():
    def __init__(self, idVeiculo, idMotorista, tipoVeiculo, marca, modelo, placa):
        self.__idVeiculo = idVeiculo
        self.__idMotorista = idMotorista
        self.__tipoVeiculo = tipoVeiculo
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa

    @property
    def getIdVeiculo(self):
        return self.__idVeiculo

    @getIdVeiculo.setter
    def setIdVeiculo(self, idVeiculo):
        self.__idVeiculo = idVeiculo

    @property
    def getIdMotorista(self):
        return self.__idMotorista

    @getIdMotorista.setter
    def setIdMotorista(self, idMotorista):
        self.__idMotorista = idMotorista

    @property
    def getTipoVeiculo(self):
        return self.__tipoVeiculo

    @getTipoVeiculo.setter
    def setTipoVeiculo(self, tipoVeiculo):
        self.__tipoVeiculo = tipoVeiculo

    @property
    def getMarca(self):
        return self.__marca

    @getMarca.setter
    def setTipoVeiculo(self, marca):
        self.__marca = marca

    @property
    def getModelo(self):
        return self.__modelo

    @getModelo.setter
    def setModelo(self, modelo):
        self.__modelo = modelo

    @property
    def getPlaca(self):
        return self.__placa

    @getPlaca.setter
    def setPlaca(self, placa):
        self.__placa = placa
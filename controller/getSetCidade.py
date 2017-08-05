class Cidades():

    def __init__(self, idCidade, idEstado, nomeCidade, cep):
        self._idCidade = idCidade
        self._idEstado = idEstado
        self. _nomeCidade = nomeCidade
        self._cep = cep

    @property
    def getIdCidade(self):
        return self._idCidade

    @getIdCidade.setter
    def setIdCidade(self, idCidade):
        self._idCidade = idCidade

    @property
    def getIdEstado(self):
        return self._idEstado

    @getIdEstado.setter
    def setIdEstado(self, idEstado):
        self._idEstado = idEstado

    @property
    def getNomeCidade(self):
        return self._nomeCidade

    @getNomeCidade.setter
    def setNomeCidade(self, nomeCidade):
        self._nomeCidade = nomeCidade

    @property
    def getCep(self):
        return self._cep

    @getCep.setter
    def setCep(self, cep):
        self._cep = cep
class Cidades():

    def __init__(self, idCidade, nomeEstado, nomeCidade, cep):
        self._idCidade = idCidade
        self._nomeEstado = nomeEstado
        self._nomeCidade = nomeCidade
        self._cep = cep

    @property
    def getIdCidade(self):
        return self._idCidade

    @getIdCidade.setter
    def setIdCidade(self, idCidade):
        self._idCidade = idCidade

    @property
    def getNomeEstado(self):
        return self._nomeEstado

    @getNomeEstado.setter
    def setNomeEstado(self, nomeEstado):
        self._nomeEstado = nomeEstado

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
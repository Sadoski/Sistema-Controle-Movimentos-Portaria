import this

class Cidades(object):

    def __init__(self, idCidade, nomeCidade, nomeEstado):
        _idCidade = idCidade
        _nomeCidade = nomeCidade
        _nomeEstado = nomeEstado

    @property
    def getIdCidade(self):
        return self._idCidade

    @getIdCidade.setter
    def setIdCidade(self, idCidade):
        this._idCidade = idCidade

    @property
    def getNomeCidade(self):
        return self._nomeCidade

    @getNomeCidade.setter
    def setNomeCidade(self, nomeCidade):
        this._nomeCidade = nomeCidade

    @property
    def getNomeEstado(self):
        return self._nomeEstado

    @getNomeEstado.setter
    def setNomeEstado(self, nomeEstado):
        this._nomeEstado = nomeEstado
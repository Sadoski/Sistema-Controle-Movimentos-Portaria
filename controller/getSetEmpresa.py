class Empresas():
    def __init__(self, idEmpresa, idPessoaJuridica, tipoEmpresa, inscricaoMunicipal, situacao):
        self._idEmpresa = idEmpresa
        self._idPessoaJuridica = idPessoaJuridica
        self._tipoEmpresa = tipoEmpresa
        self._inscricaoMunicipal = inscricaoMunicipal
        self._situacao = situacao


    @property
    def getIdEmpresa(self):
        return self._idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self._idEmpresa = idEmpresa

    @property
    def getIdPessoaJuridica(self):
        return self._idPessoaJuridica

    @getIdPessoaJuridica.setter
    def setIdPessoaJuridica(self, PessoaJuridica):
        self._idPessoaJuridica = PessoaJuridica

    @property
    def getTipoEmpresa(self):
        return self._tipoEmpresa

    @getTipoEmpresa.setter
    def setTipoEmpresa(self, tipoEmpresa):
        self._tipoEmpresa = tipoEmpresa

    @property
    def getInscricaoMunicipal(self):
        return self._inscricaoMunicipal

    @getInscricaoMunicipal.setter
    def setInscricaoMunicipal(self, inscricaoMunicipal):
        self._inscricaoMunicipal = inscricaoMunicipal

    @property
    def getSituacao(self):
        return self._situacao

    @getSituacao.setter
    def setInscricaoMunicipal(self, situacao):
        self._situacao = situacao
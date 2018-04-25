class Empresas():
    def __init__(self, idPessoa, idEmpresa, idPessoaJuridica,  tipoEmpresa, cnae, desCnae, cnpj, inscricaoEstadual, inscricaoMunicipal, fantasia, razaoSocial, endereco, numero, complemento, bairro, idCidade, cidade, estado, cep, situacao):
        self.__idPessoa = idPessoa
        self._idEmpresa = idEmpresa
        self.__idPessoaJuridica = idPessoaJuridica
        self._tipoEmpresa = tipoEmpresa
        self.__cnae = cnae
        self.__desCnae = desCnae
        self._cnpj = cnpj
        self._inscricaoEstadual = inscricaoEstadual
        self._inscricaoMunicipal = inscricaoMunicipal
        self._fantasia = fantasia
        self._razaoSocial = razaoSocial
        self._endereco = endereco
        self._numero = numero
        self._complemento = complemento
        self._bairro = bairro
        self._idCidade = idCidade
        self._cidade = cidade
        self._estado = estado
        self._cep = cep
        self._situacao = situacao

    @property
    def getIdPessoa(self):
        return self.__idPessoa

    @getIdPessoa.setter
    def setIdPessoa(self, idPessoa):
        self.self.__idPessoa = idPessoa

    @property
    def getIdEmpresa(self):
        return self._idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self._idEmpresa = idEmpresa

    @property
    def getIdPessoaJuridica(self):
        return self.__idPessoaJuridica

    @getIdPessoaJuridica.setter
    def setIdPessoaJuridica(self, PessoaJuridica):
        self.__idPessoaJuridica = PessoaJuridica


    @property
    def getTipoEmpresa(self):
        return self._tipoEmpresa

    @getTipoEmpresa.setter
    def setTipoEmpresa(self, tipoEmpresa):
        self._tipoEmpresa = tipoEmpresa

    @property
    def getCnae(self):
        return self.__cnae

    @getCnae.setter
    def setCnae(self, cnae):
        self._cnae = cnae

    @property
    def getDesCnae(self):
        return self.__desCnae

    @getDesCnae.setter
    def setDesCnae(self, desCnae):
        self.__desCnae = desCnae

    @property
    def getCnpj(self):
        return self._cnpj

    @getCnpj.setter
    def setCnpj(self, cnpj):
        self._cnpj = cnpj

    @property
    def getInscricaoEstadual(self):
        return self._inscricaoEstadual

    @getInscricaoEstadual.setter
    def setInscricaoEstadual(self, inscricaoEstadual):
        self._inscricaoEstadual = inscricaoEstadual

    @property
    def getInscricaoMunicipal(self):
        return self._inscricaoMunicipal

    @getInscricaoMunicipal.setter
    def setInscricaoMunicipal(self, inscricaoMunicipal):
        self._inscricaoMunicipal = inscricaoMunicipal

    @property
    def getFantasia(self):
        return self._fantasia

    @getFantasia.setter
    def setFantasia(self, fantasia):
        self._fantasia = fantasia

    @property
    def getRazaoSocial(self):
        return self._razaoSocial

    @getRazaoSocial.setter
    def setRazaoSocial(self, razaoSocial):
        self._razaoSocial = razaoSocial

    @property
    def getEndereco(self):
        return self._endereco

    @getEndereco.setter
    def setEndereco(self, endereco):
        self._endereco = endereco

    @property
    def getNumero(self):
        return self._numero

    @getNumero.setter
    def setNumero(self, numero):
        self._numero = numero

    @property
    def getComplemento(self):
        return self._complemento

    @getComplemento.setter
    def setComplemento(self, complemento):
        self._complemento = complemento

    @property
    def getBairro(self):
        return self._bairro

    @getBairro.setter
    def setBairro(self, bairro):
        self._bairro = bairro

    @property
    def getIdCidade(self):
        return self._idCidade

    @getIdCidade.setter
    def setIdCidade(self, idCidade):
        self._idCidade = idCidade

    @property
    def getCidade(self):
        return self._cidade

    @getCidade.setter
    def setCidade(self, cidade):
        self._cidade = cidade

    @property
    def getEstado(self):
        return self._estado

    @getEstado.setter
    def setEstado(self, estado):
        self._estado = estado

    @property
    def getSituacao(self):
        return self._situacao

    @getSituacao.setter
    def setSituacao(self, situacao):
        self._situacao = situacao
class Empresas():
    def __init__(self, idEmpresa, tipoEmpresa, cnpj, inscricaoEstadual, inscricaoMunicipal, fantasia, razaoSocial, endereco, numero, complemento, bairro, cidade, telefone):
        self._idEmpresa = idEmpresa
        self._tipoEmpresa = tipoEmpresa
        self._cnpj = cnpj
        self._inscricaoEstadual = inscricaoEstadual
        self._inscricaoMunicipal = inscricaoMunicipal
        self._fantasia = fantasia
        self._razaoSocial = razaoSocial
        self._endereco = endereco
        self._numero = numero
        self._complemento = complemento
        self._bairro = bairro
        self._cidade = cidade
        self._telefone = telefone

    @property
    def idEmpresa(self):
        return self._idEmpresa

    @idEmpresa.setter
    def idEmpresa(self, idEmpresa):
        self._idEmpresa = idEmpresa

    @property
    def tipoEmpresa(self):
        return self._tipoEmpresa

    @tipoEmpresa.setter
    def tipoEmpresa(self, tipoEmpresa):
        self._tipoEmpresa = tipoEmpresa

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def setCnpj(self, cnpj):
        self._cnpj = cnpj

    @property
    def inscricaoEstadual(self):
        return self._inscricaoEstadual

    @inscricaoEstadual.setter
    def inscricaoEstadual(self, inscricaoEstadual):
        self._inscricaoEstadual = inscricaoEstadual

    @property
    def inscricaoEstadual(self):
        return self._inscricaoMunicipal

    @inscricaoEstadual.setter
    def inscricaoEstadual(self, inscricaoMunicipal):
        self._inscricaoMunicipal = inscricaoMunicipal

    @property
    def fantasia(self):
        return self._fantasia

    @fantasia.setter
    def fantasia(self, fantasia):
        self._fantasia = fantasia

    @property
    def razaoSocial(self):
        return self._razaoSocial

    @razaoSocial.setter
    def razaoSocial(self, razaoSocial):
        self._razaoSocial = razaoSocial

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, complemento):
        self._complemento = complemento

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
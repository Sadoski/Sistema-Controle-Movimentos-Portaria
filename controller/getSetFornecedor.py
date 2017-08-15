class Fornecedor():
    def __init__(self, idFornecedor, cnpj, inscricaoEstadual, fantasia, razaoSocial, endereco, numero, complemento, bairro, telefone, site, email, cidade, empresa):
        self.__idFornecedor = idFornecedor
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.__fantasia = fantasia
        self.__razaoSocial = razaoSocial
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__telefone = telefone
        self.__site = site
        self.__email = email
        self.__cidade = cidade
        self.__empresa = empresa

    @property
    def getIdFornecedor(self):
        return self.__idFornecedor

    @getIdFornecedor.setter
    def setIdFornecedor(self, idFornecedor):
        self.__idFornecedor = idFornecedor

    @property
    def getCnpj(self):
        return self.__cnpj

    @getCnpj.setter
    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def getInscricaoEstadual(self):
        return self.__inscricaoEstadual

    @getInscricaoEstadual.setter
    def setInscricaoEstadual(self, inscricaoEstadual):
        self.__inscricaoEstadual = inscricaoEstadual

    @property
    def getFantasia(self):
        return self.__fantasia

    @getFantasia.setter
    def setFantasia(self, fantasia):
        self.__fantasia = fantasia

    @property
    def getRazaoSocial(self):
        return self.__razaoSocial

    @getRazaoSocial.setter
    def setRazaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial

    @property
    def getEndereco(self):
        return self.__endereco

    @getEndereco.setter
    def setEndereco(self, endereco):
        self.__endereco = endereco

    @property
    def getNumero(self):
        return self.__numero

    @getNumero.setter
    def setNumero(self, numero):
        self.__numero = numero

    @property
    def getComplemento(self):
        return self.__complemento

    @getComplemento.setter
    def setComplemento(self, complemento):
        self.__complemento = complemento

    @property
    def getBairro(self):
        return self.__bairro

    @getBairro.setter
    def setBairro(self, bairro):
        self.__bairro = bairro

    @property
    def getTelefone(self):
        return self.__telefone

    @getTelefone.setter
    def setTelefone(self, telefone):
        self.__telefone = telefone

    @property
    def getSite(self):
        return self.__site

    @getSite.setter
    def setSite(self, site):
        self.__site = site

    @property
    def getEmail(self):
        return self.__email

    @getEmail.setter
    def setEmail(self, email):
        self.__email = email

    @property
    def getCidade(self):
        return self.__cidade

    @getCidade.setter
    def setCidade(self, cidade):
        self.__cidade = cidade

    @property
    def getEmpresa(self):
        return self.__empresa

    @getEmpresa.setter
    def setEmpresa(self, empresa):
        self.__empresa = empresa
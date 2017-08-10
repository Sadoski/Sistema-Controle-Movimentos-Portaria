class ConfirmarEmpresa():

    def __init__(self, idEmpresa, fantasia, razaoSocial, cnpj, inscricao):
        self.__idEmpresa = idEmpresa
        self.__fantasia = fantasia
        self.__razaoSocial = razaoSocial
        self.__cnpj = cnpj
        self.__inscricao = inscricao

    @property
    def getIdEmpres(self):
        return self.__idEmpresa

    @getIdEmpres.setter
    def setIdEmpresa(self, idEmpresa):
        self.__idEmpresa = idEmpresa

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
    def getCnpj(self):
        return self.__cnpj

    @getCnpj.setter
    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def getInscricao(self):
        return self.__inscricao

    def setInscricao(self, inscricao):
        self.__inscricao = inscricao

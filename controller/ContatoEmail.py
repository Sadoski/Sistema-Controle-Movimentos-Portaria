class ContatoEmail():
    def __init__(self, codigo, contato, email, idEmpresa):
        self.__codigo = codigo
        self.__contato = contato
        self.__email = email
        self.__idEmpresa = idEmpresa

    @property
    def getCodigo(self):
        return self.__codigo

    @getCodigo.setter
    def setContato(self, codigo):
        self.__codigo = codigo

    @property
    def getContato(self):
        return self.__contato

    @getContato.setter
    def setContato(self, contato):
        self.__contato = contato

    @property
    def getEmail(self):
        return self.__email

    @getEmail.setter
    def setEmail(self, email):
        self.__email = email

    @property
    def getIdEmpresa(self):
        return self.__idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self.__idEmpresa = idEmpresa
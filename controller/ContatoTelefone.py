class ContatoTelefone():
    def __init__(self, codigo, contato, telefone, idEmpresa):
        self.__codigo = codigo
        self.__contato = contato
        self.__telefone = telefone
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
    def getTelefone(self):
        return self.__telefone

    @getTelefone.setter
    def setTelefoen(self, telefone):
        self.__telefone = telefone

    @property
    def getIdEmpresa(self):
        return self.__idEmpresa

    @getIdEmpresa.setter
    def setIdEmpresa(self, idEmpresa):
        self.__idEmpresa = idEmpresa
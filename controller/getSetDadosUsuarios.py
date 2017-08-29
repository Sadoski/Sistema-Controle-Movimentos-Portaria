class DadosUsuario():
    def __init__(self, idUsuario, nomeUsuario):
        self.__idUsuario = idUsuario
        self.__nomeUsuario = nomeUsuario

    @property
    def getIdUsuario(self):
        return self.__idUsuario

    @getIdUsuario.setter
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    @property
    def getNomeUsuario(self):
        return self.__nomeUsuario

    @getNomeUsuario.setter
    def setNomeUsuario(self, nomeUsuario):
        self.__nomeUsuario = nomeUsuario
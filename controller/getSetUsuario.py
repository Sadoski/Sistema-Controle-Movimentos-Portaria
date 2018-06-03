import this

class UsuarioGetSet():
    def __init__(self, idFuncionario, login, senha, salto):
        self._idFuncionario = idFuncionario
        self._login = login
        self._senha = senha
        self._salto = salto

    @property
    def getIdFuncionario(self):
        return self._idFuncionario

    @getIdFuncionario.setter
    def setIdFuncionario(self, idFuncionario):
        self.__idFuncionario = idFuncionario

    @property
    def getLogin(self):
        return self._login

    @getLogin.setter
    def setLogin(self, login):
        self.__login = login

    @property
    def getSenha(self):
        return self._senha

    @getSenha.setter
    def setSenha(self, senha):
        self.__senha = senha

    @property
    def getSalto(self):
        return self._salto

    @getSalto.setter
    def setSalto(self, salto):
        self.__salto = salto
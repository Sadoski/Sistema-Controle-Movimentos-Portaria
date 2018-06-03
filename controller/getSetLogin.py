import this

class LoginGetSet(object):
    def __init__(self, login, senha):
        self._login = login
        self._senha = senha

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
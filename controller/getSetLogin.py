import this

class LoginGetSet(object):
    def __init__(self, login, senha):
        _login = login
        _senha = senha

    @property
    def getLogin(self):
        return self.__login

    @getLogin.setter
    def setLogin(self, login):
        this.__login = login

    @property
    def getSenha(self):
        return self.__senha

    @getSenha.setter
    def setSenha(self, senha):
        this.__senha = senha
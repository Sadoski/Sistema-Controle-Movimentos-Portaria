import this

class LoginGetSet(object):
    __login = ''
    __senha = ''

    def getLogin(self):
        return self.__login

    def setLogin(self, login):
        this.__login = login

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        this.__senha = senha
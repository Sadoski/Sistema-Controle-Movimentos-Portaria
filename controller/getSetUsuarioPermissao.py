
class UsuarioPermissoes():
    def __init__(self, idcodigo, idFuncionario, funcionario, setor, cargo, login):
        self._idCodigo = idcodigo
        self._idFuncionario = idFuncionario
        self._funcionario = funcionario
        self._login = login
        self._setor = setor
        self._cargo = cargo

    @property
    def getIdCodigo(self):
        return self._idCodigo

    @getIdCodigo.setter
    def setIdCodigo(self, idCodigo):
        self._idCodigo = idCodigo

    @property
    def getIdFuncionario(self):
        return self._idFuncionario

    @getIdFuncionario.setter
    def setIdFuncionario(self, idFuncionario):
        self._idFuncionario = idFuncionario

    @property
    def getFuncionario(self):
        return self._funcionario

    @getFuncionario.setter
    def setFuncionario(self, funcionario):
        self.__funcionario = funcionario

    @property
    def getLogin(self):
        return self._login

    @getLogin.setter
    def setLogin(self, login):
        self.__login = login

    @property
    def getSetor(self):
        return self._setor

    @getSetor.setter
    def setSetor(self, setor):
        self.__setor = setor

    @property
    def getCargo(self):
        return self._cargo

    @getCargo.setter
    def setCargo(self, cargo):
        self.__cargo = cargo
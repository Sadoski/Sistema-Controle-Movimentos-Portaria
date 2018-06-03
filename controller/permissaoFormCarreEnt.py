class PermissaoFormCarreEnt(object):

    __idFormulario = None
    __ativo = None
    __cadastrar = None
    __cancelar = None
    __deletar = None
    __editar = None

    @property
    def getIdFormulario(self):
        return self.__idFormulario

    def setIdFormulario(self, idFormulario):
        self.__idFormulario = idFormulario

    @property
    def getAtivo(self):
        return self.__ativo

    def setAtivo(self, ativo):
        self.__ativo = ativo

    @property
    def getCadastrar(self):
        return self.__cadastrar

    def setCadastrar(self, cadastrar):
        self.__cadastrar = cadastrar

    @property
    def getCancelar(self):
        return self.__cancelar

    def setCancelar(self, cancelar):
        self.__cancelar = cancelar

    @property
    def getDeletar(self):
        return self.__deletar

    def setDeletar(self, deletar):
        self.__deletar = deletar

    @property
    def getEditar(self):
        return self.__editar

    def setEditar(self, editar):
        self.__editar = editar
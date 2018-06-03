class PermissaoFormEmpresa(object):

    idFormulario = None
    ativo = None
    cadastrar = None
    cancelar = None
    deletar = None
    editar = None

    @property
    def getIdFormulario(self):
        return self.idFormulario

    def setIdFormulario(self, idFormularios):
        self.idFormulario = idFormularios

    @property
    def getAtivo(self):
        print(self.ativo)
        return self.ativo

    @getAtivo.setter
    def setAtivo(self, ativo):
        self.ativo = ativo

    @property
    def getCadastrar(self):
        return self.cadastrar

    def setCadastrar(self, cadastrar):
        self.cadastrar = cadastrar

    @property
    def getCancelar(self):
        return self.cancelar

    def setCancelar(self, cancelar):
        self.cancelar = cancelar

    @property
    def getDeletar(self):
        return self.deletar

    def setDeletar(self, deletar):
        self.deletar = deletar

    @property
    def getEditar(self):
        return self.editar

    def setEditar(self, editar):
        self.editar = editar
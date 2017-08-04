class TipoEmpresa():
    def __init__(self, idTipoEmpresa, descricao):
        self._idTipoEmpresa = idTipoEmpresa
        self._descricao = descricao

    def idTipoempresa(self):
        return self._idTipoEmpresa

    def idTipoEmpresa(self, idTipoEmpresa):
        self._idTipoEmpresa = idTipoEmpresa

    def descricao(self):
        return self._descricao

    def descricao(self, descricao):
        self._descricao = descricao
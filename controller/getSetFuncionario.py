class Funcionario():
    def __init__(self, idFuncionario, idPessoa, idPessoaFisica, cpf, rg, nome, sobrenome, observacao, situacao, civil, deficiencia, categoria, setor, cargo, jornada, admissao, demissao, carteira, pis, serie, uf,  emissao):
        self.__idFuncionario = idFuncionario
        self.__idPessoa = idPessoa
        self.__idPessoaFisica = idPessoaFisica
        self.__cpf = cpf
        self.__rg = rg
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__observacao = observacao
        self.__situacao = situacao
        self.__civil = civil
        self.__deficiencia = deficiencia
        self.__categoria = categoria
        self.__setor = setor
        self.__cargo = cargo
        self.__jornada = jornada
        self.__admissao = admissao
        self.__demissao = demissao
        self.__carteira = carteira
        self.__pis = pis
        self.__serie = serie
        self.__uf = uf
        self.__emissao = emissao


    @property
    def getIdFuncionario(self):
        return self.__idFuncionario

    @getIdFuncionario.setter
    def setIdFuncionario(self, idFuncionario):
        self.__idFuncionario = idFuncionario

    @property
    def getIdPessoa(self):
        return self.__idPessoa

    @getIdPessoa.setter
    def setIdPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    @property
    def getIdPessoaFisica(self):
        return self.__idPessoa

    @getIdPessoaFisica.setter
    def setIdPessoaFisica(self, idPessoaFisica):
        self.__idPessoaFisica = idPessoaFisica

    @property
    def getNome(self):
        return self.__nome

    @getNome.setter
    def setNome(self, nome):
        self.__nome = nome

    @property
    def getSobrenome(self):
        return self.__sobrenome

    @getSobrenome.setter
    def setSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def getRg(self):
        return self.__rg

    @getRg.setter
    def setRg(self, rg):
        self.__rg = rg

    @property
    def getCpf(self):
        return self.__cpf

    @getCpf.setter
    def setCpf(self, cpf):
        self.__cpf = cpf

    @property
    def getObservacao(self):
        return self.__observacao

    @getObservacao.setter
    def setObservcao(self, observacao):
        self.__observacao = observacao

    @property
    def getSituacao(self):
        return self.__situacao

    @getSituacao.setter
    def setSituacao(self, situacao):
        self.__situcao = situacao

    @property
    def getCivil(self):
        return self.__civil

    @getCivil.setter
    def setCivil(self, civil):
        self.__civil= civil

    @property
    def getDeficiencia(self):
        return self.__deficiencia

    @getDeficiencia.setter
    def setDeficiencia(self, deficiencia):
        self.__deficiencia = deficiencia

    @property
    def getCategoria(self):
        return self.__categoria

    @getCategoria.setter
    def setCategoria(self, categoria):
        self.__categoria = categoria

    @property
    def getJornada(self):
        return self.__jornada

    @getJornada.setter
    def setJornada(self, jornada):
        self.__jornada = jornada

    @property
    def getSetor(self):
        return self.__setor

    @getSetor.setter
    def setSetor(self, setor):
        self.__setor = setor

    @property
    def getCargo(self):
        return self.__cargo

    @getCargo.setter
    def setCargo(self, cargo):
        self.__cargo = cargo

    @property
    def getAdmissao(self):
        return self.__admissao

    @getAdmissao.setter
    def setAdmissao(self, admissao):
        self.__admissao = admissao

    @property
    def getDemissao(self):
        return self.__demissao

    @getDemissao.setter
    def setDemissao(self, demissao):
        self.__demissao = demissao

    @property
    def getNumCarteira(self):
        return self.__carteira

    @getNumCarteira.setter
    def setNumCarteira(self, carteira):
        self.__carteira = carteira

    @property
    def getPis(self):
        return self.__pis

    @getPis.setter
    def setPis(self, pis):
        self.__pis = pis

    @property
    def getSerie(self):
        return self.__serie

    @getSerie.setter
    def setSerie(self, serie):
        self.__serie = serie

    @property
    def getUf(self):
        return self.__uf

    @getUf.setter
    def setUf(self, uf):
        self.__uf = uf

    @property
    def getEmissao(self):
        return self.__emissao

    @getEmissao.setter
    def setEmissao(self, emissao):
        self.__emissao = emissao
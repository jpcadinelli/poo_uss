class Pais:
    def __init__(self):
        self.pais = ""

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais = pais


class Estado:
    def __init__(self):
        self.estado = ""
        self.pais = None

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getPais(self):
        return self.pais.getPais()

    def setPais(self, pais):
        self.pais.setPais(pais)


class Cidade:
    def __init__(self):
        self.cidade = ""
        self.estado = None

    def getCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def getEstado(self):
        return self.estado.getEstado()

    def setEstado(self, estado):
        self.estado.setEstado(estado)


class Grupo:
    def __init__(self):
        self.presidente = None
        self.sede = None

    def getPresidente(self):
        return self.presidente

    def setPresidente(self, presidente):
        self.presidente = presidente

    def getSede(self):
        return self.sede

    def setSede(self, sede):
        self.sede = sede

    def getNomeEscolaridadePresidente(self):
        if self.presidente == None:
            return "Grupo sem presidente"
        else:
            return self.presidente.getNomeEscolaridade()

    def getNomePais(self):
        if self.pais == None:
            return "Grupo sem país"
        else:
            return self.pais.getNome()


class Empresa:
    def __init__(self):
        self.grupo = None
        self.diretor = None

    def getGrupo(self):
        return self.grupo

    def setGrupo(self, grupo):
        self.grupo = grupo

    def getDiretor(self):
        return self.diretor

    def setDiretor(self, diretor):
        self.diretor = diretor

    def getNomePais(self):
        if self.grupo == None:
            return "Empresa sem grupo"
        else:
            return self.grupo.getNomePais()

    def getNomeDiretor(self):
        if self.diretor == None:
            return "Empresa sem diretor"
        else:
            return self.diretor.getNome()


class Filial:
    def __init__(self):
        self.empresa = None
        self.cidade = None

    def getEmpresa(self):
        return self.empresa

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def getNomeEstado(self):
        if self.cidade == None:
            return "Filial sem cidade"
        else:
            return self.cidade.getNomeEstado()

    def getNomeDiretor(self):
        if self.empresa == None:
            return "Filial sem empresa"
        else:
            return self.empresa.getNomeDiretor()


class Departamento:
    def __init__(self):
        self.empresa = None
        self.chefia = None

    def getEmpresa(self):
        return self.empresa

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getChefia(self):
        return self.chefia

    def setChefia(self, chefia):
        self.chefia = chefia

    def getNomePais(self):
        if self.empresa == None:
            return "Departamento sem empresa"
        else:
            return self.empresa.getNomePais()

    def getNomeEscolaridadeChefe(self):
        if self.chefe == None:
            return "Departamento sem chefe"
        else:
            return self.chefe.getNomeEscolaridade()


class Funcionario:
    def __init__(self):
        self.nome = ""
        self.alocacao = None
        self.coordenacao = None
        self.escolaridade = None

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getAlocacao(self):
        return self.alocacao

    def setAlocacao(self, alocacao):
        self.alocacao = alocacao

    def getCoordenacao(self):
        return self.coordenacao

    def setCoordenacao(self, coordenacao):
        self.coordenacao = coordenacao

    def getEscolaridade(self):
        return self.escolaridade

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getNomeEscolaridade(self):
        if self.escolaridade == None:
            return "Funcionário sem escolaridade"
        else:
            return self.escolaridade.getNome()

    def getNomePais(self):
        if self.departamento == None:
            return "Funcionário sem Departamento"
        else:
            return self.departamento.getNomePais()

    def getNomeEstado(self):
        if self.filial == None:
            return "Funcionário sem filial"
        else:
            return self.filial.getNomeEstado()

class Escolaridade:
    def __init__(self):
        self.escolaridade = ""

    def getEscolariade(self):
        return self.escolaridade

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade


# 1. Qual a escolaridade do presidente de um grupo?
grupo = Grupo()
presidente = Funcionario()
escolaridade = Escolaridade()
grupo.setPresidente(presidente)
presidente.setEscolaridade(escolaridade)
escolaridade.setNome("Doutorado")
print(grupo.getNomeEscolaridadePresidente())

# 2. Qual o país de alocação de um funcionário?
pais = Pais()
grupo = Grupo()
empresa = Empresa()
departamento = Departamento()
funcionario = Funcionario()
pais.setNome("Brasil")
funcionario.setDepartamento(departamento)
departamento.setEmpresa(empresa)
empresa.setGrupo(grupo)
grupo.setPais(pais)
print(funcionario.getNomePais())

# 3. Qual o estado da filial que um funcionário coordena?
funcionario = Funcionario()
filial = Filial()
cidade = Cidade()
estado = Estado()
estado.setNome("RJ")
funcionario.setFilial(filial)
filial.setCidade(cidade)
cidade.setEstado(estado)
print(funcionario.getNomeEstado())

# 4. Qual a escolaridade do chefe de um departamento?
escolaridade = Escolaridade()
funcionario = Funcionario()
departamento = Departamento()
escolaridade.setNome("Mestrado")
departamento.setChefe(funcionario)
funcionario.setEscolaridade(escolaridade)
print(departamento.getNomeEscolaridadeChefe())

# 5. Qual o nome do diretor da empresa de uma filial?
filial = Filial()
empresa = Empresa()
diretor = Funcionario()
diretor.setNome("Ana")
filial.setEmpresa(empresa)
empresa.setDiretor(diretor)
print(filial.getNomeDiretor())
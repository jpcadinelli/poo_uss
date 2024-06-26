class Pais:
    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class Estado:
    def __init__(self):
        self.pais = None
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setPais(self, pais):
        self.pais = pais

    def getPais(self):
        return self.pais


class Cidade:
    def __init__(self):
        self.estado = None

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def getNomeEstado(self):
        if self.estado == None:
            return "Cidade sem estado"
        else:
            return self.estado.getNome()


class Grupo:
    def __init__(self):
        self.pais = None
        self.presidente = None

    def setPais(self, pais):
        self.pais = pais

    def getPais(self):
        return self.pais

    def setPresidente(self, presidente):
        self.presidente = presidente

    def getPresidente(self):
        return self.presidente

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

    def setGrupo(self, grupo):
        self.grupo = grupo

    def getGrupo(self):
        return self.grupo

    def setDiretor(self, diretor):
        self.diretor = diretor

    def getDiretor(self):
        return self.diretor

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


class Departamento:
    def __init__(self):
        self.empresa = None
        self.chefe = None

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getEmpresa(self):
        return self.empresa

    def setChefe(self, chefe):
        self.chefe = chefe

    def getChefe(self):
        return self.chefe

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


class Filial:
    def __init__(self):
        self.cidade = None
        self.empresa = None

    def setCidade(self, cidade):
        self.cidade = cidade

    def getCidade(self):
        return self.cidade

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getEmpresa(self):
        return self.empresa

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


class Escolaridade:
    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class Funcionario:
    def __init__(self):
        self.departamento = None
        self.escolaridade = None
        self.filial = None
        self.nome = ""

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getEscolaridade(self):
        return self.escolaridade

    def setFilial(self, filial):
        self.filial = filial

    def getFilial(self):
        return self.filial

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

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

# Escreva código em Python que responda as seguintes questões:

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
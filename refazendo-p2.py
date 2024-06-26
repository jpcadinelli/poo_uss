# Classes
class Pais:
    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class Estado():
    def __init__(self):
        self.pais = None
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais = pais

    def getNomePais(self):
        if self.pais == None:
            return "Estado sem País."
        return self.pais.getNome()


class Cidade:
    def __init__(self):
        self.estado = None
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getNomeEstado(self):
        if self.estado == None:
            return "Cidade sem Estado."
        return self.estado.getNome()

    def getNomePais(self):
        if self.estado.getPais() == None:
            return "Cidade sem País."
        return self.estado.getNomePais()


class Grupo:
    def __init__(self):
        self.nome = ""
        self.sede = None
        self.presidente = None

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getSede(self):
        return self.sede

    def setSede(self, sede):
        self.sede = sede

    def getPresidente(self):
        return self.presidente

    def setPresidente(self, presidente):
        self.presidente = presidente

    def getNomeSede(self):
        if self.sede == None:
            return "Grupo sem Sede."
        return self.sede.getNome()

    def getNomePresidente(self):
        if self.presidente == None:
            return "Grupo sem Presidente."
        return self.presidente.getNome()

    def getEscolaridadePresidente(self):
        if self.presidente == None:
            return "Grupo sem Presidente."
        return self.presidente.getNomeEscolaridade()


class Empresa:
    def __init__(self):
        self.nome = ""
        self.grupo = None
        self.diretor = None

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getGrupo(self):
        return self.grupo

    def setGrupo(self, grupo):
        self.grupo = grupo

    def getDiretor(self):
        return self.diretor

    def setDiretor(self, diretor):
        self.diretor = diretor

    def getNomeGrupo(self):
        if self.grupo == None:
            return "Empresa sem Grupo."
        return self.grupo.getNome()

    def getNomePais(self):
        if self.grupo == None:
            return "Empresa sem Grupo."
        return self.grupo.getNomeSede()

    def getNomeDiretor(self):
        if self.diretor == None:
            return "Empresa sem Diretor."
        return self.diretor.getNome()

class Filial:
    def __init__(self):
        self.nome = ""
        self.empresa = None
        self.cidade = None

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getEmpresa(self):
        return self.empresa

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def getNomeEmpresa(self):
        if self.empresa == None:
            return "Filial sem Empresa."
        return self.empresa.getNome()

    def getNomeCidade(self):
        if self.cidade == None:
            return "Filial sem Cidade."
        return self.cidade.getNome()

    def getNomeEstado(self):
        if self.cidade == None:
            return "Filial sem Cidade."
        return self.cidade.getNomeEstado()

    def getDiretorEmpresa(self):
        if self.empresa == None:
            return "Filial sem Empresa."
        return self.empresa.getNomeDiretor()


class Departamento:
    def __init__(self):
        self.nome = ""
        self.empresa = None
        self.chefia = None

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getEmpresa(self):
        return self.empresa

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getChefia(self):
        return self.chefia

    def setChefia(self, chefia):
        self.chefia = chefia

    def getNomeEmpresa(self):
        if self.empresa == None:
            return "Departamento sem Empresa."
        return self.empresa.getNome()

    def getNomeChefia(self):
        if self.chefia == None:
            return "Departamento sem Chefia."
        return self.chefia.getNome()

    def getNomePais(self):
        if self.empresa == None:
            return "Departamento sem Empresa."
        return self.empresa.getNomePais()

    def getEscolaridadeChefia(self):
        if self.chefia == None:
            return "Departamento sem Chefia."
        return self.chefia.getNomeEscolaridade()

class Escolaridade:
    def __init__(self):
        self.nome = ""

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

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

    def getNomeAlocacao(self):
        if self.alocacao == None:
            return "Funcionário sem Alocação."
        return self.alocacao.getNome()

    def getNomeCoordenacao(self):
        if self.coordenacao == None:
            return "Funcionário sem Coordenação."
        return self.coordenacao.getNome()

    def getNomeEscolaridade(self):
        if self.escolaridade == None:
            return "Funcionário sem Escolaridade."
        return self.escolaridade.getNome()

    def getPaisAlocacao(self):
        if self.alocacao == None:
            return "Funcionário sem Alocação."
        return self.alocacao.getNomePais()

    def getEstadoFilial(self):
        if self.coordenacao == None:
            return "Funcionário sem Coordenação."
        return self.coordenacao.getNomeEstado()


# Todas as classes:
## [X] - Pais
## [X] - Estado
## [X] - Cidade
## [X] - Grupo
## [X] - Empresa
## [X] - Filial
## [X] - Departamento
## [X] - Escolaridade
## [X] - Funcionario


# Teste de código:
print("\n*** BRASIL ***")
brasil = Pais()
brasil.setNome("Brasil")
print(brasil.getNome())

print("\n*** ITALIA ***")
italia = Pais()
italia.setNome("Italia")
print(italia.getNome())

print("\n*** RJ ***")
rj = Estado()
rj.setNome("Rio de Janeiro")
rj.setPais(brasil)
print(rj.getNome())
print(rj.getNomePais())

print("\n*** SP ***")
sp = Estado()
sp.setNome("São Paulo")
sp.setPais(brasil)
print(sp.getNome())
print(sp.getNomePais())

print("\n*** VALENÇA ***")
valenca = Cidade()
valenca.setNome("Valença")
valenca.setEstado(rj)
print(valenca.getNome())
print(valenca.getNomeEstado())
print(valenca.getNomePais())

print("\n*** SÃO PAULO ***")
saoPaulo = Cidade()
saoPaulo.setNome("São Paulo")
saoPaulo.setEstado(sp)
print(saoPaulo.getNome())
print(saoPaulo.getNomeEstado())
print(saoPaulo.getNomePais())

print("\n*** GT GROUP ***")
gtGroup = Grupo()
gtGroup.setNome("GT Group")
gtGroup.setSede(brasil)
print(gtGroup.getNome())
print(gtGroup.getNomeSede())
print(gtGroup.getNomePresidente())

print("\n*** DMS LOGISTICS ***")
dms = Grupo()
dms.setNome("DMS Logistics")
dms.setSede(brasil)
print(dms.getNome())
print(dms.getNomeSede())
print(dms.getNomePresidente())

print("\n*** GT ***")
gt = Empresa()
gt.setNome("GT")
gt.setGrupo(gtGroup)
print(gt.getNome())
print(gt.getNomeGrupo())

print("\n*** DGTAL LAB ***")
dgtallab = Filial()
dgtallab.setNome("DGtal Lab")
dgtallab.setEmpresa(gt)
dgtallab.setCidade(valenca)
print(dgtallab.getNome())
print(dgtallab.getNomeEmpresa())
print(dgtallab.getNomeCidade())

print("\n*** PROGRAMAÇÃO ***")
programacao = Departamento()
programacao.setNome("Programação")
programacao.setEmpresa(gt)
print(programacao.getNome())
print(programacao.getNomeEmpresa())
print(programacao.getNomeChefia())

print("\n*** FUNDADOR ***")
fundador = Departamento()
fundador.setNome("Fundador")
fundador.setEmpresa(gt)
print(fundador.getNome())
print(fundador.getNomeEmpresa())
print(fundador.getNomeChefia())

print("\n*** MESTRADO ***")
mestrado = Escolaridade()
mestrado.setNome("Mestrado")
print(mestrado.getNome())

print("\n*** SEGUNDO GRAU ***")
segundoGrau = Escolaridade()
segundoGrau.setNome("Segundo Grau")
print(segundoGrau.getNome())

print("\n*** DIEGO ***")
diego = Funcionario()
diego.setNome("Diego")
diego.setAlocacao(fundador)
diego.setCoordenacao(dgtallab)
diego.setEscolaridade(mestrado)
print(diego.getNome())
print(diego.getNomeAlocacao())
print(diego.getNomeCoordenacao())
print(diego.getNomeEscolaridade())
gtGroup.setPresidente(diego)
gt.setDiretor(diego)
fundador.setChefia(diego)

print("\n*** JP ***")
jp = Funcionario()
jp.setNome("João Pedro")
jp.setAlocacao(programacao)
jp.setEscolaridade(segundoGrau)
print(jp.getNome())
print(jp.getNomeAlocacao())
print(jp.getNomeCoordenacao())
print(jp.getNomeEscolaridade())


# Perguntas que tenho que responder:
print("\nRespostas da Prova:")

## 1. Qual a escolaridade do presidente do grupo?
print(f"Resposta 1: {gtGroup.getEscolaridadePresidente()}")

## 2. Qual o país de alocação de um funcionário?
print(f"Resposta 2: {jp.getPaisAlocacao()}")

## 3. Qual o estado da filial que um funcionário coordena?
print(f"Resposta 3: {diego.getEstadoFilial()}")

## 4. Qual a escolaridade do chefe de um departamento?
print(f"Resposta 4: {fundador.getEscolaridadeChefia()}")

## 5. Qual o nome do diretor da empresa de uma filial?
print(f"Resposta 5: {dgtallab.getDiretorEmpresa()}")

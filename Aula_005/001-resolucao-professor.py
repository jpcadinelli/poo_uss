class Escolaridade:
    def _init_(self):
        self.nome = ""
    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome

class Pessoa:
    def _init_(self):
        self.escolaridade = None
    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    def getEscolaridade(self):
        return self.escolaridade
    def getNomeEscolaridade(self):
        if self.escolaridade == None:
            return "Pessoa sem escolaridade"
        else:
            return self.escolaridade.getNome()


class Professor(Pessoa):
    def _init_(self):
        Pessoa._init_(self)

class Curso:
    def _init_(self):
        self.coordenador = None
    def setCoordenador(self, professor):
        self.coordenador = professor
    def getCoordenador(self):
        return self.coordenador
    def getNomeEscolaridadeCoordenador(self):
        if self.coordenador == None:
            return "Curso sem coordenador"
        else:
            return self.coordenador.getNomeEscolaridade()

class Escola:
    def _init_(self):
        self.diretor = None
    def setDiretor(self, professor):
        self.diretor = professor
    def getDiretor(self):
        return self.diretor
    def getNomeEscolaridadeDiretor(self):
        if self.diretor == None:
            return "Escola sem diretor"
        else:
            return self.diretor.getNomeEscolaridade()


escolaridade = Escolaridade()
escolaridade.setNome("Doutorado")
professor = Professor()
professor.setEscolaridade(escolaridade)
print(professor.getNomeEscolaridade())
curso = Curso()
curso.setCoordenador(professor)
print(curso.getNomeEscolaridadeCoordenador())
escola = Escola()
escola.setDiretor(professor)
print(escola.getNomeEscolaridadeDiretor())
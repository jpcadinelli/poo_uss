class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.naturalidade = Cidade()
        self.escolaridade = Escolaridade()
   
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
       
    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()
        self.curso = Curso()

class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.centratacao = Curso()

class Escola:
    def __init__(self):
        self.nomeEscola = ""
        self.direcao = Professor()
        self.cidade = Cidade()

class Curso:
    def __init__(self):
        self.nomeCurso = ""
        self.cordenacao = Professor()
        self.tipoEnsino = TipoEnsino()
        self.escola = Escola()

class TipoEnsino:
    def __init__(self):
        self.tipoEnsino = ""

class Escolaridade:
    def __init__(self):
        self.escolaridade = ""

class Estado:
    def __init__(self):
        self.estado = ""
        self.pais = ""

class Cidade:
    def __init__(self):
        self.estado = Estado()
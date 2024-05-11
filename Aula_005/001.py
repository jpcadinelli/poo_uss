class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.naturalidade = Cidade()
        self.escolaridade = Escolaridade()

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
        self.direcao = Professor()
        self.cidade = Cidade()

class Curso:
    def __init__(self):
        self.cordenacao = Professor()
        self.tipoEnsino = TipoEnsino()

class TipoEnsino:
    def __init__(self):
        pass

class Escolaridade:
    def __init__(self):
        pass

class Estado:
    def __init__(self):
        pass

class Cidade:
    def __init__(self):
        self.estado = Estado()
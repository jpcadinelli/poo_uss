class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.naturalidade = Cidade()

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()

class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.centratacao = Professor()

class Escola:
    def __init__(self):
        self.direcao = Professor()

class Curso:
    def __init__(self):
        self.cordenacao = Professor()

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
        pass
# Classes: Aluno, Aluno Graduacao, Aluno Pos Graduacao

# Aluno: nome, matricula, nota 1, nota 2, método para calcular média
class Aluno:

    def __init__(self):
        self.nome = ""
        self.matricula = 0
        self.nota1 = 0.0
        self.nota2 = 0.0
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setMatricula(self, matricula):
        self.matricula = matricula
    
    def getMatricula(self):
        return self.matricula
    
    def setNota1(self, nota1):
        self.nota1 = nota1
    
    def getNota1(self):
        return self.nota1
    
    def setNota2(self, nota2):
        self.nota2 = nota2
    
    def getNota2(self):
        return self.nota2
    
    def calculaMedia(self):
        return (self.nota1 + self.nota2) / 2

# Aluno Graduacao: método para verificar aprovação (média >= 6)
class AlunoGraduacao(Aluno):

    def __init__(self):
        Aluno.__init__(self)
    
    def verificaAprovacao(self):
        return (self.calculaMedia() >= 6)
    
# Aluno Pós Graduacao: método para verificar aprovação (média >= 7)
class AlunoPosGraduacao(Aluno):
    
    def __init__(self):
        Aluno.__init__(self)
    
    def verificaAprovacao(self):
        return (self.calculaMedia() >= 7)

agbom = AlunoPosGraduacao()
agbom.setNota1(5.0)
agbom.setNota2(7.0)
print(agbom.verificaAprovacao())
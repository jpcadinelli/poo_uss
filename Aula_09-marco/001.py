class Aluno:

    def __init__(self):
        self.nome = ''

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
aluno = Aluno()
aluno.setNome('João')
print(aluno.getNome())

aluno2 = Aluno()
aluno2.setNome('Maria')
print(aluno2.getNome())
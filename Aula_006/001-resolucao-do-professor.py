class Pessoa():
    def _init_(self):
        self.nome = ""
    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome

class Aluno(Pessoa):
    def _init_(self):
        Pessoa._init_(self)

class Turma():
    def _init_(self):
        self.alunos = []

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def exibirNomesAlunos(self):
        for aluno in self.alunos:
            print(aluno.getNome())

    def verificarAluno(self, aluno):
        return aluno in self.alunos

    def excluirAluno(self, aluno):
        self.alunos.remove(aluno)


turma = Turma()
aluno1 = Aluno()
aluno1.setNome("Joao")
aluno2 = Aluno()
aluno2.setNome("Maria")
aluno3 = Aluno()
aluno3.setNome("Ana")

# Questao 2
turma.matricular(aluno1)
turma.matricular(aluno2)
turma.exibirNomesAlunos()

# Questao 7
print(turma.verificarAluno(aluno1))
print(turma.verificarAluno(aluno3))

# Questao 10
turma.excluirAluno(aluno1)
print(turma.verificarAluno(aluno1))
class ProdutoBiblioteca:
    def __init__(self):
        self.titulo = ""
        self.ano = 0
        self.editora = ""

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo

    def setAno(self, ano):
        self.ano = ano

    def getAno(self):
        return self.ano

    def setEditora(self, editora):
        self.editora = editora

    def getEditora(self):
        return self.editora

class Livro(ProdutoBiblioteca):
    def __init__(self):
        ProdutoBiblioteca.__init__(self)
        self.autor_principal = ""
        self.isbn = 0
        self.estado = "Disponível"
        self.quantidade_emprestimo = 0

    def setAutorPrincipal(self, autor_pricipal):
        self.autor_principal = autor_pricipal

    def getAutorPricipal(self):
        return self.autor_principal

    def setIsbn(self, isbn):
        self.isbn = isbn

    def getIsbn(self):
        return self.isbn

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setQuantidadeEmprestimo(self, quantidade_emprestimo):
        self.quantidade_emprestimo = quantidade_emprestimo

    def getQuantidadeEmprestimo(self):
        return self.quantidade_emprestimo

    def atualizaQuantidadeEmprestimo(self):
        self.quantidade_emprestimo += 1

    def emprestarLivro(self):
        if self.estado == "Disponível":
            self.estado = "Emprestado"
            self.atualizaQuantidadeEmprestimo()
        else:
            print("Livro sob empréstimo.")

    def devolverLivro(self):
        self.estado = "Disponível"

    def exibirLivro(self):
        print("Título:", self.titulo)
        print("Ano:", self.ano)
        print("Editora:", self.editora)
        print("Autor principal:", self.autor_principal)
        print("isbn", self.isbn)
        print("Estado:", self.estado)
        print("Quantidade de empréstimos:", self.quantidade_emprestimo)

class Revista(ProdutoBiblioteca):
    def __init__(self):
        ProdutoBiblioteca.__init__(self)
        self.issn = 0

    def setIssn(self, issn):
        self.issn = issn

    def getIssn(self):
        return self.issn

    def exibirRevista(self):
        if 2024 <= 5 + self.ano:
            print("Título:", self.titulo)
            print("Ano:", self.ano)
            print("Editora:", self.editora)
            print("issn", self.issn)
        else:
            print("Não pode exibir dados da revista.")

class Pessoa:
    def __init__(self):
        self.nome = ""
        self.telefone = ""
        self.email = ""

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getTelefone(self):
        return self.telefone

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

class TrabalhadorBiblioteca(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.matricula = 0
        self.tempo_servico = 0

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def setTempoServico(self, tempo_servico):
        self.tempo_servico = tempo_servico

    def getTempoServico(self):
        return self.tempo_servico

class Bibliotecario(TrabalhadorBiblioteca):
    def __init__(self):
        TrabalhadorBiblioteca.__init__(self)
    def calcularSalario(self):
        return (2000 + (200 * self.tempo_servico))

    def exibirBibliotecário(self):
        print("Nome:", self.nome)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        print("Matrícula:", self.matricula)
        print("Tempo de serviço:", self.tempo_servico)
        print("Salário: R$", self.calcularSalario())

class Leitor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.endereco = []
        self.idade = 0

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def validar(self):
        if self.idade < 18:
            return print("O leitor não pode fazer empréstimo de livros!")
        else:
            return print("Os empréstimos estão liberados")

    def incrementarIdade(self):
        self.idade += 1

    def diminuirIdade(self):
        self.idade -= 1

    def exibirLeitor(self):
        print("Nome:", self.nome)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        print("Endereço:", self.endereco)
        print("Idade:", self.idade)
        self.validar()

class Faxineiro(TrabalhadorBiblioteca):
    def __init__(self):
        TrabalhadorBiblioteca.__init__(self)

    def calcularSalario(self):
        return (1500 + (75 * self.tempo_servico))

    def exibirFaxineiro(self):
        print("Nome:", self.nome)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        print("Matrícula:", self.matricula)
        print("Tempo de serviço:", self.tempo_servico)
        print("Salário: R$", self.calcularSalario())

#Execução dos códigos
#Classe Livro
print("******Testando*Livro********")
codigoLimpo = Livro()
codigoLimpo.setTitulo("Código Limpo")
codigoLimpo.setAno(2020)
codigoLimpo.setEditora("Editora Marcão")
codigoLimpo.setIsbn(123456789)
codigoLimpo.setAutorPrincipal("Marco Antônio")
codigoLimpo.exibirLivro()
print("")
codigoLimpo.emprestarLivro()
codigoLimpo.exibirLivro()
print("")
codigoLimpo.devolverLivro()
codigoLimpo.exibirLivro()
print("****************************")

#Classe Revista
print("")
print("******Testando*Revista*******")
revistaVeja = Revista()
revistaVeja.setTitulo("Veja")
revistaVeja.setAno(2019)
revistaVeja.setEditora("Editora Marcão")
revistaVeja.setIssn(987654321)
revistaVeja.exibirRevista()
print("****************************")
revistaVeja2 = Revista()
revistaVeja2.setTitulo("Veja")
revistaVeja2.setAno(2018)
revistaVeja2.setEditora("Editora Marcão")
revistaVeja2.setIssn(987123645)
revistaVeja2.exibirRevista()
print("****************************")

#Classe Bibliotecario
print("")
print("*****Testando*Bibliotecario*****")
bibliotecario = Bibliotecario()
bibliotecario.setNome("Marcão")
bibliotecario.setTelefone("(99) 99999-9999")
bibliotecario.setEmail("vascodagama@omaior.com")
bibliotecario.setMatricula(2019111)
bibliotecario.setTempoServico(5)
bibliotecario.exibirBibliotecário()
print("********************************")

#Classe Leitor
print("")
print("*****Teste*Leitor*****")
leitor = Leitor()
leitor.setNome("Marco Antônio")
leitor.setTelefone("(99) 999999-9999")
leitor.setEmail("omaior@vascodagama.com")
leitor.setEndereco(['rua O maior do brasil', 10, "Casa", "Vasco da Gama", "Juiz de Fora", "MG", "200000-000"])
leitor.setIdade(20)
leitor.exibirLeitor()
print("********************************")
leitor2 = Leitor()
leitor2.setNome("Gabriel")
leitor2.setTelefone("(99) 999999-9999")
leitor2.setEmail("programa-no-terminal@maluco.com")
leitor2.setEndereco(['rua Programo no Terminal', 10, "Casa", "Bairro Alegria", "Piraí", "RJ", "200000-000"])
leitor2.setIdade(17)
leitor2.exibirLeitor()
print("")
leitor2.incrementarIdade()
leitor2.exibirLeitor()
print("")
leitor2.diminuirIdade()
leitor2.exibirLeitor()
print("********************************")

#Classe Faxineiro
print("")
print("*****Testando*Faxineiro*****")
faxineiro = Faxineiro()
faxineiro.setNome("João Pedro")
faxineiro.setTelefone("(99) 99999-9999")
faxineiro.setEmail("jpcadinelli@gmail.com")
faxineiro.setMatricula(2022111)
faxineiro.setTempoServico(2)
faxineiro.exibirFaxineiro()
print("********************************")
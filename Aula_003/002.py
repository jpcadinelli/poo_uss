# Classe Pessoa:

# Atributos: nome, idade, altura, peso
# Métodos: envelhecer, crescer, ganhar_peso, perder_peso
#     • envelhecer(): Aumenta a idade da pessoa em um ano.
#     • Crescer(centímetros): Aumenta a altura da pessoa em centímetros, se a pessoa tiver menos de 21 anos.
#     • Ganhar_peso(quilos): Aumenta o peso da pessoa em quilos.
#     • Perder_peso(quilos): Diminui o peso da pessoa em quilos.

class Pessoa:

    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.altura = 0
        self.peso = 0

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade = idade
    
    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self.altura = altura
    
    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso

    def envelhecer(self):
        self.idade += 1

    def crescer(self, centimetros):
        if self.idade < 21:
            if centimetros > 0:
                self.altura += centimetros

    def ganharPeso(self, quilos):
        if quilos > 0:
            self.peso += quilos

    def perderPeso(self, quilos):
        if quilos > 0 and quilos <= self.peso:
            self.peso -= quilos


pessoa = Pessoa()
print(pessoa.getIdade())
pessoa.setIdade(19)
print(pessoa.getIdade())
pessoa.envelhecer()
print(pessoa.getIdade())
print(pessoa.getAltura())
pessoa.setAltura(180)
print(pessoa.getAltura())
pessoa.crescer(5)
print(pessoa.getAltura())
print(pessoa.getPeso())
pessoa.ganharPeso(10)
print(pessoa.getPeso())
pessoa.perderPeso(11)
print(pessoa.getPeso())
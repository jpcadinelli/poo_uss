# Classe Carro:

# Atributos: marca, modelo, ano, cor, velocidade_atual
# Métodos: acelerar, frear, ligar, desligar
# •	acelerar(quantidade): aumenta a velocidade atual do carro pela quantidade especificada.
# •	frear(quantidade): diminui a velocidade atual do carro pela quantidade especificada, sem deixar que a velocidade fique negativa.
# •	ligar(): altera o estado do carro para ligado.
# •	desligar(): altera o estado do carro para desligado e zera a velocidade atual.

class Carro:

    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.ano = 0
        self.cor = ""
        self.velocidade_atual = 0
        self.estado = "desligado"

    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getAno(self):
        return self.ano
    
    def setAno(self, ano):
        self.ano = ano

    def getCor(self):
        return self.cor
    
    def setCor(self, cor):
        self.cor = cor

    def getVelocidade_atual(self):
        return self.velocidade_atual
    
    def setVelocidade_atual(self, velocidade_atual):
        self.velocidade_atual = velocidade_atual

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado

carro = Carro()
carro.setMarca("VW")
print(carro.getMarca())
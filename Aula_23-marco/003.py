# Classe Produto:
# Atributos: nome, preco, quantidade_estoque, categoria
# Métodos: adicionar_estoque, remover_estoque, aplicar_desconto
#     • adicionar_estoque(quantidade): Adiciona quantidade ao quantidade_estoque.
#     • remover_estoque(quantidade): Remove quantidade do quantidade_estoque, se houver quantidade suficiente.
#     • aplicar_desconto(percentual): Aplica um desconto de percentual ao preco do produto.

class Produto:

    def __init__(self):
        self.nome = ""
        self.preco = 0
        self.quantidade = 0 
        self.categoria = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getCategoria(self):
        return self.categoria

    def setCategoria(self, categoria):
        self.categoria = categoria

    def adicionarEstoque(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade

    def removerEstoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade

    def aplicarDesconto(self, percentual):
        if 0 <= percentual <= 100:
            self.preco = self.preco * ((100 - percentual) / 100)


# preco = 50
# desconto = 10
# preco final = 45
# 50 * ((100 - 10) / 100)
# 50 * (90 / 100)
# 50 * 0.9
# 45


produto = Produto()
print(produto.quantidade)
produto.adicionarEstoque(10)
print(produto.quantidade)
produto.removerEstoque(8)
print(produto.quantidade)

produto.setPreco(50)

produto.aplicarDesconto(-10)
print(produto.getPreco())
produto.aplicarDesconto(110)
print(produto.getPreco())

produto.aplicarDesconto(10)
print(produto.getPreco())
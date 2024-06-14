from typing import Type

class Interruptor:
    def __init__(self, comodo):
        self.__comodo = comodo

    def acender(self):
        print("acendendo {}".format(self.__comodo))

    def apagar(self):
        print("apagando {}".format(self.__comodo))

class Pessoa:
    def acenderLuz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagarLuz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print("Fui dormir...")

if __name__ == "__main__":
    jp = Pessoa()
    interruptor_quarto = Interruptor("quarto")
    jp.acenderLuz(interruptor_quarto)
    jp.apagarLuz(interruptor_quarto)
    jp.dormir()

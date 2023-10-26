# uma classe abstrata é utilizado na criação de uma classe que não deve ser instanciada. Ela será utilizada apenas de modelo
# exemplo:

from abc import*

class Poligono(ABC):
    @abstractclassmethod
    def __init__(self):
        self.lado = None

    def qtd_lados(self):
        return self.lado

class Quadrado(Poligono):
    def __init__(self):
        self.lado = 4

    def qtd_lados(self):
        return self.lado
    
class Triangulo(Poligono):
    def __init__(self):
        self.lado = 3

    def qtd_lados(self):
        return self.lado
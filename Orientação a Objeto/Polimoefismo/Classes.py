class Veiculo:

    def locomocao(self):
        return ("Indefinido")


class Carro(Veiculo):
    
    def locomocao(self):
        return("Locomove no meio terrestre")

class Aviao(Veiculo):

    def locomocao(self):
        return("Locomove no céu")

class Navio(Veiculo):

    def locomocao(self):
        return("Locomove no ambiente aquático")

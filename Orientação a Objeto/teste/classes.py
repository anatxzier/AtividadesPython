class Loja:
    def __init__(self, nome, end, CNPJ):
        self.nome = nome
        self.end = end
        self.CNPJ = CNPJ
        self.cliente = []
        self.produto = []
        self.ADM = []
        self.Master = ADM("Master", 123)
        
    def getMaster(self):
        return self.Master

class Cliente:
    def __init__(self):
        self.nome_cli = None
        self.data = None
        self.cpf = None
        self.ende = None
        self.senha = None
        self.carrinho = {}
######################################
# Ana Júlia
    def add_produto(self, indice):
        produto_escolhido = indice
        if produto_escolhido in self.add_produto:
            self.carrinho.append(produto_escolhido)
        else: 
            print("Esse produto não existe")
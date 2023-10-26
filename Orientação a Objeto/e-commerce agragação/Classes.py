class Usuario:
    def __init__(self):
        self.usuarios = {}


    def novo_usuario(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.usuarios[self.nome] = self.senha

    def login(self,nome,senha):
        if nome in self.usuarios and senha in self.usuarios[self.nome] == self.senha:
            print ("Bem Vindo")
        else:
            print("Faça login antes")

        


class Produtos:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, nome_produto, preço):
        self.nome_produto = nome_produto
        self.preço = preço
        self.produtos[self.nome_produto] = self.preço

    def listar_produtos(self):
         for nomeproduto, valorr in self.produtos.items():
             print(f"Produto: {nomeproduto} - Valor: {valorr}")

    def adicionar_carrinho(self):
        #comp
        self.car = Carrinho()
        #adiconar 1 dic no outro



class Carrinho:
    def __init__(self):
        self.carrinho = {}
        
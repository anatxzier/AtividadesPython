class Cadastro_user:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = None

    def inserir_endereco (self,cid,est):
        self.endereco = Endereco(cid,est)

    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def getEndereço(self):
        return self.endereco
    
    def __del__(self):
        print(f"{self.nome} - Objeto Excluído")


class Endereco:
    def __init__(self, cidade,estado):
        self.cidade = cidade
        self.estado = estado

    def getCidade(self):
        return self.cidade
    
    def getEstado(self):
        return self.estado
    
    def __del__(self):
        print(f"{self.cidade} - Objeto Excluído")
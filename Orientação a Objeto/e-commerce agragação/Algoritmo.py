from Classes import *

usuario = Usuario()
produto = Produtos()
def cadastro_cliente():
    nome_cliente = str(input("Nome: "))
    senha_cliente = str(input("Senha: "))
    usuario.novo_usuario(nome_cliente, senha_cliente)
    print("Novo usuário registrado")

def login_cliente():
    nome_cliente = str(input("Nome: "))
    senha_cliente = str(input("Senha: "))
    usuario.login(nome_cliente,senha_cliente)

def us_cadastro_produto():
    print("Para adicionar um produto: \n 1º - Informe o nome do produto \n 2º Informe o valor do produto")
    nome_produto = str(input("Nome >  "))
    preço = float(input("Valor >  "))
    produto.cadastrar_produto(nome_produto,preço)
    print("Produto criado")



def main():

    x = True    

    while x == True:
        try:


            print("Bem vindo ao E-commerce")
            print("O que deseja fazer? \n [1] Cadastro Usuário \n [2] Login \n [3] Comprar \n [4] Sair")
            escolha1 = int(input(">> "))

            match escolha1:
                case 1:
                    print("Para se cadastrar informe Nome e Senha")
                    cadastro_cliente()                   

                case 2:
                    print("Insira seu nome de usuario")
                    login_cliente()
                case 3: 
                    print("--> Opções <-- \n [1] Cadastrar produto \n [2] Listar produtos \n [3] Adicionar produto ao carrinho \n [4] Adicionar produto ao carrinho \n [5] Vizualizar carrinho \n [6] Excluir produto do carrinho \n [7] Sair ")
                    escolha2 = int(input(">> "))
                    match escolha2:
                        case 1:
                            print("O que vai adicionar?")
                            us_cadastro_produto()
                        case 2:
                            print("Aqui estão os produtos registrados no Seu Usuário")
                            produto.listar_produtos()
                        case 3:
                            pass
                        case 4:
                            pass
                        case 5:
                            pass
                        case 6:
                            pass
                        case 7:
                            print("Fechando...")
                            break




                case 4:
                    print("Saindo...")
                    break



        except Exception as erro:
            (print("Valor Inválido"))
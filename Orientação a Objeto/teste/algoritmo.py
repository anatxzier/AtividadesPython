from classes import *

cliente = Cliente()

def Main():

    while True:
        try:

            print("Bem Vindo Dev Five Ecommerce")
            print("Escolha uma opção \n [1] Login Cliente \n [2] Login ADM \n [3] Sair")
            escolha1 = int(input(">> "))
            
            match escolha1:
                case 1:
                    print("Página do cliente")
                    print("Escolha uma opção \n [1] Produtos disponiveis [2] Adicionar produto ao carrinho \n [3] Visualizar carrinho \n [4] Excluir produto \n [5] Finalizar compra \n [6] Retornar ao menu \n [7] Log Out" )
                    escolha2 = int(input(">> "))
                    match escolha2:
                        case 1:
                            pass
                        case 2:
                            print("Escolha o produto que deseja e digite seu índice para adiciona-lo ao carrinho")
                            escolha_produto = int(input(">> "))
                            cliente.add_produto(escolha_produto)
                        case 3:
                            pass
                        case 4:
                            pass
                        case 5:
                            pass
                        case 6:
                            pass
                        case 7:
                            break
                        case _:
                            print("Opção Inexistente")
                case 2:
                    print("Página do Administrador")
                    print("Escolha uma opção \n [1] Cadastrar cliente \n [2] Listar cliente \n [3] Excluir cliente \n [4] Cadastrar administrador \n [5] Listar administrador \n [6] Excluir administrador \n [7] Cadastrar produtos \n [8] Listar produtos \n [9] Exluir produtos \n [10] Voltar ao menu \n [11] Log Out ")
                    escolha3 = int(input(">> "))
                    match escolha3:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            pass
                        case 4:
                            pass
                        case 5:
                            pass
                        case 6:
                            pass
                        case 7:
                            pass
                        case 8:
                            pass
                        case 9:
                            pass
                        case 10:
                            pass
                        case 11:
                            break

                        case _:
                            print("Opção Inexistente")
                case 3:
                    break

        except Exception as erro:
            ("Invalido")
from Controller import *
import os

sair = 0
while sair == 0:
    print("-> SOFTWARE TO-DO <- \n \n [1] ADICIONAR TAREFA \n [2] LISTAR TAREFA \n [3] EXCLUIR TAREFA \n [4] SAIR \n ")
    menu = input("QUAL OPÇÃO DESEJA? \n ")
    os.system("cls")

    match menu:
        case "1":
            tarefa = input("DIGITE A TAREFA \n ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            os.system("cls")            
        case "2":
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")
        case "3":
            listarTarefa = ControllerListarTarefa()
            excluir = input("Qual o índice da tarefa que deseja excluir? \n ")
            excluirTarefa = ControllerExcluirTarefa (excluir)
            os.system("pause")
            os.system("cls")
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")    
        case "4":
            print("SAINDO...")
            break
        case _:
            print("Inexistente")
            os.system("pause")
            os.system("cls")

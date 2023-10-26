from Controller import *
import os

sair = 0
while sair == 0:
    print("-> SOFTWARE TO-DO <- \n \n [1] ADICIONAR TAREFA \n [2] LISTAR TAREFA \n [3] ALTERAR TAREFA \n [4] EXCLUIR \n [5] SAIR ")
    menu = input("QUAL OPÇÃO DESEJA? \n ")
    os.system("cls")

    match menu:
        case "1":
            #adicionar tarefa
            tarefa = input("DIGITE A TAREFA \n ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            os.system("cls")            
        case "2":
            #listar tarefas
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")
        case "3":
            listarTarefa = ControllerListarTarefa()
            nova_tarefa = input("Digite a nova tarefa \n")
            indice = input("Digite o índice da tarefa que deseja excluir")
            tarefaAlterada = ControllerMudarTarefa(nova_tarefa, indice, "A")
            os.system("pause")
            os.system("cls")

        case"4":
            #concluir tarefa
            pass

        case "5":
            #listar tarefas concluidas
            pass

        case "6":
            #excluir tarefas
            listarTarefa = ControllerListarTarefa()
            excluir = input("Qual o índice da tarefa que deseja excluir? \n ")
            excluirTarefa = ControllerExcluirTarefa (excluir)
            os.system("pause")
            os.system("cls")
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")    

        case "7":
            print("SAINDO...")
            break
        case _:
            print("Inexistente")
            os.system("pause")
            os.system("cls")

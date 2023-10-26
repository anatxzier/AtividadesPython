from Dao import *
from Model import *
from random import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        try:
            self.tarefa = tarefa
            id = randint(1000, 9999)
            count = -1
            if len(TODO.listar_tarefa()) > 1:
                for tarefas in TODO.listar_tarefa():
                    count += 1
                    if count >= 1:
                        tarefas = tarefas[:4]
                        tarefas = int(tarefas)
                        if id != tarefas:
                            if self.tarefa == "":
                                print("Inválido")
                            else:
                                if TODO.adicionar_tarefa(self.tarefa, id) == True:
                                    print("Tarefa Adicionada")
                                    break

                                else:
                                    print("Problema encontrado")
                                    break

                        else:
                            id = randint(1000,9999)
            else:
                if self.tarefa == "":
                    print("Informe uma tarefa")

                else:
                    if TODO.adicionar_tarefa(self.tarefa,id) == True:
                        print("Tarefa adicionada")

                    else:
                        print("Problema Encontrado")


        except Exception:
            print("Opção inválido")
        

class ControllerExcluirTarefa:
    def __init__(self, excluir):

        try:
            x = int(excluir)
            self.excluir = x - 1

            if TODO.excluir_tarefa(self.excluir):
                print("Tarefa Excluída \n ")
            else:
                print("Não foi possível realizar esta ação")
        except Exception:
            print("Valor inválido")

        
class ControllerListarTarefa():
    def __init__(self):
        cont = -1
        for tarefa in TODO.listar_tarefa():
            cont += 1
            if cont >= 1:
                tarefa = tarefa[5:-1]
                print(f"{cont} - {tarefa}")

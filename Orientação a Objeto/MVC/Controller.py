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
                    status = "A"
                    count =-1
                    if count >= 1:
                        tarefas = tarefas.split(maxsplit=3)
                        tarefas = tarefas[0]
                        tarefas = int(tarefas)
                        if id != tarefas:
                            if self.tarefa == "":
                                print("Inválido")
                            else:
                                if TODO.adicionar_tarefa(self.tarefa, id, status) == True:
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
                    status = "A"
                    if TODO.adicionar_tarefa(self.tarefa,id, status) == True:
                        print("Tarefa adicionada")

                    else:
                        print("Problema Encontrado")


        except Exception as e:
            print("An error occurred:", str(e))

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
                tarefa = tarefa[7:-1]
                print(f"{cont} - {tarefa}")

class ControllerMudarTarefa:
    def __init__(self, tarefa_Nova, indice, Letra):
        try:
            indice = int(indice)
            if tarefa_Nova == "":
                print("Digite novamente, tarefa inválida")
            else:

                lista_id = []
                dao = DaoListar()
                cont = -1
                for tarefas in dao.listar():
                    cont += 1
                    if cont >= 1:
                        letra = tarefas[:1]
                        if letra == "A":
                            lista = tarefas.split("\t", 4)               
                            id = lista[1]
                            id = int(id)
                            lista_id.append(id)
                if indice <= len(lista_id):
                    indice -=1
                    cont = -1
                    for tarefas in dao.listar():
                        cont += 1
                        if cont >= 1:
                            lista = tarefas.split("\t", 4)               
                            id = lista[1]
                            id = int(id)
                            tarefa_A = tarefas[7:-1]
                            if id == lista_id[indice]:
                                if Letra == "A":
                                    tarefa_Atualizada = f"A\t{id}\t{tarefa_Nova}\n"
                                    TODO.alterarTarefa(tarefas, tarefa_Atualizada)
                                    break
                                else:
                                    tarefa_Atualizada = f"{Letra}\t{id}\t{tarefa_A}\n"
                                    TODO.alterarTarefa(tarefas, tarefa_Atualizada)
                                    break
                else:
                    print("Indice inválido, tente novamente")
        except Exception:
            print("Inválido")
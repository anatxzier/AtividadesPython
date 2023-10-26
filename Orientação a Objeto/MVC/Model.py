from Dao import *

class ToDo():
    def adicionar_tarefa(self, tarefa, x):
        dao = DaoAdicionar(tarefa)
        return dao.AdicionarTarefa(x)

    def excluir_tarefa(self, excluir):

        return True
        

    def listar_tarefa(self):
        dao2 = DaoListar()
        return dao2.listar()
TODO = ToDo()
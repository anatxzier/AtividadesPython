from Dao import *

class ToDo():
    def adicionar_tarefa(self, tarefa, x, status):
        dao = DaoAdicionar(tarefa)
        return dao.AdicionarTarefa(x, status)

    def excluir_tarefa(self, excluir):

        return True
        

    def listar_tarefa(self):
        dao2 = DaoListar()
        return dao2.listar()
    
    def alterarTarefa(self):
        dao3 = DaoMudarTarefa()
        return
TODO = ToDo()
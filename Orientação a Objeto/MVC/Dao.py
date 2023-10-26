Arquivo = "ToDo.txt"

class DaoAdicionar:
    def __init__(self,tarefa):
        self.tarefa = tarefa

    def AdicionarTarefa(self,x, status):
            with open(Arquivo, "a") as arquivo:
                tarefa_formatada = f"{status} \t\t{x} \t {self.tarefa}"

            with open(Arquivo, "r") as arquivo:
                ler = arquivo.read()
                
            with open(Arquivo, "a") as arquivo:
                if "Status: \tID: \tTarefa:" not in ler:
                    arquivo.write(f"Status: \tID: \tTarefa:\n")
                arquivo.write(f"{tarefa_formatada}\n")
                return True

    
class DaoListar:
    def listar(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas
        
class DaoMudarTarefa:
    def mudarTarefa(self, tarefa_Antiga, tarefa_Nova):
        with open(Arquivo, "r") as arquivo:
            conteudo = arquivo.read()

        conteudo_Atualizado = conteudo.replace(tarefa_Antiga, tarefa_Nova)
        with open(Arquivo, "w") as arquivo2:
            arquivo2.write(conteudo_Atualizado)
class Hotel:
    def __init__(self, nome, endereço, cnpj):
        self.nome = nome
        self.endereço = endereço
        self.cnpj = cnpj
        self.cliente = {}
        self.reserva = {}

        

    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel

        self.cliente[self.id] = [self.nome, self.cpf, self.tel]
        
    def listarClientes(self):
        for chave, valor in self.cliente.items():
            print(f" ID: {chave} - Nome: {valor[0]} - CPF {valor[1]} - Telefone {valor[2]}")

    def reservaQuarto (self, idCli, reserva_quarto):
        self.idCli = idCli
        self.reserva_quarto = reserva_quarto

        if self.reserva_quarto == 1:
            x = "Quarto DELUXE"
        elif self.reserva_quarto == 2:
            x = "quarto de Casal"
        elif self.reserva_quarto == 3:
            x = "SOLTEIRO"
        else:
            x = "N/A"
        

        self.reserva[self.idCli] = self.reserva_quarto = x

    def listar_reservas(self):
        for chave, valor in self.reserva.items():
            print(f" ID: {chave} - Nome: {valor[0]} - CPF {valor[1]} - Telefone {valor[2]}")



    def cancelarQuarto():
        pass

    def disponibilidadeQuarto():
        pass

class Quarto():
    def __init__(self, qtd, capacidade, desc, valor):
        self.qtd = qtd
        self.capacidade = capacidade
        self.desc = desc
        self.valor = valor

    def getqtdQuarto(self):
        return self.qtd
    
    def setReservaQuarto(self, qtd):
        self.qtd = qtd

class DeluxeQuarto(Quarto):
    pass

class CasalQuarto(Quarto):
    pass

class Solteiro(Quarto):
    pass
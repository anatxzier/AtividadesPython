from Classes import *
import os

def main():
    hotel = Hotel("Quality", "Av. Brasil", "10.123.321/0001 - 5")
    quarto_deluxe = DeluxeQuarto(2, 4, "Quarto com varanda, cama de casal e hidromassagem", 500)
    quarto_casal = CasalQuarto(4, 2, "Quarto com cama de casal", 300)
    quarto_solteiro = Solteiro(8, 1, "Quarto com uma cama", 150)
    contID = 0000


    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("---MENU---")
            print("[1] CADASTRAR CLIENTE")
            print("[2] DISPONIBILIDADE DE QUARTO")
            print("[3] RESERVAR QUARTO")
            print("[4] CANCELAR RESERVA")
            print("[5] LISTAR CLIENTES")
            print("[0] SAIR")
            print("Qual opção deseja?")
            menu = int(input(">> "))
            os.system("pause")

            match menu:
                case 1:
                    os.system("cls")
                    print("---Cadastro de Cliente---")
                    print("informe os seus dados")
                    contID += 1
                    id = contID
                    nome = input("Nome - ")
                    cpf = input("CPF - ")
                    tel = input("Telefone - ")

                    hotel.cadastrarCliente(id, nome, cpf, tel)
                    print("Cliente cadastrado")
                    print("-------")
                    os.system("pause")
                    

                case 2:
                    os.system("cls")
                    print("---Disponibilidade de quartos---")
                    print (f"Quantidade de quartos DELUXE: {quarto_deluxe.getqtdQuarto()}")
                    print (f"Quantidade de quartos CASAL: {quarto_casal.getqtdQuarto()}")
                    print (f"Quantidade de quartos SOLTEIRO: {quarto_solteiro.getqtdQuarto()}")
                    os.system('pause')


                case 3:
                    os.system("cls")
                    print("---Disponibilidade de quartos---")
                    print (f"Quantidade de quartos DELUXE: {quarto_deluxe.getqtdQuarto()}")
                    print (f"Quantidade de quartos CASAL: {quarto_casal.getqtdQuarto()}")
                    print (f"Quantidade de quartos SOLTEIRO: {quarto_solteiro.getqtdQuarto()}")
                    print("---")
                    print("")
                    print("Qual quarto deseja reservar?")
                    print("[1] - DELUXE")
                    print("[2] - CASAL")
                    print("[3] - SOLTEIRO")

                    reserva_quarto = int(input(">> "))
                    idCli = int(input("Informe o ID do cliente"))

                    hotel.reserva_quarto(idCli, reserva_quarto)

                    match reserva_quarto:
                        case 1:
                            quarto_deluxe.setReservaQuarto(quarto_deluxe.getqtdQuarto() - 1)

                        case 2:
                            quarto_casal.setReservaQuarto(quarto_casal.getqtdQuarto() - 1)

                        case 3:
                            quarto_solteiro.setReservaQuarto(quarto_solteiro.getqtdQuarto() - 1)







                    os.system("pause")

                case 4:
                    pass

                case 5:
                    os.system("cls")
                    print("Listando clientes")
                    hotel.listarClientes()
                    os.system("pause")

                case 6:
                    os.system("cls")


                case 0:
                    print("Saindo...")
                    print("----")
                    sair = True
                
                case _:
                    print("Valor Inválido")
                    print("----")








        except Exception as erro:
            print("Valor Inválido")
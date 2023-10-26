from Classes import *


funcionario = Programador("Carlos")
equipamento = Computador("Avell", "Intel Core I5")
aparelho = Celular("Samsung", "S22 ultra" )

funcionario.setFerramenta(equipamento)
print(funcionario.ferramenta_trabalho.marca)
# //////////////
print(funcionario.getFerramenta().marca)
# //////
print(funcionario.getFerramenta().getMarca())
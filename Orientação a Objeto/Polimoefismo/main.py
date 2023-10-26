from Classes import*

veiculo = Veiculo()
carro = Carro()
aviao = Aviao()
navio = Navio()


for x in (veiculo,carro,aviao,navio):
    print(x.locomocao())
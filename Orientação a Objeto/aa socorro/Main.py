from Classe import *

motor1 = Motor("Revuelto", 1500)
motor2 = Motor("Aventador", 1700)
motor3 = Motor("Sevel", 55)

roda1 = Roda("Michelin circus", 13 )
roda2 = Roda("Michelin arts", 15)

carro1 = Carro("Lamborguini")
carro2 = Carro("Bugatti")
carro3 = Carro("Ferrari")
carro4 = Carro("Gol bolinha")
carro5 = Carro("Frontier")
carro6 = Carro("Ranger")

carro1.setMotor(motor1)
carro1.setRoda(roda1)
print("Carro 1: ")
print(f"Marca: {carro1.getModelo()}")
print(f"Motor: {motor1.getNome()} / Potência: {motor1.getPotencia()}")
print(f"Roda: {roda1.getMarca()} / Aro: {roda1.getAro()}")
print("             ")

carro1.setMotor(motor2)
carro1.setRoda(roda2)
print("Carro 2: ")
print(f"Marca: {carro2.getModelo()}")
print(f"Motor: {motor2.getNome()} / Potência: {motor2.getPotencia()}")
print(f"Roda: {roda2.getMarca()} / Aro: {roda2.getAro()}")
print("             ")


print("Carro 3: ")
print(f"Marca: {carro3.getModelo()}")
print(f"Motor: {motor3.getNome()} / Potência: {motor3.getPotencia()}")
print(f"Roda: {roda1.getMarca()} / Aro: {roda1.getAro()}")
print("             ")


print("Carro 4: ")
print(f"Marca: {carro4.getModelo()}")
print(f"Motor: {motor2.getNome()} / Potência: {motor2.getPotencia()}")
print(f"Roda: {roda2.getMarca()} / Aro: {roda2.getAro()}")
print("             ")


print("Carro 5: ")
print(f"Marca: {carro5.getModelo()}")
print(f"Motor: {motor3.getNome()} / Potência: {motor3.getPotencia()}")
print(f"Roda: {roda1.getMarca()} / Aro: {roda1.getAro()}")
print("             ")

print("Carro 6: ")
print(f"Marca: {carro6.getModelo()}")
print(f"Motor: {motor1.getNome()} / Potência: {motor1.getPotencia()}")
print(f"Roda: {roda2.getMarca()} / Aro: {roda2.getAro()}")
print("             ")


class Motor:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia

    def getNome(self):
        return self.nome

    def getPotencia(self):
        return self.potencia

class Roda:
    def __init__(self, marca, aro):
        self.marca = marca
        self.aro = aro

    def getMarca(self):
        return self.marca
    
    def getAro(self):
        return self.aro
    
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.roda = None
        self.motor = None

    def getModelo(self):
        return self.modelo
    
    def getRoda(self):
        return self.roda
    
    def setRoda(self, pneu):
        self.roda = pneu
    
    def getMotor(self):
        return self.motor
    
    def setMotor(self, motor):
        self.motor = motor
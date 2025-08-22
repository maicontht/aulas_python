class Carro:
    def __init__(self, nome):    
        self.nome = nome
        self.motor = None
        self.fabricante = None 


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro1 = Carro('Fusca')
motor1 = Motor('Motor V8')
fabricante1 = Fabricante('Volkswagen')
carro1.motor = motor1
carro1.fabricante = fabricante1
print(carro1.nome)
print(carro1.motor.nome)
print(carro1.fabricante.nome)

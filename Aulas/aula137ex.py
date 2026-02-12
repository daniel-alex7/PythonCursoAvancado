# Exercicio com Classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar varios carros
# Exiba o nome do carro, motor e  fabricantes na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self.fabricante = None
        
    def inserir_motor(self, motor):
        self.motor = motor

    def inserir_fabricante(self, fabricante):
        self.fabricante = fabricante
    
#Associação    
class Motor:
    def __init__(self, nome):
        self.nome = nome
               

#Associação
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []
        
    def inserir_carro(self, carro) :
        self.carros.append(carro)
        
    
carro1 = Carro('Carro: HB20')
motor1 = Motor('Motor: V8')
fabrincante1 = Fabricante('Fabricante: Chetrolet')

carro1.inserir_motor(motor1)
carro1.inserir_fabricante(fabrincante1)
fabrincante1.inserir_carro(carro1)

print(f'Carro: {carro1.nome}')
print(f'Motor: {motor1.nome}')
print(f'Fabricante: {fabrincante1.nome}')
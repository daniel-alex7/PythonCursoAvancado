# Exercicio com Classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar varios carros
# Exiba o nome do carro, motor e  fabricantes na tela

# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
#         self._motor = None
#         self.fabricante = None
        
#     def inserir_motor(self, motor):
#         self.motor = motor

#     def inserir_fabricante(self, fabricante):
#         self.fabricante = fabricante
    
# #Associação    
# class Motor:
#     def __init__(self, nome):
#         self.nome = nome
               

# #Associação
# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome
#         self.carros = []
        
#     def inserir_carro(self, carro) :
#         self.carros.append(carro)
        
    
# carro1 = Carro('Carro: HB20')
# motor1 = Motor('Motor: V8')
# fabrincante1 = Fabricante('Fabricante: Chetrolet')

# carro1.inserir_motor(motor1)
# carro1.inserir_fabricante(fabrincante1)
# fabrincante1.inserir_carro(carro1)

# print(f'Carro: {carro1.nome}')
# print(f'Motor: {motor1.nome}')
# print(f'Fabricante: {fabrincante1.nome}')


# correção: 

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
                
        
class Motor: 
    def __init__(self, nome):
        self.nome = nome
        

class Fabricante: 
    def __init__(self, nome):
        self.nome = nome
        
        
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)
print()

hb20 = Carro('Hb20')
motor_1_2 = Motor('1.2')
chetrolet = Fabricante('Chetrolet')
hb20.fabricante = chetrolet
hb20.motor = motor_1_2

print(hb20.nome, hb20.fabricante.nome, hb20.motor.nome)
print()
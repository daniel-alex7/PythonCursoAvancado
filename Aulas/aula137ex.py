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
    
#Associação    
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

#Associação
class Fabricante:
    def __init__(self, marca):
        self.marca = marca
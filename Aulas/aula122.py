# entendendo self em classes

class Carro: 
    def __init__(self, nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelarando')

string = 'Daniel'
print(string.upper())
print()

fusca = Carro('Fusca') #self
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()
# print()

celta = Carro(nome='Celta')
Carro.acelerar(celta)
print(celta.nome)
# celta.acelerar()
# print()
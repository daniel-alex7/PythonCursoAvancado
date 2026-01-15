# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.


# string = 'Daniel' 
# print(string.upper())
# print(isinstance(string, str)) #str, string é instancia da classe str

# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome
    
# p1 = Pessoa('Daniel', 'Alexandre')
# # p1.nome = 'Daniel'
# # p1.sobrenome = 'Alexandre'


# p2 = Pessoa('Maria','Souza')
# # p2.nome = 'Maria'
# # p2.sobrenome = 'Alexandre'

# print(p1.nome)
# print(p1.sobrenome)
# print()
# print(p2.nome)
# print(p2.sobrenome)

# metodos em instancias de classes Python
# hard coded - algo escrito diretamente no codigo

class Carro: 
    def __init__(self, nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelarando')

fusca = Carro('Fusca') #self
print(fusca.nome)
fusca.acelerar()
print()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
print()
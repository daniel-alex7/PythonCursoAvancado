
# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

# @dataclass
# class Pessoa:
#     nome: str
#     # idade: int
#     sobrenome: str
    
#     @property
#     def nome_completo(self):
#         return f'{self.nome} {self.sobrenome}'
    
#     @nome_completo.setter
#     def nome_completo(self, valor):
#         nome, *sobrenome = valor.slipt()
#         self.nome = nome
#         self.sobrenome = ' '.join(sobrenome)
    
    
    
# if __name__ == '__main__':
#     p1 = Pessoa('Daniel',"Alexandre")
#     # p2 = Pessoa('Daniel', 20)
#     # print(p1 == p2)
#     p1.nome_completo = 'Maria Helena'
#     print(p1)
#     print(p1.nome_completo)




#     # part 2

# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str

#     @property
#     def nome_completo(self):
#         return f'{self.nome} {self.sobrenome}'

#     @nome_completo.setter
#     def nome_completo(self, valor):
#         nome, *sobrenome = valor.split()
#         self.nome = nome
#         self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     p1 = Pessoa('Luiz', 'Otávio')
#     p1.nome_completo = 'Maria Helena'
#     print(p1)
#     print(p1.nome_completo)
    

#  part 3 _init_ e __post_initi__  
    
# @dataclass(init=False)
# class Pessoa:
#     nome: str
#     sobrenome: str
    
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.nome_completo = f'{self.nome} {self.sobrenome}'
    
#     def __post_init__(self):
#         print('Post Init')
#         self.nome_completo = f'{self.nome} {self.sobrenome}'

#     # @property
#     # def nome_completo(self):
#     #     return f'{self.nome} {self.sobrenome}'

#     # @nome_completo.setter
#     # def nome_completo(self, valor):
#     #     nome, *sobrenome = valor.split()
#     #     self.nome = nome
#     #     self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     p1 = Pessoa('Daniel', 'Robson')
#     print(p1)
#     print(p1.nome_completo)


# part 4

@dataclass(repr=False)
class Pessoa:
    nome: str
    sobrenome: str
    

if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X'),]
    ordenar = sorted(lista, reverse=True, key=lambda p: p.nome)
    print(ordenar)

    
    
    
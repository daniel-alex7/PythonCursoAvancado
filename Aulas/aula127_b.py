# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

#  RECUPERANDO OS DADOS


import json

# class Pessoa:
#         def __init__(self, nome, idade):
#             self.nome = nome
#             self.idade = idade



   
    

# with open('aula127_a.json', 'r', encoding='utf8') as arquivo:
#     p1 = json.load(arquivo)
#     print(p1)

    
# with open('aula127_b.json', 'w', encoding='utf8') as arquivo:
#     p1 = Pessoa('Roberto', 21)

#     json.dump(
#             p1.__dict__, arquivo, indent=4,
#     )
    
    
# print(p1.nome, p1.idade)

# Correção

from aula127_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

fazer_dump()



with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    
    
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    
    
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
        
print(__name__)
    
    
    

  
    
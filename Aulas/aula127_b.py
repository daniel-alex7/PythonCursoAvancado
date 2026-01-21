# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

#  RECUPERANDO OS DADOS


import json

class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade


p1 = Pessoa('Roberto', 21)

# with open('aula127_a.json', 'r', encoding='utf8') as arquivo:
#     print(arquivo.read())
    
    
    

with open('aula127_a.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    
with open('aula127_b.json', 'w', encoding='utf8') as arquivo:
    json.load(arquivo)
  
  
    
   
    
    
    
    

  
    
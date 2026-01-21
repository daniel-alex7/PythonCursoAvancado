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



   
    

with open('aula127_a.json', 'r', encoding='utf8') as arquivo:
    p1 = json.load(arquivo)
    print(p1)

    
with open('aula127_b.json', 'w', encoding='utf8') as arquivo:
    p1 = Pessoa('Roberto', 21)

    json.dump(
            p1.__dict__, arquivo, indent=4,
    )
    
    
print(p1.nome, p1.idade)
    
    
    
    

  
    
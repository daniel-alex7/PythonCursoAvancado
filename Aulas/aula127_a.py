# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.


import json

    
with open('aula127_a.json', 'w', encoding='utf8') as arquivo:
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
            
    p1 = Pessoa(
            nome = "Daniel Robson",
            idade = 20 )  
    
    # ta funcionando
    json.dump(p1, 
            arquivo,
            ensure_ascii=False,
            indent=2)
    


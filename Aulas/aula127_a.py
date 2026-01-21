# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.


import json

# class Pessoa:
#         def __init__(self, nome, idade):
#             self.nome = nome
#             self.idade = idade


# p1 = Pessoa('Daniel', 21)

    
# with open('aula127_a.json', 'w', encoding='utf8') as arquivo:
 
#     json.dump(
#             p1.__dict__, arquivo, indent=4,
#     )

# Correção: 

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

            
p1 = Pessoa('Daniel', 20)
p2 = Pessoa('Juliana', 18)
p3 = Pessoa('Elio', 20)

bd = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
        with open(CAMINHO_ARQUIVO, 'w') as arquivo:
                print('FAZENDO DUMP')
                json.dump(bd, arquivo, ensure_ascii = False, indent = 2)
        
        
if __name__ == '__main__':
        print('ELE É O MAIN')
        fazer_dump()
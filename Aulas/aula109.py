# Cobinations, Permutations e Product = Itertools
# Cobinação - Oredem não importa = iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')

pessoa = [
    'João', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodao', 'poliéster']
]

# print_iter(combinations(pessoa, 2))
# print()
# print_iter(permutations(pessoa, 2))
# print()

print_iter(product(*camisetas))


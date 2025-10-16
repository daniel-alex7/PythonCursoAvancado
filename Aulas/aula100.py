# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)


novos_produtos.append({'nome': 'Produto 6', 'preco': 12.00})
print('Copia Profunda')
print(novos_produtos)
print()

novos_precos = [
    {**produto, 'preco': produto['preco'] * 1.01}
    for produto in novos_produtos 
]

# agora ordena pelo nome
l1 = sorted(novos_precos, key=lambda item: item['nome'] )
print('Ordenado pelo nome: ')
print(*l1, sep='\n')
print()


# Ordene os produtos por nome decrescente (do maior para menor)
l2 = sorted(novos_precos, reverse=True, key=lambda item: item['nome'] )
def exibir(lista):
    for item in lista:
        print(item)
    print()
    
print('Ordenado em ordem decrescente')
exibir(l2)
print()


# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

novos_produtos2 = copy.deepcopy(novos_produtos)

novos_produtos2.append({'nome': 'Produto 7', 'preco': 123.00})
l3 = sorted(novos_produtos2, key=lambda item: item['nome'] )
print('Ordenado pelo nome em cópia profunda: ')
print(*l3, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)


l4 = sorted(novos_produtos2, key=lambda item: item['preco'] )
print('Ordenado pelo preço: ')
print(*l4, sep='\n')
print()

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(novos_produtos2)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda p: p['preco'])
print('Produtos ordenados pelo preço por deep copy')
print(*produtos_ordenados_por_preco, sep='\n')

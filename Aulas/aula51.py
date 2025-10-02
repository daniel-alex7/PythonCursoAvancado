"""
Exercício 

Exiba os índices da lista
0 Maria
1 Helena 
2 Luiz

"""

lista = ['Maria', 'Helena', 'Luiz']

# lista está em str e indices são int, devemos fazer o seguinte para velos:


for indice in range(len(lista)):
    print(f'Os indices são: {indice} {lista[indice]}')
    
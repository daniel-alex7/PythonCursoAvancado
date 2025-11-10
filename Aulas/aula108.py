# Considerando duas lista de inteiros ou fgloats (listaA e listaB)
# Some os valores nas listas retornando uma nova lista com os valores somados:

#Se uma lista for maior que a outra, a soma só vai considerar o tamanho menor

#Exemplo:

#lista_a = [1, 2, 3, 4, 5, 6, 7]
#lista_b = [1, 2. 3, 4]

#resultado;
#lista_soma = [2, 4, 6, 8]

from itertools import zip_longest

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

soma = l1 + l2

print(list(zip(soma)))
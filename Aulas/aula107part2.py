# Considerando duas lista de inteiros ou floats (listaA e listaB)
# Some os valores nas listas retornando uma nova lista com os valores somados:

#Se uma lista for maior que a outra, a soma só vai considerar o tamanho menor

#Exemplo:

#lista_a = [1, 2, 3, 4, 5, 6, 7]
#lista_b = [1, 2. 3, 4]

#resultado;
#lista_soma = [2, 4, 6, 8]



lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# lista_soma = []

# for i in range(min(len(lista_a), len(lista_b))):
#     lista_soma.append(lista_a[i] + lista_b[i])
    

lista_soma = [a + b for a, b in 
              zip(lista_a, lista_b)
              ]
    
print(lista_soma)

# Podemos tilizar o zip_longest para capturar valores da lista maior:

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]

print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]
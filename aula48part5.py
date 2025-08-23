"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Daniel' # apelido = valor
# noutra_variavel = nome
# nome = 'Robson'
# print(nome)
# print(noutra_variavel)

lista_a = ['Luiz', 'Maria', 1, True]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa' # Quando altera uma, altera as duas
print(lista_b)
print(lista_a)
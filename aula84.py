# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.



# Inlcui numero 1 dez vezes na minha lista
lista = [numero for numero in range(10)]
print(lista)

lista = [
    numero * 2
    for numero in range(10)
    ]
print(lista)



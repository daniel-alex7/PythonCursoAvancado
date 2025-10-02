"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# lembre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4

print(x, y, resto)

# def soma(x,y):
#     return x + y

# args empacota o que envia para função dentro de uma tupla
def soma (*args):
    total = 0
    for numero in args:
        total += numero
    return total

# soma1_2_3 = soma(1,2,3)
# print(soma1_2_3)

# print(sum(1, 2, 3, 4, 5, 6, 7))

# desempacota para enviar para a função
numeros = 1, 2, 3, 4, 5, 6, 7, 8
outra_soma = soma(*numeros)
print(outra_soma)

print(*numeros) #desempacotamento
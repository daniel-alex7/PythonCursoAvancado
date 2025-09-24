"""
Exercicos com funções

Crie uma função que multiplica todos os argumentos 
não nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variavel

Crie uma função que fala se um numero é par ou ímpar.
Retorne se o núemro é par ou ímpar
"""


# Minha 
def multiplica(n1, n2):
    return n1 * n2
    
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

total = multiplica(n1, n2)
print(total)

# Professor

def multiplica(*args):
    total = 0
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplica(1, 2, 3, 4, 5)
print(multiplicacao)

def par(n1):
    if n1 % 2 == 0 : 
        return f'{n1} é par'
    return f'{n1} é impar'

n1 = int(input('Digite um número: '))
par(n1)
    

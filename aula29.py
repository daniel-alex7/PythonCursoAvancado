"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
 # int('a') # Erro de converção, levantamento de exceção

numero_str = input('Digite um número para mim dobrar: ')


try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Você não digitou um número válido!')






# print(numero_str.isdigit() ) # Verifica se a string contém apenas dígitos 


'''if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
else:
    print('Você não digitou um número válido!')
'''




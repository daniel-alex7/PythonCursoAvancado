"""
Introdução às funções (def) em Python:
Funções são trechos de códigos usados 
para replicar determinada ação ao longo do código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico
Por padrão, funções Python retornam None (nada).
"""
        #Parametros
# def Print(a, b, c):
#     print('Várias')

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome):
    print(f'Olá {nome}')

saudacao(input('Digite seu nome: '))
"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return 10
    return x + y 
# não pode executar mais nada depois de return > para execução

# var = soma(1,2)
# var = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 4)
print(soma1)
print(soma2)
print(soma(11, 20))
print(soma1 + soma2)

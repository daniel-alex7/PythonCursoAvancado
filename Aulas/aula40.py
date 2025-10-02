"""
Calculadora com while
"""

while True:
    num1 = input('Digite o primeiro numero: ')
    num2 = input('Digite o segundo numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_valido = None

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_valido = True

    except:
        numeros_valido = None
        num_1_float = 0
        num_2_float = 0
    
    if numeros_valido is None:
        print('Um ou ambos os numeros digitados são invalidos')
        continue


    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta...')
    if operador == '+':
        print(f'{num1} + {num2} = {num_1_float + num_2_float}')
  
    elif operador == '-':
        print(f'{num1} - {num2} = {num_1_float - num_2_float}')

    elif operador == '*':
        print(f'{num1} * {num2} = {num_1_float * num_2_float}')

    elif operador == '/':
        print(f'{num1} / {num2} = {num_1_float / num_2_float}')
    else:
        print('Não deveria ter chegado aqui')


    sair = input('Quer sair? [s]im:  ').lower().startswith('s')

    if sair:
        print('SAINDO...')
        break
    



    

       

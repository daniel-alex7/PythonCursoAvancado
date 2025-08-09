"""
Faça um programa que peça ao usuario para digitar um número
 inteiro e informe se este número é par ou ímpar. Caso o usuario não 
 digite um número inteiro, informe que não é número inteiro.
"""
numero = input('Digite um número inteiro: ')
try:
    numer_par =  int(numero) % 2 == 0
    numer_impar = int(numero) % 2 != 0

    if numer_par:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
except:
    print(f'O valor {numero} não é um número inteiro.')

    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no 
horário descrito, exiba a suadação apropriada.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""
hora = int(input('Digite a hora (0-23): '))

if hora <= 11 and hora >= 0:
    print('Bom dia!')
elif hora <= 17 and hora >= 12:
    print('Boa tarde!')
elif hora <= 23 and hora >= 18:
    print('Boa noite!')
else:
    print('Hora inválida! Por favor, digite um número entre 0 e 23.')


"""
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver
mais de 4 letras, escreva "Seu nome é longo", escreva "Seu nome é Normal"
maior que 6 escreva "Seu nome é muito longo"
"""
prim_nome = input('Digite seu primeiro nome: ')

if len(prim_nome) <= 4:
    print('Seu nome é curto.')
elif len(prim_nome) > 4 and len(prim_nome) <= 6:
    print('Seu nome é normal.') 
elif len(prim_nome) > 6:
    print('Seu nome é muito longo.')
else:
    print('Nome inválido! Por favor, digite um nome válido.')
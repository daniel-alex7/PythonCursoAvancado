"""
Faça um programa que peça ao usuario para digitar um número
 inteiro e informe se este número é par ou ímpar. Caso o usuario não 
 digite um número inteiro, informe que não é número inteiro.
"""
numero_int = input('Digite um número inteiro: ')

try:
    numer_par =  int(numero_int) % 2 == 0

    if numer_par:
        print(f'O número {numero_int} é par.')
    else:
        print(f'O número {numero_int} é ímpar.')

except:
    print(f'O valor {numero_int} não é um número inteiro.')

#Correção na aula

entrada = input('Digite um número inteiro: ')
try:
    numero_int = int(entrada)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {numero_int} é {par_impar_texto}.')

except:
    print('Você não digitou um número inteiro')

#Ou

if entrada.isdigit():
    numero_int = int(entrada)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {numero_int} é {par_impar_texto}.')

else:
    print('Você não digitou um número inteiro')

###########################################################################################################################################


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


#Correção na aula

entrada = input('Digite a hora em número inteiros: ')

try:
    hora = int(entrada)

    if hora <= 11 and hora >= 0:
       print('Bom dia!')
    elif hora <= 17 and hora >= 12:
       print('Boa tarde!')
    elif hora <= 23 and hora >= 18:
       print('Boa noite!')
    else:
       print('Não conheço essa hora!')
except:
    print('Você não digitou um número inteiro válido!')

###############################################################################################################################################
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

#Correção na aula

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)    

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    if tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito longo.')
else: 
    print('Por favor, mais de uma letra')
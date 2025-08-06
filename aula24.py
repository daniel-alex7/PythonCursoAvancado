# Operadores in e not in    
# Strings são iteráveis( pode navegar item por item) )
# 0 1 2 3 4 5
# D A N I E L

nome = 'Daniel'

# print(nome[2])

#print('D' in nome)  # True
#print('d' in nome)  # False
#print(10 * '-')
#print('D' not in nome)  # False
#print('d' not in nome)  # True

nome = input('Digite seu nome: ')
encontrar = input('Qual letra deseja encontrar? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
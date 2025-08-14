"""
Reptições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira. 

"""

condicao = True 

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Olá {nome}!')

    if nome == 'sai':
        break
       

print('Acabou')
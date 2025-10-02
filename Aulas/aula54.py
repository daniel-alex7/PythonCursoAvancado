"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros 
de índices inexistentes na lista.

"""
import os

lista = []

while True: #Quando for verdadeiro
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls') #limpa a tela
        valor = input('Valor: ')
        lista.append(valor) #append vai acrescentar o valor na lista

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str) #converte o numero_letra em um número positivo
            del lista[indice] #deleta o indice_numero_letra 
        except:
            print('Não foi possível apagar índice')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        sair = input('Se deseja sair digite [s]')
        if sair == 's':
            break

print('Você saiu')

